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
from collections import Counter
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

def GetQSet(elements,elSets,Q0Nsets,Q0p5Nsets,Q1Nsets,sliceNsets,slice,nSlices,contour):
	#This is a recursive function that builds the Q nodes sets. Some optimization had to be done
	#since it is quite slow if done with naive loops
	#Inputs: elSets is a numpy array containing the element sets of elements
	linInd = contour*nSlices+slice
	linIndp1c = (contour+1)*nSlices+slice			
	
	if contour>0:
		
		Q1Nset,nSetRingInside,Q0Nsets,Q0p5Nsets,Q1Nsets,sliceNsets=GetQSet(elements,elSets,Q0Nsets,Q0p5Nsets,Q1Nsets,sliceNsets,slice,nSlices,contour-1)

		#get nodes in contour set
		elSet=np.array(elSets[linInd])-1
		nSet=np.array([], dtype=int)
		for e in elSet:
			#get nodes in each element in elInsideset
			nSet=np.append(nSet,np.array(elements[e].connectivity))

		elSetOutside=np.array(elSets[linIndp1c])-1
		elSetRing=elSetOutside[~np.in1d(elSetOutside,elSet)]
		
		nSetRing=np.array([], dtype=int)
		for e in elSetRing:
			#get nodes in each element in elSetRing
			nSetRing=np.append(nSetRing,np.array(elements[e].connectivity))
			
			
		unionRing=np.in1d(nSetRing,nSetRingInside)
		Q0Nset=nSetRing[unionRing] #good	
		Q0Nset=nSetRing[np.in1d(nSetRing,nSetRingInside)]
		Q0p5Nset=nSetRingInside[~np.in1d(nSetRingInside,Q0Nset)]
		Q0p5Nset=Q0p5Nset[~np.in1d(Q0p5Nset,Q1Nset)]
		
		Q0Nsets[contour]=Q0Nset
		Q0p5Nsets[contour]=Q0p5Nset
		Q1Nsets[contour]=Q1Nset
		sliceNsets[contour]=nSet
		
		#Return Q1Nset for contour+1
		return nSet,nSetRing[~unionRing],Q0Nsets,Q0p5Nsets,Q1Nsets,sliceNsets
		
	else: 
		#get nodes in contour set
		elSet=np.array(elSets[linInd])-1
		nSet=np.array([], dtype=int)
		Q1Nset=np.array([], dtype=int)
		for e in elSet:
			#print e
			conn=np.array(elements[e].connectivity)
			#count times each node shows up. If repeated it is a collapsed node and part of Q1
			count=Counter(conn)
			for c in conn: 
				if count[c] > 1: 
					Q1Nset=np.append(Q1Nset,c) #good
					
			nSet=np.append(nSet,conn)
		#raise
		elSetOutside=np.array(elSets[linIndp1c])-1
		elSetRing=elSetOutside[~np.in1d(elSetOutside,elSet)]
		
		nSetRing=np.array([], dtype=int)
		for e in elSetRing:
			#get nodes in each element in elSetRing
			nSetRing=np.append(nSetRing,np.array(elements[e].connectivity))
		
		unionRing=np.in1d(nSetRing,nSet)
		Q0Nset=nSetRing[unionRing] #good
		Q0p5Nset=nSet[~np.in1d(nSet,Q0Nset)]
		Q0p5Nset=Q0p5Nset[~np.in1d(Q0p5Nset,Q1Nset)]
		
		Q0Nsets[contour]=Q0Nset
		Q0p5Nsets[contour]=Q0p5Nset
		Q1Nsets[contour]=Q1Nset
		sliceNsets[contour]=nSet

		#Return Q1Nset for contour+1
		return nSet,nSetRing[~unionRing],Q0Nsets,Q0p5Nsets,Q1Nsets,sliceNsets
		
