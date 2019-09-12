from abaqusConstants import *
from odbAccess import *
from textRepr import *
from shutil import copyfile
from os import getcwd, path
import numpy as np
import pprint
import time
import sys
import math
from Utilities import *
from Integration import *
from C3D20 import *

def GetCrackFrontNodes(allNodes,firstCrackNodeLabel,q):

	#reconstruct crack node front going towards 0 in z
	nFirstCrack=allNodes[firstCrackNodeLabel-1]
	posAxis=[]
	cOnAxis=[]
	for i in range(0,3,1):
		if i!=q-1:
			posAxis.append(nFirstCrack.coordinates[i])
			cOnAxis.append(i)
		else: 
			axisDir=i
	
	CFnSet=[]
	CFPosz=[]
	CFPosx=[]
	CFPosy=[]

	for n in allNodes: 
		if n.coordinates[cOnAxis[0]]==posAxis[0] and n.coordinates[cOnAxis[1]]==posAxis[1]:
			CFnSet.append(n.label)
			CFPosz.append(n.coordinates[axisDir])
			CFPosx.append(n.coordinates[cOnAxis[0]])
			CFPosy.append(n.coordinates[cOnAxis[1]])
			
	CFnSet,ind=np.unique(np.array(CFnSet), return_index=True)
	CFPosz=np.array(CFPosz)
	CFPosx=np.array(CFPosx)
	CFPosy=np.array(CFPosy)
	CFPosx=CFPosx[ind]
	CFPosy=CFPosy[ind]
	CFPosz=CFPosz[ind]
	ind=np.argsort(CFPosz)
	CFnSet=CFnSet[ind]
	CFnSet=CFnSet[::-1]
	CFPosx=CFPosx[ind]
	CFPosx=CFPosx[::-1]
	CFPosy=CFPosy[ind]
	CFPosy=CFPosy[::-1]
	CFPosz=CFPosz[ind]
	CFPosz=CFPosz[::-1]
	rPoszRelTol=(CFPosz[0]-CFPosz[1])/500.0


	#nTip=allNodes[nodeLabelTip-1]
	#labels=[nodeLabelTip]
	#
	#if crackFrontAxis==0:
	#	pos1=2
	#	pos2=1
	#elif crackFrontAxis==1:
	#	pos1=0
	#	pos2=2
	#elif crackFrontAxis==2:
	#	pos1=0
	#	pos2=1
	#
	#for n in allNodes: 
	#	if isclose(n.coordinates[pos1],nTip.coordinates[pos1]) and isclose(n.coordinates[pos2],nTip.coordinates[pos2]):
	#		labels.append(n.label)
	#		
	#labels=np.unique(np.array(labels))
	#position = np.zeros((len(labels)),dtype='float32')
	#
	#for i in range(0,len(labels)):
	#	#print labels
	#	#print allNodes[labels[i]]
	#	position[i]=allNodes[labels[i]-1].coordinates[crackFrontAxis]
	
	return CFnSet,CFPosx,CFPosy,CFPosz,cOnAxis[0],cOnAxis[1]

def GetElMaterial(part,elements,sectionElSetRange):
	#sectionElSetRange is assumed to have alternating materials
	#since we are dealing with layered materials just use boolean
	elMaterial=np.zeros((len(elements)), dtype=bool)
	for i in range(0,len(sectionElSetRange),2):
		elSection=part.elementSets['SET-'+str(sectionElSetRange[i])].elements
		for e in elSection: 
			elMaterial[e.label-1]=True
	
	return elMaterial
	
