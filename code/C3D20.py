from abaqusConstants import *
from odbAccess import *
from textRepr import *
from shutil import copyfile
from os import getcwd, path
import numpy as np
import pprint
import time
import sys

from Integration import *

def C3D20_nodal_coordinates():
	#Element node natural coordinates ordered by abaqus node id convention
	Bi=np.array([[-1,-1,-1], #node 1
		[1,-1,-1],  #node 2
		[1,1,-1],   #node 3
		[-1,1,-1],  #node 4
		[-1,-1,1],  #node 5
		[1,-1,1],   #node 6
		[1,1,1],    #node 7
		[-1,1,1],   #node 8 good to here
		[0,-1,-1],  #node 9
		[1,0,-1],   #node 10
		[0,1,-1],   #node 11
		[-1,0,-1],  #node 12 good to here
		[0,-1,1],   #node 13
		[1,0,1],    #node 14
		[0,1,1],    #node 15
		[-1,0,1],   #node 16 good to here
		[-1,-1,0],  #node 17
		[1,-1,0],   #node 18
		[1,1,0],    #node 19
		[-1,1,0]],dtype='float64')   #node 20 good to here
	
	return Bi

def C3D20_Shape(r,Bi):
	#using the shape function for C3D20, the function returns a vector of weights 
	#corresponding to the natural coordinates in r. r is a nx1 matrix where n=3 corresponds 
	#to the location in the element to be evaluated.
	
	#weights
	h=np.zeros((20, 1),dtype='float64')
	
	#Node natural coordinates ordered by abaqus node id convention
	for node in range(0,20,1): #zero based indexing so 0-19
		if node < 8:
			h[node] = 1./8.*((1.+Bi[node][0]*r[0])*(1.+Bi[node][1]*r[1])*(1.+Bi[node][2]*r[2])*(Bi[node][0]*r[0]+Bi[node][1]*r[1]+Bi[node][2]*r[2]-2.))
		elif node == 8 or node == 10 or node == 12 or node == 14: 
			h[node] = 1./4.*((1.-r[0]*r[0])*(1.+Bi[node][1]*r[1])*(1.+Bi[node][2]*r[2]))
		elif node == 9 or node == 11 or node == 13 or node == 15: 
			h[node] = 1./4.*((1.-r[1]*r[1])*(1.+Bi[node][0]*r[0])*(1.+Bi[node][2]*r[2]))
		else: #16-19
			h[node] = 1./4.*((1.-r[2]*r[2])*(1.+Bi[node][0]*r[0])*(1.+Bi[node][1]*r[1]))
			
	return h

def C3D20_Shape_Derivatives(r,Bi):
	#using the shape function for C3D20, the function returns the gradient of the shape function 
	#with respect to the local coordinates 
	
	#weights
	dhdr=np.zeros((20, 3),dtype='float64')
	
	#Node natural coordinates ordered by abaqus node id convention
	for node in range(0,20,1): #zero based indexing so 0-19
		if node < 8:
			dhdr[node,0] = 1./8.*Bi[node][0]*(1.+Bi[node][1]*r[1])*(1.+Bi[node][2]*r[2])*(2*Bi[node][0]*r[0]+Bi[node][1]*r[1]+Bi[node][2]*r[2]-1.)
			dhdr[node,1] = 1./8.*Bi[node][1]*(1.+Bi[node][0]*r[0])*(1.+Bi[node][2]*r[2])*(Bi[node][0]*r[0]+2*Bi[node][1]*r[1]+Bi[node][2]*r[2]-1.)
			dhdr[node,2] = 1./8.*Bi[node][2]*(1.+Bi[node][0]*r[0])*(1.+Bi[node][1]*r[1])*(Bi[node][0]*r[0]+Bi[node][1]*r[1]+2*Bi[node][2]*r[2]-1.)
		elif node == 8 or node == 10 or node == 12 or node == 14: 
			dhdr[node,0] = -1./2.*r[0]*(1.+Bi[node][1]*r[1])*(1.+Bi[node][2]*r[2])
			dhdr[node,1] = 1./4.*Bi[node][1]*(1.-r[0]*r[0])*(1.+Bi[node][2]*r[2])
			dhdr[node,2] = 1./4.*Bi[node][2]*(1.-r[0]*r[0])*(1.+Bi[node][1]*r[1])
		elif node == 9 or node == 11 or node == 13 or node == 15: 
			dhdr[node,0] = 1./4.*Bi[node][0]*(1.-r[1]*r[1])*(1.+Bi[node][2]*r[2])
			dhdr[node,1] = -1./2.*r[1]*(1.+Bi[node][0]*r[0])*(1.+Bi[node][2]*r[2])
			dhdr[node,2] = 1./4.*Bi[node][2]*(1.-r[1]*r[1])*(1.+Bi[node][0]*r[0])
		else: #16-19
			dhdr[node,0] = 1./4.*Bi[node][0]*(1.-r[2]*r[2])*(1.+Bi[node][1]*r[1])
			dhdr[node,1] = 1./4.*Bi[node][1]*(1.-r[2]*r[2])*(1.+Bi[node][0]*r[0])
			dhdr[node,2] = -1./2.*r[2]*(1.+Bi[node][0]*r[0])*(1.+Bi[node][1]*r[1])	
			
	return dhdr	
	
