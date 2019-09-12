from abaqusConstants import *
from odbAccess import *
from textRepr import *
from shutil import copyfile
from os import getcwd, path
import numpy as np
import pprint
import time
import sys

#Set folder with the code to be imported
sys.path.insert(1, 'E:\Dropbox\Research\Source\Abaqus-J-integral\code')

try:
	del sys.modules['Utilities']
	del sys.modules['JCore']
	del sys.modules['Integration']
	del sys.modules['C3D20']

except KeyError:
	print 'No modules to remove'
	
from C3D20 import *
from Utilities import *
from JCore import *
from Integration import *
def BuildDataForSurfaceIntegration(nodes,elements,elSet,allNodes,frame):
	#number of elements and integration points
	nElements=len(elements)
	nInt=9 #2D
	
	#load node labels into array
	nlabels=np.zeros((len(nodes)),dtype='int64')#
	cnt=0
	for n in nodes: 
		nlabels[cnt]=n.label
		cnt+=1
	
	#Get the face of each element where the surface is
	surf=np.zeros((nElements),dtype='uint8')#may be useful so storing.. 
	cnt=0
	for el in elements:
		#elem=elements[elem]
		e     = el.label
		nconn = np.array(el.connectivity) #list of node labels
		
		#get nodes of element on the surface 
		nOnSurf= nOnSurf=np.array([item in nlabels for item in nconn])
		surf[cnt]=GetElementSurface(nOnSurf)
		cnt+=1
	
	#interpolate from gauss to surface positions
	#fieldName e.g. S or LE
	#fieldComponentName e.g. S11 or LE11
	fieldName='S'
	field = frame.fieldOutputs[fieldName].getSubset(region=elSet,position=INTEGRATION_POINT) #ELEMENT_NODAL, INTEGRATION_POINT, NODAL, CENTROID
	S=np.zeros((nElements,nInt,3,3),dtype='float64')
	fieldComponentName=['S11','S22','S33','S12','S13','S23']
	fieldCI=[[0,0],[1,1],[2,2],[0,1],[0,2],[1,2]]
	for ij in range(0,len(fieldComponentName),1):
		scalarField=field.getScalarField(componentLabel=fieldComponentName[ij]) 
		Stmp=Convert_Gauss_to_Face_integration(scalarField,surf,elements) #nElements x nPoints
		for el in range(0,nElements,1): 
			for p in range(0,nInt,1):
				S[el,p,fieldCI[ij][0],fieldCI[ij][1]]=Stmp[el,p]
		if ij>2:
			for el in range(0,nElements,1): 
				for p in range(0,nInt,1):
					S[el,p,fieldCI[ij][1],fieldCI[ij][0]]=Stmp[el,p]
		
	#interpolate coordinates to surface positions
	COORD1=Coordinate_Nodal_to_Face_integration(allNodes,0,surf,elements)	#nElements x nPoints
	COORD2=Coordinate_Nodal_to_Face_integration(allNodes,1,surf,elements)	#nElements x nPoints
	COORD3=Coordinate_Nodal_to_Face_integration(allNodes,2,surf,elements)	#nElements x nPoints
	
	return S,COORD1,COORD2,COORD3,surf
	
def GetElementSurface(nOnSurf):
	#returns the element surface number based off boolean array passed in
	#surf is a nelement numpy array 
	if np.all(nOnSurf[np.array([0,1,4,5,16,17,8,12])]):
		surf=3
	elif np.all(nOnSurf[np.array([4,12,5,13,6,14,7,15])]):
		surf=2
	elif np.all(nOnSurf[np.array([0,8,1,9,2,10,3,11])]):
		surf=1
	elif np.all(nOnSurf[np.array([1,9,2,18,6,13,5,17])]):
		surf=4
	elif np.all(nOnSurf[np.array([2,18,6,14,7,19,3,10])]):
		surf=5
	elif np.all(nOnSurf[np.array([0,11,3,19,7,15,4,16])]):
		surf=6		
	else:
		raise NameError('unhandled face number')
		
	return surf
	
def Get2DdetJacLocal(root,frame,surf,allNodes,elements): 
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
	
	[NU1,ENU1,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU1,0,elements)
	[NU2,ENU2,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU2,0,elements)
	[NU3,ENU3,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU3,0,elements)
	
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
	

	return 	detJ