def BuildElementAndNodeSets(nContours,SetPrefix,nodeLabelTip,crackFrontAxis,sectionElSetRange,odb,partInstance):
	print 'Starting to build element and node sets...'
	print '================================================================='
	print ''
	
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
	print 'Building Slice Element sets'
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
				#print name
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
	print 'Time=',time.time()-t0		
			
	t1=time.time()
	#build nodeSets: setq1, setq0p5, setq0, setSlice
	print 'Building Q node sets'
	for slice in range(0,nSlices,1):
		Q0Nsets = {}
		Q0p5Nsets = {}
		Q1Nsets = {}
		sliceNsets = {}
		print slice
		_,_,Q0Nsets,Q0p5Nsets,Q1Nsets,sliceNsets=GetQSet(elements,sets,Q0Nsets,Q0p5Nsets,Q1Nsets,sliceNsets,slice,nSlices,nContours-1)
		for contour in range(0,nContours,1):
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)+'-Q0'
			root.NodeSetFromNodeLabels(name = setName, nodeLabels = ((partInstance,tuple(Q0Nsets[contour])),)) 
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)+'-Q0p5'
			root.NodeSetFromNodeLabels(name = setName, nodeLabels = ((partInstance,tuple(Q0p5Nsets[contour])),)) 
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)+'-Q1'
			root.NodeSetFromNodeLabels(name = setName, nodeLabels = ((partInstance,tuple(Q1Nsets[contour])),)) 
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)
			root.NodeSetFromNodeLabels(name = setName, nodeLabels = ((partInstance,tuple(sliceNsets[contour])),)) 
	
	print 'Time=',time.time()-t1		
		
	t2=time.time()		
	print 'Building interface sets'
	#build the interface sets
	for slice in range(0,nSlices,1):		
		for contour in range(nContours-1,-1,-1):
		
			linInd = contour*nSlices+slice
			#Build the interface sets for surface integration
			elset = np.array(sets[linInd])
			
			elsetInterfaceTop = []
			elsetInterfaceBottom = []
			nsetInterface = []
			
			if contour==nContours-1:
				masterElSet=np.array(elset)
				for e in masterElSet:
					ec=elemNbr[e]
					ec=np.array([x - 1 for x in ec]) #due to list comprehension issues..
					potentialInterface=elMaterial[ec]!=elMaterial[e-1]

					if np.any(potentialInterface):
						ec=np.array(ec[potentialInterface])
						ec=ec[np.in1d(ec+1,masterElSet)] #This line enforces that both sides of the interface must be in masterElSet
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
				
				elsetInterfaceTop,ind=np.unique(np.array(elsetInterfaceTop), return_index=True)
				elsetInterfaceBottom=np.array(elsetInterfaceBottom)
				elsetInterfaceBottom=elsetInterfaceBottom[ind]
				nsetInterface = np.unique(np.array(nsetInterface))
				masterElSetInterfaceTop = elsetInterfaceTop
				masterElSetInterfaceBottom = elsetInterfaceBottom
				masterNSetInterface = nsetInterface
			else: 
				elset=np.array(elset)
				tmp1=np.in1d(masterElSetInterfaceTop,elset)
				tmp2=np.in1d(masterElSetInterfaceBottom,elset)
				elementsToKeep=np.zeros((len(tmp2)),dtype='bool')
				for i in range(0,len(tmp2),1):
					elementsToKeep[i]=tmp1[i]==tmp2[i] and tmp2[i]

				elsetInterfaceTop=masterElSetInterfaceTop[elementsToKeep]
				elsetInterfaceBottom=masterElSetInterfaceBottom[elementsToKeep]
				ntop=[]
				for e in elsetInterfaceTop:
					ntmp=np.array(elements[e-1].connectivity)
					for toappend in ntmp:
						ntop.append(toappend)
				nbottom=[]		
				for e in elsetInterfaceBottom:
					ntmp=np.array(elements[e-1].connectivity)
					for toappend in ntmp:
						nbottom.append(toappend)

				tmp1=np.in1d(masterNSetInterface,np.array(ntop))
				tmp2=np.in1d(masterNSetInterface,np.array(nbottom))
				nodesToKeep=np.zeros((len(tmp2)),dtype='bool')
				for i in range(0,len(tmp2),1):
					nodesToKeep[i]=tmp1[i]==tmp2[i] and tmp2[i]
				nsetInterface=masterNSetInterface[nodesToKeep]	
					
			#Ensure unique (now should be handled by a clean master set
			#nsetInterface=np.unique(np.array(nsetInterface))
			#elsetInterfaceTop,ind=np.unique(np.array(elsetInterfaceTop), return_index=True)
			#elsetInterfaceBottom=np.array(elsetInterfaceBottom)
			#elsetInterfaceBottom=elsetInterfaceBottom[ind]
			
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice) + '-interface'
			root.NodeSetFromNodeLabels(name = setName, nodeLabels = ((partInstance,nsetInterface),)) 		
			
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)+'-interfaceTop'
			root.ElementSetFromElementLabels(name = setName, elementLabels = ((partInstance,tuple(elsetInterfaceTop)),)) 	

			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)+'-interfaceBottom'
			root.ElementSetFromElementLabels(name = setName, elementLabels = ((partInstance,tuple(elsetInterfaceBottom)),)) 	
	print 'Time=',time.time()-t2	
	
	t3=time.time()
	#write element sets to odb 
	for contour in range(0,nContours,1):
		for slice in range(0,nSlices,1):#slices	
			linInd=contour*nSlices+slice	
			setName=SetPrefix+'-contour-' + str(contour) +'-slice-'+str(slice)
			
			#convert element list to tuple 
			newSetElements=tuple(sets[linInd])
			root.ElementSetFromElementLabels(name = setName, elementLabels = ((partInstance,newSetElements),)) 
	
	t4=time.time()
	
	#print "time report"
	#print '++++++++++++'
	#print 'time in first loop',t1-t0
	#print 'time in first loop get El',tGetEl
	#print 'time in first loop get union',tUnion
	#print 'time in second loop',t2-t1
	#print 'time in third loop',t3-t2
	#print 'time in third loop',t4-t3
	#print '++++++++++++'
	#print '++++++++++++'	

	return odb
	
def GetStressOld(root,frame,elSetName):
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

def GetStress(root,frame,elSetName):
	#returns stress tensor for all elements in set elSet stress is accessed by the dictionary element label
	#array locations follow [element x integration point x data ] where data is in tensor form
	elSet = root.elementSets[elSetName]
	elements= root.elementSets[elSetName].elements[0]
	nEl=len(elements)
	
	#Major bug in getSubset when using region=elSet! Can give wrong element data combination!!! This doesn't matter if doing bulk operations..
	field = frame.fieldOutputs['S'].getSubset(position=INTEGRATION_POINT)
	
	dataGauss = np.array(field.bulkDataBlocks[0].data,dtype='float64') #s11,s22,s33,s12,s13,s23 ordered
	elLabel = np.array(field.bulkDataBlocks[0].elementLabels,dtype='int64')
	intLabel = np.array(field.bulkDataBlocks[0].integrationPoints,dtype='int8')
	
	nInt=np.amax(intLabel)
	
	S=np.zeros((nEl,nInt,3,3),dtype='float64')
	elLabelU=np.zeros((nEl),dtype='int64')

	for el in range(0,nEl,1):
		elLabelU[el]=np.array(elements[el].label,dtype='int64')
		#Find the label in the list
		ind=np.where(elLabelU[el]==elLabel)
		
		#Index the data and dump into a temp array
		tmpData=dataGauss[ind]
		
		S[el,:,0,0]=tmpData[:,0]
		S[el,:,1,1]=tmpData[:,1]
		S[el,:,2,2]=tmpData[:,2]
		S[el,:,0,1]=tmpData[:,3]
		S[el,:,1,0]=tmpData[:,3]
		S[el,:,0,2]=tmpData[:,4]
		S[el,:,2,0]=tmpData[:,4]
		S[el,:,1,2]=tmpData[:,5]
		S[el,:,2,1]=tmpData[:,5]
	
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
	
def GetW(S,dudX,nEl,nInt):
	W=np.zeros((nEl,nInt),dtype='float64')
	#returns strain energy for a linear elastic material
	for el in range(0,nEl,1):
		for p in range(0,nInt,1):
			for i in range(0,3,1):
				for j in range(0,3,1):
					W[el,p]+=0.25*S[el,p,i,j]*(dudX[el,p,i,j]+dudX[el,p,j,i])
					
	return W				

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