def Reduce_Gauss_Data_to_C3D20_Shape(data,nElements):
	#maps the integration point id to equivalent spatial nodal layout
	mapping=[1,3,9,7,19,21,27,25,2,6,8,4,20,24,26,22,10,12,18,16]
	dataNew=np.zeros((len(mapping), nElements),dtype='float64')
	for i in range(0,len(mapping),1): 
		dataNew[i,:]=data[mapping[i]-1,:]
	
	return dataNew

def Convert_Nodal_to_Elemental_Nodal(scalarField,elements):
	# Abaqus does not compute nodal values such as displacement for the 
	# element nodal positions. Rebuilding the element nodal field data is needed 
	# for the shape functions to be used

	#Convert scalar field to linear array of nodal values sorted by nodeid
	dataNodal = np.array(scalarField.bulkDataBlocks[0].data,dtype='float64')
	dataNodal =  np.reshape(dataNodal,(-1,1))
	dataNodal = np.squeeze(dataNodal)
	
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
	dataElementNodal = dataNodal[connectivity]
		
	#Remove dimensions of size 1, reshape to #nodes/element * #element array
	dataElementNodal = np.squeeze(dataElementNodal)
	dataElementNodal = np.reshape(dataElementNodal,(len(elements),-1))
	dataElementNodal = np.transpose(dataElementNodal)
	return [dataNodal,dataElementNodal,connectivityMat]
	
def Convert_Elemental_Nodal_to_Gauss(scalarField,elements):
	nElements=len(elements)
	dataElementNodal = np.array(scalarField.bulkDataBlocks[0].data,dtype='float64')
	dataElementNodal =  np.reshape(dataElementNodal,(nElements,-1)) 
	dataElementNodal = np.transpose(dataElementNodal)
	dataElementNodal=np.round(dataElementNodal, decimals=1)
	print 'dataElementNodal'
	print dataElementNodal
	#interpolates var between element nodal and integrations points
	[points,weights]=Gauss_Guad_3d(3) #3 is the number of quadrature points along each dimension
	
	#Get the natural nodal coordinates for the element
	Bi=C3D20_nodal_coordinates()

	#evaluate the shape functions for the points we want to interpolate/extrapolate data to 
	h=np.zeros((len(points), 20),dtype='float64')
	#print points
	for i in range(0,len(points),1):
		r = points[i,:]
		tmp = C3D20_Shape(r,Bi)
		tmp = np.squeeze(tmp)
		h[i,:]=tmp
		#print tmp

	#compute the interpolated values dataGauss
	dataGauss = np.dot(h,dataElementNodal)
	
	#print dataGauss.shape
	return dataGauss

def Convert_Gauss_to_Elemental_Nodal(scalarField,elements):
	nElements=len(elements)
	dataGauss = np.array(scalarField.bulkDataBlocks[0].data,dtype='float64')
	dataGauss =  np.reshape(dataGauss,(nElements,-1))
	dataGauss = np.transpose(dataGauss)
	
	
	#scale natural nodal coordinates due to shift in basis from nodal to Gauss points
	points=C3D20_nodal_coordinates()*sqrt(5./3.)
	dataGauss=Reduce_Gauss_Data_to_C3D20_Shape(dataGauss,nElements) #reduce data to equivalent shape function positions
	#print dataGauss
    
	#Get the natural nodal coordinates for the element
	Bi=C3D20_nodal_coordinates()
	
	#evaluate the shape functions for the points we want to interpolate/extrapolate data to 
	h=np.zeros((len(points), 20),dtype='float64')
	#print points
	for i in range(0,len(points),1):
		r = points[i,:]
		tmp = C3D20_Shape(r,Bi)
		tmp = np.squeeze(tmp)
		h[i,:]=tmp
		#print tmp
    
	#compute the interpolated values dataElNodal
	dataElNodal = np.dot(h,dataGauss)
	
	
	return dataElNodal	

