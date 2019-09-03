# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2019 replay file
# Internal Version: 2018_09_24-14.41.51 157541
# Run by dansa on Wed Aug 28 10:14:23 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=239.511444091797, 
    height=197.555557250977)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='ThroughThicknessCrackInInfinitePlaneNoSymm.odb')
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.9505, 
    farPlane=34.5919, width=16.031, height=7.46975, viewOffsetX=0.836516, 
    viewOffsetY=0.155464)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.8764, 
    farPlane=34.666, width=15.9743, height=7.44331, viewOffsetX=1.26652, 
    viewOffsetY=-1.46122)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.876, 
    farPlane=34.6664, width=15.974, height=7.4432, viewOffsetX=1.17535, 
    viewOffsetY=-0.675903)
#: 
#: Node: PLATE-1.26
#:                                         1             2             3        Magnitude
#: Base coordinates:                  6.00000e+00,  5.00000e-01,  2.00000e+00,      -      
#: Scale:                             1.96022e+06,  1.96022e+06,  1.96022e+06,      -      
#: Deformed coordinates (unscaled):   6.00000e+00,  5.00000e-01,  2.00000e+00,      -      
#: Deformed coordinates (scaled):     6.60000e+00,  4.60371e-01,  2.00000e+00,      -      
#: Displacement (unscaled):           3.06088e-07, -2.02167e-08, -3.75620e-37,  3.06755e-07
session.viewports['Viewport: 1'].view.setValues(nearPlane=22.2677, 
    farPlane=33.2747, width=0.0227051, height=0.0105796, viewOffsetX=-0.613707, 
    viewOffsetY=-1.19359)