def GetqNew(nSetQ0,nSetQ0p5,nSetQ1,nSetSlice,firstCrackNodeLabel,root,allNodes,elSetName,L,rPoszRelTol,CFPosz,isSymm):
	
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
	
	#Initialize Q0
	q=np.array(0.0)		
	for n in nodesQ0:
		conn[n.label]=q
		
	#Initialize Q0.5
	lenq=len(nodesQ0p5)
	labelq=np.zeros((lenq),dtype='int64')
	Coord2q=np.zeros((lenq),dtype='float64')		
	for i in range(0,lenq,1):
		n=nodesQ0p5[i]
		labelq[i]=n.label
		Coord2q[i]=n.coordinates[2]
		
	for p in range(0,len(CFPosz)):	
		labelq2=labelq[np.abs(Coord2q-CFPosz[p])<rPoszRelTol]	
		q=np.array(0.5*L[p])
		for i in range(0,len(labelq2),1):
				conn[labelq2[i]]=q
			
	#Initialize Q1
	lenq=len(nodesQ1)
	labelq=np.zeros((lenq),dtype='int64')
	Coord2q=np.zeros((lenq),dtype='float64')		
	for i in range(0,lenq,1):
		n=nodesQ1[i]
		labelq[i]=n.label
		Coord2q[i]=n.coordinates[2]
		
	for p in range(0,len(CFPosz)):	
		labelq2=labelq[np.abs(Coord2q-CFPosz[p])<rPoszRelTol]	
		q=np.array(L[p])
		for i in range(0,len(labelq2),1):
				conn[labelq2[i]]=q
				
						
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
	
	return dataElementNodal

def GetqNew2D(nSetQ0,nSetQ0p5,nSetQ1,nSetSlice,firstCrackNodeLabel,root,allNodes,elSetName,L,rPoszRelTol,CFPosz):
	
	nodesQ0=root.nodeSets[nSetQ0].nodes[0] #Outside nodes
	nodesQ1=root.nodeSets[nSetQ1].nodes[0] #Inside nodes
	nodesQ0p5=root.nodeSets[nSetQ0p5].nodes[0] #In between nodes
	nodesSlice=root.nodeSets[nSetSlice].nodes[0]
	elements=root.elementSets[elSetName].elements[0]
	#elLabel = [el.label for el in elements]
	
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
	
	#This is the same as the 3D case except Q0, Q0p5 and Q1 are all set to L along the crack front!
	#Initialize Q0
	lenq=len(nodesQ0)
	labelq=np.zeros((lenq),dtype='int64')
	Coord2q=np.zeros((lenq),dtype='float64')		
	for i in range(0,lenq,1):
		n=nodesQ0[i]
		labelq[i]=n.label
		Coord2q[i]=n.coordinates[2]
		
	for p in range(0,len(CFPosz)):	
		labelq2=labelq[np.abs(Coord2q-CFPosz[p])<rPoszRelTol]	
		q=np.array(L[p])
		for i in range(0,len(labelq2),1):
				conn[labelq2[i]]=q
		
	#Initialize Q0.5
	lenq=len(nodesQ0p5)
	labelq=np.zeros((lenq),dtype='int64')
	Coord2q=np.zeros((lenq),dtype='float64')		
	for i in range(0,lenq,1):
		n=nodesQ0p5[i]
		labelq[i]=n.label
		Coord2q[i]=n.coordinates[2]
		
	for p in range(0,len(CFPosz)):	
		labelq2=labelq[np.abs(Coord2q-CFPosz[p])<rPoszRelTol]	
		q=np.array(L[p])
		for i in range(0,len(labelq2),1):
				conn[labelq2[i]]=q
			
	#Initialize Q1
	lenq=len(nodesQ1)
	labelq=np.zeros((lenq),dtype='int64')
	Coord2q=np.zeros((lenq),dtype='float64')		
	for i in range(0,lenq,1):
		n=nodesQ1[i]
		labelq[i]=n.label
		Coord2q[i]=n.coordinates[2]
		
	for p in range(0,len(CFPosz)):	
		labelq2=labelq[np.abs(Coord2q-CFPosz[p])<rPoszRelTol]	
		q=np.array(L[p])
		for i in range(0,len(labelq2),1):
				conn[labelq2[i]]=q
				
						
	#map everything back to dataElementNodal
	dataElementNodal=np.zeros((lenConnectivty),dtype='float64')
	#fobj = open('debug_q3d.txt', 'w')
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
	
	return dataElementNodal
	
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
	
def GetdqdX(root,frame,allNodes,nSetQ0,nSetQ0p5,nSetQ1,firstCrackNodeLabel,nodeSetName,elSetName,L,rPoszRelTol,CFPosz,isSymm): 
	#Returns the spatial derivative of the scalarField with respect to global coordinates
	nodes=root.nodeSets[nodeSetName].nodes[0]
	elements=root.elementSets[elSetName].elements[0]
	elLabel=[el.label for el in elements]
	
	nElements=len(elements)
	nNodes=len(elements[0].connectivity)
	nPoints=GetNumIntegrationPoints(elements[0].type)
	
	#Get the nodal coordinates and map to element nodal coordinates (same thing but data structure is different)
	[ENCoord1,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,0,elements)	
	[ENCoord2,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,1,elements)
	[ENCoord3,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,2,elements)
	
	#Get q2
	ENQ2=GetqNew(nSetQ0,nSetQ0p5,nSetQ1,nodeSetName,firstCrackNodeLabel,root,allNodes,elSetName,L,rPoszRelTol,CFPosz,isSymm)

	#interpolates var between element nodal and integrations points
	points,_=Gauss_Guad_3d(3) #3 is the number of quadrature points along each dimension
	
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
	
	Jinvp=np.zeros((nPoints, 3,3),dtype='float64')
	dqdx=np.zeros((nElements,nPoints,3),dtype='float64')
	I=np.eye(3);
	
	#Initialize dictionaries for saved element data
	#print '=====start solution====='	
	for el in range(0,nElements,1):
		for p in range(0,nPoints,1): #p is looping over integration points in element elLabel[el]
			Jinvp[p,:,:]=np.linalg.inv(J[p,el,:,:])	
			tmp=np.dot(dhdr[p,:,:],Jinvp[p,:,:]) #nNodes x 3
			tmp=np.transpose(tmp)
			dqdx[el,p,:]=np.dot(tmp,ENQ2[:,el])	
			
	return 	dqdx,elLabel

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