def Coordinate_Nodal_to_Face_integration(nodes,component,faces,elements):
	# Abaqus does not compute nodal values such as displacement for the 
	# element nodal positions. Rebuilding the element nodal field data is needed 
	# for the shape functions to be used
	
	#The coordinates can be obtained from a Scalarfield when COORD are save; 
	#however, the root assembly saves COORD with node definitions and we can reduce the odb size
    #by not using COORD
	
	nElements=len(elements)
	
	#Build the element connectivity matrix
	connectivityMat=np.zeros((nElements, 20))
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
	dataElementNodal = np.reshape(dataElementNodal,(nElements,-1))
	dataElementNodal = np.transpose(dataElementNodal) #nNodes*nElement
	
	dataElSurf=np.zeros((nElements, 9),dtype='float64')
	
	for f in range(1,7,1):
		#scale natural nodal coordinates due to shift in basis from nodal to Gauss points
		points,_ =Gauss_Guad_Psuedo_2d(3,f)
		
		#Get the natural nodal coordinates for the element
		Bi=C3D20_nodal_coordinates()
		
		#evaluate the shape functions for the points we want to interpolate/extrapolate data to 
		h=np.zeros((len(points), 20),dtype='float64')
		#print points
		for i in range(0,len(points),1):
			r = points[i,:]
			tmp = C3D20_Shape(r,Bi)
			tmp = np.squeeze(tmp)
			h[i,:]=tmp
			#print tmp
		
		#compute the interpolated values dataElSurftmp
		dataElSurftmp = np.dot(h,dataElementNodal) #produces a nPointxnEl array
		for el in range(0,nElements,1):
			if faces[el]==f:
				dataElSurf[el,:]=dataElSurftmp[:,el]		
	
	return dataElSurf			
	
def Convert_Gauss_to_Face_integration(scalarField,faces,elements):
	#returns extrapolated values for  3x3 integration for each element on the face specified in faces. 
	nElements=len(elements)
	dataGauss = np.array(scalarField.bulkDataBlocks[0].data,dtype='float64')
	dataGauss =  np.reshape(dataGauss,(nElements,-1)) #produces an nElxnInt array
	dataGauss = np.transpose(dataGauss) #produces an nIntxnEl array
	dataGauss=Reduce_Gauss_Data_to_C3D20_Shape(dataGauss,nElements) #reduce data to equivalent shape function positions
	
	dataElSurf=np.zeros((nElements, 9),dtype='float64')
	
	for f in range(1,7,1):
		#scale natural nodal coordinates due to shift in basis from nodal to Gauss points
		points,_ =Gauss_Guad_Psuedo_2d(3,f)
		points=points*sqrt(5./3.) 
		
		#Get the natural nodal coordinates for the element
		Bi=C3D20_nodal_coordinates()
		
		#evaluate the shape functions for the points we want to interpolate/extrapolate data to 
		h=np.zeros((len(points), 20),dtype='float64')
		#print points
		for i in range(0,len(points),1):
			r = points[i,:]
			tmp = C3D20_Shape(r,Bi)
			tmp = np.squeeze(tmp)
			h[i,:]=tmp
			#print tmp
		
		#compute the interpolated values dataElSurftmp
		dataElSurftmp = np.dot(h,dataGauss) #produces a nPointxnEl array
		for el in range(0,nElements,1):
			if faces[el]==f:
				dataElSurf[el,:]=dataElSurftmp[:,el]		
	
	return dataElSurf	

def Convert_Elemental_Nodal_to_Nodal(scalarField,doAverage):
	print 'to be done'

def Nodal_to_Elemental_Nodal(dataNodal,elements):
	connectivityMat=np.zeros((len(elements), len(elements[0].connectivity)))
	cnt=0
	for el in elements:
		connectivityMat[cnt,:]=el.connectivity
		cnt+=1
	
	#convert the connectivity to zero based index and reshape to linear array
	connectivityMat = connectivityMat.astype(int)-1
	connectivity=np.reshape(connectivityMat,(-1,1))
	
	#Get the element nodal values
	dataElementNodal = dataNodal[connectivity]
		
	#Remove dimensions of size 1, reshape to #nodes/element * #element array
	dataElementNodal = np.squeeze(dataElementNodal)
	dataElementNodal = np.reshape(dataElementNodal,(len(elements),-1))
	dataElementNodal = np.transpose(dataElementNodal)
	return [dataElementNodal,connectivityMat]
	