import os
os.chdir(r"E:\Dropbox\Research\Source\Abaqus-J-integral\Example 1")
session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm.odb'].close(
    )
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* NameError: name 'Ensure_ODB_Is_Closed' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 64, in <module>
#*     Ensure_ODB_Is_Closed(odbPath,session)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* ImportError: No module named py
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 5, in <module>
#*     import Utilities.py
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* NameError: name 'Ensure_ODB_Is_Closed' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 64, in <module>
#*     Ensure_ODB_Is_Closed(odbPath,session)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* NameError: name 'openOdb' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 69, in <module>
#*     odb = openOdb(path=odbPath,readOnly=readOnlyOdb)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* OdbError: Cannot open file 
#* E:/Dropbox/Research/Source/Abaqus-J-integral/Example 
#* 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb. *** ERROR: No 
#* such file: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 
#* 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb.
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 69, in <module>
#*     odb = openOdb(path=odbPath,readOnly=readOnlyOdb)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* OdbError: Cannot open file 
#* E:/Dropbox/Research/Source/Abaqus-J-integral/Example 
#* 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb. *** ERROR: No 
#* such file: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 
#* 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb.
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 69, in <module>
#*     odb = openOdb(path=odbPath,readOnly=readOnlyOdb)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: things  worked to here
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: things  worked to here
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: things  worked to here
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: things  worked to here
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.2581, 
    farPlane=34.2843, width=10.9312, height=5.09346, viewOffsetX=0.19349, 
    viewOffsetY=-0.79478)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#* TypeError: BuildElementAndNodeSets() takes exactly 5 arguments (6 given)
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 92, in <module>
#*     
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* root,partInstance) #Move elements inside
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#* TypeError: BuildElementAndNodeSets() takes exactly 5 arguments (6 given)
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 92, in <module>
#*     
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* root,partInstance) #Move elements inside
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* ImportError: reload(): module Utilities not in sys.modules
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 14, in <module>
#*     reload(Utilities)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#* NameError: global name 'np' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 96, in <module>
#*     
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* root,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 66, 
#* in BuildElementAndNodeSets
#*     labels,position,pos1,pos2 = GetCrackFrontNodes(allNodes,nodeLabelTip,2)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 21, 
#* in GetCrackFrontNodes
#*     CFnSet,ind=np.unique(np.array(CFnSet), return_index=True)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* TypeError: exceptions must be old-style classes or derived from 
#* BaseException, not NoneType
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 13, in <module>
#*     raise
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* KeyError: ('Utilities',)
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 4, in <module>
#*     del sys.modules['Utilities']
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* KeyError: 'Utilities'
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 6, in <module>
#*     del sys.modules['Utilities']
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: No modules to remove
#* KeyError: 'Utilities'
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 6, in <module>
#*     del sys.modules['Utilities']
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: No modules to remove
#* KeyError: 'Utilities'
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 6, in <module>
#*     del sys.modules['Utilities']
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: No modules to remove
#* KeyError: 'Utilities'
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 6, in <module>
#*     del sys.modules['Utilities']
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* SyntaxError: ('invalid syntax', 
#* ('E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 10, 
#* 4, 'else:\n'))
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: No modules to remove
#* KeyError: 'Utilities'
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 6, in <module>
#*     del sys.modules['Utilities']
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: No modules to remove
#* AttributeError: 'NoneType' object has no attribute 'path'
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 70, in <module>
#*     Ensure_ODB_Is_Closed(copyodbPath,session)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\Utilities.py", line 
#* 22, in Ensure_ODB_Is_Closed
#*     path=os.path.normpath(session.odbs[key].path)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: No modules to remove
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#* NameError: global name 'np' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 100, in <module>
#*     
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* root,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 66, 
#* in BuildElementAndNodeSets
#*     labels,position,pos1,pos2 = GetCrackFrontNodes(allNodes,nodeLabelTip,2)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 21, 
#* in GetCrackFrontNodes
#*     CFnSet,ind=np.unique(np.array(CFnSet), return_index=True)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#* NameError: global name 'os' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 79, in <module>
#*     Ensure_ODB_Is_Closed(copyodbPath,session)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\Utilities.py", line 
#* 13, in Ensure_ODB_Is_Closed
#*     path=os.path.normpath(session.odbs[key].path)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#* NameError: global name 'GetElementConnectivities' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 109, in <module>
#*     
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* root,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 89, 
#* in BuildElementAndNodeSets
#*     elemConn, elemNbr = GetElementConnectivities(elements)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: IntV-contour-1-slice-0
#: IntV-contour-1-slice-1
#: IntV-contour-1-slice-2
#: IntV-contour-1-slice-3
#: IntV-contour-1-slice-4
#: IntV-contour-1-slice-5
#: IntV-contour-1-slice-6
#: IntV-contour-1-slice-7
#: IntV-contour-1-slice-8
#: IntV-contour-1-slice-9
#: IntV-contour-1-slice-10
#: IntV-contour-1-slice-11
#: IntV-contour-1-slice-12
#: IntV-contour-1-slice-13
#: IntV-contour-1-slice-14
#: IntV-contour-1-slice-15
#: IntV-contour-1-slice-16
#: IntV-contour-1-slice-17
#: IntV-contour-1-slice-18
#: IntV-contour-1-slice-19
#: IntV-contour-1-slice-20
#: IntV-contour-1-slice-21
#: IntV-contour-1-slice-22
#: IntV-contour-1-slice-23
#: IntV-contour-1-slice-24
#: IntV-contour-1-slice-25
#: IntV-contour-1-slice-26
#: IntV-contour-1-slice-27
#: IntV-contour-1-slice-28
#: IntV-contour-1-slice-29
#: IntV-contour-1-slice-30
#: IntV-contour-1-slice-31
#: IntV-contour-1-slice-32
#: IntV-contour-1-slice-33
#: IntV-contour-1-slice-34
#: IntV-contour-1-slice-35
#: IntV-contour-1-slice-36
#: IntV-contour-1-slice-37
#: IntV-contour-1-slice-38
#: IntV-contour-1-slice-39
#: IntV-contour-1-slice-40
#: IntV-contour-1-slice-41
#: IntV-contour-1-slice-42
#: IntV-contour-1-slice-43
#: IntV-contour-1-slice-44
#: IntV-contour-1-slice-45
#: IntV-contour-1-slice-46
#: IntV-contour-1-slice-47
#: IntV-contour-1-slice-48
#: IntV-contour-1-slice-49
#: IntV-contour-1-slice-50
#: IntV-contour-1-slice-51
#: IntV-contour-1-slice-52
#: IntV-contour-1-slice-53
#: IntV-contour-1-slice-54
#: IntV-contour-1-slice-55
#: IntV-contour-1-slice-56
#: IntV-contour-1-slice-57
#: IntV-contour-1-slice-58
#: IntV-contour-1-slice-59
#: IntV-contour-1-slice-60
#: IntV-contour-1-slice-61
#: IntV-contour-1-slice-62
#: IntV-contour-1-slice-63
#: IntV-contour-1-slice-64
#: IntV-contour-1-slice-65
#: IntV-contour-1-slice-66
#: IntV-contour-1-slice-67
#: IntV-contour-1-slice-68
#: IntV-contour-1-slice-69
#: IntV-contour-1-slice-70
#: IntV-contour-1-slice-71
#: IntV-contour-1-slice-72
#: IntV-contour-1-slice-73
#: IntV-contour-1-slice-74
#: IntV-contour-1-slice-75
#: IntV-contour-2-slice-0
#: IntV-contour-2-slice-1
#: IntV-contour-2-slice-2
#: IntV-contour-2-slice-3
#: IntV-contour-2-slice-4
#: IntV-contour-2-slice-5
#: IntV-contour-2-slice-6
#: IntV-contour-2-slice-7
#: IntV-contour-2-slice-8
#: IntV-contour-2-slice-9
#: IntV-contour-2-slice-10
#: IntV-contour-2-slice-11
#: IntV-contour-2-slice-12
#: IntV-contour-2-slice-13
#: IntV-contour-2-slice-14
#: IntV-contour-2-slice-15
#: IntV-contour-2-slice-16
#: IntV-contour-2-slice-17
#: IntV-contour-2-slice-18
#: IntV-contour-2-slice-19
#: IntV-contour-2-slice-20
#: IntV-contour-2-slice-21
#: IntV-contour-2-slice-22
#: IntV-contour-2-slice-23
#: IntV-contour-2-slice-24
#: IntV-contour-2-slice-25
#: IntV-contour-2-slice-26
#: IntV-contour-2-slice-27
#: IntV-contour-2-slice-28
#: IntV-contour-2-slice-29
#: IntV-contour-2-slice-30
#: IntV-contour-2-slice-31
#: IntV-contour-2-slice-32
#: IntV-contour-2-slice-33
#: IntV-contour-2-slice-34
#: IntV-contour-2-slice-35
#: IntV-contour-2-slice-36
#: IntV-contour-2-slice-37
#: IntV-contour-2-slice-38
#: IntV-contour-2-slice-39
#: IntV-contour-2-slice-40
#: IntV-contour-2-slice-41
#: IntV-contour-2-slice-42
#: IntV-contour-2-slice-43
#: IntV-contour-2-slice-44
#: IntV-contour-2-slice-45
#: IntV-contour-2-slice-46
#: IntV-contour-2-slice-47
#: IntV-contour-2-slice-48
#: IntV-contour-2-slice-49
#: IntV-contour-2-slice-50
#: IntV-contour-2-slice-51
#: IntV-contour-2-slice-52
#: IntV-contour-2-slice-53
#: IntV-contour-2-slice-54
#: IntV-contour-2-slice-55
#: IntV-contour-2-slice-56
#: IntV-contour-2-slice-57
#: IntV-contour-2-slice-58
#: IntV-contour-2-slice-59
#: IntV-contour-2-slice-60
#: IntV-contour-2-slice-61
#: IntV-contour-2-slice-62
#: IntV-contour-2-slice-63
#: IntV-contour-2-slice-64
#: IntV-contour-2-slice-65
#: IntV-contour-2-slice-66
#: IntV-contour-2-slice-67
#: IntV-contour-2-slice-68
#: IntV-contour-2-slice-69
#: IntV-contour-2-slice-70
#: IntV-contour-2-slice-71
#: IntV-contour-2-slice-72
#: IntV-contour-2-slice-73
#: IntV-contour-2-slice-74
#: IntV-contour-2-slice-75
#* NameError: global name 'isclose' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 109, in <module>
#*     
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* root,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 204, 
#* in BuildElementAndNodeSets
#*     if 
#* isclose(allNodes[n-1].coordinates[pos1],
#* allNodes[nodeLabelTip-1].coordinates[pos1]) and \
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: IntV-contour-1-slice-0
#: IntV-contour-1-slice-1
#: IntV-contour-1-slice-2
#: IntV-contour-1-slice-3
#: IntV-contour-1-slice-4
#: IntV-contour-1-slice-5
#: IntV-contour-1-slice-6
#: IntV-contour-1-slice-7
#: IntV-contour-1-slice-8
#: IntV-contour-1-slice-9
#: IntV-contour-1-slice-10
#: IntV-contour-1-slice-11
#: IntV-contour-1-slice-12
#: IntV-contour-1-slice-13
#: IntV-contour-1-slice-14
#: IntV-contour-1-slice-15
#: IntV-contour-1-slice-16
#: IntV-contour-1-slice-17
#: IntV-contour-1-slice-18
#: IntV-contour-1-slice-19
#: IntV-contour-1-slice-20
#: IntV-contour-1-slice-21
#: IntV-contour-1-slice-22
#: IntV-contour-1-slice-23
#: IntV-contour-1-slice-24
#: IntV-contour-1-slice-25
#: IntV-contour-1-slice-26
#: IntV-contour-1-slice-27
#: IntV-contour-1-slice-28
#: IntV-contour-1-slice-29
#: IntV-contour-1-slice-30
#: IntV-contour-1-slice-31
#: IntV-contour-1-slice-32
#: IntV-contour-1-slice-33
#: IntV-contour-1-slice-34
#: IntV-contour-1-slice-35
#: IntV-contour-1-slice-36
#: IntV-contour-1-slice-37
#: IntV-contour-1-slice-38
#: IntV-contour-1-slice-39
#: IntV-contour-1-slice-40
#: IntV-contour-1-slice-41
#: IntV-contour-1-slice-42
#: IntV-contour-1-slice-43
#: IntV-contour-1-slice-44
#: IntV-contour-1-slice-45
#: IntV-contour-1-slice-46
#: IntV-contour-1-slice-47
#: IntV-contour-1-slice-48
#: IntV-contour-1-slice-49
#: IntV-contour-1-slice-50
#: IntV-contour-1-slice-51
#: IntV-contour-1-slice-52
#: IntV-contour-1-slice-53
#: IntV-contour-1-slice-54
#: IntV-contour-1-slice-55
#: IntV-contour-1-slice-56
#: IntV-contour-1-slice-57
#: IntV-contour-1-slice-58
#: IntV-contour-1-slice-59
#: IntV-contour-1-slice-60
#: IntV-contour-1-slice-61
#: IntV-contour-1-slice-62
#: IntV-contour-1-slice-63
#: IntV-contour-1-slice-64
#: IntV-contour-1-slice-65
#: IntV-contour-1-slice-66
#: IntV-contour-1-slice-67
#: IntV-contour-1-slice-68
#: IntV-contour-1-slice-69
#: IntV-contour-1-slice-70
#: IntV-contour-1-slice-71
#: IntV-contour-1-slice-72
#: IntV-contour-1-slice-73
#: IntV-contour-1-slice-74
#: IntV-contour-1-slice-75
#: IntV-contour-2-slice-0
#: IntV-contour-2-slice-1
#: IntV-contour-2-slice-2
#: IntV-contour-2-slice-3
#: IntV-contour-2-slice-4
#: IntV-contour-2-slice-5
#: IntV-contour-2-slice-6
#: IntV-contour-2-slice-7
#: IntV-contour-2-slice-8
#: IntV-contour-2-slice-9
#: IntV-contour-2-slice-10
#: IntV-contour-2-slice-11
#: IntV-contour-2-slice-12
#: IntV-contour-2-slice-13
#: IntV-contour-2-slice-14
#: IntV-contour-2-slice-15
#: IntV-contour-2-slice-16
#: IntV-contour-2-slice-17
#: IntV-contour-2-slice-18
#: IntV-contour-2-slice-19
#: IntV-contour-2-slice-20
#: IntV-contour-2-slice-21
#: IntV-contour-2-slice-22
#: IntV-contour-2-slice-23
#: IntV-contour-2-slice-24
#: IntV-contour-2-slice-25
#: IntV-contour-2-slice-26
#: IntV-contour-2-slice-27
#: IntV-contour-2-slice-28
#: IntV-contour-2-slice-29
#: IntV-contour-2-slice-30
#: IntV-contour-2-slice-31
#: IntV-contour-2-slice-32
#: IntV-contour-2-slice-33
#: IntV-contour-2-slice-34
#: IntV-contour-2-slice-35
#: IntV-contour-2-slice-36
#: IntV-contour-2-slice-37
#: IntV-contour-2-slice-38
#: IntV-contour-2-slice-39
#: IntV-contour-2-slice-40
#: IntV-contour-2-slice-41
#: IntV-contour-2-slice-42
#: IntV-contour-2-slice-43
#: IntV-contour-2-slice-44
#: IntV-contour-2-slice-45
#: IntV-contour-2-slice-46
#: IntV-contour-2-slice-47
#: IntV-contour-2-slice-48
#: IntV-contour-2-slice-49
#: IntV-contour-2-slice-50
#: IntV-contour-2-slice-51
#: IntV-contour-2-slice-52
#: IntV-contour-2-slice-53
#: IntV-contour-2-slice-54
#: IntV-contour-2-slice-55
#: IntV-contour-2-slice-56
#: IntV-contour-2-slice-57
#: IntV-contour-2-slice-58
#: IntV-contour-2-slice-59
#: IntV-contour-2-slice-60
#: IntV-contour-2-slice-61
#: IntV-contour-2-slice-62
#: IntV-contour-2-slice-63
#: IntV-contour-2-slice-64
#: IntV-contour-2-slice-65
#: IntV-contour-2-slice-66
#: IntV-contour-2-slice-67
#: IntV-contour-2-slice-68
#: IntV-contour-2-slice-69
#: IntV-contour-2-slice-70
#: IntV-contour-2-slice-71
#: IntV-contour-2-slice-72
#: IntV-contour-2-slice-73
#: IntV-contour-2-slice-74
#: IntV-contour-2-slice-75
#* NameError: global name 'odb' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 109, in <module>
#*     
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* root,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 257, 
#* in BuildElementAndNodeSets
#*     odb.save()
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#* NameError: global name 'odb' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* odb,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 72, 
#* in BuildElementAndNodeSets
#*     root=odb.rootAssembly
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: test2-contour-1-slice-0
#: test2-contour-1-slice-1
#: test2-contour-1-slice-2
#: test2-contour-1-slice-3
#: test2-contour-1-slice-4
#: test2-contour-1-slice-5
#: test2-contour-1-slice-6
#: test2-contour-1-slice-7
#: test2-contour-1-slice-8
#: test2-contour-1-slice-9
#: test2-contour-1-slice-10
#: test2-contour-1-slice-11
#: test2-contour-1-slice-12
#: test2-contour-1-slice-13
#: test2-contour-1-slice-14
#: test2-contour-1-slice-15
#: test2-contour-1-slice-16
#: test2-contour-1-slice-17
#: test2-contour-1-slice-18
#: test2-contour-1-slice-19
#: test2-contour-1-slice-20
#: test2-contour-1-slice-21
#: test2-contour-1-slice-22
#: test2-contour-1-slice-23
#: test2-contour-1-slice-24
#: test2-contour-1-slice-25
#: test2-contour-1-slice-26
#: test2-contour-1-slice-27
#: test2-contour-1-slice-28
#: test2-contour-1-slice-29
#: test2-contour-1-slice-30
#: test2-contour-1-slice-31
#: test2-contour-1-slice-32
#: test2-contour-1-slice-33
#: test2-contour-1-slice-34
#: test2-contour-1-slice-35
#: test2-contour-1-slice-36
#: test2-contour-1-slice-37
#: test2-contour-1-slice-38
#: test2-contour-1-slice-39
#: test2-contour-1-slice-40
#: test2-contour-1-slice-41
#: test2-contour-1-slice-42
#: test2-contour-1-slice-43
#: test2-contour-1-slice-44
#: test2-contour-1-slice-45
#: test2-contour-1-slice-46
#: test2-contour-1-slice-47
#: test2-contour-1-slice-48
#: test2-contour-1-slice-49
#: test2-contour-1-slice-50
#: test2-contour-1-slice-51
#: test2-contour-1-slice-52
#: test2-contour-1-slice-53
#: test2-contour-1-slice-54
#: test2-contour-1-slice-55
#: test2-contour-1-slice-56
#: test2-contour-1-slice-57
#: test2-contour-1-slice-58
#: test2-contour-1-slice-59
#: test2-contour-1-slice-60
#: test2-contour-1-slice-61
#: test2-contour-1-slice-62
#: test2-contour-1-slice-63
#: test2-contour-1-slice-64
#: test2-contour-1-slice-65
#: test2-contour-1-slice-66
#: test2-contour-1-slice-67
#: test2-contour-1-slice-68
#: test2-contour-1-slice-69
#: test2-contour-1-slice-70
#: test2-contour-1-slice-71
#: test2-contour-1-slice-72
#: test2-contour-1-slice-73
#: test2-contour-1-slice-74
#: test2-contour-1-slice-75
#: test2-contour-2-slice-0
#: test2-contour-2-slice-1
#: test2-contour-2-slice-2
#: test2-contour-2-slice-3
#: test2-contour-2-slice-4
#: test2-contour-2-slice-5
#: test2-contour-2-slice-6
#: test2-contour-2-slice-7
#: test2-contour-2-slice-8
#: test2-contour-2-slice-9
#: test2-contour-2-slice-10
#: test2-contour-2-slice-11
#: test2-contour-2-slice-12
#: test2-contour-2-slice-13
#: test2-contour-2-slice-14
#: test2-contour-2-slice-15
#: test2-contour-2-slice-16
#: test2-contour-2-slice-17
#: test2-contour-2-slice-18
#: test2-contour-2-slice-19
#: test2-contour-2-slice-20
#: test2-contour-2-slice-21
#: test2-contour-2-slice-22
#: test2-contour-2-slice-23
#: test2-contour-2-slice-24
#: test2-contour-2-slice-25
#: test2-contour-2-slice-26
#: test2-contour-2-slice-27
#: test2-contour-2-slice-28
#: test2-contour-2-slice-29
#: test2-contour-2-slice-30
#: test2-contour-2-slice-31
#: test2-contour-2-slice-32
#: test2-contour-2-slice-33
#: test2-contour-2-slice-34
#: test2-contour-2-slice-35
#: test2-contour-2-slice-36
#: test2-contour-2-slice-37
#: test2-contour-2-slice-38
#: test2-contour-2-slice-39
#: test2-contour-2-slice-40
#: test2-contour-2-slice-41
#: test2-contour-2-slice-42
#: test2-contour-2-slice-43
#: test2-contour-2-slice-44
#: test2-contour-2-slice-45
#: test2-contour-2-slice-46
#: test2-contour-2-slice-47
#: test2-contour-2-slice-48
#: test2-contour-2-slice-49
#: test2-contour-2-slice-50
#: test2-contour-2-slice-51
#: test2-contour-2-slice-52
#: test2-contour-2-slice-53
#: test2-contour-2-slice-54
#: test2-contour-2-slice-55
#: test2-contour-2-slice-56
#: test2-contour-2-slice-57
#: test2-contour-2-slice-58
#: test2-contour-2-slice-59
#: test2-contour-2-slice-60
#: test2-contour-2-slice-61
#: test2-contour-2-slice-62
#: test2-contour-2-slice-63
#: test2-contour-2-slice-64
#: test2-contour-2-slice-65
#: test2-contour-2-slice-66
#: test2-contour-2-slice-67
#: test2-contour-2-slice-68
#: test2-contour-2-slice-69
#: test2-contour-2-slice-70
#: test2-contour-2-slice-71
#: test2-contour-2-slice-72
#: test2-contour-2-slice-73
#: test2-contour-2-slice-74
#: test2-contour-2-slice-75
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.3842, 
    farPlane=35.0801, width=15.4271, height=7.18835, cameraPosition=(26.1552, 
    9.96175, 19.1059), cameraUpVector=(-0.487203, 0.799467, -0.351405), 
    cameraTarget=(6.51655, 1.66634, 0.817117))
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: test2-contour-1-slice-0
#: test2-contour-1-slice-1
#: test2-contour-1-slice-2
#: test2-contour-1-slice-3
#: test2-contour-1-slice-4
#: test2-contour-1-slice-5
#: test2-contour-1-slice-6
#: test2-contour-1-slice-7
#: test2-contour-1-slice-8
#: test2-contour-1-slice-9
#: test2-contour-1-slice-10
#: test2-contour-1-slice-11
#: test2-contour-1-slice-12
#: test2-contour-1-slice-13
#: test2-contour-1-slice-14
#: test2-contour-1-slice-15
#: test2-contour-1-slice-16
#: test2-contour-1-slice-17
#: test2-contour-1-slice-18
#: test2-contour-1-slice-19
#: test2-contour-1-slice-20
#: test2-contour-1-slice-21
#: test2-contour-1-slice-22
#: test2-contour-1-slice-23
#: test2-contour-1-slice-24
#: test2-contour-1-slice-25
#: test2-contour-1-slice-26
#: test2-contour-1-slice-27
#: test2-contour-1-slice-28
#: test2-contour-1-slice-29
#: test2-contour-1-slice-30
#: test2-contour-1-slice-31
#: test2-contour-1-slice-32
#: test2-contour-1-slice-33
#: test2-contour-1-slice-34
#: test2-contour-1-slice-35
#: test2-contour-1-slice-36
#: test2-contour-1-slice-37
#: test2-contour-1-slice-38
#: test2-contour-1-slice-39
#: test2-contour-1-slice-40
#: test2-contour-1-slice-41
#: test2-contour-1-slice-42
#: test2-contour-1-slice-43
#: test2-contour-1-slice-44
#: test2-contour-1-slice-45
#: test2-contour-1-slice-46
#: test2-contour-1-slice-47
#: test2-contour-1-slice-48
#: test2-contour-1-slice-49
#: test2-contour-1-slice-50
#: test2-contour-1-slice-51
#: test2-contour-1-slice-52
#: test2-contour-1-slice-53
#: test2-contour-1-slice-54
#: test2-contour-1-slice-55
#: test2-contour-1-slice-56
#: test2-contour-1-slice-57
#: test2-contour-1-slice-58
#: test2-contour-1-slice-59
#: test2-contour-1-slice-60
#: test2-contour-1-slice-61
#: test2-contour-1-slice-62
#: test2-contour-1-slice-63
#: test2-contour-1-slice-64
#: test2-contour-1-slice-65
#: test2-contour-1-slice-66
#: test2-contour-1-slice-67
#: test2-contour-1-slice-68
#: test2-contour-1-slice-69
#: test2-contour-1-slice-70
#: test2-contour-1-slice-71
#: test2-contour-1-slice-72
#: test2-contour-1-slice-73
#: test2-contour-1-slice-74
#: test2-contour-1-slice-75
#: test2-contour-2-slice-0
#: test2-contour-2-slice-1
#: test2-contour-2-slice-2
#: test2-contour-2-slice-3
#: test2-contour-2-slice-4
#: test2-contour-2-slice-5
#: test2-contour-2-slice-6
#: test2-contour-2-slice-7
#: test2-contour-2-slice-8
#: test2-contour-2-slice-9
#: test2-contour-2-slice-10
#: test2-contour-2-slice-11
#: test2-contour-2-slice-12
#: test2-contour-2-slice-13
#: test2-contour-2-slice-14
#: test2-contour-2-slice-15
#: test2-contour-2-slice-16
#: test2-contour-2-slice-17
#: test2-contour-2-slice-18
#: test2-contour-2-slice-19
#: test2-contour-2-slice-20
#: test2-contour-2-slice-21
#: test2-contour-2-slice-22
#: test2-contour-2-slice-23
#: test2-contour-2-slice-24
#: test2-contour-2-slice-25
#: test2-contour-2-slice-26
#: test2-contour-2-slice-27
#: test2-contour-2-slice-28
#: test2-contour-2-slice-29
#: test2-contour-2-slice-30
#: test2-contour-2-slice-31
#: test2-contour-2-slice-32
#: test2-contour-2-slice-33
#: test2-contour-2-slice-34
#: test2-contour-2-slice-35
#: test2-contour-2-slice-36
#: test2-contour-2-slice-37
#: test2-contour-2-slice-38
#: test2-contour-2-slice-39
#: test2-contour-2-slice-40
#: test2-contour-2-slice-41
#: test2-contour-2-slice-42
#: test2-contour-2-slice-43
#: test2-contour-2-slice-44
#: test2-contour-2-slice-45
#: test2-contour-2-slice-46
#: test2-contour-2-slice-47
#: test2-contour-2-slice-48
#: test2-contour-2-slice-49
#: test2-contour-2-slice-50
#: test2-contour-2-slice-51
#: test2-contour-2-slice-52
#: test2-contour-2-slice-53
#: test2-contour-2-slice-54
#: test2-contour-2-slice-55
#: test2-contour-2-slice-56
#: test2-contour-2-slice-57
#: test2-contour-2-slice-58
#: test2-contour-2-slice-59
#: test2-contour-2-slice-60
#: test2-contour-2-slice-61
#: test2-contour-2-slice-62
#: test2-contour-2-slice-63
#: test2-contour-2-slice-64
#: test2-contour-2-slice-65
#: test2-contour-2-slice-66
#: test2-contour-2-slice-67
#: test2-contour-2-slice-68
#: test2-contour-2-slice-69
#: test2-contour-2-slice-70
#: test2-contour-2-slice-71
#: test2-contour-2-slice-72
#: test2-contour-2-slice-73
#: test2-contour-2-slice-74
#: test2-contour-2-slice-75
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=23.7582, 
    farPlane=32.2502, width=9.17611, height=24.3662, cameraPosition=(12.7187, 
    3.38643, 28.1584), cameraUpVector=(-0.424011, 0.854519, -0.300021), 
    cameraTarget=(6.51654, 1.66634, 0.817118))
#: 
#: Node: PLATE-1.26
#:                                         1             2             3        Magnitude
#: Base coordinates:                  6.00000e+00,  5.00000e-01,  2.00000e+00,      -      
#: No deformed coordinates for current plot.
session.viewports['Viewport: 1'].view.setValues(nearPlane=25.532, 
    farPlane=30.4765, width=0.251974, height=0.669091, viewOffsetX=-1.09349, 
    viewOffsetY=-0.858058)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: test2-contour-1-slice-0