def BuildElementAndNodeSets(nContours,SetPrefix,nodeLabelTip,crackFrontAxis,sectionElSetRange,odb,partInstance):
	#Get components of odb
	root=odb.rootAssembly
	#Get the elements
	part=root.instances[partInstance]
	elements=part.elements

	#Get nodes
	allNodes = root.instances[partInstance].nodes
	labels,CFPosx,CFPosy,position,pos1,pos2 = GetCrackFrontNodes(allNodes,nodeLabelTip,crackFrontAxis)
	
	#debug labels
	#for i in range(0,len(labels),1):
	#	print labels[i],position[i],CFPosx[i],CFPosy[i]
	#raise	
	
	#sid=np.argsort(position) 
	#position=position[sid[::-1]]
	#labels=labels[sid[::-1]]

	#remove side nodes (every other)
	labels=labels[0::2]
	#print position
	#print labels
	#raise
	
	nNodes=len(labels)

	elemConn, elemNbr = GetElementConnectivities(elements)

	#Due to some bug in Abaqus, section information is incorrect at the element level. I did not 
	#find the reason for this, but I spent a better part of a day trying to get it directly and gave up.
	#For this reason the user needs to specify a starting and ending sequency for section elsets. 
	#The sets are then used to get the material information assuming alternative materials which each sussecessive set
	elMaterial = GetElMaterial(part,elements,sectionElSetRange)

	sets = {}
	nSlices = nNodes 
	tUnion=0
	tGetEl=0
	
	t0=time.time()
	#compute nContours + 1 due to how node sets are defined and for interfaces to be appropriately captured
	for contour in range(0,nContours+1,1):
		if contour==0:
			for slice in range(0,nSlices,1):#slices
				t0=time.time()
				linInd=contour*nSlices+slice
				
				tmp1=np.array(elemConn[labels[slice]])
				
				#This section made the element sections one element wide.
				#if slice>0:					
				#	#remove elements from previous set using sorted search 
				#	tmp1=tmp1[~np.in1d(tmp1,tmp2)]
				#
				#tmp2=tmp1
				sets[linInd]=list(tmp1)
				#print sets[linInd]

		else: 
			for slice in range(0,nSlices,1):#slices
				#get the linear index for the sets
				linIndprev=(contour-1)*nSlices+slice
				linInd=(contour)*nSlices+slice

				#initialize set
				sets[linInd] = []

				#get elements from previous contour level
				ePrev=sets[linIndprev]

				#get all elements attached to previous sets
				tlast=time.time()
				for e in ePrev:
					ec=elemNbr[e]
					for ee in ec:
						#if not any(x==ee for x in sets[linInd]):
						sets[linInd].append(ee)
				
				tGetEl=tGetEl+time.time()-tlast
				#sort element labels
				tmp=np.array(sets[linInd])
				tmp=np.unique(tmp)
				sid=np.argsort(tmp)
				sets[linInd]=list(tmp[sid])
				#print sets[linInd]
				
			#remove elements not in slice by using overlapping sets
			#first store data for last two cases before data is remove
			tmpendm1=np.array(sets[contour*nSlices+nSlices-2]) #20 end
			tmpendm2=np.array(sets[contour*nSlices+nSlices-3]) #19
			tmpendm3=np.array(sets[contour*nSlices+nSlices-4]) #18
			tmpendm4=np.array(sets[contour*nSlices+nSlices-5]) #17
			tmpendm5=np.array(sets[contour*nSlices+nSlices-6]) #16
			tlast=time.time()
			for slice in range(0,nSlices,1):#slices
				#get the linear index for the sets
				linInd=contour*nSlices+slice	
				name=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)
				print name
				if slice==(nSlices-3): 
					tmp1=tmpendm3
					tmp2=tmpendm5
					tmp1=tmp1[~np.in1d(tmp1,tmp2)]
					sets[linInd]=list(tmp1)
				elif slice==(nSlices-2): 
					tmp1=tmpendm2
					tmp2=tmpendm4
					tmp1=tmp1[~np.in1d(tmp1,tmp2)]
					sets[linInd]=list(tmp1)
				elif slice==(nSlices-1): 
					tmp1=tmpendm1
					tmp2=tmpendm3
					tmp1=tmp1[~np.in1d(tmp1,tmp2)]
					sets[linInd]=list(tmp1)
				else:
					tmp1=np.array(sets[linInd+1])
					tmp2=np.array(sets[linInd+3])
					tmp1=tmp1[~np.in1d(tmp1,tmp2)]
					sets[linInd]=list(tmp1)
			tUnion=tUnion+time.time()-tlast
	t1=time.time()
	#nodeSets: setq1, setq0p5, setq0, setSlice
	for contour in range(0,nContours,1):
		for slice in range(0,nSlices,1):
			linInd = contour*nSlices+slice
			linIndp1c = (contour+1)*nSlices+slice			
			if contour > 0:
				linIndm1c = (contour-1)*nSlices+slice
				elInsideset = np.array(sets[linIndm1c])
				elset = np.array(sets[linInd])
				elsetp1 = np.array(sets[linIndp1c])
				elOutsideset=elsetp1[~np.in1d(elsetp1,elset)]
				
				#start loading up the node sets
				nsetQ1 = () 
				for e in elInsideset:
					#get nodes in each element in elInsideset
					nsetQ1 = nsetQ1 + elements[e-1].connectivity
									
				nsetQ0 = () 
				for e in elOutsideset:
					#get nodes in each element in elOutsideset
					nsetQ0 = nsetQ0 + elements[e-1].connectivity					
			else: 
				elset = np.array(sets[linInd])
				elsetp1 = np.array(sets[linIndp1c])
				elOutsideset=elsetp1[~np.in1d(elsetp1,elset)]
				
				nsetQ1 = () 
				#for the inner ring use the yx based coordinates 
				for e in elset:
					nconn=elements[e-1].connectivity	
					for n in nconn: 
						if isclose(allNodes[n-1].coordinates[pos1],allNodes[nodeLabelTip-1].coordinates[pos1]) and \
							isclose(allNodes[n-1].coordinates[pos2],allNodes[nodeLabelTip-1].coordinates[pos2]):
							nsetQ1 = nsetQ1 + tuple([n])
	
					#get nodes in each element in elInsideset
							
									
				nsetQ0 = () 
				for e in elOutsideset:
					#get nodes in each element in elInsideset
					nsetQ0 = nsetQ0 + elements[e-1].connectivity					
				
			#get all node we are interested in in the nodesets nsetQ0, etc..
			nsetSlice = () #empty tuple
			for e in sets[linInd]:
				#get nodes in each element in elset
				nsetSlice = nsetSlice + elements[e-1].connectivity
			
			#trim node sets by unions
			nsetQ0=np.array(nsetQ0)
			nsetQ1=np.array(nsetQ1)
			nsetSlice=np.array(nsetSlice)
			
			nsetQ0=nsetQ0[np.in1d(nsetQ0,nsetSlice)]
			nsetQ0p5=nsetSlice[~np.in1d(nsetSlice,nsetQ0)]
			#nsetQ1=np.unique(nsetQ1)
			#nsetQ0p5=np.unique(nsetQ0p5)
			nsetQ0p5=tuple(nsetQ0p5[~np.in1d(nsetQ0p5,nsetQ1)])

			nsetQ0=tuple(nsetQ0)
			nsetQ0p5=tuple(nsetQ0p5)
			nsetQ1=tuple(nsetQ1)
			nsetSlice=tuple(nsetSlice)

			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)+'-Q0'
			root.NodeSetFromNodeLabels(name = setName, nodeLabels = ((partInstance,nsetQ0),)) 
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)+'-Q0p5'
			root.NodeSetFromNodeLabels(name = setName, nodeLabels = ((partInstance,nsetQ0p5),)) 
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)+'-Q1'
			root.NodeSetFromNodeLabels(name = setName, nodeLabels = ((partInstance,nsetQ1),)) 
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)
			root.NodeSetFromNodeLabels(name = setName, nodeLabels = ((partInstance,nsetSlice),)) 
			
			#Build the interface sets for surface integration
			elset = np.array(sets[linInd])

			elsetInterfaceTop = []
			elsetInterfaceBottom = []
			nsetInterface = []
			for e in elset:
				ec=elemNbr[e]
				ec=np.array([x - 1 for x in ec]) #due to list comprehension issues..
				potentialInterface=elMaterial[ec]!=elMaterial[e-1]

				if np.any(potentialInterface):
					ec=ec[potentialInterface]
					eNodes=np.array(elements[e-1].connectivity)

					for ee in ec:
						eeNodes=np.array(elements[ee].connectivity)
						nodes2Append=eeNodes[np.in1d(eeNodes,eNodes)]
						
						if len(nodes2Append)>3: #i.e. if it is a face relationship

							for toappend in nodes2Append:
								nsetInterface.append(toappend)
								
							posee=0
							for n in eeNodes: 
								posee+=allNodes[n-1].coordinates[1]
							pose=0
							for n in eNodes: 
								pose+=allNodes[n-1].coordinates[1]
								
							if posee>pose:
								elsetInterfaceTop.append(ee+1)
								elsetInterfaceBottom.append(e)
							else:
								elsetInterfaceTop.append(e)
								elsetInterfaceBottom.append(ee+1)
			
			#Ensure unique
			nsetInterface=np.unique(np.array(nsetInterface))
			elsetInterfaceTop,ind=np.unique(np.array(elsetInterfaceTop), return_index=True)
			elsetInterfaceBottom=np.array(elsetInterfaceBottom)
			elsetInterfaceBottom=elsetInterfaceBottom[ind]
			
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice) + '-interface'
			root.NodeSetFromNodeLabels(name = setName, nodeLabels = ((partInstance,nsetInterface),)) 		
			
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)+'-interfaceTop'
			root.ElementSetFromElementLabels(name = setName, elementLabels = ((partInstance,tuple(elsetInterfaceTop)),)) 	

			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)+'-interfaceBottom'
			root.ElementSetFromElementLabels(name = setName, elementLabels = ((partInstance,tuple(elsetInterfaceBottom)),)) 	
			
	t2=time.time()
	#write sets to odb 
	for contour in range(0,nContours,1):
		for slice in range(0,nSlices,1):#slices	
			linInd=contour*nSlices+slice	
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)
			
			#convert element list to tuple 
			newSetElements=tuple(sets[linInd])
			root.ElementSetFromElementLabels(name = setName, elementLabels = ((partInstance,newSetElements),)) 
	
	t3=time.time()
	
	print "time report"
	print '++++++++++++'
	print 'time in first loop',t1-t0
	print 'time in first loop get El',tGetEl
	print 'time in first loop get union',tUnion
	print 'time in second loop',t2-t1
	print 'time in third loop',t3-t2
	print '++++++++++++'
	print '++++++++++++'	

	return odb
	