def ScalarField_Nodal_to_Elemental_Nodal(scalarField,blockComponent,elements):
	# Abaqus does not compute nodal values such as displacement for the 
	# element nodal positions. Rebuilding the element nodal field data is needed 
	# for the shape functions to be used

	#Convert scalar field to linear array of nodal values sorted by nodeid
	dataNodal = np.array(scalarField.bulkDataBlocks[blockComponent].data,dtype='float64')
	dataNodal =  np.reshape(dataNodal,(-1,1))
	dataNodal = np.squeeze(dataNodal)
	
	dataElementNodal, connectivityMat = Nodal_to_Elemental_Nodal(dataNodal,elements)
	return dataNodal, dataElementNodal, connectivityMat
	
def Coordinate_Nodal_to_Elemental_Nodal(nodes,component,elements):
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
		

#The following functions were used in validating the various aspects of the functions above.		
def Compare_Nodal_to_Elemental_Nodal(dataNodal,dataElementNodalMat,connectivityMat):	
	NodalNodeId=np.arange(1,len(dataNodal)+1,1)
	
	dataElementNodalMat=np.transpose(dataElementNodalMat)
	#print dataElementNodalMat.shape
	#print connectivityMat.shape
	#print connectivityMat
	nElements=len(dataElementNodalMat)
	#print nElements
	nNodes=20
	ElementalNodeId=np.zeros((nElements*nNodes,1),dtype=int)
	ElementalNodal=np.zeros((nElements*nNodes,1))
	ElementalId=np.zeros((nElements*nNodes,1),dtype=int)

	cnt=0
	for i in range(0,nElements,1):
		for j in range(0,nNodes,1):
			ElementalNodeId[cnt]=connectivityMat[i,j]
			ElementalNodal[cnt]=dataElementNodalMat[i,j]
			ElementalId[cnt]=i+1
			cnt+=1
	
	ElementalNodeId=np.squeeze(ElementalNodeId)
	ElementalNodal=np.squeeze(ElementalNodal)

	[u,unique]=np.unique(ElementalNodeId,return_index=True)
	ElementalNodeId=ElementalNodeId[unique]
	ElementalNodal=ElementalNodal[unique]
	
	ElementalNodeId=np.squeeze(ElementalNodeId)
	ElementalNodal=np.squeeze(ElementalNodal)
	dataNodal=np.squeeze(dataNodal)
	
	error=ElementalNodal-dataNodal
	#for i in range(0,len(ElementalNodeId),1):
	#	print ElementalNodeId[i],error[i]
	
	return not np.any(error)		
	
	fieldName='PEEQR'
	description='Plastic Equivalent Strain-rate'
	
	# Initialize the time variables where TT and TTAU are related by TTAU=TT+DT
	TT = 0.0
	
	# Loop over the steps
	for i in range(len(allSteps)):
		# Get current step object and the number of increments (frameLen) in step
		step = steps[allSteps[i]]
		frameLen = len(step.frames)  
		
		# Loop over the frames
		for j in range(0,frameLen,1):
			# Compute time variables
			currentFrame = step.frames[j]
			TTAU = currentFrame.frameValue
			DT = TTAU-TT
			
			# Extract the plastic equivalent strain (PEEQ) as a scalar field so we can do math
			PEEQ = currentFrame.fieldOutputs['PEEQ']
			PEEQTAU = PEEQ.getScalarField()
			
			# Handle first frame/step initialization and computation of PEEQR
			if i==0 and j==0:
				#Initialize strain-rate field to zero
				PEEQR = PEEQTAU
			else:
				PEEQR = (PEEQTAU-PEEQTT)/DT

			# Assign new variable
			currentFrame = Create_FieldObject_from_Existing_FieldOutput(currentFrame,
				fieldName,description,PEEQR)
				
			# Update old PEEQ and Time
			PEEQTT=PEEQTAU
			TT = TTAU
			print 'stepName = ', step.name, ', frameNumber = ', j, ', frameTime = ', TTAU
	
	odb.save()
	