## Section for 2D integration
def Get2DdetJac(root,frame,partInstance,surf,allNodes,elements): 
	#Returns the spatial derivative of the scalarField with respect to global coordinates	
	elLabel = [el.label for el in elements]
	
	nElements=len(elements)
	nNodes=len(elements[0].connectivity)
	nPoints=9
	
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
	

	
	#get the natural nodal coordinates for the element
	Bi=C3D20_nodal_coordinates()
	
	detJ=np.zeros((nElements,nPoints),dtype='float64')

	#Loop over possible faces
	for f in range(1,7,1):	
		#interpolates var between element nodal and integrations points
		points,_=Gauss_Guad_Psuedo_2d(3,f)
		#print points
		
		#evaluate the derivative of the shape functions for the points we want to interpolate/extrapolate data to 
		dhdr=np.zeros((nPoints,nNodes,3),dtype='float64')#
		

		#For each integration point, get the derivative of the shape functions with respect to natural local coordinates
		for i in range(0,nPoints,1):#
			r = points[i,:]
			tmp = C3D20_Shape_Derivatives(r,Bi) #20x3 array
			#dhdr = np.squeeze(tmp)
			dhdr[i,:,:]=tmp #nPointx20x3 array
			
		V1=np.zeros((nPoints,nElements, 3),dtype='float64')
		V2=np.zeros((nPoints,nElements, 3),dtype='float64')

		if f==1 or f==2:
			#dr ds
			V1[:,:,0]= np.dot(dhdr[:,:,0],ENCoord1) #dx/dr	#npoints x nelement array
			V2[:,:,0]= np.dot(dhdr[:,:,1],ENCoord1) #dx/ds
			V1[:,:,1]= np.dot(dhdr[:,:,0],ENCoord2) #dy/dr	
			V2[:,:,1]= np.dot(dhdr[:,:,1],ENCoord2) #dy/ds
			V1[:,:,2]= np.dot(dhdr[:,:,0],ENCoord3) #dz/dr
			V2[:,:,2]= np.dot(dhdr[:,:,1],ENCoord3) #dz/ds
		elif f==6 or f==4:
			#ds dt
			V1[:,:,0]= np.dot(dhdr[:,:,1],ENCoord1) #dx/ds
			V2[:,:,0]= np.dot(dhdr[:,:,2],ENCoord1) #dx/dt
			V1[:,:,1]= np.dot(dhdr[:,:,1],ENCoord2) #dy/ds
			V2[:,:,1]= np.dot(dhdr[:,:,2],ENCoord2) #dy/dt
			V1[:,:,2]= np.dot(dhdr[:,:,1],ENCoord3) #dz/ds
			V2[:,:,2]= np.dot(dhdr[:,:,2],ENCoord3) #dz/dt
		elif f==5 or f==3:
			#dr dt
			V1[:,:,0]= np.dot(dhdr[:,:,0],ENCoord1) #dx/dr	#npoints x nelement array
			V2[:,:,0]= np.dot(dhdr[:,:,2],ENCoord1) #dx/dt
			V1[:,:,1]= np.dot(dhdr[:,:,0],ENCoord2) #dy/dr	
			V2[:,:,1]= np.dot(dhdr[:,:,2],ENCoord2) #dy/dt
			V1[:,:,2]= np.dot(dhdr[:,:,0],ENCoord3) #dz/dr
			V2[:,:,2]= np.dot(dhdr[:,:,2],ENCoord3) #dz/dt
		else: 
			raise NameError('unhandled face number')
		
		#Get the magnitude of the cross product representing the of the integration point on the face
		tmp=np.cross(V1,V2)
		for el in range(0,nElements,1):
			for p in range(0,nPoints,1):
				if surf[el]==f:
					detJ[el,p]=np.linalg.norm(tmp[p,el])
					#print 'original',detJ[el,p]
					#detJ[el,p]=np.sqrt((V1[p,el,1]*V2[p,el,2]-V1[p,el,2]*V2[p,el,1])**2 \
					#+(V1[p,el,2]*V2[p,el,0]-V1[p,el,0]*V2[p,el,2])**2 \
					#+(V1[p,el,0]*V2[p,el,1]-V1[p,el,1]*V2[p,el,0])**2)
					#print 'new',detJ[el,p]

	return 	detJ,elLabel

def Get2DdudX(root,partInstance,frame,allNodes,nodeSetName,elSetName,surf): 
	#Returns the spatial derivative of the scalarField with respect to global coordinates
	nodes=root.nodeSets[nodeSetName].nodes[0]
	elements=root.elementSets[elSetName].elements[0]
	
	elLabel = [el.label for el in elements]
	
	nElements=len(elements)
	nNodes=len(elements[0].connectivity)
	nPoints=9#GetNumIntegrationPoints(elements[0].type)
	
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
	

	
	#get the natural nodal coordinates for the element
	Bi=C3D20_nodal_coordinates()
	
	dudx=np.zeros((nElements,nPoints,3,3),dtype='float64')
	#Loop over possible faces
	for f in range(1,7,1):	
		#interpolates var between element nodal and integrations points
		points,_=Gauss_Guad_Psuedo_2d(3,f)
		#print points
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
		I=np.eye(3);
		
		#Initialize dictionaries for saved element data
		#print '=====start solution====='	
		#cnt=0
		for el in range(0,nElements,1):
			if surf[el]==f:
				#cnt+=1
				#print 'entering to assign dudx for the', cnt, 'time'
				for p in range(0,nPoints,1): #p is looping over integration points in element elLabel[el]
					detJ[el,p]=np.linalg.det(J[p,el,:,:])
					Jinvp[p,:,:]=np.linalg.inv(J[p,el,:,:])	
					tmp=np.dot(dhdr[p,:,:],Jinvp[p,:,:]) #nNodes x 3
					tmp=np.transpose(tmp)
					dudx[el,p,0,:]=np.dot(tmp,ENU1[:,el])
					dudx[el,p,1,:]=np.dot(tmp,ENU2[:,el])
					dudx[el,p,2,:]=np.dot(tmp,ENU3[:,el])
				
	return 	dudx,elLabel
	
	