def MicromechanicalSurfaceIntegral(nodeSetName,elSetName,normals,stepNumber,frameNumber,odb,partInstance):
	#for a symmetric quarter model, the function takes three node sets and three element sets and 
	#performs surface integration according to eqn 1.42 in the documentation
	
	#Get components of odb
	root=odb.rootAssembly
		
	#Get nodes and elements
	allNodes = root.instances[partInstance].nodes 
	allElements=root.elementSets[' ALL ELEMENTS'].elements[0]

	#Get the frames in the step 
	steps=odb.steps

	# Get the step keys
	allSteps = steps.keys()

	# Get current step object and the number of increments (frameLen) in step
	step = steps[allSteps[stepNumber]]

	# Get frames in step
	frames=step.frames
	frame=frames[frameNumber]
	
	#Initialize array to hold SBarijtmp, storing for each surface
	SBarik=np.zeros((len(nodeSetName),3,3),dtype='float64')
	
	#loop over the surfaces 
	for i in range(0,len(nodeSetName),1):
		#Get the surface normal 
		norm=np.array(normals[i])
	
		#Get stress and coordinates of integration points
		nodes=root.nodeSets[nodeSetName[i]].nodes[0]
		elements=root.elementSets[elSetName[i]].elements[0]
		nElements=len(elements)
		elSet = root.elementSets[elSetName[i]]
		S,COORD1,COORD2,COORD3,surf=BuildDataForSurfaceIntegration(nodes,elements,elSet,allNodes,frame)
		
		#Get the area Jacobian
		detJ2D = Get2DdetJacLocal(root,frame,surf,allNodes,elements)
		
		#Get the Gauss weights (indendent on the face)
		_,wp=Gauss_Guad_Psuedo_2d(3,1)
		
		for el in range(0,nElements,1):
			for p in range(0,9,1):
				#Compute Sijnj
				Sijnj=np.dot(S[el,p,:,:],norm)
				#print 'Sijnj',Sijnj.shape
				#print 'wp',wp.shape
				#print 'COORD1',COORD1.shape
				#print 'detJ2D',detJ2D.shape
				#print 'SBarik',SBarik.shape

				#Compute SBarik
				for j in range(0,3,1):
					SBarik[i,j,0]=SBarik[i,j,0]+Sijnj[j]*COORD1[el,p]*detJ2D[el,p]*wp[p]
					SBarik[i,j,1]=SBarik[i,j,1]+Sijnj[j]*COORD2[el,p]*detJ2D[el,p]*wp[p]
					SBarik[i,j,2]=SBarik[i,j,2]+Sijnj[j]*COORD3[el,p]*detJ2D[el,p]*wp[p]
				
	
	#Get the Jacobian for integration
	detJac=GetdetJacLocal(root,frame,allNodes,allElements)

	#Get Gauss integrations weights
	_,wp = Gauss_Guad_3d(3)
	wp = np.reshape(wp,(-1))

	##Perform quadrature
	##====================
	Vbar=0
	for el in range(0,len(allElements),1):
		for p in range(0,27,1):
			Vbar=Vbar+detJac[el,p]*wp[p] #summation of integration volumes

	
	#print 'error S11%',SBarik[0,0,0]/(20*20*20))*100
	print 'S11=',SBarik[0,0,0]/Vbar, 'error S11',(1000-SBarik[0,0,0]/Vbar)/(1+1000)*100,'%'
	print 'S22=',SBarik[1,1,1]/Vbar,'error S22',(-10000-SBarik[1,1,1]/Vbar)/(1+10000)*100,'%'
	print 'S33=',SBarik[2,2,2]/Vbar,'error S33',(-5000-SBarik[2,2,2]/Vbar)/(1+5000)*100,'%'