def Test_Convert_Nodal_to_Elemental_Nodal(currentFrame,elements,fieldName,fieldComponentName):
	#Get the displacement field and convert to element/nodal displacement matrix
	field = currentFrame.fieldOutputs[fieldName] #.getSubset(position=ELEMENT_NODAL)
	
	scalarField=field.getScalarField(componentLabel=fieldComponentName) #ELEMENT_NODAL, INTEGRATION_POINT, NODAL, CENTROID

	#Convert the nodal values to element nodal values (exported as numpy matrix
	[dataNodal,dataElementNodal,connectivityMat] = \
		Convert_Nodal_to_Elemental_Nodal(scalarField,elements)
	
	#Verify the mapping is correct by comparing values at element node labels and node labels
	isGood = Compare_Nodal_to_Elemental_Nodal(dataNodal,dataElementNodal,connectivityMat)
	if isGood: 
		print "Test Passed: Element Nodal and Nodal values match" 
	else:
		raise NameError("!!!Test Failed: Element Nodal and Nodal values do not match!!!")
		
def Test_Convert_Element_Nodal_to_Gauss(currentFrame,elements,fieldName,fieldComponentName):
	#Get the displacement field and convert to element/nodal displacement matrix
	field = currentFrame.fieldOutputs[fieldName].getSubset(position=ELEMENT_NODAL)
	field2 = currentFrame.fieldOutputs[fieldName].getSubset(position=INTEGRATION_POINT)
	scalarField=field.getScalarField(componentLabel=fieldComponentName) #ELEMENT_NODAL, INTEGRATION_POINT, NODAL, CENTROID
	scalarField2=field2.getScalarField(componentLabel=fieldComponentName) #ELEMENT_NODAL, INTEGRATION_POINT, NODAL, CENTROID
	
	dataGauss=Convert_Elemental_Nodal_to_Gauss(scalarField,elements)
	
	dataGauss2 = np.array(scalarField2.bulkDataBlocks[0].data,dtype='float64')
	dataGauss2 =  np.reshape(dataGauss2,(len(elements),-1))
	dataGauss2 = np.transpose(dataGauss2)
	
	for i in range(0,len(elements)-1,1):
		eldata=dataGauss[:,i]
		eldata2=dataGauss2[:,i]
	 	for j in range(0,len(eldata),1):
			print("Integration label: %02d, Mine: %21.16e, Abaqus: %21.16e, diff: %21.16e  " % (j+1,eldata[j],eldata2[j],abs(eldata[j]-eldata2[j]) ))

def Test_Convert_Gauss_to_Element_Nodal(currentFrame,elements,fieldName,fieldComponentName):
	#Get the displacement field and convert to element/nodal displacement matrix
	field2 = currentFrame.fieldOutputs[fieldName].getSubset(position=ELEMENT_NODAL)
	field = currentFrame.fieldOutputs[fieldName].getSubset(position=INTEGRATION_POINT)
	scalarField=field.getScalarField(componentLabel=fieldComponentName) #ELEMENT_NODAL, INTEGRATION_POINT, NODAL, CENTROID
	scalarField2=field2.getScalarField(componentLabel=fieldComponentName) #ELEMENT_NODAL, INTEGRATION_POINT, NODAL, CENTROID

	dataElNodal=Convert_Gauss_to_Elemental_Nodal(scalarField,elements)
	nodeLabels = scalarField2.bulkDataBlocks[0].nodeLabels
	nodeLabels =  np.reshape(nodeLabels,(len(elements),-1))
	nodeLabels = np.transpose(nodeLabels)
	#print scalarField2.bulkDataBlocks[0].data
	dataElNodal2 = np.array(scalarField2.bulkDataBlocks[0].data,dtype='float64')
	dataElNodal2 =  np.reshape(dataElNodal2,(len(elements),-1))
	dataElNodal2 = np.transpose(dataElNodal2)
	dataElNodal3 = np.round(dataElNodal2,1)
	for i in range(0,len(elements)-1,1):
		eldata=dataElNodal[:,i]
		eldata2=dataElNodal2[:,i]
		eldata3=dataElNodal3[:,i]
	 	for j in range(0,len(eldata2),1):
			print("Node Label: %02d, Mine: %17.10e, Abaqus: %17.10e, My Error: %17.10e, Abaqus error: %17.10e  " % (nodeLabels[j,i],eldata[j],eldata2[j],abs(eldata[j]-eldata3[j]),abs(eldata2[j]-eldata3[j]) ))
		