def Get2DStress(nodes,elements1,elements2,elSetName,allNodes,root,frame):
	#This routine returns data for surface integration defined by nodes using the
	#data at integration points in elements/elSet 
	#Quantities returned: Stress,du/dX,W, and q
	#number of elements and integration points

	nElements=len(elements1)
	nInt2D=9 #2D
	
	#load node labels into array
	nlabels=np.zeros((len(nodes)),dtype='int64')#
	cnt=0
	for n in nodes: 
		nlabels[cnt]=n.label
		cnt+=1
	
	#Get the face of each element where the surface is
	surf=np.zeros((nElements),dtype='uint8')#may be useful so storing.. 
	cnt=0
	for i in range(0,nElements,1):
		#Get on one side of the interface
		el1=elements1[i]
		e1     = el1.label
		nconn1 = np.array(el1.connectivity) #list of node labels
		
		#Get on other side of interface
		el2=elements2[i]
		e2     = el2.label
		nconn2 = np.array(el2.connectivity) #list of node labels
		
		#get nodes of element on the surface 
		nOnSurf=np.array([item in nconn2 for item in nconn1])
		
		#nOnSurf=nconnm[np.in1d(nconnm,nconnp)]
		#print nconnm
		#print nconnp
		#print nOnSurf
		surf[cnt]=C3D20_GetElementSurface(nOnSurf)
		cnt+=1
		
	#Get stress and energy for the elements
	S3D,elLabel,_,_ = GetStress(root,frame,elSetName)

	#Interpolate from gauss to surface positions
	S = np.zeros((nElements,nInt2D,3,3),dtype='float64')
	S[:,:,0,0] = Convert_Gauss_to_Face_integration(S3D[:,:,0,0],surf,elements1)
	S[:,:,1,1] = Convert_Gauss_to_Face_integration(S3D[:,:,1,1],surf,elements1)
	S[:,:,2,2] = Convert_Gauss_to_Face_integration(S3D[:,:,2,2],surf,elements1)
	S[:,:,0,1] = Convert_Gauss_to_Face_integration(S3D[:,:,0,1],surf,elements1)
	S[:,:,0,2] = Convert_Gauss_to_Face_integration(S3D[:,:,0,2],surf,elements1)
	S[:,:,1,2] = Convert_Gauss_to_Face_integration(S3D[:,:,1,2],surf,elements1)
	S[:,:,1,0] = S[:,:,0,1]
	S[:,:,2,0] = S[:,:,0,2]
	S[:,:,2,1] = S[:,:,1,2]
	
	#cnt=0
	#for el in elements:
	#	print el.label,elLabel[cnt],surf[cnt],S3D[cnt,0,2,2]
	#	cnt+=1
	return S,surf,elLabel

def WriteJToFile(namePrefix,contours,slices,J,pos,TTAU):
	##open file to write Js to
	time= '%5.3f' % (TTAU)
	fname=namePrefix+time+'.txt'
	fobj = open(fname, 'w')
	
	#write header for with contour levels
	fobj.write('%f' % (float('nan'))) #spot holder in upper right corner of table
	for contour in contours: 
		fobj.write(',%d' % (contour))
	for slice in range(0,len(slices),1):	
		fobj.write('\n%f' % (pos[slice]))
		for contour in range(0,len(contours),1): 
			fobj.write(',%E' % (J[slice,contour]))
	fobj.close()

def GetContourMask(els,elLabel):
	elLabelSub=[]
	for el in els:
		elLabelSub.append(el.label)
		
	mask=np.in1d(np.array(elLabel),np.array(elLabelSub))
	
	return mask
	
def WriteSpatialJint(namePrefix,S,dudX,W,detJac,wp,krd2,lz,allNodes,elements,surf,slice,TTAU,factor):
	##Get the coordinates of the integration points on the element surfaces
	COORD1=Convert_Coordinate_Nodal_to_Face_integration(allNodes,0,surf,elements)	#nElements x nPoints
	COORD2=Convert_Coordinate_Nodal_to_Face_integration(allNodes,1,surf,elements)	#nElements x nPoints
	COORD3=Convert_Coordinate_Nodal_to_Face_integration(allNodes,2,surf,elements)	#nElements x nPoints
			
	##Construct the file name and handle file opening
	time= '%5.3f' % (TTAU)
	fname=namePrefix+'spatial_'+time+'.txt'
	if slice==0:
		fobj = open(fname, 'w')
	else:
		fobj = open(fname, 'a')
	
	##Calculate JInt contribution for each integration point and write file
	Jint=0
	for el in range(0,len(elements),1):
		for p in range(0,9,1):
			J=factor*np.dot(np.dot(S[el,p,:,:],dudX[el,p,:,1])-W[el,p]*krd2,lz[el,p,:])#*detJac[el,p]*wp[p]
			#J=factor*np.dot(np.dot(S[el,p,:,:],dudX[el,p,:,1])-W[el,p]*krd2,lz)#*detJac[el,p]*wp[p]
			fobj.write('%E, %f, %f, %f, %d\n' % (J,COORD1[el,p],COORD2[el,p],COORD3[el,p],slice))
	
	fobj.close()
	
def GetCrackFrontInterface(root,allNodes,nSetSlice,firstCrackNodeLabel): 

	#reconstruct crack node front going towards 0 in z
	nodesSlice=root.nodeSets[nSetSlice].nodes[0]
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
	CFnSet=CFnSet[::-1] #Skips mid nodes
	CFPosz=CFPosz[ind]
	CFPosz=CFPosz[::-1] #Skips mid nodes
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
		
	Lc=GetTrapIntLc(CFPosz,L) #returns the length of the interface
		
	return PoszOut,L,Lc,rPoszRelTol,CFPosz
	