#: test2-contour-1-slice-1
#: test2-contour-1-slice-2
#: test2-contour-1-slice-3
#: test2-contour-1-slice-4
#: test2-contour-1-slice-5
#: test2-contour-1-slice-6
#: test2-contour-1-slice-7
#: test2-contour-1-slice-8
#: test2-contour-1-slice-9
#: test2-contour-1-slice-10
#: test2-contour-1-slice-11
#: test2-contour-1-slice-12
#: test2-contour-1-slice-13
#: test2-contour-1-slice-14
#: test2-contour-1-slice-15
#: test2-contour-1-slice-16
#: test2-contour-1-slice-17
#: test2-contour-1-slice-18
#: test2-contour-1-slice-19
#: test2-contour-1-slice-20
#: test2-contour-2-slice-0
#: test2-contour-2-slice-1
#: test2-contour-2-slice-2
#: test2-contour-2-slice-3
#: test2-contour-2-slice-4
#: test2-contour-2-slice-5
#: test2-contour-2-slice-6
#: test2-contour-2-slice-7
#: test2-contour-2-slice-8
#: test2-contour-2-slice-9
#: test2-contour-2-slice-10
#: test2-contour-2-slice-11
#: test2-contour-2-slice-12
#: test2-contour-2-slice-13
#: test2-contour-2-slice-14
#: test2-contour-2-slice-15
#: test2-contour-2-slice-16
#: test2-contour-2-slice-17
#: test2-contour-2-slice-18
#: test2-contour-2-slice-19
#: test2-contour-2-slice-20
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=22.8687, 
    farPlane=33.3085, width=0.102634, height=0.272535, viewOffsetX=-0.941425, 
    viewOffsetY=-0.987842)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: test2-contour-1-slice-0
#: test2-contour-1-slice-1
#: test2-contour-1-slice-2
#: test2-contour-1-slice-3
#: test2-contour-1-slice-4
#: test2-contour-1-slice-5
#: test2-contour-1-slice-6
#: test2-contour-1-slice-7
#: test2-contour-1-slice-8
#: test2-contour-1-slice-9
#: test2-contour-1-slice-10
#: test2-contour-1-slice-11
#: test2-contour-1-slice-12
#: test2-contour-1-slice-13
#: test2-contour-1-slice-14
#: test2-contour-1-slice-15
#: test2-contour-1-slice-16
#: test2-contour-1-slice-17
#: test2-contour-1-slice-18
#: test2-contour-1-slice-19
#: test2-contour-1-slice-20
#: test2-contour-2-slice-0
#: test2-contour-2-slice-1
#: test2-contour-2-slice-2
#: test2-contour-2-slice-3
#: test2-contour-2-slice-4
#: test2-contour-2-slice-5
#: test2-contour-2-slice-6
#: test2-contour-2-slice-7
#: test2-contour-2-slice-8
#: test2-contour-2-slice-9
#: test2-contour-2-slice-10
#: test2-contour-2-slice-11
#: test2-contour-2-slice-12
#: test2-contour-2-slice-13
#: test2-contour-2-slice-14
#: test2-contour-2-slice-15
#: test2-contour-2-slice-16
#: test2-contour-2-slice-17
#: test2-contour-2-slice-18
#: test2-contour-2-slice-19
#: test2-contour-2-slice-20
#: time report
#: ++++++++++++
#: time in first loop 1.57899999619
#: time in first loop 1.91199994087
#: time in first loop 0.0120000839233
#: ++++++++++++
#: ++++++++++++
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: test2-contour-1-slice-0
#: test2-contour-1-slice-1
#: test2-contour-1-slice-2
#: test2-contour-1-slice-3
#: test2-contour-1-slice-4
#: test2-contour-1-slice-5
#: test2-contour-1-slice-6
#: test2-contour-1-slice-7
#: test2-contour-1-slice-8
#: test2-contour-1-slice-9
#: test2-contour-1-slice-10
#: test2-contour-1-slice-11
#: test2-contour-1-slice-12
#: test2-contour-1-slice-13
#: test2-contour-1-slice-14
#: test2-contour-1-slice-15
#: test2-contour-1-slice-16
#: test2-contour-1-slice-17
#: test2-contour-1-slice-18
#: test2-contour-1-slice-19
#: test2-contour-1-slice-20
#: test2-contour-2-slice-0
#: test2-contour-2-slice-1
#: test2-contour-2-slice-2
#: test2-contour-2-slice-3
#: test2-contour-2-slice-4
#: test2-contour-2-slice-5
#: test2-contour-2-slice-6
#: test2-contour-2-slice-7
#: test2-contour-2-slice-8
#: test2-contour-2-slice-9
#: test2-contour-2-slice-10
#: test2-contour-2-slice-11
#: test2-contour-2-slice-12
#: test2-contour-2-slice-13
#: test2-contour-2-slice-14
#: test2-contour-2-slice-15
#: test2-contour-2-slice-16
#: test2-contour-2-slice-17
#: test2-contour-2-slice-18
#: test2-contour-2-slice-19
#: test2-contour-2-slice-20
#: time report
#: ++++++++++++
#: time in first loop 1.56900000572
#: time in first loop 1.82400012016
#: time in first loop 0.0119998455048
#: ++++++++++++
#: ++++++++++++
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: test2-contour-1-slice-0
#: test2-contour-1-slice-1
#: test2-contour-1-slice-2
#: test2-contour-1-slice-3
#: test2-contour-1-slice-4
#: test2-contour-1-slice-5
#: test2-contour-1-slice-6
#: test2-contour-1-slice-7
#: test2-contour-1-slice-8
#: test2-contour-1-slice-9
#: test2-contour-1-slice-10
#: test2-contour-1-slice-11
#: test2-contour-1-slice-12
#: test2-contour-1-slice-13
#: test2-contour-1-slice-14
#: test2-contour-1-slice-15
#: test2-contour-1-slice-16
#: test2-contour-1-slice-17
#: test2-contour-1-slice-18
#: test2-contour-1-slice-19
#: test2-contour-1-slice-20
#: test2-contour-2-slice-0
#: test2-contour-2-slice-1
#: test2-contour-2-slice-2
#: test2-contour-2-slice-3
#: test2-contour-2-slice-4
#: test2-contour-2-slice-5
#: test2-contour-2-slice-6
#: test2-contour-2-slice-7
#: test2-contour-2-slice-8
#: test2-contour-2-slice-9
#: test2-contour-2-slice-10
#: test2-contour-2-slice-11
#: test2-contour-2-slice-12
#: test2-contour-2-slice-13
#: test2-contour-2-slice-14
#: test2-contour-2-slice-15
#: test2-contour-2-slice-16
#: test2-contour-2-slice-17
#: test2-contour-2-slice-18
#: test2-contour-2-slice-19
#: test2-contour-2-slice-20
#: test2-contour-3-slice-0
#: test2-contour-3-slice-1
#: test2-contour-3-slice-2
#: test2-contour-3-slice-3
#: test2-contour-3-slice-4
#: test2-contour-3-slice-5
#: test2-contour-3-slice-6
#: test2-contour-3-slice-7
#: test2-contour-3-slice-8
#: test2-contour-3-slice-9
#: test2-contour-3-slice-10
#: test2-contour-3-slice-11
#: test2-contour-3-slice-12
#: test2-contour-3-slice-13
#: test2-contour-3-slice-14
#: test2-contour-3-slice-15
#: test2-contour-3-slice-16
#: test2-contour-3-slice-17
#: test2-contour-3-slice-18
#: test2-contour-3-slice-19
#: test2-contour-3-slice-20
#: test2-contour-4-slice-0
#: test2-contour-4-slice-1
#: test2-contour-4-slice-2
#: test2-contour-4-slice-3
#: test2-contour-4-slice-4
#: test2-contour-4-slice-5
#: test2-contour-4-slice-6
#: test2-contour-4-slice-7
#: test2-contour-4-slice-8
#: test2-contour-4-slice-9
#: test2-contour-4-slice-10
#: test2-contour-4-slice-11
#: test2-contour-4-slice-12
#: test2-contour-4-slice-13
#: test2-contour-4-slice-14
#: test2-contour-4-slice-15
#: test2-contour-4-slice-16
#: test2-contour-4-slice-17
#: test2-contour-4-slice-18
#: test2-contour-4-slice-19
#: test2-contour-4-slice-20
#: test2-contour-5-slice-0
#: test2-contour-5-slice-1
#: test2-contour-5-slice-2
#: test2-contour-5-slice-3
#: test2-contour-5-slice-4
#: test2-contour-5-slice-5
#: test2-contour-5-slice-6
#: test2-contour-5-slice-7
#: test2-contour-5-slice-8
#: test2-contour-5-slice-9
#: test2-contour-5-slice-10
#: test2-contour-5-slice-11
#: test2-contour-5-slice-12
#: test2-contour-5-slice-13
#: test2-contour-5-slice-14
#: test2-contour-5-slice-15
#: test2-contour-5-slice-16
#: test2-contour-5-slice-17
#: test2-contour-5-slice-18
#: test2-contour-5-slice-19
#: test2-contour-5-slice-20
#: test2-contour-6-slice-0
#: test2-contour-6-slice-1
#: test2-contour-6-slice-2
#: test2-contour-6-slice-3
#: test2-contour-6-slice-4
#: test2-contour-6-slice-5
#: test2-contour-6-slice-6
#: test2-contour-6-slice-7
#: test2-contour-6-slice-8
#: test2-contour-6-slice-9
#: test2-contour-6-slice-10
#: test2-contour-6-slice-11
#: test2-contour-6-slice-12
#: test2-contour-6-slice-13
#: test2-contour-6-slice-14
#: test2-contour-6-slice-15
#: test2-contour-6-slice-16
#: test2-contour-6-slice-17
#: test2-contour-6-slice-18
#: test2-contour-6-slice-19
#: test2-contour-6-slice-20
#: test2-contour-7-slice-0
#: test2-contour-7-slice-1
#: test2-contour-7-slice-2
#: test2-contour-7-slice-3
#: test2-contour-7-slice-4
#: test2-contour-7-slice-5
#: test2-contour-7-slice-6
#: test2-contour-7-slice-7
#: test2-contour-7-slice-8
#: test2-contour-7-slice-9
#: test2-contour-7-slice-10
#: test2-contour-7-slice-11
#: test2-contour-7-slice-12
#: test2-contour-7-slice-13
#: test2-contour-7-slice-14
#: test2-contour-7-slice-15
#: test2-contour-7-slice-16
#: test2-contour-7-slice-17
#: test2-contour-7-slice-18
#: test2-contour-7-slice-19
#: test2-contour-7-slice-20
#: test2-contour-8-slice-0
#: test2-contour-8-slice-1
#: test2-contour-8-slice-2
#: test2-contour-8-slice-3
#: test2-contour-8-slice-4
#: test2-contour-8-slice-5
#: test2-contour-8-slice-6
#: test2-contour-8-slice-7
#: test2-contour-8-slice-8
#: test2-contour-8-slice-9
#: test2-contour-8-slice-10
#: test2-contour-8-slice-11
#: test2-contour-8-slice-12
#: test2-contour-8-slice-13
#: test2-contour-8-slice-14
#: test2-contour-8-slice-15
#: test2-contour-8-slice-16
#: test2-contour-8-slice-17
#: test2-contour-8-slice-18
#: test2-contour-8-slice-19
#: test2-contour-8-slice-20
#: test2-contour-9-slice-0
#: test2-contour-9-slice-1
#: test2-contour-9-slice-2
#: test2-contour-9-slice-3
#: test2-contour-9-slice-4
#: test2-contour-9-slice-5
#: test2-contour-9-slice-6
#: test2-contour-9-slice-7
#: test2-contour-9-slice-8
#: test2-contour-9-slice-9
#: test2-contour-9-slice-10
#: test2-contour-9-slice-11
#: test2-contour-9-slice-12
#: test2-contour-9-slice-13
#: test2-contour-9-slice-14
#: test2-contour-9-slice-15
#: test2-contour-9-slice-16
#: test2-contour-9-slice-17
#: test2-contour-9-slice-18
#: test2-contour-9-slice-19
#: test2-contour-9-slice-20
#: test2-contour-10-slice-0
#: test2-contour-10-slice-1
#: test2-contour-10-slice-2
#: test2-contour-10-slice-3
#: test2-contour-10-slice-4
#: test2-contour-10-slice-5
#: test2-contour-10-slice-6
#: test2-contour-10-slice-7
#: test2-contour-10-slice-8
#: test2-contour-10-slice-9
#: test2-contour-10-slice-10
#: test2-contour-10-slice-11
#: test2-contour-10-slice-12
#: test2-contour-10-slice-13
#: test2-contour-10-slice-14
#: test2-contour-10-slice-15
#: test2-contour-10-slice-16
#: test2-contour-10-slice-17
#: test2-contour-10-slice-18
#: test2-contour-10-slice-19
#: test2-contour-10-slice-20
#: time report
#: ++++++++++++
#: time in first loop 54.0940001011
#: time in second loop 8.87399983406
#: time in third loop 0.0900001525879
#: ++++++++++++
#: ++++++++++++
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#* NameError: global name 't' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py", 
#* line 104, in <module>
#*     
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* odb,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 100, 
#* in BuildElementAndNodeSets
#*     t
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: test2-contour-1-slice-0
#: test2-contour-1-slice-1
#: test2-contour-1-slice-2
#: test2-contour-1-slice-3
#: test2-contour-1-slice-4
#: test2-contour-1-slice-5
#: test2-contour-1-slice-6
#: test2-contour-1-slice-7
#: test2-contour-1-slice-8
#: test2-contour-1-slice-9
#: test2-contour-1-slice-10
#: test2-contour-1-slice-11
#: test2-contour-1-slice-12
#: test2-contour-1-slice-13
#: test2-contour-1-slice-14
#: test2-contour-1-slice-15
#: test2-contour-1-slice-16
#: test2-contour-1-slice-17
#: test2-contour-1-slice-18
#: test2-contour-1-slice-19
#: test2-contour-1-slice-20
#: test2-contour-2-slice-0
#: test2-contour-2-slice-1
#: test2-contour-2-slice-2
#: test2-contour-2-slice-3
#: test2-contour-2-slice-4
#: test2-contour-2-slice-5
#: test2-contour-2-slice-6
#: test2-contour-2-slice-7
#: test2-contour-2-slice-8
#: test2-contour-2-slice-9
#: test2-contour-2-slice-10
#: test2-contour-2-slice-11
#: test2-contour-2-slice-12
#: test2-contour-2-slice-13
#: test2-contour-2-slice-14
#: test2-contour-2-slice-15
#: test2-contour-2-slice-16
#: test2-contour-2-slice-17
#: test2-contour-2-slice-18
#: test2-contour-2-slice-19
#: test2-contour-2-slice-20
#: test2-contour-3-slice-0
#: test2-contour-3-slice-1
#: test2-contour-3-slice-2
#: test2-contour-3-slice-3
#: test2-contour-3-slice-4
#: test2-contour-3-slice-5
#: test2-contour-3-slice-6
#: test2-contour-3-slice-7
#: test2-contour-3-slice-8
#: test2-contour-3-slice-9
#: test2-contour-3-slice-10
#: test2-contour-3-slice-11
#: test2-contour-3-slice-12
#: test2-contour-3-slice-13
#: test2-contour-3-slice-14
#: test2-contour-3-slice-15
#: test2-contour-3-slice-16
#: test2-contour-3-slice-17
#: test2-contour-3-slice-18
#: test2-contour-3-slice-19
#: test2-contour-3-slice-20
#: test2-contour-4-slice-0
#: test2-contour-4-slice-1
#: test2-contour-4-slice-2
#: test2-contour-4-slice-3
#: test2-contour-4-slice-4
#: test2-contour-4-slice-5
#: test2-contour-4-slice-6
#: test2-contour-4-slice-7
#: test2-contour-4-slice-8
#: test2-contour-4-slice-9
#: test2-contour-4-slice-10
#: test2-contour-4-slice-11
#: test2-contour-4-slice-12
#: test2-contour-4-slice-13
#: test2-contour-4-slice-14
#: test2-contour-4-slice-15
#: test2-contour-4-slice-16
#: test2-contour-4-slice-17
#: test2-contour-4-slice-18
#: test2-contour-4-slice-19
#: test2-contour-4-slice-20
#: test2-contour-5-slice-0
#: test2-contour-5-slice-1
#: test2-contour-5-slice-2
#: test2-contour-5-slice-3
#: test2-contour-5-slice-4
#: test2-contour-5-slice-5
#: test2-contour-5-slice-6
#: test2-contour-5-slice-7
#: test2-contour-5-slice-8
#: test2-contour-5-slice-9
#: test2-contour-5-slice-10
#: test2-contour-5-slice-11
#: test2-contour-5-slice-12
#: test2-contour-5-slice-13
#: test2-contour-5-slice-14
#: test2-contour-5-slice-15
#: test2-contour-5-slice-16
#: test2-contour-5-slice-17
#: test2-contour-5-slice-18
#: test2-contour-5-slice-19
#: test2-contour-5-slice-20
#: test2-contour-6-slice-0
#: test2-contour-6-slice-1
#: test2-contour-6-slice-2
#: test2-contour-6-slice-3
#: test2-contour-6-slice-4
#: test2-contour-6-slice-5
#: test2-contour-6-slice-6
#: test2-contour-6-slice-7
#: test2-contour-6-slice-8
#: test2-contour-6-slice-9
#: test2-contour-6-slice-10
#: test2-contour-6-slice-11
#: test2-contour-6-slice-12
#: test2-contour-6-slice-13
#: test2-contour-6-slice-14
#: test2-contour-6-slice-15
#: test2-contour-6-slice-16
#: test2-contour-6-slice-17
#: test2-contour-6-slice-18
#: test2-contour-6-slice-19
#: test2-contour-6-slice-20
#: test2-contour-7-slice-0
#: test2-contour-7-slice-1
#: test2-contour-7-slice-2
#: test2-contour-7-slice-3
#: test2-contour-7-slice-4
#: test2-contour-7-slice-5
#: test2-contour-7-slice-6
#: test2-contour-7-slice-7
#: test2-contour-7-slice-8
#: test2-contour-7-slice-9
#: test2-contour-7-slice-10
#: test2-contour-7-slice-11
#: test2-contour-7-slice-12
#: test2-contour-7-slice-13
#: test2-contour-7-slice-14
#: test2-contour-7-slice-15
#: test2-contour-7-slice-16
#: test2-contour-7-slice-17
#: test2-contour-7-slice-18
#: test2-contour-7-slice-19
#: test2-contour-7-slice-20
#: test2-contour-8-slice-0
#: test2-contour-8-slice-1
#: test2-contour-8-slice-2
#: test2-contour-8-slice-3
#: test2-contour-8-slice-4
#: test2-contour-8-slice-5
#: test2-contour-8-slice-6
#: test2-contour-8-slice-7
#: test2-contour-8-slice-8
#: test2-contour-8-slice-9
#: test2-contour-8-slice-10
#: test2-contour-8-slice-11
#: test2-contour-8-slice-12
#: test2-contour-8-slice-13
#: test2-contour-8-slice-14
#: test2-contour-8-slice-15
#: test2-contour-8-slice-16
#: test2-contour-8-slice-17
#: test2-contour-8-slice-18
#: test2-contour-8-slice-19
#: test2-contour-8-slice-20
#: test2-contour-9-slice-0
#: test2-contour-9-slice-1
#: test2-contour-9-slice-2
#: test2-contour-9-slice-3
#: test2-contour-9-slice-4
#: test2-contour-9-slice-5
#: test2-contour-9-slice-6
#: test2-contour-9-slice-7
#: test2-contour-9-slice-8
#: test2-contour-9-slice-9
#: test2-contour-9-slice-10
#: test2-contour-9-slice-11
#: test2-contour-9-slice-12
#: test2-contour-9-slice-13
#: test2-contour-9-slice-14
#: test2-contour-9-slice-15
#: test2-contour-9-slice-16
#: test2-contour-9-slice-17
#: test2-contour-9-slice-18
#: test2-contour-9-slice-19
#: test2-contour-9-slice-20
#: test2-contour-10-slice-0
#: test2-contour-10-slice-1
#: test2-contour-10-slice-2
#: test2-contour-10-slice-3
#: test2-contour-10-slice-4
#: test2-contour-10-slice-5
#: test2-contour-10-slice-6
#: test2-contour-10-slice-7
#: test2-contour-10-slice-8
#: test2-contour-10-slice-9
#: test2-contour-10-slice-10
#: test2-contour-10-slice-11
#: test2-contour-10-slice-12
#: test2-contour-10-slice-13
#: test2-contour-10-slice-14
#: test2-contour-10-slice-15
#: test2-contour-10-slice-16
#: test2-contour-10-slice-17
#: test2-contour-10-slice-18
#: test2-contour-10-slice-19
#: test2-contour-10-slice-20
#: time report
#: ++++++++++++
#: time in first loop 53.5920000076
#: time in first loop get El 53.4499988556
#: time in first loop get union 0.0930001735687
#: time in second loop 9.10899996758
#: time in third loop 0.0929999351501
#: ++++++++++++
#: ++++++++++++
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: test2-contour-1-slice-0
#: test2-contour-1-slice-1
#: test2-contour-1-slice-2
#: test2-contour-1-slice-3
#: test2-contour-1-slice-4
#: test2-contour-1-slice-5
#: test2-contour-1-slice-6
#: test2-contour-1-slice-7
#: test2-contour-1-slice-8
#: test2-contour-1-slice-9
#: test2-contour-1-slice-10
#: test2-contour-1-slice-11
#: test2-contour-1-slice-12
#: test2-contour-1-slice-13
#: test2-contour-1-slice-14
#: test2-contour-1-slice-15
#: test2-contour-1-slice-16
#: test2-contour-1-slice-17
#: test2-contour-1-slice-18
#: test2-contour-1-slice-19
#: test2-contour-1-slice-20
#: test2-contour-2-slice-0
#: test2-contour-2-slice-1
#: test2-contour-2-slice-2
#: test2-contour-2-slice-3
#: test2-contour-2-slice-4
#: test2-contour-2-slice-5
#: test2-contour-2-slice-6
#: test2-contour-2-slice-7
#: test2-contour-2-slice-8
#: test2-contour-2-slice-9
#: test2-contour-2-slice-10
#: test2-contour-2-slice-11
#: test2-contour-2-slice-12
#: test2-contour-2-slice-13
#: test2-contour-2-slice-14
#: test2-contour-2-slice-15
#: test2-contour-2-slice-16
#: test2-contour-2-slice-17
#: test2-contour-2-slice-18
#: test2-contour-2-slice-19
#: test2-contour-2-slice-20
#: test2-contour-3-slice-0
#: test2-contour-3-slice-1
#: test2-contour-3-slice-2
#: test2-contour-3-slice-3
#: test2-contour-3-slice-4
#: test2-contour-3-slice-5
#: test2-contour-3-slice-6
#: test2-contour-3-slice-7
#: test2-contour-3-slice-8
#: test2-contour-3-slice-9
#: test2-contour-3-slice-10
#: test2-contour-3-slice-11
#: test2-contour-3-slice-12
#: test2-contour-3-slice-13
#: test2-contour-3-slice-14
#: test2-contour-3-slice-15
#: test2-contour-3-slice-16
#: test2-contour-3-slice-17
#: test2-contour-3-slice-18
#: test2-contour-3-slice-19
#: test2-contour-3-slice-20
#: test2-contour-4-slice-0
#: test2-contour-4-slice-1
#: test2-contour-4-slice-2
#: test2-contour-4-slice-3
#: test2-contour-4-slice-4
#: test2-contour-4-slice-5
#: test2-contour-4-slice-6
#: test2-contour-4-slice-7
#: test2-contour-4-slice-8
#: test2-contour-4-slice-9
#: test2-contour-4-slice-10
#: test2-contour-4-slice-11
#: test2-contour-4-slice-12
#: test2-contour-4-slice-13
#: test2-contour-4-slice-14
#: test2-contour-4-slice-15
#: test2-contour-4-slice-16
#: test2-contour-4-slice-17
#: test2-contour-4-slice-18
#: test2-contour-4-slice-19
#: test2-contour-4-slice-20
#: test2-contour-5-slice-0
#: test2-contour-5-slice-1
#: test2-contour-5-slice-2
#: test2-contour-5-slice-3
#: test2-contour-5-slice-4
#: test2-contour-5-slice-5
#: test2-contour-5-slice-6
#: test2-contour-5-slice-7
#: test2-contour-5-slice-8
#: test2-contour-5-slice-9
#: test2-contour-5-slice-10
#: test2-contour-5-slice-11
#: test2-contour-5-slice-12
#: test2-contour-5-slice-13
#: test2-contour-5-slice-14
#: test2-contour-5-slice-15
#: test2-contour-5-slice-16
#: test2-contour-5-slice-17
#: test2-contour-5-slice-18
#: test2-contour-5-slice-19
#: test2-contour-5-slice-20
#: test2-contour-6-slice-0
#: test2-contour-6-slice-1
#: test2-contour-6-slice-2
#: test2-contour-6-slice-3
#: test2-contour-6-slice-4
#: test2-contour-6-slice-5
#: test2-contour-6-slice-6
#: test2-contour-6-slice-7
#: test2-contour-6-slice-8
#: test2-contour-6-slice-9
#: test2-contour-6-slice-10
#: test2-contour-6-slice-11
#: test2-contour-6-slice-12
#: test2-contour-6-slice-13
#: test2-contour-6-slice-14
#: test2-contour-6-slice-15
#: test2-contour-6-slice-16
#: test2-contour-6-slice-17
#: test2-contour-6-slice-18
#: test2-contour-6-slice-19
#: test2-contour-6-slice-20
#: test2-contour-7-slice-0
#: test2-contour-7-slice-1
#: test2-contour-7-slice-2
#: test2-contour-7-slice-3
#: test2-contour-7-slice-4
#: test2-contour-7-slice-5
#: test2-contour-7-slice-6
#: test2-contour-7-slice-7
#: test2-contour-7-slice-8
#: test2-contour-7-slice-9
#: test2-contour-7-slice-10
#: test2-contour-7-slice-11
#: test2-contour-7-slice-12
#: test2-contour-7-slice-13
#: test2-contour-7-slice-14
#: test2-contour-7-slice-15
#: test2-contour-7-slice-16
#: test2-contour-7-slice-17
#: test2-contour-7-slice-18
#: test2-contour-7-slice-19
#: test2-contour-7-slice-20
#: test2-contour-8-slice-0
#: test2-contour-8-slice-1
#: test2-contour-8-slice-2
#: test2-contour-8-slice-3
#: test2-contour-8-slice-4
#: test2-contour-8-slice-5
#: test2-contour-8-slice-6
#: test2-contour-8-slice-7
#: test2-contour-8-slice-8
#: test2-contour-8-slice-9
#: test2-contour-8-slice-10
#: test2-contour-8-slice-11
#: test2-contour-8-slice-12
#: test2-contour-8-slice-13
#: test2-contour-8-slice-14
#: test2-contour-8-slice-15
#: test2-contour-8-slice-16
#: test2-contour-8-slice-17
#: test2-contour-8-slice-18
#: test2-contour-8-slice-19
#: test2-contour-8-slice-20
#: test2-contour-9-slice-0
#: test2-contour-9-slice-1
#: test2-contour-9-slice-2
#: test2-contour-9-slice-3
#: test2-contour-9-slice-4
#: test2-contour-9-slice-5
#: test2-contour-9-slice-6
#: test2-contour-9-slice-7
#: test2-contour-9-slice-8
#: test2-contour-9-slice-9
#: test2-contour-9-slice-10
#: test2-contour-9-slice-11
#: test2-contour-9-slice-12
#: test2-contour-9-slice-13
#: test2-contour-9-slice-14
#: test2-contour-9-slice-15
#: test2-contour-9-slice-16
#: test2-contour-9-slice-17
#: test2-contour-9-slice-18
#: test2-contour-9-slice-19
#: test2-contour-9-slice-20
#: test2-contour-10-slice-0
#: test2-contour-10-slice-1
#: test2-contour-10-slice-2
#: test2-contour-10-slice-3
#: test2-contour-10-slice-4
#: test2-contour-10-slice-5
#: test2-contour-10-slice-6
#: test2-contour-10-slice-7
#: test2-contour-10-slice-8
#: test2-contour-10-slice-9
#: test2-contour-10-slice-10
#: test2-contour-10-slice-11
#: test2-contour-10-slice-12
#: test2-contour-10-slice-13
#: test2-contour-10-slice-14
#: test2-contour-10-slice-15
#: test2-contour-10-slice-16
#: test2-contour-10-slice-17
#: test2-contour-10-slice-18
#: test2-contour-10-slice-19
#: test2-contour-10-slice-20
#: time report
#: ++++++++++++
#: time in first loop 0.650000095367
#: time in first loop get El 0.31699848175
#: time in first loop get union 0.0900001525879
#: time in second loop 9.30900001526
#: time in third loop 0.0889999866486
#: ++++++++++++
#: ++++++++++++
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=22.8687, 
    farPlane=33.3085, width=0.102634, height=0.272535, viewOffsetX=-0.93122, 
    viewOffsetY=-0.98355)
