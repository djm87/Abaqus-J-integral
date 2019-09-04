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
odbName="ThroughThicknessCrackInInfinitePlane"
odbPath = os.path.normpath(workingDir+"/odb/"+odbName+".odb")

#Open odb read only mode
readOnlyOdb = False

#Close odb before opening 
closeBeforeOdb=True

#Close odb after opening 
closeAfterOdb=False

#Copy odb to new odb if writing 
copyOdb=False 
copyodbNameEnd="_copy"
copyodbPath=os.path.normpath(workingDir+"/odb/"+odbName+copyodbNameEnd+".odb")

#Save odb
saveOdb=False

#Set the part instance to perform calculations on
partInstance = "PLATE-1"


##The following are specific to the J integral 
#The crack front axis
crackFrontAxis=3 #i.e. 3 is along the z direction

#Set the number of contour levels
nContourLvls=12 

#Set the first node label at the crack tip 
nodeLabelTip=17 

#model is symmetric about the crack tip (matters only for scaling J integral by 2)
isSymm=True

#Build element sets (needed for calculating the J integral
buildElSet=False

#Element set preface name (Once a set has been added with this name it cannot be overwritten or removed)
SetPrefix='test'

#Should the J integral be computed
computeJ=True

#Which contours should be evaluated (a list and cant exceed the number of contours in ElSet)
contours=range(12) #explicitly [0,1,2] for instance

#Which frame should be evaluate (a list, a frame corresponds to some time, -1 is automatically the last frame)
frameNumbers=[-1]

#Which slices should be evaluated (a list)
slices=range(20)

#Specify the step number (not a list, -1 is automatically the last step) 
stepNumber=-1
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


if buildElSet:
	odb = BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,odb,partInstance) #Move elements inside

if computeJ:
	CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,nodeLabelTip,isSymm,odb,partInstance)
	
if saveOdb:
	odb.save()
	
if closeAfterOdb:
	odb.close()
