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
	del sys.modules['C3D20']
	del sys.modules['Integration']
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
odbName="J-Indenter_Quarter_copy"
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
partInstance = "SPECIMEN-1"


##The following are specific to the J integral 
#The crack front axis
crackFrontAxis=3 #i.e. 3 is along the z direction

#Set the number of contour levels
nContourLvls=21

#Set the first node label at the crack tip 
nodeLabelTip=1780 

#Set the beginning and ending elSet range for the material sections
sectionElSetRange=range(0,125,1) #e.g. for sets include 0 through 124

#model is symmetric about the crack tip (matters only for scaling J integral by 2)
isSymm=True

#Build element sets (needed for calculating the J integral
buildElSet=False

#Element set preface name (Once a set has been added with this name it cannot be overwritten or removed)
SetPrefix='test-contour'

#Should the J integral be computed
computeJ=True
JFnamePrefix='Js_'

#Should the J integral around interfaces be computed
computeJInterface=True
JInt=np.array([])
JIntFnamePrefix='Js_Interface_'

#Should the stress intensity factor be computed
computeK=True
KFnamePrefix='Ks_'
E=60e3
v=0.3

#unit scaling
#This model doesn't seem to have consistent SI units based on the modulus values and lengths.. revisit
#
Junit=1 #1e-6J/um^2 
Kunit=1 #sqrt(1e-6J/um^2 N/um^2  ) 


#Which contours should be evaluated (a list and cant exceed the number of contours in ElSet)
contours=range(0,20,1) #explicitly [0,1,2] for instance

#Which frame should be evaluate (a list, a frame corresponds to some time, -1 is automatically the last frame)
frameNumbers=[-1]#range(2,10,1)

#Which slices should be evaluated (a list)
slices=[0]#range(29)

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

t0=time.time()
if buildElSet:
	odb = BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,sectionElSetRange,odb,partInstance) #Move elements inside

t1=time.time()
if computeJInterface:
	JInt=CalculateDomainJIntegralInterface(Junit,stepNumber,frameNumbers,contours,slices,SetPrefix,nodeLabelTip,isSymm,odb,partInstance,JIntFnamePrefix)

t2=time.time()
if computeJ:
	J=CalculateDomainJIntegral(Junit,JInt,stepNumber,frameNumbers,contours,slices,SetPrefix,nodeLabelTip,isSymm,odb,partInstance,JFnamePrefix)	

t3=time.time()	
if computeK:
	CalculateK(Kunit,J,E,v,KFnamePrefix,SetPrefix,contours,slices,nodeLabelTip,stepNumber,frameNumbers,odb,partInstance)
	
t4=time.time()
if saveOdb:
	odb.save()
	
if closeAfterOdb:
	odb.close()

print "time report"
print '++++++++++++'
print 'time building sets',t1-t0
print 'time in J integral Surface',t2-t1
print 'time in J integral Volume',t3-t2
print 'time in J to KI',t4-t3