session.viewports['Viewport: 1'].view.setValues(farPlane=33.3071, 
    viewOffsetX=-0.954655, viewOffsetY=-1.01061)
session.viewports['Viewport: 1'].view.setValues(nearPlane=22.858, 
    farPlane=33.3192, width=0.168293, height=0.446885, viewOffsetX=-0.950735, 
    viewOffsetY=-0.986831)
session.viewports['Viewport: 1'].view.setValues(nearPlane=23.1064, 
    farPlane=33.5366, width=0.170122, height=0.451742, cameraPosition=(23.5563, 
    14.8104, 19.176), cameraUpVector=(-0.457761, 0.676477, -0.576917), 
    cameraTarget=(6.7327, 1.68734, 0.907995), viewOffsetX=-0.961068, 
    viewOffsetY=-0.997556)
session.viewports['Viewport: 1'].view.setValues(nearPlane=22.1253, 
    farPlane=34.5177, width=4.96097, height=13.1734, viewOffsetX=-0.381774, 
    viewOffsetY=1.42873)
session.viewports['Viewport: 1'].view.setValues(nearPlane=20.5898, 
    farPlane=35.2925, width=4.61667, height=12.2591, cameraPosition=(33.4193, 
    -1.61958, -3.53326), cameraUpVector=(-0.182269, 0.766016, 0.616439), 
    cameraTarget=(5.67849, 2.09398, -1.16167), viewOffsetX=-0.355278, 
    viewOffsetY=1.32957)
session.viewports['Viewport: 1'].view.setValues(nearPlane=23.3488, 
    farPlane=34.3128, width=5.23529, height=13.9018, cameraPosition=(20.0011, 
    8.82244, -23.3109), cameraUpVector=(0.030382, 0.74779, 0.663239), 
    cameraTarget=(5.22919, 1.7138, -0.50245), viewOffsetX=-0.402884, 
    viewOffsetY=1.50773)
session.viewports['Viewport: 1'].view.setValues(nearPlane=24.1308, 
    farPlane=33.5308, width=1.10583, height=2.93642, viewOffsetX=-0.971569, 
    viewOffsetY=-0.0290987)
session.viewports['Viewport: 1'].view.setValues(nearPlane=24.1166, 
    farPlane=33.5449, width=1.10518, height=2.9347, cameraPosition=(19.9937, 
    8.79446, -23.3244), cameraUpVector=(0.00898988, 0.757746, 0.652488), 
    cameraTarget=(5.2218, 1.68582, -0.515958), viewOffsetX=-0.970999, 
    viewOffsetY=-0.0290817)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       9