def GetStrainFromdudX(frame,allNodes,elements): 
	
	#Computes the small strain measure E as exported by Abaqus
	
	elLabel = elements.label
	
	nElements=1#len(elements)
	nNodes=len(elements.connectivity)
	nPoints=GetNumIntegrationPoints(elements.type)
	
	#print 'get nodal coordinates in element nodal'
	#Get the nodal coordinates and map to element nodal coordinates (same thing but data structure is different)
	[ENCoord1,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,0,[elements])	
	[ENCoord2,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,1,[elements])
	[ENCoord3,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,2,[elements])
	
	#print 'get displacements in element nodal'
	#Get the nodal data and map to element nodal data.
	#elSet = root.elementSets[elSetName]
	field = frame.fieldOutputs['U'].getSubset(position=NODAL)
	SFU1=field.getScalarField(componentLabel='U1') 
	SFU2=field.getScalarField(componentLabel='U2') 
	SFU3=field.getScalarField(componentLabel='U3') 
	
	[NU1,ENU1,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU1,0,[elements])
	[NU2,ENU2,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU2,0,[elements])
	[NU3,ENU3,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU3,0,[elements])

	##interpolates var between element nodal and integrations points
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
	
	#Initialize arrays
	detJ=np.zeros((nElements,nPoints),dtype='float64')
	Jinvp=np.zeros((nPoints, 3,3),dtype='float64')
	dudx=np.zeros((3,3),dtype='float64')
	dudxt=np.zeros((3,3),dtype='float64')
	strain=np.zeros((nPoints,3,3),dtype='float64')

	I=np.eye(3);
	
	#Initialize dictionaries for saved element data
	#print '=====start solution====='
	#print nPoints
	for el in range(0,nElements,1):
		for p in range(0,nPoints,1): #p is looping over integration points in element elLabel[el]
			detJ[el,p]=np.linalg.det(J[p,el,:,:])
			Jinvp[p,:,:]=np.linalg.inv(J[p,el,:,:])	
			tmp=np.dot(dhdr[p,:,:],Jinvp[p,:,:]) #nNodes x 3
			tmp=np.transpose(tmp)
			dudx[0,:]=np.dot(tmp,ENU1[:,el])
			dudx[1,:]=np.dot(tmp,ENU2[:,el])
			dudx[2,:]=np.dot(tmp,ENU3[:,el])
			for i in range(0,3,1):
				for j in range(0,3,1):
					dudxt[j,i]=dudx[i,j]	
			print p, 0.5*(dudx+dudxt)

def GetIVOL(frame,allNodes,elements): 
	
	#For an element the IVOL variable is calculated from the Jacobian and 
	#Returns the spatial derivative of the scalarField with respect to global coordinates
	elLabel = elements.label
	
	nElements=1#len(elements)
	nNodes=len(elements.connectivity)
	nPoints=GetNumIntegrationPoints(elements.type)
	
	#print 'get nodal coordinates in element nodal'
	#Get the nodal coordinates and map to element nodal coordinates (same thing but data structure is different)
	[ENCoord1,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,0,[elements])	
	[ENCoord2,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,1,[elements])
	[ENCoord3,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,2,[elements])
	
	#print 'get displacements in element nodal'
	#Get the nodal data and map to element nodal data.
	#elSet = root.elementSets[elSetName]
	field = frame.fieldOutputs['U'].getSubset(position=NODAL)
	SFU1=field.getScalarField(componentLabel='U1') 
	SFU2=field.getScalarField(componentLabel='U2') 
	SFU3=field.getScalarField(componentLabel='U3') 
	
	[NU1,ENU1,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU1,0,[elements])
	[NU2,ENU2,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU2,0,[elements])
	[NU3,ENU3,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU3,0,[elements])

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
	detJWp=np.zeros((nElements,nPoints),dtype='float64')
	_,wp = Gauss_Guad_3d(3)
	wp = np.reshape(wp,(-1))
	
	
	#Initialize dictionaries for saved element data
	#print '=====start solution====='	
	for el in range(0,nElements,1):
		for p in range(0,nPoints,1): #p is looping over integration points in element elLabel[el]
			detJ[el,p]=np.linalg.det(J[p,el,:,:])
			detJWp[el,p]=detJ[el,p]*wp[p]
	print detJ
	print detJWp	
	