def GetStress(root,frame,elSetName):
	#returns stress tensor for all elements in set elSet stress is accessed by the dictionary element label
	#array locations follow [element x integration point x data ] where data is in tensor form
	elSet = root.elementSets[elSetName]
	field = frame.fieldOutputs['S'].getSubset(region=elSet,position=INTEGRATION_POINT)
	
	dataGauss = np.array(field.bulkDataBlocks[0].data,dtype='float64') #s11,s22,s33,s12,s13,s23 ordered
	elLabel = np.array(field.bulkDataBlocks[0].elementLabels,dtype='int64')
	intLabel = np.array(field.bulkDataBlocks[0].integrationPoints,dtype='int8')

	nEl=len(np.unique(elLabel))
	nData=len(intLabel)
	nInt=np.amax(intLabel)
	
	S=np.zeros((nEl,nInt,3,3),dtype='float64')
	elLabelU=np.zeros((nEl),dtype='int64')

	el=0
	for i in range(0,nData,nInt):
		tmpData=dataGauss[i:i+nInt]
		
		for p in range(0,nInt,1): 
			S[el,p,0,0]=tmpData[p,0]
			S[el,p,1,1]=tmpData[p,1]
			S[el,p,2,2]=tmpData[p,2]
			S[el,p,0,1]=tmpData[p,3]
			S[el,p,1,0]=tmpData[p,3]
			S[el,p,0,2]=tmpData[p,4]
			S[el,p,2,0]=tmpData[p,4]
			S[el,p,1,2]=tmpData[p,5]
			S[el,p,2,1]=tmpData[p,5]
		
		elLabelU[el]=elLabel[i]
		el+=1

	return S,elLabelU,nEl,nInt

def GetStrain(root,frame,elSetName):
	#returns stress tensor for all elements in set elSet stress is accessed by the dictionary element label
	#array locations follow [element x integration point x data ] where data is in tensor form
	elSet = root.elementSets[elSetName]
	field = frame.fieldOutputs['EE'].getSubset(region=elSet,position=INTEGRATION_POINT)
	
	dataGauss = np.array(field.bulkDataBlocks[0].data,dtype='float64') #s11,s22,s33,s12,s13,s23 ordered
	elLabel = np.array(field.bulkDataBlocks[0].elementLabels,dtype='int64')
	intLabel = np.array(field.bulkDataBlocks[0].integrationPoints,dtype='int8')

	nEl=len(np.unique(elLabel))
	nData=len(intLabel)
	nInt=np.amax(intLabel)
	
	EE=np.zeros((nEl,nInt,3,3),dtype='float64')
	elLabelU=np.zeros((nEl),dtype='int64')

	el=0
	for i in range(0,nData,nInt):
		tmpData=dataGauss[i:i+nInt]
		
		for p in range(0,nInt,1): 
			EE[el,p,0,0]=tmpData[p,0]
			EE[el,p,1,1]=tmpData[p,1]
			EE[el,p,2,2]=tmpData[p,2]
			EE[el,p,0,1]=tmpData[p,3]
			EE[el,p,1,0]=tmpData[p,3]
			EE[el,p,0,2]=tmpData[p,4]
			EE[el,p,2,0]=tmpData[p,4]
			EE[el,p,1,2]=tmpData[p,5]
			EE[el,p,2,1]=tmpData[p,5]
		
		elLabelU[el]=elLabel[i]
		el+=1

	return EE,elLabelU,nEl,nInt
	
def GetW(S,EE,nEl,nInt):
	W=np.zeros((nEl,nInt),dtype='float64')
	#returns strain energy for a linear elastic material
	for el in range(0,nEl,1):
		for p in range(0,nInt,1):
			for i in range(0,3,1):
				for j in range(0,3,1):
					W[el,p]=W[el,p]+0.5*(S[el,p,i,j]*EE[el,p,i,j])
	return W				
	
	# Abaqus does not compute nodal values such as displacement for the 
	# element nodal positions. Rebuilding the element nodal field data is needed 
	# for the shape functions to be used
	
	#The coordinates can be obtained from a Scalarfield when COORD are save; 
	#however, the root assembly saves COORD with node definitions and we can reduce the odb size
    #by not using COORD
	
	#Build the element connectivity matrix
	connectivityMat=np.zeros((len(elements), 20))
	cnt=0
	for el in elements:
		connectivityMat[cnt,:]=el.connectivity
		cnt+=1
	
	#convert the connectivity to zero based index and reshape to linear array
	connectivityMat = connectivityMat.astype(int)-1
	connectivity=np.reshape(connectivityMat,(-1,1))
	
	#Get the element nodal values
	#print connectivity
	#print len(nodes)
	dataElementNodal=np.zeros((len(connectivity)),dtype='float64')
	for i in range(0,len(connectivity),1):
		dataElementNodal[i] = nodes[connectivity[i][0]].coordinates[component]
		
	#Remove dimensions of size 1, reshape to #nodes/element * #element array
	dataElementNodal = np.squeeze(dataElementNodal)
	dataElementNodal = np.reshape(dataElementNodal,(len(elements),-1))
	dataElementNodal = np.transpose(dataElementNodal)
	return [dataElementNodal,connectivityMat]	

