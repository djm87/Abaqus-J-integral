import Utilities
import Integration
import C3D20 
import JCore

#Get the working directory 
workingDir=os.getcwd()

#******************************************************************************
#Run options 
#******************************************************************************
#ODB name 
odbPath = os.path.normpath(workingDir+"/Job-3PB-Quarter-All-C3D20-Dan.odb")

#Open odb read only mode
readOnlyOdb = True

#Close odb before opening 
closeBeforeOdb=True

#Close odb after opening 
closeAfterOdb=False

#Copy odb to new odb if writing 
copyOdb=False 
copyodbPath=os.path.normpath(workingDir+"/Job-3PB-Quarter-All-C3D20-Dan.odb")

#Set the part instance to perform calculations on
partInstance = "NOCHEDSPECIMEN-C-1"


##The following are specific to the J integral
#The crack front axis
crackFrontAxis=3 

#Set the number of contour levels
nContourLvls=10 

#Set the first node label at the crack tip 
nodeLabelTip=512 

#model is symmetric about the crack tip
symm=False

#Build element sets (needed for calculating the J integral
buildElSet=False

#Element set preface name (Once a set has been added with this name it cannot be overwritten or removed)
ElSetName='test2'

#******************************************************************************
#Open ODB
#******************************************************************************
if closeBeforeOdb:
	if copyOdb:
		Ensure_ODB_Is_Closed(copyodbPath,session)
	else:
		Ensure_ODB_Is_Closed(odbPath,session)
if copyOdb:
	copyfile(odbPath, copyodbPath)
	odb = openOdb(path=copyodbPath,readOnly=readOnlyOdb)
else:
	odb = openOdb(path=odbPath,readOnly=readOnlyOdb)

# Get components of odb
root=odb.rootAssembly
part=root.instances[partInstance]
steps=odb.steps

# Get the step keys
allSteps = steps.keys()

# Get current step object and the number of increments (frameLen) in step
step = steps[allSteps[-1]]

# Get current data frame and time
frames=step.frames
lastFrame = frames[-1]

#current time
TTAU = lastFrame.frameValue

#Get the elements
elements=part.elements

if buildElSet:

	BuildElementAndNodeSets(nContourLvls,nodeLabelTip,crackFrontAxis,elements,root,partInstance) #Move elements inside

if closeAfterOdb:
	odb.close()