#: Number of Node Sets:          830
#: Number of Steps:              1
#: test2-contour-1-slice-0
#: test2-contour-1-slice-1
#: test2-contour-1-slice-2
#: test2-contour-1-slice-3
#: test2-contour-1-slice-4
#: test2-contour-1-slice-5
#: test2-contour-1-slice-6
#: test2-contour-1-slice-7
#: test2-contour-1-slice-8
#: test2-contour-1-slice-9
#: test2-contour-1-slice-10
#: test2-contour-1-slice-11
#: test2-contour-1-slice-12
#: test2-contour-1-slice-13
#: test2-contour-1-slice-14
#: test2-contour-1-slice-15
#: test2-contour-1-slice-16
#: test2-contour-1-slice-17
#: test2-contour-1-slice-18
#: test2-contour-1-slice-19
#: test2-contour-1-slice-20
#: test2-contour-2-slice-0
#: test2-contour-2-slice-1
#: test2-contour-2-slice-2
#: test2-contour-2-slice-3
#: test2-contour-2-slice-4
#: test2-contour-2-slice-5
#: test2-contour-2-slice-6
#: test2-contour-2-slice-7
#: test2-contour-2-slice-8
#: test2-contour-2-slice-9
#: test2-contour-2-slice-10
#: test2-contour-2-slice-11
#: test2-contour-2-slice-12
#: test2-contour-2-slice-13
#: test2-contour-2-slice-14
#: test2-contour-2-slice-15
#: test2-contour-2-slice-16
#: test2-contour-2-slice-17
#: test2-contour-2-slice-18
#: test2-contour-2-slice-19
#: test2-contour-2-slice-20
#: test2-contour-3-slice-0
#: test2-contour-3-slice-1
#: test2-contour-3-slice-2
#: test2-contour-3-slice-3
#: test2-contour-3-slice-4
#: test2-contour-3-slice-5
#: test2-contour-3-slice-6
#: test2-contour-3-slice-7
#: test2-contour-3-slice-8
#: test2-contour-3-slice-9
#: test2-contour-3-slice-10
#: test2-contour-3-slice-11
#: test2-contour-3-slice-12
#: test2-contour-3-slice-13
#: test2-contour-3-slice-14
#: test2-contour-3-slice-15
#: test2-contour-3-slice-16
#: test2-contour-3-slice-17
#: test2-contour-3-slice-18
#: test2-contour-3-slice-19
#: test2-contour-3-slice-20
#: test2-contour-4-slice-0
#: test2-contour-4-slice-1
#: test2-contour-4-slice-2
#: test2-contour-4-slice-3
#: test2-contour-4-slice-4
#: test2-contour-4-slice-5
#: test2-contour-4-slice-6
#: test2-contour-4-slice-7
#: test2-contour-4-slice-8
#: test2-contour-4-slice-9
#: test2-contour-4-slice-10
#: test2-contour-4-slice-11
#: test2-contour-4-slice-12
#: test2-contour-4-slice-13
#: test2-contour-4-slice-14
#: test2-contour-4-slice-15
#: test2-contour-4-slice-16
#: test2-contour-4-slice-17
#: test2-contour-4-slice-18
#: test2-contour-4-slice-19
#: test2-contour-4-slice-20
#: test2-contour-5-slice-0
#: test2-contour-5-slice-1
#: test2-contour-5-slice-2
#: test2-contour-5-slice-3
#: test2-contour-5-slice-4
#: test2-contour-5-slice-5
#: test2-contour-5-slice-6
#: test2-contour-5-slice-7
#: test2-contour-5-slice-8
#: test2-contour-5-slice-9
#: test2-contour-5-slice-10
#: test2-contour-5-slice-11
#: test2-contour-5-slice-12
#: test2-contour-5-slice-13
#: test2-contour-5-slice-14
#: test2-contour-5-slice-15
#: test2-contour-5-slice-16
#: test2-contour-5-slice-17
#: test2-contour-5-slice-18
#: test2-contour-5-slice-19
#: test2-contour-5-slice-20
#: test2-contour-6-slice-0
#: test2-contour-6-slice-1
#: test2-contour-6-slice-2
#: test2-contour-6-slice-3
#: test2-contour-6-slice-4
#: test2-contour-6-slice-5
#: test2-contour-6-slice-6
#: test2-contour-6-slice-7
#: test2-contour-6-slice-8
#: test2-contour-6-slice-9
#: test2-contour-6-slice-10
#: test2-contour-6-slice-11
#: test2-contour-6-slice-12
#: test2-contour-6-slice-13
#: test2-contour-6-slice-14
#: test2-contour-6-slice-15
#: test2-contour-6-slice-16
#: test2-contour-6-slice-17
#: test2-contour-6-slice-18
#: test2-contour-6-slice-19
#: test2-contour-6-slice-20
#: test2-contour-7-slice-0
#: test2-contour-7-slice-1
#: test2-contour-7-slice-2
#: test2-contour-7-slice-3
#: test2-contour-7-slice-4
#: test2-contour-7-slice-5
#: test2-contour-7-slice-6
#: test2-contour-7-slice-7
#: test2-contour-7-slice-8
#: test2-contour-7-slice-9
#: test2-contour-7-slice-10
#: test2-contour-7-slice-11
#: test2-contour-7-slice-12
#: test2-contour-7-slice-13
#: test2-contour-7-slice-14
#: test2-contour-7-slice-15
#: test2-contour-7-slice-16
#: test2-contour-7-slice-17
#: test2-contour-7-slice-18
#: test2-contour-7-slice-19
#: test2-contour-7-slice-20
#: test2-contour-8-slice-0
#: test2-contour-8-slice-1
#: test2-contour-8-slice-2
#: test2-contour-8-slice-3
#: test2-contour-8-slice-4
#: test2-contour-8-slice-5
#: test2-contour-8-slice-6
#: test2-contour-8-slice-7
#: test2-contour-8-slice-8
#: test2-contour-8-slice-9
#: test2-contour-8-slice-10
#: test2-contour-8-slice-11
#: test2-contour-8-slice-12
#: test2-contour-8-slice-13
#: test2-contour-8-slice-14
#: test2-contour-8-slice-15
#: test2-contour-8-slice-16
#: test2-contour-8-slice-17
#: test2-contour-8-slice-18
#: test2-contour-8-slice-19
#: test2-contour-8-slice-20
#: test2-contour-9-slice-0
#: test2-contour-9-slice-1
#: test2-contour-9-slice-2
#: test2-contour-9-slice-3
#: test2-contour-9-slice-4
#: test2-contour-9-slice-5
#: test2-contour-9-slice-6
#: test2-contour-9-slice-7
#: test2-contour-9-slice-8
#: test2-contour-9-slice-9
#: test2-contour-9-slice-10
#: test2-contour-9-slice-11
#: test2-contour-9-slice-12
#: test2-contour-9-slice-13
#: test2-contour-9-slice-14
#: test2-contour-9-slice-15
#: test2-contour-9-slice-16
#: test2-contour-9-slice-17
#: test2-contour-9-slice-18
#: test2-contour-9-slice-19
#: test2-contour-9-slice-20
#: test2-contour-10-slice-0
#: test2-contour-10-slice-1
#: test2-contour-10-slice-2
#: test2-contour-10-slice-3
#: test2-contour-10-slice-4
#: test2-contour-10-slice-5
#: test2-contour-10-slice-6
#: test2-contour-10-slice-7
#: test2-contour-10-slice-8
#: test2-contour-10-slice-9
#: test2-contour-10-slice-10
#: test2-contour-10-slice-11
#: test2-contour-10-slice-12
#: test2-contour-10-slice-13
#: test2-contour-10-slice-14
#: test2-contour-10-slice-15
#: test2-contour-10-slice-16
#: test2-contour-10-slice-17
#: test2-contour-10-slice-18
#: test2-contour-10-slice-19
#: test2-contour-10-slice-20
#: test2-contour-11-slice-0
#: test2-contour-11-slice-1
#: test2-contour-11-slice-2
#: test2-contour-11-slice-3
#: test2-contour-11-slice-4
#: test2-contour-11-slice-5
#: test2-contour-11-slice-6
#: test2-contour-11-slice-7
#: test2-contour-11-slice-8
#: test2-contour-11-slice-9
#: test2-contour-11-slice-10
#: test2-contour-11-slice-11
#: test2-contour-11-slice-12
#: test2-contour-11-slice-13
#: test2-contour-11-slice-14
#: test2-contour-11-slice-15
#: test2-contour-11-slice-16
#: test2-contour-11-slice-17
#: test2-contour-11-slice-18
#: test2-contour-11-slice-19
#: test2-contour-11-slice-20
#: test2-contour-12-slice-0
#: test2-contour-12-slice-1
#: test2-contour-12-slice-2
#: test2-contour-12-slice-3
#: test2-contour-12-slice-4
#: test2-contour-12-slice-5
#: test2-contour-12-slice-6
#: test2-contour-12-slice-7
#: test2-contour-12-slice-8
#: test2-contour-12-slice-9
#: test2-contour-12-slice-10
#: test2-contour-12-slice-11
#: test2-contour-12-slice-12
#: test2-contour-12-slice-13
#: test2-contour-12-slice-14
#: test2-contour-12-slice-15
#: test2-contour-12-slice-16
#: test2-contour-12-slice-17
#: test2-contour-12-slice-18
#: test2-contour-12-slice-19
#: test2-contour-12-slice-20
#: test2-contour-13-slice-0
#: test2-contour-13-slice-1
#: test2-contour-13-slice-2
#: test2-contour-13-slice-3
#: test2-contour-13-slice-4
#: test2-contour-13-slice-5
#: test2-contour-13-slice-6
#: test2-contour-13-slice-7
#: test2-contour-13-slice-8
#: test2-contour-13-slice-9
#: test2-contour-13-slice-10
#: test2-contour-13-slice-11
#: test2-contour-13-slice-12
#: test2-contour-13-slice-13
#: test2-contour-13-slice-14
#: test2-contour-13-slice-15
#: test2-contour-13-slice-16
#: test2-contour-13-slice-17
#: test2-contour-13-slice-18
#: test2-contour-13-slice-19
#: test2-contour-13-slice-20
#: time report
#: ++++++++++++
#: time in first loop 1.03900003433
#: time in first loop get El 0.514001846313
#: time in first loop get union 0.148999452591
#: time in second loop 15.5550000668
#: time in third loop 0.138000011444
#: ++++++++++++
#: ++++++++++++
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=22.4102, 
    farPlane=33.767, width=2.0856, height=5.53809, viewOffsetX=-0.440392, 
    viewOffsetY=-1.13294)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.0007, 
    farPlane=30.649, width=2.51281, height=6.67252, cameraPosition=(8.26736, 
    3.50051, 29.7137), cameraUpVector=(-0.162463, 0.912252, -0.376034), 
    cameraTarget=(7.02803, 1.99301, 1.69295), viewOffsetX=-0.530602, 
    viewOffsetY=-1.36502)
session.viewports['Viewport: 1'].view.setValues(nearPlane=25.6868, 
    farPlane=31.9629, width=8.60952, height=22.8617, viewOffsetX=0.171932, 
    viewOffsetY=-0.274943)
session.viewports['Viewport: 1'].view.setValues(nearPlane=22.2416, 
    farPlane=36.8989, width=7.45477, height=19.7954, cameraPosition=(27.2728, 
    10.6949, 19.6222), cameraUpVector=(-0.444797, 0.797747, -0.40713), 
    cameraTarget=(7.55177, 2.19555, 1.51651), viewOffsetX=0.148871, 
    viewOffsetY=-0.238066)
session.viewports['Viewport: 1'].view.setValues(nearPlane=23.7613, 
    farPlane=35.3793, width=1.49827, height=3.97851, viewOffsetX=-0.720952, 
    viewOffsetY=-1.18969)
import os
os.chdir(r"E:\Dropbox\Research\Source\Abaqus-J-integral\Example 3")
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       133
#: Number of Node Sets:          768
#: Number of Steps:              1
#* KeyError: PLATE-1
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     odb = 
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* odb,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 75, 
#* in BuildElementAndNodeSets
#*     part=root.instances[partInstance]
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
#: 
#: Node: NOCHEDSPECIMEN-C-1.512
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24600e+01,  2.72977e+00,  2.78150e+00,      -      
#: No deformed coordinates for current plot.
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.223, 
    farPlane=64.4117, width=0.0188531, height=0.0500626, viewOffsetX=1.71858, 
    viewOffsetY=-3.44969)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       133