def GetdudX(root,partInstance,frame,allNodes,nodeSetName,elSetName): 
	#Returns the spatial derivative of the scalarField with respect to global coordinates
	nodes=root.nodeSets[nodeSetName].nodes[0]
	elements=root.elementSets[elSetName].elements[0]
	
	elLabel = [el.label for el in elements]
	
	nElements=len(elements)
	nNodes=len(elements[0].connectivity)
	nPoints=GetNumIntegrationPoints(elements[0].type)
	
	#print 'get nodal coordinates in element nodal'
	#Get the nodal coordinates and map to element nodal coordinates (same thing but data structure is different)
	[ENCoord1,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,0,elements)	
	[ENCoord2,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,1,elements)
	[ENCoord3,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,2,elements)
	
	#print 'get displacements in element nodal'
	#Get the nodal data and map to element nodal data.
	#elSet = root.elementSets[elSetName]
	field = frame.fieldOutputs['U'].getSubset(position=NODAL)
	SFU1=field.getScalarField(componentLabel='U1') 
	SFU2=field.getScalarField(componentLabel='U2') 
	SFU3=field.getScalarField(componentLabel='U3') 
	
	keys=root.instances.keys()
	cnt=0
	for key in keys:
		if key==partInstance:
			instanceNumber=cnt
		cnt+=1
		
	[NU1,ENU1,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU1,instanceNumber,elements)
	[NU2,ENU2,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU2,instanceNumber,elements)
	[NU3,ENU3,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU3,instanceNumber,elements)
	
	#ENCoord1=ENCoord1+ENU1
	#ENCoord2=ENCoord2+ENU2
	#ENCoord3=ENCoord3+ENU3
	
	#interpolates var between element nodal and integrations points
	[points,weights]=Gauss_Guad_3d(3) #3 is the number of quadrature points along each dimension
	
	#get the natural nodal coordinates for the element
	Bi=C3D20_nodal_coordinates()
	
	#print 'get dhdr'
	#evaluate the derivative of the shape functions for the points we want to interpolate/extrapolate data to 
	dhdr=np.zeros((nPoints,nNodes,3),dtype='float64')#
	

	#For each integration point, get the derivative of the shape functions with respect to natural local coordinates
	for i in range(0,nPoints,1):#
		r = points[i,:]
		tmp = C3D20_Shape_Derivatives(r,Bi) #20x3 array
		#dhdr = np.squeeze(tmp)
		dhdr[i,:,:]=tmp #nPointx20x3 array
	
	#print 'get J'
	##Build the Jacobian for each of the integration points n integration points x elements array
	J=np.zeros((nPoints,nElements, 3,3),dtype='float64')
	J[:,:,0,0]= np.dot(dhdr[:,:,0],ENCoord1)	#npoints x nelement array
	J[:,:,0,1]= np.dot(dhdr[:,:,1],ENCoord1)
	J[:,:,0,2]= np.dot(dhdr[:,:,2],ENCoord1)	
	J[:,:,1,0]= np.dot(dhdr[:,:,0],ENCoord2)	
	J[:,:,1,1]= np.dot(dhdr[:,:,1],ENCoord2)
	J[:,:,1,2]= np.dot(dhdr[:,:,2],ENCoord2)
	J[:,:,2,0]= np.dot(dhdr[:,:,0],ENCoord3)	
	J[:,:,2,1]= np.dot(dhdr[:,:,1],ENCoord3)
	J[:,:,2,2]= np.dot(dhdr[:,:,2],ENCoord3)
	
	detJ=np.zeros((nElements,nPoints),dtype='float64')
	Jinvp=np.zeros((nPoints, 3,3),dtype='float64')
	dudx=np.zeros((nElements,nPoints,3,3),dtype='float64')
	I=np.eye(3);
	
	#Initialize dictionaries for saved element data
	#print '=====start solution====='	
	for el in range(0,nElements,1):
		for p in range(0,nPoints,1): #p is looping over integration points in element elLabel[el]
			detJ[el,p]=np.linalg.det(J[p,el,:,:])
			Jinvp[p,:,:]=np.linalg.inv(J[p,el,:,:])	
			tmp=np.dot(dhdr[p,:,:],Jinvp[p,:,:]) #nNodes x 3
			tmp=np.transpose(tmp)
			dudx[el,p,0,:]=np.dot(tmp,ENU1[:,el])
			dudx[el,p,1,:]=np.dot(tmp,ENU2[:,el])
			dudx[el,p,2,:]=np.dot(tmp,ENU3[:,el])
			
	return 	dudx, detJ, elLabel

def GetqLinear(nSetQ0,nSetSlice,firstCrackNodeLabel,root,allNodes,elSetName,isSymm):
	
	nodesQ0=root.nodeSets[nSetQ0].nodes[0] #Outside nodes
	nodesSlice=root.nodeSets[nSetSlice].nodes[0]
	elements=root.elementSets[elSetName].elements[0]
	
	#build the element node connectivity since we want Q defined at 
	#element nodal locations for compute the gradient
	connectivityMat=np.zeros((len(elements), len(elements[0].connectivity)))
	cnt=0
	for el in elements:
		connectivityMat[cnt,:]=el.connectivity
		cnt+=1
	
	#reshape connectivity to linear array
	connectivityMat = connectivityMat.astype(int)
	connectivity=np.reshape(connectivityMat,(-1,1))
	lenConnectivty=len(connectivity)
	
	#convert connectivity to a dictionary so node labels can be used to index position
	conn={}
	for n in connectivity: 
		conn[n[0]]=-1
	
	#reconstruct crack node front going towards 0 in z
	nFirstCrack=allNodes[firstCrackNodeLabel-1]
	posAxis=[]
	posAxis.append(nFirstCrack.coordinates[0])
	posAxis.append(nFirstCrack.coordinates[1])
	
	CFnSet=[]
	CFPosz=[]
	for n in nodesSlice: 
		if n.coordinates[0]==posAxis[0] and n.coordinates[1]==posAxis[1]:
			CFnSet.append(n.label)
			CFPosz.append(n.coordinates[2])
			
	CFnSet,ind=np.unique(np.array(CFnSet), return_index=True)
	CFPosz=np.array(CFPosz)
	CFPosz=CFPosz[ind]
	ind=np.argsort(CFPosz)
	CFnSet=CFnSet[ind]
	CFnSet=CFnSet[::-1]
	CFPosz=CFPosz[ind]
	CFPosz=CFPosz[::-1]
	rPoszRelTol=(CFPosz[0]-CFPosz[1])/8.0
	
	if CFPosz[-1]==0 and len(CFnSet)==3:
		L=[0.0,0.5,1.0]
		PoszOut=0
	elif len(CFnSet)==3:
		L=[1.0,0.5,0.0]
		PoszOut=CFPosz[0]
	else: 
		L=[0.0,0.5,1.0,0.5,0.0]
		PoszOut=CFPosz[2]

		
	intLcL=GetTrapIntLc(CFPosz,L) #make this subsample q 
		
	for p in range(0,len(CFPosz)):
		#Initialize lists for boundary nodes
		#print L[p]
		xb=[]
		yb=[]
		xyb=[]
		thetab=[]
		for i in range(0,len(nodesQ0),1):
			n=nodesQ0[i]
			xtmp=n.coordinates[0]-posAxis[0]
			ytmp=n.coordinates[1]-posAxis[1]
			xytmp=[xtmp, ytmp]
			if isclose(n.coordinates[2],CFPosz[p],rPoszRelTol) and not any(n==xytmp for n in xyb): #no repeat nodes
				xb.append(xtmp)
				yb.append(ytmp)
				xyb.append(xytmp)
		#find the angle for polar coordinates
		for i in range(0,len(xb),1):
			thetab.append(atan2(yb[i],xb[i]))
			if thetab[i]<0:
				thetab[i]=thetab[i]+2*math.pi
		
		#Sort by angle	
		ind=np.argsort(np.array(thetab))
		xb=np.array(xb)
		xb=list(xb[ind])
		yb=np.array(yb)
		yb=list(yb[ind])
		thetab=np.array(thetab)
		thetab=list(thetab[ind])
	
		#Make the boundary so it is closed 
		if not len(xb)==0 and not isSymm:
			xb.append(xb[0])
			yb.append(yb[0])
			thetab.append(thetab[0]+2*math.pi)
		
		
		#build the slope for boundary 
		mb=[]
		for i in range(0,len(xb)-1,1): 
			#print i,yb[i],yb[i+1],xb[i],xb[i+1]
			if xb[i]==xb[i+1]:
				mb.append(np.nan)
			else:
				mb.append((yb[i]-yb[i+1])/(xb[i]-xb[i+1]))
		
		#loop over nodes that can be set 0<x<=1
		xn=[]
		yn=[]
		labeln=[]
		for i in range(0,len(nodesSlice)-1,1):
			n=nodesSlice[i]
			if isclose(n.coordinates[2],CFPosz[p],rPoszRelTol) and not any(lab==n.label for lab in labeln):
				xn.append(n.coordinates[0]-posAxis[0])
				yn.append(n.coordinates[1]-posAxis[1])
				labeln.append(n.label)
				
		#Interpolate Q 
		for i in range(0,len(yn),1):
			rn=sqrt(yn[i]*yn[i]+xn[i]*xn[i])
			if L[p]==0:
				conn[labeln[i]]=np.array(L[p])
			elif rn==0: 
				#On the node crack
				conn[labeln[i]]=np.array(L[p])
			else:	
				thetan=atan2(yn[i],xn[i])
				if thetan<0:
					thetan=thetan+2*math.pi
			
				#find where to interpolate
				for j in range(0,len(xb),1): 
					if thetab[j]==thetan:
						rQ0=sqrt(xb[j]*xb[j]+yb[j]*yb[j])
						conn[labeln[i]]=np.array(L[p]*(1-rn/rQ0))
						break
					elif thetab[j]>thetan:
						ind=j-1
						if xn[i] !=0:
							mn=yn[i]/xn[i]
							if np.isnan(mb[ind]):
								#print ind,yb[ind],yb[ind+1],xb[ind],xb[ind+1]
								xQ0=xb[ind]
							else:
								xQ0=-mb[ind]/(mn-mb[ind])*xb[ind]+yb[ind]/(mn-mb[ind])
							yQ0=mn*xQ0
							rQ0=sqrt(xQ0*xQ0+yQ0*yQ0)
						else:
							rQ0=sqrt(xb[ind]*xb[ind]+yb[ind]*yb[ind])

						conn[labeln[i]]=np.array(L[p]*(1-rn/rQ0))
						break 

						
	#map everything back to dataElementNodal
	dataElementNodal=np.zeros((lenConnectivty),dtype='float64')
	#fobj = open('debug_q.txt', 'w')
	for i in range(0,lenConnectivty): 
		#id=connectivity[i][0]
		#crd=allNodes[id-1].coordinates
		#label=allNodes[id-1].label
		#fobj.write('%d,%f,%f,%f,%f\n' % (label,crd[0],crd[1],crd[2],conn[id]))
		dataElementNodal[i]=conn[connectivity[i][0]]
		
	#fobj.close()
	if any(x==-1 for x in conn):
		print '=================' 
		print 'not all of the q could be set appriately!! You must fix before J can be calculated'
		print '=================' 
		
		
	#Remove dimensions of size 1, reshape to #nodes/element * #element array
	dataElementNodal = np.squeeze(dataElementNodal)
	dataElementNodal = np.reshape(dataElementNodal,(len(elements),-1))
	dataElementNodal = np.transpose(dataElementNodal)
	
	#print dataElementNodal
	
	#print dataElementNodal
	return dataElementNodal,intLcL,PoszOut

