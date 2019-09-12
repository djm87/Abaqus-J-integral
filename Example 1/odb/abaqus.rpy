# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2019 replay file
# Internal Version: 2018_09_24-14.41.51 157541
# Run by dansa on Tue Sep  3 21:17:17 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=240.0, 
    height=199.907424926758)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='ThroughThicknessCrackInInfinitePlane.odb')
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlane.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       12
#: Number of Node Sets:          830
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
import os
os.chdir(r"E:\Dropbox\Research\Source\Abaqus-J-integral\Example 1")
#: 
#: Node: PLATE-1.17
#:                                         1             2             3        Magnitude
#: Base coordinates:                  6.00000e+00,  5.00000e-01,  2.00000e+00,      -      
#: No deformed coordinates for current plot.
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.605, 
    farPlane=19.5482, width=0.0810675, height=0.0381234, viewOffsetX=1.04284, 
    viewOffsetY=-2.2787)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: No modules to remove
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlane_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       12
#: Number of Node Sets:          830
#: Number of Steps:              1
#: test-contour-1-slice-0
#: test-contour-1-slice-1
#: test-contour-1-slice-2
#: test-contour-1-slice-3
#: test-contour-1-slice-4
#: test-contour-1-slice-5
#: test-contour-1-slice-6
#: test-contour-1-slice-7
#: test-contour-1-slice-8
#: test-contour-1-slice-9
#: test-contour-1-slice-10
#: test-contour-1-slice-11
#: test-contour-1-slice-12
#: test-contour-1-slice-13
#: test-contour-1-slice-14
#: test-contour-1-slice-15
#: test-contour-1-slice-16
#: test-contour-1-slice-17
#: test-contour-1-slice-18
#: test-contour-1-slice-19
#: test-contour-1-slice-20
#: test-contour-2-slice-0
#: test-contour-2-slice-1
#: test-contour-2-slice-2
#: test-contour-2-slice-3
#: test-contour-2-slice-4
#: test-contour-2-slice-5
#: test-contour-2-slice-6
#: test-contour-2-slice-7
#: test-contour-2-slice-8
#: test-contour-2-slice-9
#: test-contour-2-slice-10
#: test-contour-2-slice-11
#: test-contour-2-slice-12
#: test-contour-2-slice-13
#: test-contour-2-slice-14
#: test-contour-2-slice-15
#: test-contour-2-slice-16
#: test-contour-2-slice-17
#: test-contour-2-slice-18
#: test-contour-2-slice-19
#: test-contour-2-slice-20
#: test-contour-3-slice-0
#: test-contour-3-slice-1
#: test-contour-3-slice-2
#: test-contour-3-slice-3
#: test-contour-3-slice-4
#: test-contour-3-slice-5
#: test-contour-3-slice-6
#: test-contour-3-slice-7
#: test-contour-3-slice-8
#: test-contour-3-slice-9
#: test-contour-3-slice-10
#: test-contour-3-slice-11
#: test-contour-3-slice-12
#: test-contour-3-slice-13
#: test-contour-3-slice-14
#: test-contour-3-slice-15
#: test-contour-3-slice-16
#: test-contour-3-slice-17
#: test-contour-3-slice-18
#: test-contour-3-slice-19
#: test-contour-3-slice-20
#: test-contour-4-slice-0
#: test-contour-4-slice-1
#: test-contour-4-slice-2
#: test-contour-4-slice-3
#: test-contour-4-slice-4
#: test-contour-4-slice-5
#: test-contour-4-slice-6
#: test-contour-4-slice-7
#: test-contour-4-slice-8
#: test-contour-4-slice-9
#: test-contour-4-slice-10
#: test-contour-4-slice-11
#: test-contour-4-slice-12
#: test-contour-4-slice-13
#: test-contour-4-slice-14
#: test-contour-4-slice-15
#: test-contour-4-slice-16
#: test-contour-4-slice-17
#: test-contour-4-slice-18
#: test-contour-4-slice-19
#: test-contour-4-slice-20
#: test-contour-5-slice-0
#: test-contour-5-slice-1
#: test-contour-5-slice-2
#: test-contour-5-slice-3
#: test-contour-5-slice-4
#: test-contour-5-slice-5
#: test-contour-5-slice-6
#: test-contour-5-slice-7
#: test-contour-5-slice-8
#: test-contour-5-slice-9
#: test-contour-5-slice-10
#: test-contour-5-slice-11
#: test-contour-5-slice-12
#: test-contour-5-slice-13
#: test-contour-5-slice-14
#: test-contour-5-slice-15
#: test-contour-5-slice-16
#: test-contour-5-slice-17
#: test-contour-5-slice-18
#: test-contour-5-slice-19
#: test-contour-5-slice-20
#: test-contour-6-slice-0
#: test-contour-6-slice-1
#: test-contour-6-slice-2
#: test-contour-6-slice-3
#: test-contour-6-slice-4
#: test-contour-6-slice-5
#: test-contour-6-slice-6
#: test-contour-6-slice-7
#: test-contour-6-slice-8
#: test-contour-6-slice-9
#: test-contour-6-slice-10
#: test-contour-6-slice-11
#: test-contour-6-slice-12
#: test-contour-6-slice-13
#: test-contour-6-slice-14
#: test-contour-6-slice-15
#: test-contour-6-slice-16
#: test-contour-6-slice-17
#: test-contour-6-slice-18
#: test-contour-6-slice-19
#: test-contour-6-slice-20
#: test-contour-7-slice-0
#: test-contour-7-slice-1
#: test-contour-7-slice-2
#: test-contour-7-slice-3
#: test-contour-7-slice-4
#: test-contour-7-slice-5
#: test-contour-7-slice-6
#: test-contour-7-slice-7
#: test-contour-7-slice-8
#: test-contour-7-slice-9
#: test-contour-7-slice-10
#: test-contour-7-slice-11
#: test-contour-7-slice-12
#: test-contour-7-slice-13
#: test-contour-7-slice-14
#: test-contour-7-slice-15
#: test-contour-7-slice-16
#: test-contour-7-slice-17
#: test-contour-7-slice-18
#: test-contour-7-slice-19
#: test-contour-7-slice-20
#: test-contour-8-slice-0
#: test-contour-8-slice-1
#: test-contour-8-slice-2
#: test-contour-8-slice-3
#: test-contour-8-slice-4
#: test-contour-8-slice-5
#: test-contour-8-slice-6
#: test-contour-8-slice-7
#: test-contour-8-slice-8
#: test-contour-8-slice-9
#: test-contour-8-slice-10
#: test-contour-8-slice-11
#: test-contour-8-slice-12
#: test-contour-8-slice-13
#: test-contour-8-slice-14
#: test-contour-8-slice-15
#: test-contour-8-slice-16
#: test-contour-8-slice-17
#: test-contour-8-slice-18
#: test-contour-8-slice-19
#: test-contour-8-slice-20
#: test-contour-9-slice-0
#: test-contour-9-slice-1
#: test-contour-9-slice-2
#: test-contour-9-slice-3
#: test-contour-9-slice-4
#: test-contour-9-slice-5
#: test-contour-9-slice-6
#: test-contour-9-slice-7
#: test-contour-9-slice-8
#: test-contour-9-slice-9
#: test-contour-9-slice-10
#: test-contour-9-slice-11
#: test-contour-9-slice-12
#: test-contour-9-slice-13
#: test-contour-9-slice-14
#: test-contour-9-slice-15
#: test-contour-9-slice-16
#: test-contour-9-slice-17
#: test-contour-9-slice-18
#: test-contour-9-slice-19
#: test-contour-9-slice-20
#: test-contour-10-slice-0
#: test-contour-10-slice-1
#: test-contour-10-slice-2
#: test-contour-10-slice-3
#: test-contour-10-slice-4
#: test-contour-10-slice-5
#: test-contour-10-slice-6
#: test-contour-10-slice-7
#: test-contour-10-slice-8
#: test-contour-10-slice-9
#: test-contour-10-slice-10
#: test-contour-10-slice-11
#: test-contour-10-slice-12
#: test-contour-10-slice-13
#: test-contour-10-slice-14
#: test-contour-10-slice-15
#: test-contour-10-slice-16
#: test-contour-10-slice-17
#: test-contour-10-slice-18
#: test-contour-10-slice-19
#: test-contour-10-slice-20
#: test-contour-11-slice-0
#: test-contour-11-slice-1
#: test-contour-11-slice-2
#: test-contour-11-slice-3
#: test-contour-11-slice-4
#: test-contour-11-slice-5
#: test-contour-11-slice-6
#: test-contour-11-slice-7
#: test-contour-11-slice-8
#: test-contour-11-slice-9
#: test-contour-11-slice-10
#: test-contour-11-slice-11
#: test-contour-11-slice-12
#: test-contour-11-slice-13
#: test-contour-11-slice-14
#: test-contour-11-slice-15
#: test-contour-11-slice-16
#: test-contour-11-slice-17
#: test-contour-11-slice-18
#: test-contour-11-slice-19
#: test-contour-11-slice-20
#: test-contour-12-slice-0
#: test-contour-12-slice-1
#: test-contour-12-slice-2
#: test-contour-12-slice-3
#: test-contour-12-slice-4
#: test-contour-12-slice-5
#: test-contour-12-slice-6
#: test-contour-12-slice-7
#: test-contour-12-slice-8
#: test-contour-12-slice-9
#: test-contour-12-slice-10
#: test-contour-12-slice-11
#: test-contour-12-slice-12
#: test-contour-12-slice-13
#: test-contour-12-slice-14
#: test-contour-12-slice-15
#: test-contour-12-slice-16
#: test-contour-12-slice-17
#: test-contour-12-slice-18
#: test-contour-12-slice-19
#: test-contour-12-slice-20
#: time report
#: ++++++++++++
#: time in first loop 0.559000015259
#: time in first loop get El 0.273999452591
#: time in first loop get union 0.0989999771118
#: time in second loop 8.22599983215
#: time in third loop 0.0989999771118
#: ++++++++++++
#: ++++++++++++
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.5106, 
    farPlane=19.6425, width=1.10098, height=0.517757, viewOffsetX=1.06943, 
    viewOffsetY=-2.15868)
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlane_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.5832, 
    farPlane=19.5699, width=0.315708, height=0.148467, viewOffsetX=1.06167, 
    viewOffsetY=-2.24993)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlane.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       12