#: Number of Node Sets:          768
#: Number of Steps:              1
#: test2-contour-1-slice-0
#: test2-contour-1-slice-1
#: test2-contour-1-slice-2
#: test2-contour-1-slice-3
#: test2-contour-1-slice-4
#: test2-contour-1-slice-5
#: test2-contour-1-slice-6
#: test2-contour-1-slice-7
#: test2-contour-1-slice-8
#: test2-contour-1-slice-9
#: test2-contour-1-slice-10
#: test2-contour-1-slice-11
#: test2-contour-1-slice-12
#: test2-contour-1-slice-13
#: test2-contour-1-slice-14
#: test2-contour-1-slice-15
#: test2-contour-1-slice-16
#: test2-contour-1-slice-17
#: test2-contour-1-slice-18
#: test2-contour-1-slice-19
#: test2-contour-1-slice-20
#: test2-contour-1-slice-21
#: test2-contour-1-slice-22
#: test2-contour-1-slice-23
#: test2-contour-1-slice-24
#: test2-contour-1-slice-25
#: test2-contour-1-slice-26
#: test2-contour-1-slice-27
#: test2-contour-1-slice-28
#: test2-contour-1-slice-29
#: test2-contour-1-slice-30
#: test2-contour-1-slice-31
#: test2-contour-1-slice-32
#: test2-contour-1-slice-33
#: test2-contour-1-slice-34
#: test2-contour-1-slice-35
#: test2-contour-1-slice-36
#: test2-contour-1-slice-37
#: test2-contour-1-slice-38
#: test2-contour-1-slice-39
#: test2-contour-1-slice-40
#: test2-contour-1-slice-41
#: test2-contour-1-slice-42
#: test2-contour-1-slice-43
#: test2-contour-1-slice-44
#: test2-contour-1-slice-45
#: test2-contour-1-slice-46
#: test2-contour-1-slice-47
#: test2-contour-1-slice-48
#: test2-contour-1-slice-49
#: test2-contour-1-slice-50
#: test2-contour-1-slice-51
#: test2-contour-1-slice-52
#: test2-contour-1-slice-53
#: test2-contour-1-slice-54
#: test2-contour-1-slice-55
#: test2-contour-1-slice-56
#: test2-contour-1-slice-57
#: test2-contour-1-slice-58
#: test2-contour-1-slice-59
#: test2-contour-1-slice-60
#: test2-contour-1-slice-61
#: test2-contour-1-slice-62
#: test2-contour-1-slice-63
#: test2-contour-1-slice-64
#: test2-contour-1-slice-65
#: test2-contour-1-slice-66
#: test2-contour-1-slice-67
#: test2-contour-1-slice-68
#: test2-contour-1-slice-69
#: test2-contour-1-slice-70
#: test2-contour-1-slice-71
#: test2-contour-1-slice-72
#: test2-contour-1-slice-73
#: test2-contour-1-slice-74
#: test2-contour-1-slice-75
#: test2-contour-1-slice-76
#: test2-contour-1-slice-77
#: test2-contour-1-slice-78
#: test2-contour-1-slice-79
#: test2-contour-1-slice-80
#: test2-contour-1-slice-81
#: test2-contour-1-slice-82
#: test2-contour-1-slice-83
#: test2-contour-1-slice-84
#: test2-contour-1-slice-85
#: test2-contour-1-slice-86
#: test2-contour-1-slice-87
#: test2-contour-1-slice-88
#: test2-contour-1-slice-89
#: test2-contour-1-slice-90
#: test2-contour-1-slice-91
#: test2-contour-1-slice-92
#: test2-contour-1-slice-93
#: test2-contour-2-slice-0
#: test2-contour-2-slice-1
#: test2-contour-2-slice-2
#: test2-contour-2-slice-3
#: test2-contour-2-slice-4
#: test2-contour-2-slice-5
#: test2-contour-2-slice-6
#: test2-contour-2-slice-7
#: test2-contour-2-slice-8
#: test2-contour-2-slice-9
#: test2-contour-2-slice-10
#: test2-contour-2-slice-11
#: test2-contour-2-slice-12
#: test2-contour-2-slice-13
#: test2-contour-2-slice-14
#: test2-contour-2-slice-15
#: test2-contour-2-slice-16
#: test2-contour-2-slice-17
#: test2-contour-2-slice-18
#: test2-contour-2-slice-19
#: test2-contour-2-slice-20
#: test2-contour-2-slice-21
#: test2-contour-2-slice-22
#: test2-contour-2-slice-23
#: test2-contour-2-slice-24
#: test2-contour-2-slice-25
#: test2-contour-2-slice-26
#: test2-contour-2-slice-27
#: test2-contour-2-slice-28
#: test2-contour-2-slice-29
#: test2-contour-2-slice-30
#: test2-contour-2-slice-31
#: test2-contour-2-slice-32
#: test2-contour-2-slice-33
#: test2-contour-2-slice-34
#: test2-contour-2-slice-35
#: test2-contour-2-slice-36
#: test2-contour-2-slice-37
#: test2-contour-2-slice-38
#: test2-contour-2-slice-39
#: test2-contour-2-slice-40
#: test2-contour-2-slice-41
#: test2-contour-2-slice-42
#: test2-contour-2-slice-43
#: test2-contour-2-slice-44
#: test2-contour-2-slice-45
#: test2-contour-2-slice-46
#: test2-contour-2-slice-47
#: test2-contour-2-slice-48
#: test2-contour-2-slice-49
#: test2-contour-2-slice-50
#: test2-contour-2-slice-51
#: test2-contour-2-slice-52
#: test2-contour-2-slice-53
#: test2-contour-2-slice-54
#: test2-contour-2-slice-55
#: test2-contour-2-slice-56
#: test2-contour-2-slice-57
#: test2-contour-2-slice-58
#: test2-contour-2-slice-59
#: test2-contour-2-slice-60
#: test2-contour-2-slice-61
#: test2-contour-2-slice-62
#: test2-contour-2-slice-63
#: test2-contour-2-slice-64
#: test2-contour-2-slice-65
#: test2-contour-2-slice-66
#: test2-contour-2-slice-67
#: test2-contour-2-slice-68
#: test2-contour-2-slice-69
#: test2-contour-2-slice-70
#: test2-contour-2-slice-71
#: test2-contour-2-slice-72
#: test2-contour-2-slice-73
#: test2-contour-2-slice-74
#: test2-contour-2-slice-75
#: test2-contour-2-slice-76
#: test2-contour-2-slice-77
#: test2-contour-2-slice-78
#: test2-contour-2-slice-79
#: test2-contour-2-slice-80
#: test2-contour-2-slice-81
#: test2-contour-2-slice-82
#: test2-contour-2-slice-83
#: test2-contour-2-slice-84
#: test2-contour-2-slice-85
#: test2-contour-2-slice-86
#: test2-contour-2-slice-87
#: test2-contour-2-slice-88
#: test2-contour-2-slice-89
#: test2-contour-2-slice-90
#: test2-contour-2-slice-91
#: test2-contour-2-slice-92
#: test2-contour-2-slice-93
#: time report
#: ++++++++++++
#: time in first loop 0.266000032425
#: time in first loop get El 0.200999259949
#: time in first loop get union 0.0469999313354
#: time in second loop 1.88199996948
#: time in third loop 0.0469999313354
#: ++++++++++++
#: ++++++++++++
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.6295, 
    farPlane=65.0053, width=2.91961, height=7.75274, viewOffsetX=3.15868, 
    viewOffsetY=-1.83475)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.5925, 
    farPlane=65.0423, width=2.91689, height=7.7455, viewOffsetX=1.65058, 
    viewOffsetY=-3.66313)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.1579, 
    farPlane=64.4768, width=0.339277, height=0.900915, viewOffsetX=1.66362, 
    viewOffsetY=-3.4459)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.1535, 
    farPlane=64.4812, width=0.339239, height=0.900816, viewOffsetX=1.76968, 
    viewOffsetY=-3.40813)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.192, 
    farPlane=64.4427, width=0.172625, height=0.458387, viewOffsetX=1.74606, 
    viewOffsetY=-3.43652)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       133
#: Number of Node Sets:          768
#: Number of Steps:              1
#: test3-contour-1-slice-0
#: test3-contour-1-slice-1
#: test3-contour-1-slice-2
#: test3-contour-1-slice-3
#: test3-contour-1-slice-4
#: test3-contour-1-slice-5
#: test3-contour-1-slice-6
#: test3-contour-1-slice-7
#: test3-contour-1-slice-8
#: test3-contour-1-slice-9
#: test3-contour-1-slice-10
#: test3-contour-1-slice-11
#: test3-contour-1-slice-12
#: test3-contour-1-slice-13
#: test3-contour-1-slice-14
#: test3-contour-1-slice-15
#: test3-contour-1-slice-16
#: test3-contour-1-slice-17
#: test3-contour-1-slice-18
#: test3-contour-1-slice-19
#: test3-contour-1-slice-20
#: test3-contour-1-slice-21
#: test3-contour-1-slice-22
#: test3-contour-1-slice-23
#: test3-contour-1-slice-24
#: test3-contour-1-slice-25
#: test3-contour-1-slice-26
#: test3-contour-1-slice-27
#: test3-contour-1-slice-28
#: test3-contour-1-slice-29
#: test3-contour-1-slice-30
#: test3-contour-1-slice-31
#: test3-contour-1-slice-32
#: test3-contour-1-slice-33
#: test3-contour-1-slice-34
#: test3-contour-1-slice-35
#: test3-contour-1-slice-36
#: test3-contour-1-slice-37
#: test3-contour-1-slice-38
#: test3-contour-1-slice-39
#: test3-contour-1-slice-40
#: test3-contour-1-slice-41
#: test3-contour-1-slice-42
#: test3-contour-1-slice-43
#: test3-contour-1-slice-44
#: test3-contour-1-slice-45
#: test3-contour-1-slice-46
#: test3-contour-1-slice-47
#: test3-contour-1-slice-48
#: test3-contour-1-slice-49
#: test3-contour-1-slice-50
#: test3-contour-1-slice-51
#: test3-contour-1-slice-52
#: test3-contour-1-slice-53
#: test3-contour-1-slice-54
#: test3-contour-1-slice-55
#: test3-contour-1-slice-56
#: test3-contour-1-slice-57
#: test3-contour-1-slice-58
#: test3-contour-1-slice-59
#: test3-contour-1-slice-60
#: test3-contour-1-slice-61
#: test3-contour-1-slice-62
#: test3-contour-1-slice-63
#: test3-contour-1-slice-64
#: test3-contour-1-slice-65
#: test3-contour-1-slice-66
#: test3-contour-1-slice-67
#: test3-contour-1-slice-68
#: test3-contour-1-slice-69
#: test3-contour-1-slice-70
#: test3-contour-1-slice-71
#: test3-contour-1-slice-72
#: test3-contour-1-slice-73
#: test3-contour-1-slice-74
#: test3-contour-1-slice-75
#: test3-contour-1-slice-76
#: test3-contour-1-slice-77
#: test3-contour-1-slice-78
#: test3-contour-1-slice-79
#: test3-contour-1-slice-80
#: test3-contour-1-slice-81
#: test3-contour-1-slice-82
#: test3-contour-1-slice-83
#: test3-contour-1-slice-84
#: test3-contour-1-slice-85
#: test3-contour-1-slice-86
#: test3-contour-1-slice-87
#: test3-contour-1-slice-88
#: test3-contour-1-slice-89
#: test3-contour-1-slice-90
#: test3-contour-1-slice-91
#: test3-contour-1-slice-92
#: test3-contour-1-slice-93
#: test3-contour-2-slice-0
#: test3-contour-2-slice-1
#: test3-contour-2-slice-2
#: test3-contour-2-slice-3
#: test3-contour-2-slice-4
#: test3-contour-2-slice-5
#: test3-contour-2-slice-6
#: test3-contour-2-slice-7
#: test3-contour-2-slice-8
#: test3-contour-2-slice-9
#: test3-contour-2-slice-10
#: test3-contour-2-slice-11
#: test3-contour-2-slice-12
#: test3-contour-2-slice-13
#: test3-contour-2-slice-14
#: test3-contour-2-slice-15
#: test3-contour-2-slice-16
#: test3-contour-2-slice-17
#: test3-contour-2-slice-18
#: test3-contour-2-slice-19
#: test3-contour-2-slice-20
#: test3-contour-2-slice-21
#: test3-contour-2-slice-22
#: test3-contour-2-slice-23
#: test3-contour-2-slice-24
#: test3-contour-2-slice-25
#: test3-contour-2-slice-26
#: test3-contour-2-slice-27
#: test3-contour-2-slice-28
#: test3-contour-2-slice-29
#: test3-contour-2-slice-30
#: test3-contour-2-slice-31
#: test3-contour-2-slice-32
#: test3-contour-2-slice-33
#: test3-contour-2-slice-34
#: test3-contour-2-slice-35
#: test3-contour-2-slice-36
#: test3-contour-2-slice-37
#: test3-contour-2-slice-38
#: test3-contour-2-slice-39
#: test3-contour-2-slice-40
#: test3-contour-2-slice-41
#: test3-contour-2-slice-42
#: test3-contour-2-slice-43
#: test3-contour-2-slice-44
#: test3-contour-2-slice-45
#: test3-contour-2-slice-46
#: test3-contour-2-slice-47
#: test3-contour-2-slice-48
#: test3-contour-2-slice-49
#: test3-contour-2-slice-50
#: test3-contour-2-slice-51
#: test3-contour-2-slice-52
#: test3-contour-2-slice-53
#: test3-contour-2-slice-54
#: test3-contour-2-slice-55
#: test3-contour-2-slice-56
#: test3-contour-2-slice-57
#: test3-contour-2-slice-58
#: test3-contour-2-slice-59
#: test3-contour-2-slice-60
#: test3-contour-2-slice-61
#: test3-contour-2-slice-62
#: test3-contour-2-slice-63
#: test3-contour-2-slice-64
#: test3-contour-2-slice-65
#: test3-contour-2-slice-66
#: test3-contour-2-slice-67
#: test3-contour-2-slice-68
#: test3-contour-2-slice-69
#: test3-contour-2-slice-70
#: test3-contour-2-slice-71
#: test3-contour-2-slice-72
#: test3-contour-2-slice-73
#: test3-contour-2-slice-74
#: test3-contour-2-slice-75
#: test3-contour-2-slice-76
#: test3-contour-2-slice-77
#: test3-contour-2-slice-78
#: test3-contour-2-slice-79
#: test3-contour-2-slice-80
#: test3-contour-2-slice-81
#: test3-contour-2-slice-82
#: test3-contour-2-slice-83
#: test3-contour-2-slice-84
#: test3-contour-2-slice-85
#: test3-contour-2-slice-86
#: test3-contour-2-slice-87
#: test3-contour-2-slice-88
#: test3-contour-2-slice-89
#: test3-contour-2-slice-90
#: test3-contour-2-slice-91
#: test3-contour-2-slice-92
#: test3-contour-2-slice-93
#: time report
#: ++++++++++++
#: time in first loop 0.220999956131
#: time in first loop get El 0.15900015831
#: time in first loop get union 0.0429997444153
#: time in second loop 1.94100022316
#: time in third loop 0.0479998588562
#: ++++++++++++
#: ++++++++++++
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.1893, 
    farPlane=64.4454, width=0.164265, height=0.436189, viewOffsetX=1.77504, 
    viewOffsetY=-3.44504)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       133
#: Number of Node Sets:          768
#: Number of Steps:              1
#: node labels
#: [    512 2234748 2234743 2234740 2234738 2234746   42605 2234728 2234731
#:  2234723 2234733 2234725   42606 2234710 2234708 2234713 2234716 2234718
#:    42607 2234703 2234698 2234695 2234693 2234701   42608 2234683 2234678
#:  2234680 2234686 2234688   42609 2234671 2234668 2234665 2234663 2234673
#:    42610 2234648 2234658 2234656 2234653 2234650   42611 2234633 2234643
#:  2234641 2234638 2234635   42612 2234618 2234620 2234623 2234626 2234628
#:    42613 2234605 2234608 2234611 2234613 2234603   42614 2234588 2234598
#:  2234596 2234593 2234590   42615 2234583 2234581 2234578 2234575 2234573
#:    42616 2234568 2234566 2234560 2234563 2234558   42617 2234553 2234551
#:  2234548 2234545 2234543   42618 2234530 2234538 2234536 2234533 2234528
#:    42619 2234518 2234515 2234523 2234521 2234513   42620 2234498 2234500
#:  2234506 2234508 2234503   42621 2234483 2234485 2234488 2234491 2234493
#:    42622 2234470 2234478 2234476 2234473 2234468   42623 2234463 2234461
#:  2234458 2234455 2234453   42624 2234448 2234443 2234446 2234438 2234440
#:    42625 2234423 2234425 2234428 2234431 2234433   42626 2234416 2234418
#:  2234413 2234410 2234408   42627 2234403 2234401 2234398 2234395 2234393
#:    42628 2234383 2234386 2234388 2234378 2234380   42629 2234365 2234368
#:  2234371 2234373 2234363   42630 2234358 2234356 2234353 2234350 2234348
#:    42631 2234343 2234341 2234333 2234335 2234338   42632 2234318 2234320
#:  2234326 2234328 2234323   42633 2234305 2234303 2234308 2234311 2234313
#:    42634 2234280 2234283 2234288 2234293 2234296     511]
#: node labels
#: [ 2.7815001   2.73663712  2.73663712  2.73663712  2.73663712  2.73663712
#:   2.69177413  2.64691114  2.64691114  2.64691114  2.64691114  2.64691114
#:   2.6020484   2.55718565  2.55718565  2.55718565  2.55718565  2.55718565
#:   2.51232266  2.46745968  2.46745968  2.46745968  2.46745968  2.46745968
#:   2.42259669  2.37773371  2.37773371  2.37773371  2.37773371  2.37773371
#:   2.33287096  2.28800821  2.28800821  2.28800821  2.28800821  2.28800821
#:   2.24314523  2.19828224  2.19828224  2.19828224  2.19828224  2.19828224
#:   2.15341926  2.10855627  2.10855627  2.10855627  2.10855627  2.10855627
#:   2.06369352  2.01883078  2.01883078  2.01883078  2.01883078  2.01883078
#:   1.97396779  1.9291048   1.9291048   1.9291048   1.9291048   1.9291048
#:   1.88424194  1.83937907  1.83937907  1.83937907  1.83937907  1.83937907
#:   1.79451609  1.74965322  1.74965322  1.74965322  1.74965322  1.74965322
#:   1.70479035  1.65992737  1.65992737  1.65992737  1.65992737  1.65992737
#:   1.6150645   1.57020164  1.57020164  1.57020164  1.57020164  1.57020164
#:   1.52533877  1.4804759   1.4804759   1.4804759   1.4804759   1.4804759
#:   1.43561292  1.39074993  1.39074993  1.39074993  1.39074993  1.39074993
#:   1.34588706  1.3010242   1.3010242   1.3010242   1.3010242   1.3010242
#:   1.25616133  1.21129847  1.21129847  1.21129847  1.21129847  1.21129847
#:   1.16643548  1.12157249  1.12157249  1.12157249  1.12157249  1.12157249
#:   1.07670963  1.03184676  1.03184676  1.03184676  1.03184676  1.03184676
#:   0.9869839   0.94212097  0.94212097  0.94212097  0.94212097  0.94212097
#:   0.89725804  0.85239518  0.85239518  0.85239518  0.85239518  0.85239518
#:   0.80753225  0.76266932  0.76266932  0.76266932  0.76266932  0.76266932
#:   0.71780646  0.67294359  0.67294359  0.67294359  0.67294359  0.67294359
#:   0.62808067  0.58321774  0.58321774  0.58321774  0.58321774  0.58321774
#:   0.53835481  0.49349192  0.49349192  0.49349192  0.49349192  0.49349192
#:   0.44862902  0.40376613  0.40376613  0.40376613  0.40376613  0.40376613
#:   0.35890323  0.3140403   0.3140403   0.3140403   0.3140403   0.3140403
#:   0.26917741  0.22431451  0.22431451  0.22431451  0.22431451  0.22431451
#:   0.17945161  0.13458872  0.13458872  0.13458872  0.13458872  0.13458872
#:   0.08972581  0.0448629   0.0448629   0.0448629   0.0448629   0.0448629   0.        ] 0 1
#* TypeError: exceptions must be old-style classes or derived from 
#* BaseException, not NoneType
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 106, in <module>
#*     odb = 
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* odb,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 87, 
#* in BuildElementAndNodeSets
#*     raise
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
#: 
#: Node: NOCHEDSPECIMEN-C-1.512
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24600e+01,  2.72977e+00,  2.78150e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: NOCHEDSPECIMEN-C-1.565768
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24535e+01,  2.72213e+00,  2.73664e+00,      -      
#: No deformed coordinates for current plot.
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.2081, 
    farPlane=64.4266, width=0.083206, height=0.125409, viewOffsetX=1.75423, 
    viewOffsetY=-3.42089)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.1133, 
    farPlane=64.1006, width=0.0850793, height=0.128233, cameraPosition=(
    36.7072, 30.9715, 40.4744), cameraUpVector=(-0.498438, 0.678454, 
    -0.539685), cameraTarget=(9.38927, 6.78199, 2.98166), viewOffsetX=1.79373, 
    viewOffsetY=-3.49791)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.0739, 
    farPlane=64.1399, width=0.281089, height=0.423662, viewOffsetX=1.81309, 
    viewOffsetY=-3.45964)