def GetqNew(nSetQ0,nSetQ0p5,nSetQ1,nSetSlice,firstCrackNodeLabel,root,allNodes,elSetName,isSymm):
	
	nodesQ0=root.nodeSets[nSetQ0].nodes[0] #Outside nodes
	nodesQ1=root.nodeSets[nSetQ1].nodes[0] #Inside nodes
	nodesQ0p5=root.nodeSets[nSetQ0p5].nodes[0] #In between nodes
	nodesSlice=root.nodeSets[nSetSlice].nodes[0]
	elements=root.elementSets[elSetName].elements[0]
	
	#build the element node connectivity since we want Q defined at 
	#element nodal locations for compute the gradient
	connectivityMat=np.zeros((len(elements), len(elements[0].connectivity)))
	cnt=0
	for el in elements:
		connectivityMat[cnt,:]=el.connectivity
		cnt+=1
	
	#reshape connectivity to linear array
	connectivityMat = connectivityMat.astype(int)
	connectivity=np.reshape(connectivityMat,(-1,1))
	lenConnectivty=len(connectivity)
	
	#convert connectivity to a dictionary so node labels can be used to index position
	conn={}
	for n in connectivity: 
		conn[n[0]]=-1
	
	#reconstruct crack node front going towards 0 in z
	nFirstCrack=allNodes[firstCrackNodeLabel-1]
	posAxis=[]
	posAxis.append(nFirstCrack.coordinates[0])
	posAxis.append(nFirstCrack.coordinates[1])
	
	CFnSet=[]
	CFPosz=[]
	for n in nodesSlice: 
		if n.coordinates[0]==posAxis[0] and n.coordinates[1]==posAxis[1]:
			CFnSet.append(n.label)
			CFPosz.append(n.coordinates[2])
			
	CFnSet,ind=np.unique(np.array(CFnSet), return_index=True)
	CFPosz=np.array(CFPosz)
	CFPosz=CFPosz[ind]
	ind=np.argsort(CFPosz)
	CFnSet=CFnSet[ind]
	CFnSet=CFnSet[::-1]
	CFPosz=CFPosz[ind]
	CFPosz=CFPosz[::-1]
	rPoszRelTol=(CFPosz[0]-CFPosz[1])/8.0
	
	if CFPosz[-1]==0 and len(CFnSet)==3:
		L=[0.0,0.5,1.0]
		PoszOut=0
	elif len(CFnSet)==3:
		L=[1.0,0.5,0.0]
		PoszOut=CFPosz[0]
	else: 
		L=[0.0,0.5,1.0,0.5,0.0]
		PoszOut=CFPosz[2]

		
	intLcL=GetTrapIntLc(CFPosz,L) #make this subsample q 
		
	for p in range(0,len(CFPosz)):
		#Initialize lists for boundary nodes
		labelq0=[]
		for i in range(0,len(nodesQ0),1):
			n=nodesQ0[i]
			if isclose(n.coordinates[2],CFPosz[p],rPoszRelTol) and not any(lab==n.label for lab in labelq0):
				labelq0.append(n.label)
				
		for i in range(0,len(labelq0),1):
				conn[labelq0[i]]=np.array(0.0)
				
		#Initialize lists for inbetween nodes 
		labelq0p5=[]
		for i in range(0,len(nodesQ0p5),1):
			n=nodesQ0p5[i]
			if isclose(n.coordinates[2],CFPosz[p],rPoszRelTol) and not any(lab==n.label for lab in labelq0p5):
				labelq0p5.append(n.label)
		
		for i in range(0,len(labelq0p5),1):
				conn[labelq0p5[i]]=np.array(0.5*L[p])
		
		#Initialize lists for inner nodes
		labelq1=[]
		for i in range(0,len(nodesQ1),1):
			n=nodesQ1[i]
			if isclose(n.coordinates[2],CFPosz[p],rPoszRelTol) and not any(lab==n.label for lab in labelq1):
				labelq1.append(n.label)
				
		for i in range(0,len(labelq1),1):
				conn[labelq1[i]]=np.array(1.0*L[p])	
								
	#map everything back to dataElementNodal
	dataElementNodal=np.zeros((lenConnectivty),dtype='float64')
	#fobj = open('debug_q.txt', 'w')
	for i in range(0,lenConnectivty): 
		#id=connectivity[i][0]
		#crd=allNodes[id-1].coordinates
		#label=allNodes[id-1].label
		#fobj.write('%d,%f,%f,%f,%f\n' % (label,crd[0],crd[1],crd[2],conn[id]))
		dataElementNodal[i]=conn[connectivity[i][0]]
		
	#fobj.close()
	if any(x==-1 for x in conn):
		print '=================' 
		print 'not all of the q could be set appriately!! You must fix before J can be calculated'
		print '=================' 
		raise
		
		
	#Remove dimensions of size 1, reshape to #nodes/element * #element array
	dataElementNodal = np.squeeze(dataElementNodal)
	dataElementNodal = np.reshape(dataElementNodal,(len(elements),-1))
	dataElementNodal = np.transpose(dataElementNodal)
	
	#print dataElementNodal
	
	#print dataElementNodal
	return dataElementNodal,intLcL,PoszOut
		