def GetCrackFrontInterface2D(root,allNodes,nSetSlice,firstCrackNodeLabel): 

	#reconstruct crack node front going towards 0 in z
	nodesSlice=root.nodeSets[nSetSlice].nodes[0]
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
	CFnSet=CFnSet[::-1] #Skips mid nodes
	CFPosz=CFPosz[ind]
	CFPosz=CFPosz[::-1] #Skips mid nodes
	
	if CFPosz[-1]==0 and len(CFnSet)==3:
		L=[1.0,1.0,1.0]
		PoszOut=0
	elif len(CFnSet)==3:
		L=[1.0,1.0,1.0]
		PoszOut=CFPosz[0]
	else: 
		L=[1.0,1.0,1.0,1.0,1.0]
		PoszOut=CFPosz[2]	
		
	LenCrackFront=GetTrapIntLc(CFPosz,L) #returns the length of the interface
		
	return PoszOut,LenCrackFront
	
def CalculateDomainJIntegralOld(stepNumber,frameNumbers,contours,slices,SetPrefix,nodeLabelTip,isSymm,odb,partInstance): 
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

				#Get du/dX, where X is the reference coordinates and u is displacement in the current frame. 
				#The Jacobian is also computed when calculating the derivatives and is returned here
				dudX,detJac,dudXElLabels = GetdudX(root,partInstance,frame,allNodes,nSetSlice,elSetSlice)
				
				#Strain energy density defined for linear elasticity as computed for linear elasticity as U=1/2*Sijeij where e is linear strain
				W = GetW(S,dudX,nEl,nInt)
				
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
					JAll[sliceCnt]=2*Jbar/(intLcL)
				else: 
					JAll[sliceCnt]=Jbar/intLcL
				print JAll[sliceCnt]
				sliceCnt+=1
			fobj.close()
			fobj = open(fname, 'a+')
			#print processed contour values to file
			fobj.write('\n%d' % (contourId))	
			for i in range(0,len(slices),1):
				fobj.write(',%f' % (JAll[i]))
				
		fobj.close()

def CalculateDomainJIntegral(Junit,JInt,stepNumber,frameNumbers,contours,slices,SetPrefix,nodeLabelTip,isSymm,odb,partInstance,JFnamePrefix): 
	##This routine calculates the so called domain J integral
	##Assumptions: C3D20 elements, small strains, crack extension direction [0,1,0], straight crackfront
	##Assumptions: nodeLabelTip is not at zero (used when reconstructing the crack front)
	##output: J(s) - energy release rate along the crack front (file)
	##==============================================================================================================
	
	print 'Starting calculations for the J Integral...'
	print '==========================================='
	print '' 
	
	##Initialize Abaqus variables
	##=============================
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

	#Initialize J data container and slice position so we can later write to file
	J=np.zeros((len(frameNumbers),len(slices),len(contours)),dtype='float64')

	slicePosition=np.zeros((len(slices)),dtype='float64')
	
	#Sort slice and contour lists
	contours.sort(reverse = True) #starts with largest contour first to save computations
	slices.sort()	

	##loop over specified frames and compute J
	##======================
	for frame in range(0,len(frameNumbers),1):
		frameId=frameNumbers[frame]
		##Get the frame and time
		##======================
		cframe = frames[frameId]
		TTAU = cframe.frameValue
		
		#Check that the necessary field variables exist at the appropriate locations
		##==========================================
		CheckFieldExists(cframe,'U','NODAL') #displacements
		CheckFieldExists(cframe,'S','INTEGRATION_POINT') #stress 
				
		##loop over the slices and contours specified
		##==========================================
		for slice in range(0,len(slices),1):
			sliceId=slices[slice]
			print 'Processing slice #:',sliceId
			
			#Get slice position and the crack length for the slice
			nSetSlice=SetPrefix+'-contour-'+str(contours[-1])+'-slice-'+str(sliceId)
			CheckSetExists(root,nSetSlice,'node')
			slicePosition[slice],L,Lc,rPoszRelTol,CFPosz=GetCrackFrontInterface(root,allNodes,nSetSlice,nodeLabelTip) 
			
			for contour in range(0,len(contours),1):
				contourId=contours[contour]
				print '___Contour: ', contourId
				
				##build the node set and element set names 
				##========================================
				nSetSlice=SetPrefix+'-contour-'+str(contourId)+'-slice-'+str(sliceId)
				nSetQ0=nSetSlice+'-Q0'
				nSetQ0p5=nSetSlice+'-Q0p5'
				nSetQ1=nSetSlice+'-Q1'
				elSetSlice=nSetSlice
				
				##Check that node and element sets exist	(ensures only that they exist, not that they are valid..)
				##=====================================
				CheckSetExists(root,nSetQ0,'node')
				CheckSetExists(root,nSetQ0p5,'node')
				CheckSetExists(root,nSetQ1,'node')
				CheckSetExists(root,nSetSlice,'node')
				CheckSetExists(root,elSetSlice,'element')
				
				##For a slice compute all data once and after that just compute a mask based on the elementsets
				##============================================================================================
				#If the largest contour compute all quantities
				t0=time.time()
				if contour==0:
					#Stress Sij 
					S,SElLabels,nEl,nInt = GetStress(root,cframe,elSetSlice)

					#Get du/dX, where X is the reference coordinates and u is displacement in the current frame. 
					#The Jacobian is also computed when calculating the derivatives and is returned here
					dudX,detJac,dudXElLabels = GetdudX(root,partInstance,cframe,allNodes,nSetSlice,elSetSlice)
					
					#Strain energy density defined for linear elasticity as computed for linear elasticity as U=1/2*Sijeij where e is linear strain
					W = GetW(S,dudX,nEl,nInt)
					
					#Get dqdX, a weighting term defined as a pyramid function similar to what Abaqus uses
					dqdX,dqdXElLabels=GetdqdX(root,cframe,allNodes,nSetQ0,nSetQ0p5,nSetQ1,nodeLabelTip,nSetSlice,elSetSlice,L,rPoszRelTol,CFPosz,isSymm)

					#Get the Jacobian for integration
					#detJac=GetdetJac(root,partInstance,frame,allNodes,nSetSlice,elSetSlice)
					
					#Get Gauss integrations weights
					_,wp = Gauss_Guad_3d(3)
					wp = np.reshape(wp,(-1))

					#Initialize the croneker delta evaluation 
					krd2=np.zeros((3),dtype='float64')
					krd2[1]=1
					
					if isSymm:
						factor=Junit*2.0/Lc 
					else:
						factor=Junit*1.0/Lc 
					
					#Create mask with all values true
					mask=np.ones(nEl,dtype=bool)

				else:
					#Compute a mask for sub contours
					els=root.elementSets[elSetSlice].elements[0]
					mask = GetContourMask(els,SElLabels)

					#Get dqdX, a weighting term defined as a pyramid function similar to what Abaqus uses
					dqdXtmp,dqdXElLabels=GetdqdX(root,cframe,allNodes,nSetQ0,nSetQ0p5,nSetQ1,nodeLabelTip,nSetSlice,elSetSlice,L,rPoszRelTol,CFPosz,isSymm)
										
					#dqdX doesn't have the same number of elements need to map back to original array
					dqdXElLabels=np.array(dqdXElLabels)
					SElLabels=np.array(SElLabels)
					for el in range(0,len(els),1):
						elabel=np.array(dqdXElLabels[el])
						ind=np.where(SElLabels==dqdXElLabels[el])
						dqdX[ind,:,:]=dqdXtmp[el,:,:]
					
				##Perform quadrature
				##====================
				Jbar=0
				for el in range(0,nEl,1):
					if mask[el]:	
						for p in range(0,nInt,1):
							Jbar+=np.dot((np.dot(S[el,p,:,:],dudX[el,p,:,1])-W[el,p]*krd2),dqdX[el,p,:])*detJac[el,p]*wp[p]
			
				#Store J
				J[frame][slice][contour]=factor*Jbar
				print 'J far =',J[frame][slice][contour]
				if JInt.shape[0]==len(frameNumbers) and JInt.shape[1]==len(slices) and JInt.shape[2]==len(contours):
					print 'J tip =',J[frame][slice][contour]+JInt[frame][slice][contour]
				#print 'Time for contour comps', time.time()-t0
				
		##Write the computed J values to a file 
		##=====================================
		WriteJToFile(JFnamePrefix,contours,slices,J[frame],slicePosition,TTAU)	
		if JInt.shape[0]==len(frameNumbers) and JInt.shape[1]==len(slices) and JInt.shape[2]==len(contours):
			WriteJToFile(JFnamePrefix+'corrected_',contours,slices,J[frame]+JInt[frame],slicePosition,TTAU)
	if JInt.shape[0]==len(frameNumbers) and JInt.shape[1]==len(slices) and JInt.shape[2]==len(contours):
		return J+JInt
	else:
		return J
		