session.viewports['Viewport: 1'].view.setValues(farPlane=64.1436, 
    cameraPosition=(36.5692, 30.8369, 40.6618), cameraUpVector=(-0.537486, 
    0.673202, -0.507846), cameraTarget=(9.25128, 6.64744, 3.16901))
#: 
#: Node: NOCHEDSPECIMEN-C-1.42605
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24600e+01,  2.72977e+00,  2.69177e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: NOCHEDSPECIMEN-C-1.1585070
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.21440e+01,  2.36128e+00,  2.15342e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: NOCHEDSPECIMEN-C-1.2234706
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24591e+01,  2.72743e+00,  2.60205e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: NOCHEDSPECIMEN-C-1.42606
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24600e+01,  2.72977e+00,  2.60205e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: NOCHEDSPECIMEN-C-1.512
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24600e+01,  2.72977e+00,  2.78150e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: NOCHEDSPECIMEN-C-1.42605
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24600e+01,  2.72977e+00,  2.69177e+00,      -      
#: No deformed coordinates for current plot.
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.0985, 
    farPlane=64.1154, width=0.161159, height=0.242901, viewOffsetX=1.77621, 
    viewOffsetY=-3.49682)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       133
#: Number of Node Sets:          768
#: Number of Steps:              1
#: test3-contour-1-slice-0
#: test3-contour-1-slice-1
#: test3-contour-1-slice-2
#: test3-contour-1-slice-3
#: test3-contour-1-slice-4
#: test3-contour-1-slice-5
#: test3-contour-1-slice-6
#: test3-contour-1-slice-7
#: test3-contour-1-slice-8
#: test3-contour-1-slice-9
#: test3-contour-1-slice-10
#: test3-contour-1-slice-11
#: test3-contour-1-slice-12
#: test3-contour-1-slice-13
#: test3-contour-1-slice-14
#: test3-contour-1-slice-15
#: test3-contour-1-slice-16
#: test3-contour-1-slice-17
#: test3-contour-1-slice-18
#: test3-contour-1-slice-19
#: test3-contour-1-slice-20
#: test3-contour-1-slice-21
#: test3-contour-1-slice-22
#: test3-contour-1-slice-23
#: test3-contour-1-slice-24
#: test3-contour-1-slice-25
#: test3-contour-1-slice-26
#: test3-contour-1-slice-27
#: test3-contour-1-slice-28
#: test3-contour-1-slice-29
#: test3-contour-1-slice-30
#: test3-contour-1-slice-31
#: test3-contour-1-slice-32
#: test3-contour-1-slice-33
#: test3-contour-1-slice-34
#: test3-contour-1-slice-35
#: test3-contour-1-slice-36
#: test3-contour-1-slice-37
#: test3-contour-1-slice-38
#: test3-contour-1-slice-39
#: test3-contour-1-slice-40
#: test3-contour-1-slice-41
#: test3-contour-1-slice-42
#: test3-contour-1-slice-43
#: test3-contour-1-slice-44
#: test3-contour-1-slice-45
#: test3-contour-1-slice-46
#: test3-contour-1-slice-47
#: test3-contour-1-slice-48
#: test3-contour-1-slice-49
#: test3-contour-1-slice-50
#: test3-contour-1-slice-51
#: test3-contour-1-slice-52
#: test3-contour-1-slice-53
#: test3-contour-1-slice-54
#: test3-contour-1-slice-55
#: test3-contour-1-slice-56
#: test3-contour-1-slice-57
#: test3-contour-1-slice-58
#: test3-contour-1-slice-59
#: test3-contour-1-slice-60
#: test3-contour-1-slice-61
#: test3-contour-1-slice-62
#: test3-contour-1-slice-63
#: test3-contour-1-slice-64
#: test3-contour-1-slice-65
#: test3-contour-1-slice-66
#: test3-contour-1-slice-67
#: test3-contour-1-slice-68
#: test3-contour-1-slice-69
#: test3-contour-1-slice-70
#: test3-contour-1-slice-71
#: test3-contour-1-slice-72
#: test3-contour-1-slice-73
#: test3-contour-1-slice-74
#: test3-contour-1-slice-75
#: test3-contour-1-slice-76
#: test3-contour-1-slice-77
#: test3-contour-1-slice-78
#: test3-contour-1-slice-79
#: test3-contour-1-slice-80
#: test3-contour-1-slice-81
#: test3-contour-1-slice-82
#: test3-contour-1-slice-83
#: test3-contour-1-slice-84
#: test3-contour-1-slice-85
#: test3-contour-1-slice-86
#: test3-contour-1-slice-87
#: test3-contour-1-slice-88
#: test3-contour-1-slice-89
#: test3-contour-1-slice-90
#: test3-contour-1-slice-91
#: test3-contour-1-slice-92
#: test3-contour-1-slice-93
#: test3-contour-2-slice-0
#: test3-contour-2-slice-1
#: test3-contour-2-slice-2
#: test3-contour-2-slice-3
#: test3-contour-2-slice-4
#: test3-contour-2-slice-5
#: test3-contour-2-slice-6
#: test3-contour-2-slice-7
#: test3-contour-2-slice-8
#: test3-contour-2-slice-9
#: test3-contour-2-slice-10
#: test3-contour-2-slice-11
#: test3-contour-2-slice-12
#: test3-contour-2-slice-13
#: test3-contour-2-slice-14
#: test3-contour-2-slice-15
#: test3-contour-2-slice-16
#: test3-contour-2-slice-17
#: test3-contour-2-slice-18
#: test3-contour-2-slice-19
#: test3-contour-2-slice-20
#: test3-contour-2-slice-21
#: test3-contour-2-slice-22
#: test3-contour-2-slice-23
#: test3-contour-2-slice-24
#: test3-contour-2-slice-25
#: test3-contour-2-slice-26
#: test3-contour-2-slice-27
#: test3-contour-2-slice-28
#: test3-contour-2-slice-29
#: test3-contour-2-slice-30
#: test3-contour-2-slice-31
#: test3-contour-2-slice-32
#: test3-contour-2-slice-33
#: test3-contour-2-slice-34
#: test3-contour-2-slice-35
#: test3-contour-2-slice-36
#: test3-contour-2-slice-37
#: test3-contour-2-slice-38
#: test3-contour-2-slice-39
#: test3-contour-2-slice-40
#: test3-contour-2-slice-41
#: test3-contour-2-slice-42
#: test3-contour-2-slice-43
#: test3-contour-2-slice-44
#: test3-contour-2-slice-45
#: test3-contour-2-slice-46
#: test3-contour-2-slice-47
#: test3-contour-2-slice-48
#: test3-contour-2-slice-49
#: test3-contour-2-slice-50
#: test3-contour-2-slice-51
#: test3-contour-2-slice-52
#: test3-contour-2-slice-53
#: test3-contour-2-slice-54
#: test3-contour-2-slice-55
#: test3-contour-2-slice-56
#: test3-contour-2-slice-57
#: test3-contour-2-slice-58
#: test3-contour-2-slice-59
#: test3-contour-2-slice-60
#: test3-contour-2-slice-61
#: test3-contour-2-slice-62
#: test3-contour-2-slice-63
#: test3-contour-2-slice-64
#: test3-contour-2-slice-65
#: test3-contour-2-slice-66
#: test3-contour-2-slice-67
#: test3-contour-2-slice-68
#: test3-contour-2-slice-69
#: test3-contour-2-slice-70
#: test3-contour-2-slice-71
#: test3-contour-2-slice-72
#: test3-contour-2-slice-73
#: test3-contour-2-slice-74
#: test3-contour-2-slice-75
#: test3-contour-2-slice-76
#: test3-contour-2-slice-77
#: test3-contour-2-slice-78
#: test3-contour-2-slice-79
#: test3-contour-2-slice-80
#: test3-contour-2-slice-81
#: test3-contour-2-slice-82
#: test3-contour-2-slice-83
#: test3-contour-2-slice-84
#: test3-contour-2-slice-85
#: test3-contour-2-slice-86
#: test3-contour-2-slice-87
#: test3-contour-2-slice-88
#: test3-contour-2-slice-89
#: test3-contour-2-slice-90
#: test3-contour-2-slice-91
#: test3-contour-2-slice-92
#: test3-contour-2-slice-93
#* OdbError: Duplicate set or surface name test3-contour-0-slice-0-Q0
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 106, in <module>
#*     odb = 
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* odb,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 257, 
#* in BuildElementAndNodeSets
#*     root.NodeSetFromNodeLabels(name = setName, nodeLabels = 
#* ((partInstance,nsetQ0),))
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       133
#: Number of Node Sets:          768
#: Number of Steps:              1
#: test4-contour-1-slice-0
#: test4-contour-1-slice-1
#: test4-contour-1-slice-2
#: test4-contour-1-slice-3
#: test4-contour-1-slice-4
#: test4-contour-1-slice-5
#: test4-contour-1-slice-6
#: test4-contour-1-slice-7
#: test4-contour-1-slice-8
#: test4-contour-1-slice-9
#: test4-contour-1-slice-10
#: test4-contour-1-slice-11
#: test4-contour-1-slice-12
#: test4-contour-1-slice-13
#: test4-contour-1-slice-14
#: test4-contour-1-slice-15
#: test4-contour-1-slice-16
#: test4-contour-1-slice-17
#: test4-contour-1-slice-18
#: test4-contour-1-slice-19
#: test4-contour-1-slice-20
#: test4-contour-1-slice-21
#: test4-contour-1-slice-22
#: test4-contour-1-slice-23
#: test4-contour-1-slice-24
#: test4-contour-1-slice-25
#: test4-contour-1-slice-26
#: test4-contour-1-slice-27
#: test4-contour-1-slice-28
#: test4-contour-1-slice-29
#: test4-contour-1-slice-30
#: test4-contour-1-slice-31
#: test4-contour-1-slice-32
#: test4-contour-1-slice-33
#: test4-contour-1-slice-34
#: test4-contour-1-slice-35
#: test4-contour-1-slice-36
#: test4-contour-1-slice-37
#: test4-contour-1-slice-38
#: test4-contour-1-slice-39
#: test4-contour-1-slice-40
#: test4-contour-1-slice-41
#: test4-contour-1-slice-42
#: test4-contour-1-slice-43
#: test4-contour-1-slice-44
#: test4-contour-1-slice-45
#: test4-contour-1-slice-46
#: test4-contour-1-slice-47
#: test4-contour-1-slice-48
#: test4-contour-1-slice-49
#: test4-contour-1-slice-50
#: test4-contour-1-slice-51
#: test4-contour-1-slice-52
#: test4-contour-1-slice-53
#: test4-contour-1-slice-54
#: test4-contour-1-slice-55
#: test4-contour-1-slice-56
#: test4-contour-1-slice-57
#: test4-contour-1-slice-58
#: test4-contour-1-slice-59
#: test4-contour-1-slice-60
#: test4-contour-1-slice-61
#: test4-contour-1-slice-62
#: test4-contour-1-slice-63
#: test4-contour-1-slice-64
#: test4-contour-1-slice-65
#: test4-contour-1-slice-66
#: test4-contour-1-slice-67
#: test4-contour-1-slice-68
#: test4-contour-1-slice-69
#: test4-contour-1-slice-70
#: test4-contour-1-slice-71
#: test4-contour-1-slice-72
#: test4-contour-1-slice-73
#: test4-contour-1-slice-74
#: test4-contour-1-slice-75
#: test4-contour-1-slice-76
#: test4-contour-1-slice-77
#: test4-contour-1-slice-78
#: test4-contour-1-slice-79
#: test4-contour-1-slice-80
#: test4-contour-1-slice-81
#: test4-contour-1-slice-82
#: test4-contour-1-slice-83
#: test4-contour-1-slice-84
#: test4-contour-1-slice-85
#: test4-contour-1-slice-86
#: test4-contour-1-slice-87
#: test4-contour-1-slice-88
#: test4-contour-1-slice-89
#: test4-contour-1-slice-90
#: test4-contour-1-slice-91
#: test4-contour-1-slice-92
#: test4-contour-1-slice-93
#: test4-contour-2-slice-0
#: test4-contour-2-slice-1
#: test4-contour-2-slice-2
#: test4-contour-2-slice-3
#: test4-contour-2-slice-4
#: test4-contour-2-slice-5
#: test4-contour-2-slice-6
#: test4-contour-2-slice-7
#: test4-contour-2-slice-8
#: test4-contour-2-slice-9
#: test4-contour-2-slice-10
#: test4-contour-2-slice-11
#: test4-contour-2-slice-12
#: test4-contour-2-slice-13
#: test4-contour-2-slice-14
#: test4-contour-2-slice-15
#: test4-contour-2-slice-16
#: test4-contour-2-slice-17
#: test4-contour-2-slice-18
#: test4-contour-2-slice-19
#: test4-contour-2-slice-20
#: test4-contour-2-slice-21
#: test4-contour-2-slice-22
#: test4-contour-2-slice-23
#: test4-contour-2-slice-24
#: test4-contour-2-slice-25
#: test4-contour-2-slice-26
#: test4-contour-2-slice-27
#: test4-contour-2-slice-28
#: test4-contour-2-slice-29
#: test4-contour-2-slice-30
#: test4-contour-2-slice-31
#: test4-contour-2-slice-32
#: test4-contour-2-slice-33
#: test4-contour-2-slice-34
#: test4-contour-2-slice-35
#: test4-contour-2-slice-36
#: test4-contour-2-slice-37
#: test4-contour-2-slice-38
#: test4-contour-2-slice-39
#: test4-contour-2-slice-40
#: test4-contour-2-slice-41
#: test4-contour-2-slice-42
#: test4-contour-2-slice-43
#: test4-contour-2-slice-44
#: test4-contour-2-slice-45
#: test4-contour-2-slice-46
#: test4-contour-2-slice-47
#: test4-contour-2-slice-48
#: test4-contour-2-slice-49
#: test4-contour-2-slice-50
#: test4-contour-2-slice-51
#: test4-contour-2-slice-52
#: test4-contour-2-slice-53
#: test4-contour-2-slice-54
#: test4-contour-2-slice-55
#: test4-contour-2-slice-56
#: test4-contour-2-slice-57
#: test4-contour-2-slice-58
#: test4-contour-2-slice-59
#: test4-contour-2-slice-60
#: test4-contour-2-slice-61
#: test4-contour-2-slice-62
#: test4-contour-2-slice-63
#: test4-contour-2-slice-64
#: test4-contour-2-slice-65
#: test4-contour-2-slice-66
#: test4-contour-2-slice-67
#: test4-contour-2-slice-68
#: test4-contour-2-slice-69
#: test4-contour-2-slice-70
#: test4-contour-2-slice-71
#: test4-contour-2-slice-72
#: test4-contour-2-slice-73
#: test4-contour-2-slice-74
#: test4-contour-2-slice-75
#: test4-contour-2-slice-76
#: test4-contour-2-slice-77
#: test4-contour-2-slice-78
#: test4-contour-2-slice-79
#: test4-contour-2-slice-80
#: test4-contour-2-slice-81
#: test4-contour-2-slice-82
#: test4-contour-2-slice-83
#: test4-contour-2-slice-84
#: test4-contour-2-slice-85
#: test4-contour-2-slice-86
#: test4-contour-2-slice-87
#: test4-contour-2-slice-88
#: test4-contour-2-slice-89
#: test4-contour-2-slice-90
#: test4-contour-2-slice-91
#: test4-contour-2-slice-92
#: test4-contour-2-slice-93
#: time report
#: ++++++++++++
#: time in first loop 0.0729999542236
#: time in first loop get El 0.0139997005463
#: time in first loop get union 0.0409998893738
#: time in second loop 1.84400010109
#: time in third loop 0.0469999313354
#: ++++++++++++
#: ++++++++++++
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.1816, 
    farPlane=64.4532, width=0.197733, height=0.298026, viewOffsetX=1.78748, 
    viewOffsetY=-3.38275)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       133