def Getq(nSetQ0,nSetQ0p5,nSetQ1,allNodes,AxisPosition1,AxisPosition2,AxisPosition3,elSetName):
	
	nodesQ0=root.nodeSets[nSetQ0].nodes[0]
	nodesQ0p5=root.nodeSets[nSetQ0p5].nodes[0]
	nodesQ1=root.nodeSets[nSetQ1].nodes[0]
	elements=root.elementSets[elSetName].elements[0]
	
	connectivityMat=np.zeros((len(elements), len(elements[0].connectivity)))
	cnt=0
	for el in elements:
		connectivityMat[cnt,:]=el.connectivity
		cnt+=1
	
	#reshape connectivity to linear array
	connectivityMat = connectivityMat.astype(int)
	connectivity=np.reshape(connectivityMat,(-1,1))
	lenConnectivty=len(connectivity)
	
	#convert connectivity to a dictionary so node labels can be used to index position
	conn={}
	for n in connectivity: 
		conn[n[0]]=-1
	
	#using the node labels from each set assign 0, 0.5 or 1 	
	fobj = open('Q0.txt', 'w')
	for n in nodesQ0:
		if isclose(n.coordinates[2],AxisPosition1):
			conn[n.label]=0.0
			fobj.write('%f,%f,%f\n' % (n.coordinates[0],n.coordinates[1],n.coordinates[2]))
			#print n.label,n.coordinates[0],n.coordinates[1],n.coordinates[2]
		elif isclose(n.coordinates[2],AxisPosition2):
			conn[n.label]=0.0
		elif isclose(n.coordinates[2],AxisPosition3):
			conn[n.label]=0.0
		else:
			conn[n.label]=0.0
			
	fobj.close()
	
	for n in nodesQ0p5:
		if isclose(n.coordinates[2],AxisPosition1):
			conn[n.label]=0.5
			#print n.label,n.coordinates[0],n.coordinates[1],n.coordinates[2]
		elif isclose(n.coordinates[2],AxisPosition2):
			conn[n.label]=0.0
		elif isclose(n.coordinates[2],AxisPosition3):
			conn[n.label]=0.0
		else:
			conn[n.label]=0.0
	for n in nodesQ1: 
		if isclose(n.coordinates[2],AxisPosition1):
			conn[n.label]=1.0
			#print n.label,n.coordinates[0],n.coordinates[1],n.coordinates[2]
		elif isclose(n.coordinates[2],AxisPosition2):
			conn[n.label]=0.5
		elif isclose(n.coordinates[2],AxisPosition3):
			conn[n.label]=0.0
		else: 
			conn[n.label]=0.0
		#conn[n.label]=1.0
		if n.label==520:
			conn[n.label]=0.0
		elif n.label==34777:
			conn[n.label]=0.5
		elif n.label==17:
			conn[n.label]=1.0
			
	#map everything back to dataElementNodal
	dataElementNodal=np.zeros((lenConnectivty),dtype='float64')
	fobj = open('debug_q.txt', 'w')
	for i in range(0,lenConnectivty): 
		id=connectivity[i][0]
		crd=allNodes[id-1].coordinates
		label=allNodes[id-1].label
		fobj.write('%d,%f,%f,%f,%f\n' % (label,crd[0],crd[1],crd[2],conn[id]))
		dataElementNodal[i]=conn[connectivity[i][0]]
		
	fobj.close()
	#Remove dimensions of size 1, reshape to #nodes/element * #element array
	dataElementNodal = np.squeeze(dataElementNodal)
	dataElementNodal = np.reshape(dataElementNodal,(len(elements),-1))
	dataElementNodal = np.transpose(dataElementNodal)

	#print dataElementNodal
	return dataElementNodal

def GetLamdaq(nSetP,elSetName):
	
	nodesP=root.nodeSets[nSetP].nodes[0]
	elements=root.elementSets[elSetName].elements[0]
	
	connectivityMat=np.zeros((len(elements), len(elements[0].connectivity)))
	cnt=0
	for el in elements:
		connectivityMat[cnt,:]=el.connectivity
		cnt+=1
	
	#reshape connectivity to linear array
	connectivityMat = connectivityMat.astype(int)
	connectivity=np.reshape(connectivityMat,(-1,1))
	lenConnectivty=len(connectivity)
	
	#convert connectivity to a dictionary so node labels can be used to index position
	conn={}
	for n in connectivity: 
		conn[n[0]]=0
	
	#using the node labels from each set assign 0, 0.5 or 1 	
	for n in nodesP:
		conn[n.label]=1
		
	#map everything back to dataElementNodal
	dataElementNodal=np.zeros((lenConnectivty),dtype='float64')
	for i in range(0,lenConnectivty): 
		#if conn[connectivity[i][0]]==-1:
		#	#print connectivity[i][0]
		dataElementNodal[i]=conn[connectivity[i][0]]
	
	#Remove dimensions of size 1, reshape to #nodes/element * #element array
	dataElementNodal = np.squeeze(dataElementNodal)
	dataElementNodal = np.reshape(dataElementNodal,(len(elements),-1))
	dataElementNodal = np.transpose(dataElementNodal)

	#print dataElementNodal
	return dataElementNodal	
	