def CalculateDomainJIntegralInterface(Junit,stepNumber,frameNumbers,contours,slices,SetPrefix,nodeLabelTip,isSymm,odb,partInstance,JIntFnamePrefix): 
	##This routine calculates the material force at surfaces where there is a change in material between elements and integrates
	##the material force over the interface.
	##Assumptions: C3D20 elements, small strains, interface normal [0,1,0], crack extension direction [0,1,0], straight crackfront
	##Assumptions: nodeLabelTip is not at zero (used when reconstructing the crack front)
	##output: J-Interface(s) - energy release rate along the crack front that is due to the interfaces (file)
	##output: Spatial energy densities in the interfaces (file)
	##==============================================================================================================
	
	print 'Starting calculations for the Material force at the interface...'
	print '================================================================='
	print ''
	
	##Initialize Abaqus variables
	##=============================
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

	#Initialize J data container and slice position so we can later write to file
	JInt=np.zeros((len(frameNumbers),len(slices),len(contours)),dtype='float64')

	slicePosition=np.zeros((len(slices)),dtype='float64')
	
	#Sort slice and contour lists
	contours.sort(reverse = True) #starts with largest contour first to save computations
	slices.sort()	

	#Set the surface normals for the interfaces
	z=np.array([0,1,0])

	##loop over specified frames and compute J
	##======================
	for frame in range(0,len(frameNumbers),1):
		frameId=frameNumbers[frame]
		##Get the frame and time
		##======================
		cframe = frames[frameId]
		TTAU = cframe.frameValue
		
		#Check that the necessary field variables exist at the appropriate locations
		##==========================================
		CheckFieldExists(cframe,'U','NODAL') #displacements
		CheckFieldExists(cframe,'S','INTEGRATION_POINT') #stress 
				
		##loop over the slices and contours specified
		##==========================================
		for slice in range(0,len(slices),1):
			sliceId=slices[slice]
			print 'Processing slice #:',sliceId
			
			#Get slice position and the crack length for the slice
			nSetSlice=SetPrefix+'-contour-'+str(contours[-1])+'-slice-'+str(sliceId)
			CheckSetExists(root,nSetSlice,'node')
			slicePosition[slice],L,Lc,rPoszRelTol,CFPosz=GetCrackFrontInterface(root,allNodes,nSetSlice,nodeLabelTip) 
			
			for contour in range(0,len(contours),1):
				contourId=contours[contour]
				print '___Contour: ', contourId
				
				##build the node set and element set names 
				##========================================
				nSetSlice=SetPrefix+'-contour-'+str(contourId)+'-slice-'+str(sliceId)
				nSetQ0=nSetSlice+'-Q0'
				nSetQ0p5=nSetSlice+'-Q0p5'
				nSetQ1=nSetSlice+'-Q1'
				nSetInterface=nSetSlice+'-interface'
				elSetSlice=nSetSlice
				elSetInterfaceBottom=nSetSlice+'-interfaceBottom'
				elSetInterfaceTop=nSetSlice+'-interfaceTop'
				
				##Check that node and element sets exist	(ensures only that they exist, not that they are valid..)
				##=====================================
				CheckSetExists(root,nSetQ0,'node')
				CheckSetExists(root,nSetQ0p5,'node')
				CheckSetExists(root,nSetQ1,'node')
				CheckSetExists(root,nSetSlice,'node')
				CheckSetExists(root,nSetInterface,'node')
				CheckSetExists(root,elSetSlice,'element')
				CheckSetExists(root,elSetInterfaceBottom,'element')
				CheckSetExists(root,elSetInterfaceTop,'element')
				
				##For a slice compute all data once and after that just compute a mask based on the elementsets
				##============================================================================================
				t00=time.time()
				InterfaceElements=root.elementSets[elSetInterfaceBottom].elements
				if InterfaceElements!=None:
					#If the largest contour compute all quantities
					if contour==0:
						#Get the nodes at the interface
						nodes=root.nodeSets[nSetInterface].nodes[0]
						
						#At the bottom of the interface
						elsm=root.elementSets[elSetInterfaceBottom].elements[0]
						elsp=root.elementSets[elSetInterfaceTop].elements[0]
						nEls=len(elsm)
						elsSetm = root.elementSets[elSetInterfaceBottom].elements[0]
						Sm,surfm,elLabelm=Get2DStress(nodes,elsm,elsp,elSetInterfaceBottom,allNodes,root,cframe)
						dudXm,_ = Get2DdudX(root,partInstance,cframe,allNodes,nSetInterface,elSetInterfaceBottom,surfm)
						Wm = GetW(Sm,dudXm,nEls,9)

						#At the top of the interface
						elsSetp = root.elementSets[elSetInterfaceTop].elements[0]
						Sp,surfp,elLabelp=Get2DStress(nodes,elsp,elsm,elSetInterfaceTop,allNodes,root,cframe)		
						dudXp,elLabelp2 = Get2DdudX(root,partInstance,cframe,allNodes,nSetInterface,elSetInterfaceTop,surfp)
						Wp = GetW(Sp,dudXp,nEls,9)
						
						
						#Average stress 
						S=(Sp+Sm)/2.0
						
						#Take differences across the interface
						dudX=dudXp-dudXm
						W=Wp-Wm
						
						#Get the area Jacobian
						detJac,elLabel = Get2DdetJac(root,cframe,partInstance,surfp,allNodes,elsp)
						
						#Get Q2 along L
						Q2EN=GetqNew2D(nSetQ0,nSetQ0p5,nSetQ1,nSetSlice,nodeLabelTip,root,allNodes,elSetSlice,L,rPoszRelTol,CFPosz)
						elSlice = root.elementSets[elSetSlice].elements[0]
						lz=Convert_Q2_to_Face_integration(Q2EN,surfm,elsm,elSlice,z)													
						
						#Get the Gauss weights (independent on the face so chose random face=1)
						_,wp=Gauss_Guad_Psuedo_2d(3,1)
						
						#Initialize the Kronecker delta evaluation 
						krd2=np.zeros((3),dtype='float64')
						krd2[1]=1
										
						if isSymm:
							factor=Junit*2.0/Lc 
						else:
							factor=Junit*1.0/Lc
						
						#Export spatial data of the material force as energy density
						#Currently exporting J/m^3*m^2/m.. not the density. Fix when units are fixed
						WriteSpatialJint(JIntFnamePrefix,S,dudX,W,detJac,wp,krd2,lz,allNodes,elsm,surfm,slice,TTAU,1.0)	

						#Initialize mask
						mask=np.ones((len(elsm)),dtype='bool')
					else:
						#Compute a mask sub contours
						elsm=root.elementSets[elSetInterfaceBottom].elements[0]
						mask = GetContourMask(elsm,elLabelm)
						
					##Perform quadrature
					##====================
					Jbar=0
					for el in range(0,nEls,1):
						if mask[el]:
							for p in range(0,9,1):
								Jbar+=np.dot(np.dot(S[el,p,:,:],dudX[el,p,:,1])-W[el,p]*krd2,lz[el,p,:])*detJac[el,p]*wp[p]
													
							#print elLabelm[el],elLabelp[el],surfm[el],surfm[el],S[el,0,0,0]

					#Store Jint
					JInt[frame][slice][contour]=factor*Jbar
					print 'Jint =',JInt[frame][slice][contour]

		##Write the computed J values to a file 
		##=====================================
		WriteJToFile(JIntFnamePrefix,contours,slices,JInt[frame],slicePosition,TTAU)	
	return JInt
	