def MicromechanicalVolumeIntegral(nodeSetName,elSetName,stepNumber,frameNumber,odb,partInstance):
	
	#Note: data arrays are stored per element per integration point
	#Stress Sij
	
	#Get components of odb
	root=odb.rootAssembly
	
	#Get nodes and elements
	allNodes = root.instances[partInstance].nodes 
	allElements=root.elementSets[' ALL ELEMENTS'].elements[0]

	#Get the frames in the step 
	steps=odb.steps

	# Get the step keys
	allSteps = steps.keys()

	# Get current step object and the number of increments (frameLen) in step
	step = steps[allSteps[stepNumber]]

	# Get frames in step
	frames=step.frames
	frame=frames[frameNumber]
	
	S,SElLabels,nEl,nInt = GetStressLocal(root,frame,' ALL ELEMENTS')

	#Get the Jacobian for integration
	detJac=GetdetJacLocal(root,frame,allNodes,allElements)

	#Get Gauss integrations weights
	_,wp = Gauss_Guad_3d(3)
	wp = np.reshape(wp,(-1))

	##Perform quadrature
	##====================
	Sbar=0
	Vbar=0
	for el in range(0,nEl,1):
		for p in range(0,nInt,1):
			Sbar=Sbar+S[el,p,0,0]*detJac[el,p]*wp[p]
			Vbar=Vbar+detJac[el,p]*wp[p] #summation of integration volumes
			
	print 'By Volume Integration S11=',Sbar/Vbar,'error S11',(1000-Sbar/Vbar)/(1+1000)*100,'%'
	Sbar=0
	Vbar=0
	for el in range(0,nEl,1):
		for p in range(0,nInt,1):
			Sbar=Sbar+S[el,p,1,1]*detJac[el,p]*wp[p]
			Vbar=Vbar+detJac[el,p]*wp[p] #summation of integration volumes
	
	
	print 'By Volume Integration S22=',Sbar/Vbar,'error S22',(-10000-Sbar/Vbar)/(1+10000)*100,'%'
	Sbar=0
	Vbar=0
	for el in range(0,nEl,1):
		for p in range(0,nInt,1):
			Sbar=Sbar+S[el,p,2,2]*detJac[el,p]*wp[p]
			Vbar=Vbar+detJac[el,p]*wp[p] #summation of integration volumes
	print 'By Volume Integration S33=',Sbar/Vbar,'error S33',(-5000-Sbar/Vbar)/(1+5000)*100,'%'
	
def GetStressLocal(root,frame,elSetName):
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

def GetdetJacLocal(root,frame,allNodes,elements): 
	#Returns the spatial derivative of the scalarField with respect to global coordinates	
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
	
	[NU1,ENU1,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU1,0,elements)
	[NU2,ENU2,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU2,0,elements)
	[NU3,ENU3,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU3,0,elements)
	
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


#Get the working directory 
workingDir=os.getcwd()

#******************************************************************************
#Run options 
#******************************************************************************
#ODB name 
odbName="SC-of-homo-cube"
odbPath = os.path.normpath(workingDir+"/model/"+odbName+".odb")

#Open odb read only mode
readOnlyOdb = False

#Close odb before opening 
closeBeforeOdb=True

#Close odb after opening 
closeAfterOdb=False

#Copy odb to new odb if writing 
copyOdb=False 
copyodbNameEnd="_copy"
copyodbPath=os.path.normpath(workingDir+"/model/"+odbName+copyodbNameEnd+".odb")

#Save odb
saveOdb=False

#Set the part instance to perform calculations on
partInstance = "MICROSTRUCTURE-1"

#model is symmetric about the crack tip (matters only for scaling J integral by 2)
isSymm=True

#Specify the step number (not a list, -1 is automatically the last step) 
stepNumber=-1

#Specify the frame number (not a list, -1 is automatically the last frame)
frameNumber=-1

#Get Volume integral
ComputeVolume=True

#Get Surface integral
ComputeSurface=True

#Specify the nodeset and element set names of the outside surfaces 
nodeSetName=['X_NODE','Y_NODE','Z_NODE']
elSetName=['X_ELEMENT','Y_ELEMENT','Z_ELEMENT']
normals=[[1,0,0],[0,1,0],[0,0,1]]

#******************************************************************************
#Open ODB
#******************************************************************************
if closeBeforeOdb:
	if copyOdb:
		Ensure_ODB_Is_Closed(copyodbPath,session)
	else:
		Ensure_ODB_Is_Closed(odbPath,session)
if copyOdb:
	Ensure_ODB_Is_Closed(copyodbPath,session)
	copyfile(odbPath, copyodbPath)
	odb = openOdb(path=copyodbPath,readOnly=readOnlyOdb)
else:
	odb = openOdb(path=odbPath,readOnly=readOnlyOdb)

if ComputeVolume:
	MicromechanicalVolumeIntegral(nodeSetName,elSetName,stepNumber,frameNumber,odb,partInstance)
if ComputeSurface:
	MicromechanicalSurfaceIntegral(nodeSetName,elSetName,normals,stepNumber,frameNumber,odb,partInstance)
	
if saveOdb:
	odb.save()
	
if closeAfterOdb:
	odb.close()