def GetdqdX(root,frame,allNodes,nSetQ0,nSetQ0p5,nSetQ1,firstCrackNodeLabel,nodeSetName,elSetName,isSymm): 
	#Returns the spatial derivative of the scalarField with respect to global coordinates
	nodes=root.nodeSets[nodeSetName].nodes[0]
	elements=root.elementSets[elSetName].elements[0]
	elLabel=[el.label for el in elements]
	
	nElements=len(elements)
	nNodes=len(elements[0].connectivity)
	nPoints=GetNumIntegrationPoints(elements[0].type)
	
	#print 'get nodal coordinates in element nodal'
	#Get the nodal coordinates and map to element nodal coordinates (same thing but data structure is different)
	[ENCoord1,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,0,elements)	
	[ENCoord2,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,1,elements)
	[ENCoord3,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,2,elements)
	
	#field = frame.fieldOutputs['U'].getSubset(position=NODAL)
	#SFU1=field.getScalarField(componentLabel='U1') 
	#SFU2=field.getScalarField(componentLabel='U2') 
	#SFU3=field.getScalarField(componentLabel='U3') 
	#
	#[NU1,ENU1,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU1,1,elements)
	#[NU2,ENU2,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU2,1,elements)
	#[NU3,ENU3,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU3,1,elements)
	
	#ENCoord1=ENCoord1+ENU1
	#ENCoord2=ENCoord2+ENU2
	#ENCoord3=ENCoord3+ENU3
	
	
	
	#Q is function defined as 1 on nSetQ1, 0.5 on nSetQ0p5,and 0 on nSetQ0
	#This function returns Q in the element nodal format
	#AxisPosition1=allNodes[17-1].coordinates[2]
	#AxisPosition2=allNodes[34777-1].coordinates[2]
	#AxisPosition3=allNodes[520-1].coordinates[2]
	#ENQ2=Getq(nSetQ0,nSetQ0p5,nSetQ1,allNodes,AxisPosition1,AxisPosition2,AxisPosition3,elSetName)
	#ENQ2=GetLamdaq(nSetP,elSetName)
	
	#ENQ2,intLcL,posz=GetqLinear(nSetQ0,nodeSetName,firstCrackNodeLabel,root,allNodes,elSetName,isSymm) #is good
	ENQ2,intLcL,posz=GetqNew(nSetQ0,nSetQ0p5,nSetQ1,nodeSetName,firstCrackNodeLabel,root,allNodes,elSetName,isSymm)
	#for i in range(0,nElements):
	#	print 'El#',elLabel[i],ENQ2[:,i]
	
	
	#interpolates var between element nodal and integrations points
	[points,weights]=Gauss_Guad_3d(3) #3 is the number of quadrature points along each dimension
	
	#get the natural nodal coordinates for the element
	Bi=C3D20_nodal_coordinates()
	
	#print 'get dhdr'
	#evaluate the derivative of the shape functions for the points we want to interpolate/extrapolate data to 
	dhdr=np.zeros((nPoints,nNodes,3),dtype='float64')#
	

	#For each integration point, get the derivative of the shape functions with respect to natural local coordinates
	for i in range(0,nPoints,1):#
		r = points[i,:]
		tmp = C3D20_Shape_Derivatives(r,Bi) #20x3 array
		#dhdr = np.squeeze(tmp)
		dhdr[i,:,:]=tmp #nPointx20x3 array
	
	#print 'get J'
	##Build the Jacobian for each of the integration points n integration points x elements array
	J=np.zeros((nPoints,nElements, 3,3),dtype='float64')
	J[:,:,0,0]= np.dot(dhdr[:,:,0],ENCoord1)	#npoints x nelement array
	J[:,:,0,1]= np.dot(dhdr[:,:,1],ENCoord1)
	J[:,:,0,2]= np.dot(dhdr[:,:,2],ENCoord1)	
	J[:,:,1,0]= np.dot(dhdr[:,:,0],ENCoord2)	
	J[:,:,1,1]= np.dot(dhdr[:,:,1],ENCoord2)
	J[:,:,1,2]= np.dot(dhdr[:,:,2],ENCoord2)
	J[:,:,2,0]= np.dot(dhdr[:,:,0],ENCoord3)	
	J[:,:,2,1]= np.dot(dhdr[:,:,1],ENCoord3)
	J[:,:,2,2]= np.dot(dhdr[:,:,2],ENCoord3)
	
	detJ=np.zeros((nElements,nPoints),dtype='float64')
	Jinvp=np.zeros((nPoints, 3,3),dtype='float64')
	dqdx=np.zeros((nElements,nPoints,3),dtype='float64')
	I=np.eye(3);
	
	#Initialize dictionaries for saved element data
	#print '=====start solution====='	
	for el in range(0,nElements,1):
		for p in range(0,nPoints,1): #p is looping over integration points in element elLabel[el]
			detJ[el,p]=np.linalg.det(J[p,el,:,:])
			Jinvp[p,:,:]=np.linalg.inv(J[p,el,:,:])	
			tmp=np.dot(dhdr[p,:,:],Jinvp[p,:,:]) #nNodes x 3
			tmp=np.transpose(tmp)
			dqdx[el,p,:]=np.dot(tmp,ENQ2[:,el])	
			
	return 	dqdx,intLcL,posz,elLabel

def GetdetJac(root,partInstance,frame,allNodes,nodeSetName,elSetName): 
	#Returns the spatial derivative of the scalarField with respect to global coordinates
	nodes=root.nodeSets[nodeSetName].nodes[0]
	elements=root.elementSets[elSetName].elements[0]
	
	elLabel = [el.label for el in elements]
	
	nElements=len(elements)
	nNodes=len(elements[0].connectivity)
	nPoints=GetNumIntegrationPoints(elements[0].type)
	
	#print 'get nodal coordinates in element nodal'
	#Get the nodal coordinates and map to element nodal coordinates (same thing but data structure is different)
	[ENCoord1,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,0,elements)	
	[ENCoord2,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,1,elements)
	[ENCoord3,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,2,elements)
	
	#print 'get displacements in element nodal'
	#Get the nodal data and map to element nodal data.
	#elSet = root.elementSets[elSetName]
	field = frame.fieldOutputs['U'].getSubset(position=NODAL)
	SFU1=field.getScalarField(componentLabel='U1') 
	SFU2=field.getScalarField(componentLabel='U2') 
	SFU3=field.getScalarField(componentLabel='U3') 
	
	keys=root.instances.keys()
	cnt=0
	for key in keys:
		if key==partInstance:
			instanceNumber=cnt
		cnt+=1
		
	[NU1,ENU1,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU1,instanceNumber,elements)
	[NU2,ENU2,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU2,instanceNumber,elements)
	[NU3,ENU3,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU3,instanceNumber,elements)
	
	#Use to get the mapping to current element volume
	#ENCoord1=ENCoord1+ENU1
	#ENCoord2=ENCoord2+ENU2
	#ENCoord3=ENCoord3+ENU3
	
	#interpolates var between element nodal and integrations points
	[points,weights]=Gauss_Guad_3d(3) #3 is the number of quadrature points along each dimension
	
	#get the natural nodal coordinates for the element
	Bi=C3D20_nodal_coordinates()
	
	#print 'get dhdr'
	#evaluate the derivative of the shape functions for the points we want to interpolate/extrapolate data to 
	dhdr=np.zeros((nPoints,nNodes,3),dtype='float64')#
	

	#For each integration point, get the derivative of the shape functions with respect to natural local coordinates
	for i in range(0,nPoints,1):#
		r = points[i,:]
		tmp = C3D20_Shape_Derivatives(r,Bi) #20x3 array
		#dhdr = np.squeeze(tmp)
		dhdr[i,:,:]=tmp #nPointx20x3 array
	
	#print 'get J'
	##Build the Jacobian for each of the integration points n integration points x elements array
	J=np.zeros((nPoints,nElements, 3,3),dtype='float64')
	J[:,:,0,0]= np.dot(dhdr[:,:,0],ENCoord1)	#npoints x nelement array
	J[:,:,0,1]= np.dot(dhdr[:,:,1],ENCoord1)
	J[:,:,0,2]= np.dot(dhdr[:,:,2],ENCoord1)	
	J[:,:,1,0]= np.dot(dhdr[:,:,0],ENCoord2)	
	J[:,:,1,1]= np.dot(dhdr[:,:,1],ENCoord2)
	J[:,:,1,2]= np.dot(dhdr[:,:,2],ENCoord2)
	J[:,:,2,0]= np.dot(dhdr[:,:,0],ENCoord3)	
	J[:,:,2,1]= np.dot(dhdr[:,:,1],ENCoord3)
	J[:,:,2,2]= np.dot(dhdr[:,:,2],ENCoord3)
	
	detJ=np.zeros((nElements,nPoints),dtype='float64')
	
	#Initialize dictionaries for saved element data
	#print '=====start solution====='	
	for el in range(0,nElements,1):
		for p in range(0,nPoints,1): #p is looping over integration points in element elLabel[el]
			detJ[el,p]=np.linalg.det(J[p,el,:,:])
		
	return 	detJ