#: Number of Node Sets:          830
#: Number of Steps:              1
#: test-contour-1-slice-0
#: test-contour-1-slice-1
#: test-contour-1-slice-2
#: test-contour-1-slice-3
#: test-contour-1-slice-4
#: test-contour-1-slice-5
#: test-contour-1-slice-6
#: test-contour-1-slice-7
#: test-contour-1-slice-8
#: test-contour-1-slice-9
#: test-contour-1-slice-10
#: test-contour-1-slice-11
#: test-contour-1-slice-12
#: test-contour-1-slice-13
#: test-contour-1-slice-14
#: test-contour-1-slice-15
#: test-contour-1-slice-16
#: test-contour-1-slice-17
#: test-contour-1-slice-18
#: test-contour-1-slice-19
#: test-contour-1-slice-20
#: test-contour-2-slice-0
#: test-contour-2-slice-1
#: test-contour-2-slice-2
#: test-contour-2-slice-3
#: test-contour-2-slice-4
#: test-contour-2-slice-5
#: test-contour-2-slice-6
#: test-contour-2-slice-7
#: test-contour-2-slice-8
#: test-contour-2-slice-9
#: test-contour-2-slice-10
#: test-contour-2-slice-11
#: test-contour-2-slice-12
#: test-contour-2-slice-13
#: test-contour-2-slice-14
#: test-contour-2-slice-15
#: test-contour-2-slice-16
#: test-contour-2-slice-17
#: test-contour-2-slice-18
#: test-contour-2-slice-19
#: test-contour-2-slice-20
#: test-contour-3-slice-0
#: test-contour-3-slice-1
#: test-contour-3-slice-2
#: test-contour-3-slice-3
#: test-contour-3-slice-4
#: test-contour-3-slice-5
#: test-contour-3-slice-6
#: test-contour-3-slice-7
#: test-contour-3-slice-8
#: test-contour-3-slice-9
#: test-contour-3-slice-10
#: test-contour-3-slice-11
#: test-contour-3-slice-12
#: test-contour-3-slice-13
#: test-contour-3-slice-14
#: test-contour-3-slice-15
#: test-contour-3-slice-16
#: test-contour-3-slice-17
#: test-contour-3-slice-18
#: test-contour-3-slice-19
#: test-contour-3-slice-20
#: test-contour-4-slice-0
#: test-contour-4-slice-1
#: test-contour-4-slice-2
#: test-contour-4-slice-3
#: test-contour-4-slice-4
#: test-contour-4-slice-5
#: test-contour-4-slice-6
#: test-contour-4-slice-7
#: test-contour-4-slice-8
#: test-contour-4-slice-9
#: test-contour-4-slice-10
#: test-contour-4-slice-11
#: test-contour-4-slice-12
#: test-contour-4-slice-13
#: test-contour-4-slice-14
#: test-contour-4-slice-15
#: test-contour-4-slice-16
#: test-contour-4-slice-17
#: test-contour-4-slice-18
#: test-contour-4-slice-19
#: test-contour-4-slice-20
#: test-contour-5-slice-0
#: test-contour-5-slice-1
#: test-contour-5-slice-2
#: test-contour-5-slice-3
#: test-contour-5-slice-4
#: test-contour-5-slice-5
#: test-contour-5-slice-6
#: test-contour-5-slice-7
#: test-contour-5-slice-8
#: test-contour-5-slice-9
#: test-contour-5-slice-10
#: test-contour-5-slice-11
#: test-contour-5-slice-12
#: test-contour-5-slice-13
#: test-contour-5-slice-14
#: test-contour-5-slice-15
#: test-contour-5-slice-16
#: test-contour-5-slice-17
#: test-contour-5-slice-18
#: test-contour-5-slice-19
#: test-contour-5-slice-20
#: test-contour-6-slice-0
#: test-contour-6-slice-1
#: test-contour-6-slice-2
#: test-contour-6-slice-3
#: test-contour-6-slice-4
#: test-contour-6-slice-5
#: test-contour-6-slice-6
#: test-contour-6-slice-7
#: test-contour-6-slice-8
#: test-contour-6-slice-9
#: test-contour-6-slice-10
#: test-contour-6-slice-11
#: test-contour-6-slice-12
#: test-contour-6-slice-13
#: test-contour-6-slice-14
#: test-contour-6-slice-15
#: test-contour-6-slice-16
#: test-contour-6-slice-17
#: test-contour-6-slice-18
#: test-contour-6-slice-19
#: test-contour-6-slice-20
#: test-contour-7-slice-0
#: test-contour-7-slice-1
#: test-contour-7-slice-2
#: test-contour-7-slice-3
#: test-contour-7-slice-4
#: test-contour-7-slice-5
#: test-contour-7-slice-6
#: test-contour-7-slice-7
#: test-contour-7-slice-8
#: test-contour-7-slice-9
#: test-contour-7-slice-10
#: test-contour-7-slice-11
#: test-contour-7-slice-12
#: test-contour-7-slice-13
#: test-contour-7-slice-14
#: test-contour-7-slice-15
#: test-contour-7-slice-16
#: test-contour-7-slice-17
#: test-contour-7-slice-18
#: test-contour-7-slice-19
#: test-contour-7-slice-20
#: test-contour-8-slice-0
#: test-contour-8-slice-1
#: test-contour-8-slice-2
#: test-contour-8-slice-3
#: test-contour-8-slice-4
#: test-contour-8-slice-5
#: test-contour-8-slice-6
#: test-contour-8-slice-7
#: test-contour-8-slice-8
#: test-contour-8-slice-9
#: test-contour-8-slice-10
#: test-contour-8-slice-11
#: test-contour-8-slice-12
#: test-contour-8-slice-13
#: test-contour-8-slice-14
#: test-contour-8-slice-15
#: test-contour-8-slice-16
#: test-contour-8-slice-17
#: test-contour-8-slice-18
#: test-contour-8-slice-19
#: test-contour-8-slice-20
#: test-contour-9-slice-0
#: test-contour-9-slice-1
#: test-contour-9-slice-2
#: test-contour-9-slice-3
#: test-contour-9-slice-4
#: test-contour-9-slice-5
#: test-contour-9-slice-6
#: test-contour-9-slice-7
#: test-contour-9-slice-8
#: test-contour-9-slice-9
#: test-contour-9-slice-10
#: test-contour-9-slice-11
#: test-contour-9-slice-12
#: test-contour-9-slice-13
#: test-contour-9-slice-14
#: test-contour-9-slice-15
#: test-contour-9-slice-16
#: test-contour-9-slice-17
#: test-contour-9-slice-18
#: test-contour-9-slice-19
#: test-contour-9-slice-20
#: test-contour-10-slice-0
#: test-contour-10-slice-1
#: test-contour-10-slice-2
#: test-contour-10-slice-3
#: test-contour-10-slice-4
#: test-contour-10-slice-5
#: test-contour-10-slice-6
#: test-contour-10-slice-7
#: test-contour-10-slice-8
#: test-contour-10-slice-9
#: test-contour-10-slice-10
#: test-contour-10-slice-11
#: test-contour-10-slice-12
#: test-contour-10-slice-13
#: test-contour-10-slice-14
#: test-contour-10-slice-15
#: test-contour-10-slice-16
#: test-contour-10-slice-17
#: test-contour-10-slice-18
#: test-contour-10-slice-19
#: test-contour-10-slice-20
#: test-contour-11-slice-0
#: test-contour-11-slice-1
#: test-contour-11-slice-2
#: test-contour-11-slice-3
#: test-contour-11-slice-4
#: test-contour-11-slice-5
#: test-contour-11-slice-6
#: test-contour-11-slice-7
#: test-contour-11-slice-8
#: test-contour-11-slice-9
#: test-contour-11-slice-10
#: test-contour-11-slice-11
#: test-contour-11-slice-12
#: test-contour-11-slice-13
#: test-contour-11-slice-14
#: test-contour-11-slice-15
#: test-contour-11-slice-16
#: test-contour-11-slice-17
#: test-contour-11-slice-18
#: test-contour-11-slice-19
#: test-contour-11-slice-20
#: test-contour-12-slice-0
#: test-contour-12-slice-1
#: test-contour-12-slice-2
#: test-contour-12-slice-3
#: test-contour-12-slice-4
#: test-contour-12-slice-5
#: test-contour-12-slice-6
#: test-contour-12-slice-7
#: test-contour-12-slice-8
#: test-contour-12-slice-9
#: test-contour-12-slice-10
#: test-contour-12-slice-11
#: test-contour-12-slice-12
#: test-contour-12-slice-13
#: test-contour-12-slice-14
#: test-contour-12-slice-15
#: test-contour-12-slice-16
#: test-contour-12-slice-17
#: test-contour-12-slice-18
#: test-contour-12-slice-19
#: test-contour-12-slice-20
#: time report
#: ++++++++++++
#: time in first loop 0.65499997139
#: time in first loop get El 0.321999549866
#: time in first loop get union 0.111999988556
#: time in second loop 8.59100008011
#: time in third loop 0.0999999046326
#: ++++++++++++
#: ++++++++++++
#: Processing Contour:  0
#: slice #: 0
#* IndexError: Sequence index out of range
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1219, in CalculateDomainJIntegral
#*     dudX,detJac,dudXElLabels = 
#* GetdudX(root,frame,allNodes,nSetSlice,elSetSlice)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 444, 
#* in GetdudX
#*     [NU1,ENU1,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU1,1,elements)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\C3D20.py", line 213, 
#* in ScalarField_Nodal_to_Elemental_Nodal
#*     dataNodal = 
#* np.array(scalarField.bulkDataBlocks[blockComponent].data,dtype='float64')
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlane.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       12
#: Number of Node Sets:          830
#: Number of Steps:              1
#: Processing Contour:  0
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
#: Processing Contour:  1
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
#: Processing Contour:  2
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
#: Processing Contour:  3
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
#: Processing Contour:  4
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
#: Processing Contour:  5
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
#: Processing Contour:  6
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
#: Processing Contour:  7
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
#: Processing Contour:  8
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
#: Processing Contour:  9
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
#: Processing Contour:  10
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
#: Processing Contour:  11
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: slice #: 5
#: slice #: 6
#: slice #: 7
#: slice #: 8
#: slice #: 9
#: slice #: 10
#: slice #: 11
#: slice #: 12
#: slice #: 13
#: slice #: 14
#: slice #: 15
#: slice #: 16
#: slice #: 17
#: slice #: 18
#: slice #: 19
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.5863, 
    farPlane=20.5669, width=12.4833, height=5.87049, viewOffsetX=1.73354, 
    viewOffsetY=0.460095)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
    'Magnitude'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.6606, 
    farPlane=20.897, width=11.101, height=5.22045, viewOffsetX=1.85268, 
    viewOffsetY=0.207403)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.1773, 
    farPlane=20.8306, width=11.5929, height=5.45177, cameraPosition=(15.4507, 
    0.0335948, 11.3218), cameraUpVector=(-0.120777, 0.971433, -0.204283), 
    cameraTarget=(3.27628, 1.86221, 0.982845), viewOffsetX=1.93477, 
    viewOffsetY=0.216593)