#: Number of Node Sets:          768
#: Number of Steps:              1
#: node labels
#: [    512 2234748 2234743 2234740 2234738 2234746   42605 2234728 2234731
#:  2234723 2234733 2234725   42606 2234710 2234708 2234713 2234716 2234718
#:    42607 2234703 2234698 2234695 2234693 2234701   42608 2234683 2234678
#:  2234680 2234686 2234688   42609 2234671 2234668 2234665 2234663 2234673
#:    42610 2234648 2234658 2234656 2234653 2234650   42611 2234633 2234643
#:  2234641 2234638 2234635   42612 2234618 2234620 2234623 2234626 2234628
#:    42613 2234605 2234608 2234611 2234613 2234603   42614 2234588 2234598
#:  2234596 2234593 2234590   42615 2234583 2234581 2234578 2234575 2234573
#:    42616 2234568 2234566 2234560 2234563 2234558   42617 2234553 2234551
#:  2234548 2234545 2234543   42618 2234530 2234538 2234536 2234533 2234528
#:    42619 2234518 2234515 2234523 2234521 2234513   42620 2234498 2234500
#:  2234506 2234508 2234503   42621 2234483 2234485 2234488 2234491 2234493
#:    42622 2234470 2234478 2234476 2234473 2234468   42623 2234463 2234461
#:  2234458 2234455 2234453   42624 2234448 2234443 2234446 2234438 2234440
#:    42625 2234423 2234425 2234428 2234431 2234433   42626 2234416 2234418
#:  2234413 2234410 2234408   42627 2234403 2234401 2234398 2234395 2234393
#:    42628 2234383 2234386 2234388 2234378 2234380   42629 2234365 2234368
#:  2234371 2234373 2234363   42630 2234358 2234356 2234353 2234350 2234348
#:    42631 2234343 2234341 2234333 2234335 2234338   42632 2234318 2234320
#:  2234326 2234328 2234323   42633 2234305 2234303 2234308 2234311 2234313
#:    42634 2234280 2234283 2234288 2234293 2234296     511]
#: node labels
#: [ 2.7815001   2.73663712  2.73663712  2.73663712  2.73663712  2.73663712
#:   2.69177413  2.64691114  2.64691114  2.64691114  2.64691114  2.64691114
#:   2.6020484   2.55718565  2.55718565  2.55718565  2.55718565  2.55718565
#:   2.51232266  2.46745968  2.46745968  2.46745968  2.46745968  2.46745968
#:   2.42259669  2.37773371  2.37773371  2.37773371  2.37773371  2.37773371
#:   2.33287096  2.28800821  2.28800821  2.28800821  2.28800821  2.28800821
#:   2.24314523  2.19828224  2.19828224  2.19828224  2.19828224  2.19828224
#:   2.15341926  2.10855627  2.10855627  2.10855627  2.10855627  2.10855627
#:   2.06369352  2.01883078  2.01883078  2.01883078  2.01883078  2.01883078
#:   1.97396779  1.9291048   1.9291048   1.9291048   1.9291048   1.9291048
#:   1.88424194  1.83937907  1.83937907  1.83937907  1.83937907  1.83937907
#:   1.79451609  1.74965322  1.74965322  1.74965322  1.74965322  1.74965322
#:   1.70479035  1.65992737  1.65992737  1.65992737  1.65992737  1.65992737
#:   1.6150645   1.57020164  1.57020164  1.57020164  1.57020164  1.57020164
#:   1.52533877  1.4804759   1.4804759   1.4804759   1.4804759   1.4804759
#:   1.43561292  1.39074993  1.39074993  1.39074993  1.39074993  1.39074993
#:   1.34588706  1.3010242   1.3010242   1.3010242   1.3010242   1.3010242
#:   1.25616133  1.21129847  1.21129847  1.21129847  1.21129847  1.21129847
#:   1.16643548  1.12157249  1.12157249  1.12157249  1.12157249  1.12157249
#:   1.07670963  1.03184676  1.03184676  1.03184676  1.03184676  1.03184676
#:   0.9869839   0.94212097  0.94212097  0.94212097  0.94212097  0.94212097
#:   0.89725804  0.85239518  0.85239518  0.85239518  0.85239518  0.85239518
#:   0.80753225  0.76266932  0.76266932  0.76266932  0.76266932  0.76266932
#:   0.71780646  0.67294359  0.67294359  0.67294359  0.67294359  0.67294359
#:   0.62808067  0.58321774  0.58321774  0.58321774  0.58321774  0.58321774
#:   0.53835481  0.49349192  0.49349192  0.49349192  0.49349192  0.49349192
#:   0.44862902  0.40376613  0.40376613  0.40376613  0.40376613  0.40376613
#:   0.35890323  0.3140403   0.3140403   0.3140403   0.3140403   0.3140403
#:   0.26917741  0.22431451  0.22431451  0.22431451  0.22431451  0.22431451
#:   0.17945161  0.13458872  0.13458872  0.13458872  0.13458872  0.13458872
#:   0.08972581  0.0448629   0.0448629   0.0448629   0.0448629   0.0448629   0.        ] 0 1
#* TypeError: exceptions must be old-style classes or derived from 
#* BaseException, not NoneType
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 106, in <module>
#*     odb = 
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* odb,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 87, 
#* in BuildElementAndNodeSets
#*     raise
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlaneNoSymm_copy.odb'].close(
    )
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.1425, 
    farPlane=64.4923, width=0.366755, height=0.552779, viewOffsetX=1.86213, 
    viewOffsetY=-3.39839)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       133
#: Number of Node Sets:          768
#: Number of Steps:              1
#: 0 1
#: 12.46 2.72977
#* TypeError: 'int' object has no attribute '__getitem__'
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 106, in <module>
#*     odb = 
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* odb,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 85, 
#* in BuildElementAndNodeSets
#*     print labels[i],position[i],pos1[i],pos2[i]
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       133
#: Number of Node Sets:          768
#: Number of Steps:              1
#: 512 2.7815 512 2.7815
#: 2234748 2.73664
#: 2234743 2.73664
#: 2234740 2.73664
#: 2234738 2.73664
#: 2234746 2.73664
#: 42605 2.69177
#: 2234728 2.64691
#: 2234731 2.64691
#: 2234723 2.64691
#: 2234733 2.64691
#: 2234725 2.64691
#: 42606 2.60205
#: 2234710 2.55719
#: 2234708 2.55719
#: 2234713 2.55719
#: 2234716 2.55719
#: 2234718 2.55719
#: 42607 2.51232
#: 2234703 2.46746
#: 2234698 2.46746
#: 2234695 2.46746
#: 2234693 2.46746
#: 2234701 2.46746
#: 42608 2.4226
#: 2234683 2.37773
#: 2234678 2.37773
#: 2234680 2.37773
#: 2234686 2.37773
#: 2234688 2.37773
#: 42609 2.33287
#: 2234671 2.28801
#: 2234668 2.28801
#: 2234665 2.28801
#: 2234663 2.28801
#: 2234673 2.28801
#: 42610 2.24315
#: 2234648 2.19828
#: 2234658 2.19828
#: 2234656 2.19828
#: 2234653 2.19828
#: 2234650 2.19828
#: 42611 2.15342
#: 2234633 2.10856
#: 2234643 2.10856
#: 2234641 2.10856
#: 2234638 2.10856
#: 2234635 2.10856
#: 42612 2.06369
#: 2234618 2.01883
#: 2234620 2.01883
#: 2234623 2.01883
#: 2234626 2.01883
#: 2234628 2.01883
#: 42613 1.97397
#: 2234605 1.9291
#: 2234608 1.9291
#: 2234611 1.9291
#: 2234613 1.9291
#: 2234603 1.9291
#: 42614 1.88424
#: 2234588 1.83938
#: 2234598 1.83938
#: 2234596 1.83938
#: 2234593 1.83938
#: 2234590 1.83938
#: 42615 1.79452
#: 2234583 1.74965
#: 2234581 1.74965
#: 2234578 1.74965
#: 2234575 1.74965
#: 2234573 1.74965
#: 42616 1.70479
#: 2234568 1.65993
#: 2234566 1.65993
#: 2234560 1.65993
#: 2234563 1.65993
#: 2234558 1.65993
#: 42617 1.61506
#: 2234553 1.5702
#: 2234551 1.5702
#: 2234548 1.5702
#: 2234545 1.5702
#: 2234543 1.5702
#: 42618 1.52534
#: 2234530 1.48048
#: 2234538 1.48048
#: 2234536 1.48048
#: 2234533 1.48048
#: 2234528 1.48048
#: 42619 1.43561
#: 2234518 1.39075
#: 2234515 1.39075
#: 2234523 1.39075
#: 2234521 1.39075
#: 2234513 1.39075
#: 42620 1.34589
#: 2234498 1.30102
#: 2234500 1.30102
#: 2234506 1.30102
#: 2234508 1.30102
#: 2234503 1.30102
#: 42621 1.25616
#: 2234483 1.2113
#: 2234485 1.2113
#: 2234488 1.2113
#: 2234491 1.2113
#: 2234493 1.2113
#: 42622 1.16644
#: 2234470 1.12157
#: 2234478 1.12157
#: 2234476 1.12157
#: 2234473 1.12157
#: 2234468 1.12157
#: 42623 1.07671
#: 2234463 1.03185
#: 2234461 1.03185
#: 2234458 1.03185
#: 2234455 1.03185
#: 2234453 1.03185
#: 42624 0.986984
#: 2234448 0.942121
#: 2234443 0.942121
#: 2234446 0.942121
#: 2234438 0.942121
#: 2234440 0.942121
#: 42625 0.897258
#: 2234423 0.852395
#: 2234425 0.852395
#: 2234428 0.852395
#: 2234431 0.852395
#: 2234433 0.852395
#: 42626 0.807532
#: 2234416 0.762669
#: 2234418 0.762669
#: 2234413 0.762669
#: 2234410 0.762669
#: 2234408 0.762669
#: 42627 0.717806
#: 2234403 0.672944
#: 2234401 0.672944
#: 2234398 0.672944
#: 2234395 0.672944
#: 2234393 0.672944
#: 42628 0.628081
#: 2234383 0.583218
#: 2234386 0.583218
#: 2234388 0.583218
#: 2234378 0.583218
#: 2234380 0.583218
#: 42629 0.538355
#: 2234365 0.493492
#: 2234368 0.493492
#: 2234371 0.493492
#: 2234373 0.493492
#: 2234363 0.493492
#: 42630 0.448629
#: 2234358 0.403766
#: 2234356 0.403766
#: 2234353 0.403766
#: 2234350 0.403766
#: 2234348 0.403766
#: 42631 0.358903
#: 2234343 0.31404
#: 2234341 0.31404
#: 2234333 0.31404
#: 2234335 0.31404
#: 2234338 0.31404
#: 42632 0.269177
#: 2234318 0.224315
#: 2234320 0.224315
#: 2234326 0.224315
#: 2234328 0.224315
#: 2234323 0.224315
#: 42633 0.179452
#: 2234305 0.134589
#: 2234303 0.134589
#: 2234308 0.134589
#: 2234311 0.134589
#: 2234313 0.134589
#: 42634 0.0897258
#: 2234280 0.0448629
#: 2234283 0.0448629
#: 2234288 0.0448629
#: 2234293 0.0448629
#: 2234296 0.0448629
#: 511 0.0
#* TypeError: exceptions must be old-style classes or derived from 
#* BaseException, not NoneType
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 106, in <module>
#*     odb = 
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* odb,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 85, 
#* in BuildElementAndNodeSets
#*     raise
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/Job-3PB-Quarter-All-C3D20-Dan.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
#: 
#: Node: NOCHEDSPECIMEN-C-1.565768
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24535e+01,  2.72213e+00,  2.73664e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: NOCHEDSPECIMEN-C-1.42605
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24600e+01,  2.72977e+00,  2.69177e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: NOCHEDSPECIMEN-C-1.2234748
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24600e+01,  2.72977e+00,  2.73664e+00,      -      
#: No deformed coordinates for current plot.
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.2192, 
    farPlane=64.4156, width=0.0401216, height=0.0604719, viewOffsetX=1.7212, 
    viewOffsetY=-3.44374)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1.73917, 
    viewOffsetY=-3.43543)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.2132, 
    farPlane=64.4216, width=0.0768489, height=0.115828, viewOffsetX=1.73789, 
    viewOffsetY=-3.43764)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1.7401, 
    viewOffsetY=-3.43223)
#: 
#: ODB: Job-3PB-Quarter-All-C3D20-Dan.odb
#:    Number of nodes: 2234751
#:    Number of elements: 539370
#:    Element types: ARSR C3D20 RNODE3D 
#: 
#: ODB: Job-3PB-Quarter-All-C3D20-Dan.odb
#:    Number of nodes: 2234751
#:    Number of elements: 539370
#:    Element types: ARSR C3D20 RNODE3D 