def GetIntegralofShapeP(root,nSetQ1):
	
	nodes=root.nodeSets[nSetQ1].nodes[0]
	nNodes=len(nodes)
	print 'nnodes',nNodes
	points=np.zeros((nNodes, 3),dtype='float64')
	for i in range(0,nNodes,1): 
		points[i,0]=nodes[i].coordinates[0]
		points[i,1]=nodes[i].coordinates[1]
		points[i,2]=nodes[i].coordinates[2]
		print 'z_dir',points[i,2]
	#get the natural nodal coordinates for the element
	Bi=C3D20_nodal_coordinates()
	
	
	#evaluate the shape functions for the points we want to interpolate/extrapolate data to 
	h=np.zeros((len(points), 20),dtype='float64')
	#print points
	for i in range(0,len(points),1):
		r = points[i,:]
		tmp = C3D20_Shape(r,Bi)
		tmp = np.squeeze(tmp)
		h[i,:]=tmp
	
	print h
	raise

def GetTrapIntLc(CFPosz,L):
	val=0
	for i in range(0,len(CFPosz)-1,1):
		val+=abs(CFPosz[i+1]-CFPosz[i])*(L[i]+L[i+1])/2
	return val

def CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,nodeLabelTip,isSymm,odb,partInstance): 
	#inputs:
	#an odb with node sets and element made by BuildElementAndNodeSets
	#nodeSet names for q0,q0.5,q1,allNodes in slice/contour
	#elementSet name for slice/contour
	#frame for computation, must include U,S, and EE (the mechanical strains
	#
	#output: 
	# J(s) - energy release rate along the crack front
	
	#Get components of odb
	root=odb.rootAssembly
	#Get elements
	part=root.instances[partInstance]
	elements=part.elements

	#Get nodes
	allNodes = root.instances[partInstance].nodes 
	
	#Get the frames in the step 
	steps=odb.steps

	# Get the step keys
	allSteps = steps.keys()

	# Get current step object and the number of increments (frameLen) in step
	step = steps[allSteps[stepNumber]]

	# Get frames in step
	frames=step.frames

	#Initialize J data container 
	JAll=np.zeros((len(slices)),dtype='float64')
	
	#loop over frames
	for frameId in frameNumbers:
		#Get the frame and time
		frame = frames[frameId]
		TTAU = frame.frameValue
		
		#Check that the necessary field variables exist at the appropriate locations
		CheckFieldExists(frame,'U','NODAL') #displacements
		CheckFieldExists(frame,'EE','INTEGRATION_POINT') #mechanical strain 
		CheckFieldExists(frame,'S','INTEGRATION_POINT') #stress 
	
	
		#open file to write Js to
		fname='Js-at-time-'+str(TTAU)+'.txt'
		fobj = open(fname, 'w')
		#write empty header
		fobj.write('%f' % (float('nan')))
			
		#loop over each contour level to be computed 
		for contourId in contours:	
			sliceCnt=0
			print 'Processing Contour: ', contourId
			for sliceId in slices:
				print 'slice #:',sliceId
				##build the node set and element set names 
				##========================================
				nSetSlice=SetPrefix+'-contour-'+str(contourId)+'-slice-'+str(sliceId)
				nSetQ0=nSetSlice+'-Q0'
				nSetQ0p5=nSetSlice+'-Q0p5'
				nSetQ1=nSetSlice+'-Q1'
				elSetSlice=nSetSlice
				
				#Check that node and element sets exist	(ensures only that they exist, not that they are valid..)
				CheckSetExists(root,nSetQ0,'node')
				CheckSetExists(root,nSetQ0p5,'node')
				CheckSetExists(root,nSetQ1,'node')
				CheckSetExists(root,nSetSlice,'node')
				CheckSetExists(root,elSetSlice,'element')

				##Get for each element and at each integration points: sij, du/dX, W, dQ/dX, det(jacobian), wp
				##=============================================================================================
				#Note: data arrays are stored per element per integration point
				#Stress Sij 
				S,SElLabels,nEl,nInt = GetStress(root,frame,elSetSlice)

				#Get strain EEij 
				EE,EEElLabels,nEl,nInt = GetStrain(root,frame,elSetSlice)
				
				#Mechanical strain energy density, W=U (stored by Abaqus in SENER and computed for linear elasticity as U=1/2*SijEEij)
				W = GetW(S,EE,nEl,nInt) 
				
				#Get du/dX, where X is the reference coordinates and u is displacement in the current frame. 
				#The Jacobian is also computed when calculating the derivatives and is returned here
				dudX,detJac,dudXElLabels = GetdudX(root,partInstance,frame,allNodes,nSetSlice,elSetSlice)
				
				#Get dqdX, a weighting term defined as a pyramid function similar to what Abaqus uses
				dqdX,intLcL,slicePos,dudXElLabels=GetdqdX(root,frame,allNodes,nSetQ0,nSetQ0p5,nSetQ1,nodeLabelTip,nSetSlice,elSetSlice,isSymm)
				
				#print positions of each Js value as header
				if contourId==contours[0]:
					fobj.write(',%f' % (slicePos))
				
				#Get the Jacobian for integration
				detJac=GetdetJac(root,partInstance,frame,allNodes,nSetSlice,elSetSlice)
				
				#Get Gauss integrations weights
				_,wp = Gauss_Guad_3d(3)
				wp = np.reshape(wp,(-1))
				
				##Perform quadrature
				##====================
				Jbar=0
				krd2=np.zeros((3),dtype='float64')
				krd2[1]=1
				for el in range(0,nEl,1):
					for p in range(0,nInt,1):
						Jbar=Jbar+np.dot((np.dot(S[el,p,:,:],dudX[el,p,:,1])-W[el,p]*krd2),dqdX[el,p,:])*detJac[el,p]*wp[p]
				
				if isSymm: 
					JAll[sliceCnt]=2*Jbar/intLcL
				else: 
					JAll[sliceCnt]=Jbar/intLcL
					
				sliceCnt+=1
			fobj.close()
			fobj = open(fname, 'a+')
			#print processed contour values to file
			fobj.write('\n%d' % (contourId))	
			for i in range(0,len(slices),1):
				fobj.write(',%f' % (JAll[i]))
				
		fobj.close()

				