def CalculateK(Kunit,J,E,v,KFnamePrefix,SetPrefix,contours,slices,nodeLabelTip,stepNumber,frameNumbers,odb,partInstance):
	print 'Starting calculations of KI from J...'
	print '================================================================='
	print ''
	print 'the stress intensity factor is being calculated assuming'
	print 'only mode I and plane strain.'
	##Initialize Abaqus variables
	##=============================
	#Get components of odb
	root=odb.rootAssembly
	
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
	
	#Initialize array
	slicePosition=np.zeros((len(slices)),dtype='float64')

	for frame in range(0,len(frameNumbers),1):
		frameId=frameNumbers[frame]
		##Get the frame and time
		##======================
		cframe = frames[frameId]
		TTAU = cframe.frameValue
		
		##loop over the slices and contours specified
		##==========================================
		for slice in range(0,len(slices),1):
			sliceId=slices[slice]
			#Get slice position and the crack length for the slice
			nSetSlice=SetPrefix+'-contour-'+str(contours[-1])+'-slice-'+str(sliceId)
			CheckSetExists(root,nSetSlice,'node')
			slicePosition[slice],_=GetCrackFrontInterface2D(root,allNodes,nSetSlice,nodeLabelTip) 
		
		tmp=J[frame,:,:]
		KI=Kunit*np.sqrt(tmp*(E/(1-v**2)))
		print KI.shape
		WriteJToFile(KFnamePrefix,contours,slices,KI,slicePosition,TTAU)	
