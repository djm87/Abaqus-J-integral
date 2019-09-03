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
except KeyError:
	print 'No modules to remove'

from Utilities import *
from JCore import *

#Get the working directory 
workingDir=os.getcwd()

#******************************************************************************
#Run options 
#******************************************************************************
#ODB name 
odbName="ThroughThicknessCrackInInfinitePlaneNoSymm"
odbPath = os.path.normpath(workingDir+"/odb/"+odbName+".odb")

#Open odb read only mode
readOnlyOdb = False

#Close odb before opening 
closeBeforeOdb=True

#Close odb after opening 
closeAfterOdb=False

#Copy odb to new odb if writing 
copyOdb=True 
copyodbNameEnd="_copy"
copyodbPath=os.path.normpath(workingDir+"/odb/"+odbName+copyodbNameEnd+".odb")

#Set the part instance to perform calculations on
partInstance = "PLATE-1"


##The following are specific to the J integral 
#The crack front axis
crackFrontAxis=3 #i.e. 3 is along the z direction

qdir=1
#Set the number of contour levels
nContourLvls=13 

#Set the first node label at the crack tip 
nodeLabelTip=26 

#model is symmetric about the crack tip (matters only for scaling J integral by 2)
symm=False

#Build element sets (needed for calculating the J integral
buildElSet=True

#Element set preface name (Once a set has been added with this name it cannot be overwritten or removed)
SetPrefix='test2'

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


if buildElSet:
	BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,odb,partInstance) #Move elements inside

if closeAfterOdb:
	odb.close()
