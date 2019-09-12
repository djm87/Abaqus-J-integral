# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2019 replay file
# Internal Version: 2018_09_24-14.41.51 157541
# Run by dansa on Tue Sep  3 10:05:15 2019
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
o2 = session.openOdb(name='J-Indenter_Quarter_homo.odb')
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb'].close(
    )
import os
os.chdir(r"E:\Dropbox\Research\Source\Abaqus-J-integral\Example 3")
o1 = session.openOdb(
    name='E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: 
#: Node: SPECIMEN-1.1780
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24600e+01,  2.13520e+00,  2.78150e+00,      -      
#: No deformed coordinates for current plot.
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.2221, 
    farPlane=64.4127, width=0.057181, height=0.0268904, viewOffsetX=1.71118, 
    viewOffsetY=-3.78627)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: No modules to remove
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#* KeyError: NOCHEDSPECIMEN-C-1
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 106, in <module>
#*     odb = 
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* odb,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 88, 
#* in BuildElementAndNodeSets
#*     part=root.instances[partInstance]
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: 1780 2.7815 12.46 2.1352
#: 1789773 2.73183 12.46 2.1352
#: 55801 2.68216 12.46 2.1352
#: 1789776 2.63249 12.46 2.1352
#: 55800 2.58282 12.46 2.1352
#: 1789779 2.53315 12.46 2.1352
#: 55799 2.48348 12.46 2.1352
#: 1789782 2.43381 12.46 2.1352
#: 55798 2.38414 12.46 2.1352
#: 1789785 2.33447 12.46 2.1352
#: 55797 2.2848 12.46 2.1352
#: 1789788 2.23513 12.46 2.1352
#: 55796 2.18546 12.46 2.1352
#: 1789791 2.13579 12.46 2.1352
#: 55795 2.08613 12.46 2.1352
#: 1789794 2.03646 12.46 2.1352
#: 55794 1.98679 12.46 2.1352
#: 1789797 1.93712 12.46 2.1352
#: 55793 1.88745 12.46 2.1352
#: 1789800 1.83778 12.46 2.1352
#: 55792 1.78811 12.46 2.1352
#: 1789803 1.73844 12.46 2.1352
#: 55791 1.68877 12.46 2.1352
#: 1789806 1.6391 12.46 2.1352
#: 55790 1.58943 12.46 2.1352
#: 1789809 1.53976 12.46 2.1352
#: 55789 1.49009 12.46 2.1352
#: 1789812 1.44042 12.46 2.1352
#: 55788 1.39075 12.46 2.1352
#: 1789815 1.34108 12.46 2.1352
#: 55787 1.29141 12.46 2.1352
#: 1789818 1.24174 12.46 2.1352
#: 55786 1.19207 12.46 2.1352
#: 1789821 1.1424 12.46 2.1352
#: 55785 1.09273 12.46 2.1352
#: 1789824 1.04306 12.46 2.1352
#: 55784 0.993393 12.46 2.1352
#: 1789827 0.943723 12.46 2.1352
#: 55783 0.894054 12.46 2.1352
#: 1789830 0.844384 12.46 2.1352
#: 55782 0.794714 12.46 2.1352
#: 1789833 0.745045 12.46 2.1352
#: 55781 0.695375 12.46 2.1352
#: 1789836 0.645705 12.46 2.1352
#: 55780 0.596036 12.46 2.1352
#: 1789839 0.546366 12.46 2.1352
#: 55779 0.496696 12.46 2.1352
#: 1789842 0.447027 12.46 2.1352
#: 55778 0.397357 12.46 2.1352
#: 1789845 0.347687 12.46 2.1352
#: 55777 0.298018 12.46 2.1352
#: 1789848 0.248348 12.46 2.1352
#: 55776 0.198679 12.46 2.1352
#: 1789851 0.149009 12.46 2.1352
#: 55775 0.0993393 12.46 2.1352
#: 1789854 0.0496696 12.46 2.1352
#: 1779 0.0 12.46 2.1352
#* TypeError: exceptions must be old-style classes or derived from 
#* BaseException, not NoneType
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 106, in <module>
#*     odb = 
#* BuildElementAndNodeSets(nContourLvls,SetPrefix,nodeLabelTip,crackFrontAxis,
#* odb,partInstance) #Move elements inside
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 97, 
#* in BuildElementAndNodeSets
#*     raise
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
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
#: time report
#: ++++++++++++
#: time in first loop 0.0390000343323
#: time in first loop get El 0.0110001564026
#: time in first loop get union 0.0170001983643
#: time in second loop 1.19899988174
#: time in third loop 0.0139999389648
#: ++++++++++++
#: ++++++++++++
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.8817, 
    farPlane=64.753, width=4.22314, height=1.98601, viewOffsetX=2.15893, 
    viewOffsetY=-3.58138)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.8601, 
    farPlane=64.7747, width=4.22085, height=1.98493, viewOffsetX=2.74524, 
    viewOffsetY=-3.31538)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.2148, 
    farPlane=64.42, width=0.122982, height=0.0578345, viewOffsetX=1.7389, 
    viewOffsetY=-3.75376)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=1.74943, 
    viewOffsetY=-3.78224)
cliCommand("""range(29)""")
#: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#* SyntaxError: ('invalid syntax', 
#* ('E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
#* 107, 114, 
#* '\tCalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,
#* SetPrefix,nodeLabelTip,isSymm,odb,partInstance): \n'))
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#* NameError: global name 'lastFrame' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1034, in CalculateDomainJIntegral
#*     TTAU = lastFrame.frameValue
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: Field variable  U  at position  NODAL  does not exists
#* NameError: global name 'currentFrame' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1037, in CalculateDomainJIntegral
#*     CheckFieldExists(frame,'U','NODAL') #displacements
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\Utilities.py", line 
#* 44, in CheckFieldExists
#*     field = currentFrame.fieldOutputs[fieldName].getSubset(position=NODAL)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: Field variable  U  at position  NODAL  does not exists
#* NameError: global name 'currentFrame' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1037, in CalculateDomainJIntegral
#*     CheckFieldExists(frame,'U','NODAL') #displacements
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\Utilities.py", line 
#* 44, in CheckFieldExists
#*     field = currentFrame.fieldOutputs[fieldName].getSubset(position=NODAL)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#* NameError: global name 'contour' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1048, in CalculateDomainJIntegral
#*     nSetSlice=SetPrefix+'-contour-'+str(contour)+'-slice-'+str(slice)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#* NameError: global name 'Coordinate_Nodal_to_Elemental_Nodal' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1075, in CalculateDomainJIntegral
#*     dudX,detJac,dudXElLabels = 
#* GetdudX(root,frame,allNodes,nSetSlice,elSetSlice)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 430, 
#* in GetdudX
#*     [ENCoord1,ECM]=Coordinate_Nodal_to_Elemental_Nodal(allNodes,0,elements)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#* IndexError: 0-d arrays can't be indexed.
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1076, in CalculateDomainJIntegral
#*     dudX,detJac,dudXElLabels = 
#* GetdudX(root,frame,allNodes,nSetSlice,elSetSlice)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 443, 
#* in GetdudX
#*     [NU1,ENU1,ECM]=ScalarField_Nodal_to_Elemental_Nodal(SFU1,0,elements)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\C3D20.py", line 217, 
#* in ScalarField_Nodal_to_Elemental_Nodal
#*     dataElementNodal, connectivityMat = 
#* Nodal_to_Elemental_Nodal(dataNodal,elements)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\C3D20.py", line 199, 
#* in Nodal_to_Elemental_Nodal
#*     dataElementNodal = dataNodal[connectivity]
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: 3.0
#* NameError: global name 'root' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1080, in CalculateDomainJIntegral
#*     
#* dqdX,intLcL,dudXElLabels=GetdqdX(root,frame,allNodes,nSetQ0,nSetQ0p5,nSetQ1,
#* nodeLabelTip,nSetSlice,elSetSlice,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 836, 
#* in GetdqdX
#*     
#* ENQ2,intLcL=GetqLinear(nSetQ0,nodeSetName,firstCrackNodeLabel,allNodes,
#* elSetName,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 503, 
#* in GetqLinear
#*     nodesQ0=root.nodeSets[nSetQ0].nodes[0] #Outside nodes
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: 3.0
#* NameError: global name 'math' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1080, in CalculateDomainJIntegral
#*     
#* dqdX,intLcL,dudXElLabels=GetdqdX(root,frame,allNodes,nSetQ0,nSetQ0p5,nSetQ1,
#* nodeLabelTip,nSetSlice,elSetSlice,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 836, 
#* in GetdqdX
#*     
#* ENQ2,intLcL=GetqLinear(nSetQ0,nodeSetName,firstCrackNodeLabel,root,allNodes,
#* elSetName,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 577, 
#* in GetqLinear
#*     thetab[i]=thetab[i]+2*math.pi
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: 3.0
#: [[ 0.0694092   0.07027512  0.07074966  0.07076866  0.07074272  0.07069308
#:    0.07062879  0.07054816  0.07045125  0.070337    0.07020277  0.07004711
#:    0.06986734  0.06966055  0.0694216   0.06914599  0.06882623  0.06845331
#:    0.06801617  0.06749892  0.06688236  0.06614221  0.06523784  0.06411565
#:    0.06268805  0.06079119  0.05809922  0.05342117  0.04548158]
#:  [ 0.          0.          0.          0.          0.          0.          0.
#:    0.          0.          0.          0.          0.          0.          0.
#:    0.          0.          0.          0.          0.          0.          0.
#:    0.          0.          0.          0.          0.          0.          0.
#:    0.        ]]
#: [[ 0.0694092   0.07027512  0.07074966  0.07076866  0.07074272  0.07069308
#:    0.07062879  0.07054816  0.07045125  0.070337    0.07020277  0.07004711
#:    0.06986734  0.06966055  0.0694216   0.06914599  0.06882623  0.06845331
#:    0.06801617  0.06749892  0.06688236  0.06614221  0.06523784  0.06411565
#:    0.06268805  0.06079119  0.05809922  0.05342117  0.04548158]
#:  [ 0.07368221  0.07353619  0.07402055  0.07404095  0.07401321  0.07396099
#:    0.07389275  0.07380741  0.07370519  0.07358487  0.07344395  0.07328047
#:    0.07309163  0.07287355  0.07262216  0.07233257  0.07199635  0.0716046
#:    0.07114479  0.07060142  0.06995393  0.06917604  0.0682266   0.06704759
#:    0.06554647  0.06355526  0.06071238  0.05581119  0.04837313]]
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
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
#: test-contour-1-slice-21
#: test-contour-1-slice-22
#: test-contour-1-slice-23
#: test-contour-1-slice-24
#: test-contour-1-slice-25
#: test-contour-1-slice-26
#: test-contour-1-slice-27
#: test-contour-1-slice-28
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
#: test-contour-2-slice-21
#: test-contour-2-slice-22
#: test-contour-2-slice-23
#: test-contour-2-slice-24
#: test-contour-2-slice-25
#: test-contour-2-slice-26
#: test-contour-2-slice-27
#: test-contour-2-slice-28
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
#: test-contour-3-slice-21
#: test-contour-3-slice-22
#: test-contour-3-slice-23
#: test-contour-3-slice-24
#: test-contour-3-slice-25
#: test-contour-3-slice-26
#: test-contour-3-slice-27
#: test-contour-3-slice-28
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
#: test-contour-4-slice-21
#: test-contour-4-slice-22
#: test-contour-4-slice-23
#: test-contour-4-slice-24
#: test-contour-4-slice-25
#: test-contour-4-slice-26
#: test-contour-4-slice-27
#: test-contour-4-slice-28
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
#: test-contour-5-slice-21
#: test-contour-5-slice-22
#: test-contour-5-slice-23
#: test-contour-5-slice-24
#: test-contour-5-slice-25
#: test-contour-5-slice-26
#: test-contour-5-slice-27
#: test-contour-5-slice-28
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
#: test-contour-6-slice-21
#: test-contour-6-slice-22
#: test-contour-6-slice-23
#: test-contour-6-slice-24
#: test-contour-6-slice-25
#: test-contour-6-slice-26
#: test-contour-6-slice-27
#: test-contour-6-slice-28
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
#: test-contour-7-slice-21
#: test-contour-7-slice-22
#: test-contour-7-slice-23
#: test-contour-7-slice-24
#: test-contour-7-slice-25
#: test-contour-7-slice-26
#: test-contour-7-slice-27
#: test-contour-7-slice-28
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
#: test-contour-8-slice-21
#: test-contour-8-slice-22
#: test-contour-8-slice-23
#: test-contour-8-slice-24
#: test-contour-8-slice-25
#: test-contour-8-slice-26
#: test-contour-8-slice-27
#: test-contour-8-slice-28
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
#: test-contour-9-slice-21
#: test-contour-9-slice-22
#: test-contour-9-slice-23
#: test-contour-9-slice-24
#: test-contour-9-slice-25
#: test-contour-9-slice-26
#: test-contour-9-slice-27
#: test-contour-9-slice-28
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
#: test-contour-10-slice-21
#: test-contour-10-slice-22
#: test-contour-10-slice-23
#: test-contour-10-slice-24
#: test-contour-10-slice-25
#: test-contour-10-slice-26
#: test-contour-10-slice-27
#: test-contour-10-slice-28
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
#: test-contour-11-slice-21
#: test-contour-11-slice-22
#: test-contour-11-slice-23
#: test-contour-11-slice-24
#: test-contour-11-slice-25
#: test-contour-11-slice-26
#: test-contour-11-slice-27
#: test-contour-11-slice-28
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
#: test-contour-12-slice-21
#: test-contour-12-slice-22
#: test-contour-12-slice-23
#: test-contour-12-slice-24
#: test-contour-12-slice-25
#: test-contour-12-slice-26
#: test-contour-12-slice-27
#: test-contour-12-slice-28
#: time report
#: ++++++++++++
#: time in first loop 0.697000026703
#: time in first loop get El 0.402998924255
#: time in first loop get union 0.110000371933
#: time in second loop 6.95799994469
#: time in third loop 0.111000061035
#: ++++++++++++
#: ++++++++++++
#* Command successfully aborted.
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1080, in CalculateDomainJIntegral
#*     
#* dqdX,intLcL,dudXElLabels=GetdqdX(root,frame,allNodes,nSetQ0,nSetQ0p5,nSetQ1,
#* nodeLabelTip,nSetSlice,elSetSlice,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 836, 
#* in GetdqdX
#*     
#* ENQ2,intLcL=GetqLinear(nSetQ0,nodeSetName,firstCrackNodeLabel,root,allNodes,
#* elSetName,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 577, 
#* in GetqLinear
#*     thetab[i]=thetab[i]+2*math.pi
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.93, 
    farPlane=64.7048, width=1.26034, height=0.983352, viewOffsetX=2.2084, 
    viewOffsetY=-3.32451)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.8778, 
    farPlane=64.757, width=1.2587, height=0.982067, viewOffsetX=1.86432, 
    viewOffsetY=-3.82275)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.1245, 
    farPlane=64.5103, width=0.394073, height=0.307465, viewOffsetX=1.7425, 
    viewOffsetY=-3.82043)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.118, 
    farPlane=64.5168, width=0.394008, height=0.307415, viewOffsetX=1.77363, 
    viewOffsetY=-3.7755)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.6223, 
    farPlane=65.2581, width=0.398962, height=0.31128, cameraPosition=(44.173, 
    33.8943, 31.6777), cameraUpVector=(-0.554189, 0.635506, -0.537593), 
    cameraTarget=(9.63934, 6.98822, 3.03157), viewOffsetX=1.79593, 
    viewOffsetY=-3.82296)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.621, 
    farPlane=65.2595, width=0.398949, height=0.31127, viewOffsetX=1.81314, 
    viewOffsetY=-3.88875)
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.5625, 
    farPlane=66.5824, width=0.447481, height=0.349136, cameraPosition=(63.147, 
    14.3047, 14.2963), cameraUpVector=(-0.377157, 0.85327, -0.360116), 
    cameraTarget=(12.3559, 7.77236, 3.58628), viewOffsetX=2.03371, 
    viewOffsetY=-4.36181)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: Processing Contour:  0
#* NameError: global name 'fobj' is not defined
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1086, in CalculateDomainJIntegral
#*     
#* dqdX,intLcL,slicePos[sliceCnt],dudXElLabels=GetdqdX(root,frame,allNodes,
#* nSetQ0,nSetQ0p5,nSetQ1,nodeLabelTip,nSetSlice,elSetSlice,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 841, 
#* in GetdqdX
#*     
#* ENQ2,intLcL,posz=GetqLinear(nSetQ0,nodeSetName,firstCrackNodeLabel,root,
#* allNodes,elSetName,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 660, 
#* in GetqLinear
#*     fobj.close()
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: Processing Contour:  0
#: Processing Contour:  1
#: Processing Contour:  2
#: Processing Contour:  3
#: Processing Contour:  4
#: Processing Contour:  5
#: Processing Contour:  6
#: Processing Contour:  7
#: Processing Contour:  8
#: Processing Contour:  9
#: Processing Contour:  10
#* FloatingPointError: divide by zero encountered in float_scalars
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1086, in CalculateDomainJIntegral
#*     
#* dqdX,intLcL,slicePos[sliceCnt],dudXElLabels=GetdqdX(root,frame,allNodes,
#* nSetQ0,nSetQ0p5,nSetQ1,nodeLabelTip,nSetSlice,elSetSlice,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 841, 
#* in GetdqdX
#*     
#* ENQ2,intLcL,posz=GetqLinear(nSetQ0,nodeSetName,firstCrackNodeLabel,root,
#* allNodes,elSetName,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 604, 
#* in GetqLinear
#*     mb.append((yb[i]-yb[i+1])/(xb[i]-xb[i+1]))
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: Processing Contour:  10
#: slice #: 0
#: 0 0.05024 0.05024 0.0 -0.00758076
#: 1 0.05024 0.05024 -0.00758076 -0.0151625
#: 2 0.05024 0.05024 -0.0151625 -0.0234118
#: 3 0.05024 0.05024 -0.0234118 -0.031662
#: 4 0.05024 0.05024 -0.031662 -0.0406389
#: 5 0.05024 0.05024 -0.0406389 -0.0496159
#: 6 0.05024 0.05024 -0.0496159 -0.0593843
#: 7 0.05024 0.05024 -0.0593843 -0.0691538
#: 8 0.05024 0.0376801 -0.0691538 -0.0691538
#* FloatingPointError: divide by zero encountered in float_scalars
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1087, in CalculateDomainJIntegral
#*     
#* dqdX,intLcL,slicePos[sliceCnt],dudXElLabels=GetdqdX(root,frame,allNodes,
#* nSetQ0,nSetQ0p5,nSetQ1,nodeLabelTip,nSetSlice,elSetSlice,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 841, 
#* in GetdqdX
#*     
#* ENQ2,intLcL,posz=GetqLinear(nSetQ0,nodeSetName,firstCrackNodeLabel,root,
#* allNodes,elSetName,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 604, 
#* in GetqLinear
#*     mb.append((yb[i]-yb[i+1])/(xb[i]-xb[i+1]))
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: Processing Contour:  10
#: slice #: 0
#: 0 0.05024 0.05024 0.0 -0.00758076
#: 1 0.05024 0.05024 -0.00758076 -0.0151625
#: 2 0.05024 0.05024 -0.0151625 -0.0234118
#: 3 0.05024 0.05024 -0.0234118 -0.031662
#: 4 0.05024 0.05024 -0.031662 -0.0406389
#: 5 0.05024 0.05024 -0.0406389 -0.0496159
#: 6 0.05024 0.05024 -0.0496159 -0.0593843
#: 7 0.05024 0.05024 -0.0593843 -0.0691538
#: 8 0.05024 0.0376801 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 10 0.02512 0.0220258 -0.0691538 -0.0747337
#: 11 0.0220258 0.0189316 -0.0747337 -0.0803137
#: 12 0.0189316 0.0157847 -0.0803137 -0.0842819
#: 13 0.0157847 0.0126379 -0.0842819 -0.0882502
#: 14 0.0126379 0.00950575 -0.0882502 -0.0909357
#: 15 0.00950575 0.00637341 -0.0909357 -0.0936213
#: 16 0.00637341 0.0031867 -0.0936213 -0.0943747
#: 17 0.0031867 0.0 -0.0943747 -0.0951271
#: 18 0.0 -0.00315881 -0.0951271 -0.0939579
#: 19 -0.00315881 -0.00631762 -0.0939579 -0.0927887
#: 20 -0.00631762 -0.00948238 -0.0927887 -0.0904884
#: 21 -0.00948238 -0.0126469 -0.0904884 -0.0881882
#: 22 -0.0126469 -0.0157919 -0.0881882 -0.0842257
#: 23 -0.0157919 -0.0189366 -0.0842257 -0.0802622
#: 24 -0.0189366 -0.0220284 -0.0802622 -0.074708
#: 25 -0.0220284 -0.02512 -0.074708 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 27 -0.0376801 -0.05024 -0.0691538 -0.0691538
#: 28 -0.05024 -0.05024 -0.0691538 -0.0593843
#: 29 -0.05024 -0.05024 -0.0593843 -0.0496159
#: 30 -0.05024 -0.05024 -0.0496159 -0.0406389
#: 31 -0.05024 -0.05024 -0.0406389 -0.031662
#: 32 -0.05024 -0.05024 -0.031662 -0.0234118
#: 33 -0.05024 -0.05024 -0.0234118 -0.0151625
#: 34 -0.05024 -0.05024 -0.0151625 -0.00758076
#: 35 -0.05024 -0.05024 -0.00758076 0.0
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: 0 0.05024 0.05024 0.0 -0.0153885
#: 1 0.05024 0.05024 -0.0153885 -0.0320902
#: 2 0.05024 0.05024 -0.0320902 -0.0502195
#: 3 0.05024 0.05024 -0.0502195 -0.0699053
#: 4 0.05024 0.02512 -0.0699053 -0.0704823
#: 5 0.02512 0.0189192 -0.0704823 -0.081809
#: 6 0.0189192 0.0126266 -0.081809 -0.0897284
#: 7 0.0126266 0.0063591 -0.0897284 -0.0951395
#: 8 0.0063591 0.0 -0.0951395 -0.0970201
#: 9 0.0 -0.00632811 -0.0970201 -0.0945578
#: 10 -0.00632811 -0.0126605 -0.0945578 -0.0899363
#: 11 -0.0126605 -0.0189462 -0.0899363 -0.0820303
#: 12 -0.0189462 -0.02512 -0.0820303 -0.0704823
#: 13 -0.02512 -0.05024 -0.0704823 -0.0699053
#: 14 -0.05024 -0.05024 -0.0699053 -0.0502195
#: 15 -0.05024 -0.05024 -0.0502195 -0.0320902
#: 16 -0.05024 -0.05024 -0.0320902 -0.0153885
#: 17 -0.05024 -0.05024 -0.0153885 0.0
#: 0 0.05024 0.05024 0.0 -0.00780773
#: 1 0.05024 0.05024 -0.00780773 -0.0156145
#: 2 0.05024 0.05024 -0.0156145 -0.024066
#: 3 0.05024 0.05024 -0.024066 -0.0325174
#: 4 0.05024 0.05024 -0.0325174 -0.0416708
#: 5 0.05024 0.05024 -0.0416708 -0.0508242
#: 6 0.05024 0.05024 -0.0508242 -0.0607405
#: 7 0.05024 0.05024 -0.0607405 -0.0706577
#: 8 0.05024 0.0376801 -0.0706577 -0.0712347
#: 9 0.0376801 0.02512 -0.0712347 -0.0718107
#: 10 0.02512 0.0220134 -0.0718107 -0.0775576
#: 11 0.0220134 0.0189068 -0.0775576 -0.0833035
#: 12 0.0189068 0.0157609 -0.0833035 -0.0872545
#: 13 0.0157609 0.0126152 -0.0872545 -0.0912066
#: 14 0.0126152 0.00948 -0.0912066 -0.0939322
#: 15 0.00948 0.00634503 -0.0939322 -0.0966578
#: 16 0.00634503 0.0031724 -0.0966578 -0.097785
#: 17 0.0031724 0.0 -0.097785 -0.0989122
#: 18 0.0 -0.00316954 -0.0989122 -0.0976191
#: 19 -0.00316954 -0.00633883 -0.0976191 -0.0963259
#: 20 -0.00633883 -0.00950623 -0.0963259 -0.0940046
#: 21 -0.00950623 -0.0126739 -0.0940046 -0.0916834
#: 22 -0.0126739 -0.0158148 -0.0916834 -0.0877409
#: 23 -0.0158148 -0.0189557 -0.0877409 -0.0837984
#: 24 -0.0189557 -0.022038 -0.0837984 -0.0778046
#: 25 -0.022038 -0.02512 -0.0778046 -0.0718107
#: 26 -0.02512 -0.0376801 -0.0718107 -0.0712347
#: 27 -0.0376801 -0.05024 -0.0712347 -0.0706577
#: 28 -0.05024 -0.05024 -0.0706577 -0.0607405
#: 29 -0.05024 -0.05024 -0.0607405 -0.0508242
#: 30 -0.05024 -0.05024 -0.0508242 -0.0416708
#: 31 -0.05024 -0.05024 -0.0416708 -0.0325174
#: 32 -0.05024 -0.05024 -0.0325174 -0.024066
#: 33 -0.05024 -0.05024 -0.024066 -0.0156145
#: 34 -0.05024 -0.05024 -0.0156145 -0.00780773
#: 35 -0.05024 -0.05024 -0.00780773 0.0
#: slice #: 1
#: 0 0.05024 0.05024 0.0 -0.00758076
#: 1 0.05024 0.05024 -0.00758076 -0.0151625
#: 2 0.05024 0.05024 -0.0151625 -0.0234118
#: 3 0.05024 0.05024 -0.0234118 -0.031662
#: 4 0.05024 0.05024 -0.031662 -0.0406389
#: 5 0.05024 0.05024 -0.0406389 -0.0496159
#: 6 0.05024 0.05024 -0.0496159 -0.0593843
#: 7 0.05024 0.05024 -0.0593843 -0.0691538
#: 8 0.05024 0.0376801 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 10 0.02512 0.0220258 -0.0691538 -0.0747337
#: 11 0.0220258 0.0189316 -0.0747337 -0.0803137
#: 12 0.0189316 0.0157847 -0.0803137 -0.0842819
#: 13 0.0157847 0.0126379 -0.0842819 -0.0882502
#: 14 0.0126379 0.00950575 -0.0882502 -0.0909357
#: 15 0.00950575 0.00637341 -0.0909357 -0.0936213
#: 16 0.00637341 0.0031867 -0.0936213 -0.0943747
#: 17 0.0031867 0.0 -0.0943747 -0.0951271
#: 18 0.0 -0.00315881 -0.0951271 -0.0939579
#: 19 -0.00315881 -0.00631762 -0.0939579 -0.0927887
#: 20 -0.00631762 -0.00948238 -0.0927887 -0.0904884
#: 21 -0.00948238 -0.0126469 -0.0904884 -0.0881882
#: 22 -0.0126469 -0.0157919 -0.0881882 -0.0842257
#: 23 -0.0157919 -0.0189366 -0.0842257 -0.0802622
#: 24 -0.0189366 -0.0220284 -0.0802622 -0.074708
#: 25 -0.0220284 -0.02512 -0.074708 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 27 -0.0376801 -0.05024 -0.0691538 -0.0691538
#: 28 -0.05024 -0.05024 -0.0691538 -0.0593843
#: 29 -0.05024 -0.05024 -0.0593843 -0.0496159
#: 30 -0.05024 -0.05024 -0.0496159 -0.0406389
#: 31 -0.05024 -0.05024 -0.0406389 -0.031662
#: 32 -0.05024 -0.05024 -0.031662 -0.0234118
#: 33 -0.05024 -0.05024 -0.0234118 -0.0151625
#: 34 -0.05024 -0.05024 -0.0151625 -0.00758076
#: 35 -0.05024 -0.05024 -0.00758076 0.0
#: 0 0.05024 0.05024 0.0 -0.0153885
#: 1 0.05024 0.05024 -0.0153885 -0.0320902
#: 2 0.05024 0.05024 -0.0320902 -0.0502195
#: 3 0.05024 0.05024 -0.0502195 -0.0699053
#: 4 0.05024 0.02512 -0.0699053 -0.0704823
#: 5 0.02512 0.0189192 -0.0704823 -0.081809
#: 6 0.0189192 0.0126266 -0.081809 -0.0897284
#: 7 0.0126266 0.0063591 -0.0897284 -0.0951395
#: 8 0.0063591 0.0 -0.0951395 -0.0970201
#: 9 0.0 -0.00632811 -0.0970201 -0.0945578
#: 10 -0.00632811 -0.0126605 -0.0945578 -0.0899363
#: 11 -0.0126605 -0.0189462 -0.0899363 -0.0820303
#: 12 -0.0189462 -0.02512 -0.0820303 -0.0704823
#: 13 -0.02512 -0.05024 -0.0704823 -0.0699053
#: 14 -0.05024 -0.05024 -0.0699053 -0.0502195
#: 15 -0.05024 -0.05024 -0.0502195 -0.0320902
#: 16 -0.05024 -0.05024 -0.0320902 -0.0153885
#: 17 -0.05024 -0.05024 -0.0153885 0.0
#: 0 0.05024 0.05024 0.0 -0.00780773
#: 1 0.05024 0.05024 -0.00780773 -0.0156145
#: 2 0.05024 0.05024 -0.0156145 -0.024066
#: 3 0.05024 0.05024 -0.024066 -0.0325174
#: 4 0.05024 0.05024 -0.0325174 -0.0416708
#: 5 0.05024 0.05024 -0.0416708 -0.0508242
#: 6 0.05024 0.05024 -0.0508242 -0.0607405
#: 7 0.05024 0.05024 -0.0607405 -0.0706577
#: 8 0.05024 0.0376801 -0.0706577 -0.0712347
#: 9 0.0376801 0.02512 -0.0712347 -0.0718107
#: 10 0.02512 0.0220134 -0.0718107 -0.0775576
#: 11 0.0220134 0.0189068 -0.0775576 -0.0833035
#: 12 0.0189068 0.0157609 -0.0833035 -0.0872545
#: 13 0.0157609 0.0126152 -0.0872545 -0.0912066
#: 14 0.0126152 0.00948 -0.0912066 -0.0939322
#: 15 0.00948 0.00634503 -0.0939322 -0.0966578
#: 16 0.00634503 0.0031724 -0.0966578 -0.097785
#: 17 0.0031724 0.0 -0.097785 -0.0989122
#: 18 0.0 -0.00316954 -0.0989122 -0.0976191
#: 19 -0.00316954 -0.00633883 -0.0976191 -0.0963259
#: 20 -0.00633883 -0.00950623 -0.0963259 -0.0940046
#: 21 -0.00950623 -0.0126739 -0.0940046 -0.0916834
#: 22 -0.0126739 -0.0158148 -0.0916834 -0.0877409
#: 23 -0.0158148 -0.0189557 -0.0877409 -0.0837984
#: 24 -0.0189557 -0.022038 -0.0837984 -0.0778046
#: 25 -0.022038 -0.02512 -0.0778046 -0.0718107
#: 26 -0.02512 -0.0376801 -0.0718107 -0.0712347
#: 27 -0.0376801 -0.05024 -0.0712347 -0.0706577
#: 28 -0.05024 -0.05024 -0.0706577 -0.0607405
#: 29 -0.05024 -0.05024 -0.0607405 -0.0508242
#: 30 -0.05024 -0.05024 -0.0508242 -0.0416708
#: 31 -0.05024 -0.05024 -0.0416708 -0.0325174
#: 32 -0.05024 -0.05024 -0.0325174 -0.024066
#: 33 -0.05024 -0.05024 -0.024066 -0.0156145
#: 34 -0.05024 -0.05024 -0.0156145 -0.00780773
#: 35 -0.05024 -0.05024 -0.00780773 0.0
#: 0 0.05024 0.05024 0.0 -0.0158396
#: 1 0.05024 0.05024 -0.0158396 -0.0329456
#: 2 0.05024 0.05024 -0.0329456 -0.0514288
#: 3 0.05024 0.05024 -0.0514288 -0.0714092
#: 4 0.05024 0.02512 -0.0714092 -0.0729227
#: 5 0.02512 0.0189333 -0.0729227 -0.0850859
#: 6 0.0189333 0.0126448 -0.0850859 -0.0930147
#: 7 0.0126448 0.00636935 -0.0930147 -0.0984564
#: 8 0.00636935 0.0 -0.0984564 -0.100526
#: 9 0.0 -0.0063529 -0.100526 -0.0979815
#: 10 -0.0063529 -0.0126967 -0.0979815 -0.0933447
#: 11 -0.0126967 -0.018975 -0.0933447 -0.0854311
#: 12 -0.018975 -0.02512 -0.0854311 -0.0729227
#: 13 -0.02512 -0.05024 -0.0729227 -0.0714092
#: 14 -0.05024 -0.05024 -0.0714092 -0.0514288
#: 15 -0.05024 -0.05024 -0.0514288 -0.0329456
#: 16 -0.05024 -0.05024 -0.0329456 -0.0158396
#: 17 -0.05024 -0.05024 -0.0158396 0.0
#: 0 0.05024 0.05024 0.0 -0.0080328
#: 1 0.05024 0.05024 -0.0080328 -0.0160656
#: 2 0.05024 0.05024 -0.0160656 -0.0247202
#: 3 0.05024 0.05024 -0.0247202 -0.0333738
#: 4 0.05024 0.05024 -0.0333738 -0.0427027
#: 5 0.05024 0.05024 -0.0427027 -0.0520325
#: 6 0.05024 0.05024 -0.0520325 -0.0620966
#: 7 0.05024 0.05024 -0.0620966 -0.0721607
#: 8 0.05024 0.0376801 -0.0721607 -0.0730972
#: 9 0.0376801 0.02512 -0.0730972 -0.0740337
#: 10 0.02512 0.0220399 -0.0740337 -0.080451
#: 11 0.0220399 0.01896 -0.080451 -0.0868692
#: 12 0.01896 0.0158172 -0.0868692 -0.0908461
#: 13 0.0158172 0.0126741 -0.0908461 -0.0948219
#: 14 0.0126741 0.00953388 -0.0948219 -0.0975389
#: 15 0.00953388 0.00639367 -0.0975389 -0.100255
#: 16 0.00639367 0.00319672 -0.100255 -0.101197
#: 17 0.00319672 0.0 -0.101197 -0.102139
#: 18 0.0 -0.0031836 -0.102139 -0.100888
#: 19 -0.0031836 -0.00636721 -0.100888 -0.099638
#: 20 -0.00636721 -0.00954342 -0.099638 -0.0973225
#: 21 -0.00954342 -0.0127199 -0.0973225 -0.0950069
#: 22 -0.0127199 -0.0158572 -0.0950069 -0.0910349
#: 23 -0.0158572 -0.0189943 -0.0910349 -0.0870628
#: 24 -0.0189943 -0.0220571 -0.0870628 -0.0805483
#: 25 -0.0220571 -0.02512 -0.0805483 -0.0740337
#: 26 -0.02512 -0.0376801 -0.0740337 -0.0730972
#: 27 -0.0376801 -0.05024 -0.0730972 -0.0721607
#: 28 -0.05024 -0.05024 -0.0721607 -0.0620966
#: 29 -0.05024 -0.05024 -0.0620966 -0.0520325
#: 30 -0.05024 -0.05024 -0.0520325 -0.0427027
#: 31 -0.05024 -0.05024 -0.0427027 -0.0333738
#: 32 -0.05024 -0.05024 -0.0333738 -0.0247202
#: 33 -0.05024 -0.05024 -0.0247202 -0.0160656
#: 34 -0.05024 -0.05024 -0.0160656 -0.0080328
#: 35 -0.05024 -0.05024 -0.0080328 0.0
#: slice #: 2
#: 0 0.05024 0.05024 0.0 -0.00780773
#: 1 0.05024 0.05024 -0.00780773 -0.0156145
#: 2 0.05024 0.05024 -0.0156145 -0.024066
#: 3 0.05024 0.05024 -0.024066 -0.0325174
#: 4 0.05024 0.05024 -0.0325174 -0.0416708
#: 5 0.05024 0.05024 -0.0416708 -0.0508242
#: 6 0.05024 0.05024 -0.0508242 -0.0607405
#: 7 0.05024 0.05024 -0.0607405 -0.0706577
#: 8 0.05024 0.0376801 -0.0706577 -0.0712347
#: 9 0.0376801 0.02512 -0.0712347 -0.0718107
#: 10 0.02512 0.0220134 -0.0718107 -0.0775576
#: 11 0.0220134 0.0189068 -0.0775576 -0.0833035
#: 12 0.0189068 0.0157609 -0.0833035 -0.0872545
#: 13 0.0157609 0.0126152 -0.0872545 -0.0912066
#: 14 0.0126152 0.00948 -0.0912066 -0.0939322
#: 15 0.00948 0.00634503 -0.0939322 -0.0966578
#: 16 0.00634503 0.0031724 -0.0966578 -0.097785
#: 17 0.0031724 0.0 -0.097785 -0.0989122
#: 18 0.0 -0.00316954 -0.0989122 -0.0976191
#: 19 -0.00316954 -0.00633883 -0.0976191 -0.0963259
#: 20 -0.00633883 -0.00950623 -0.0963259 -0.0940046
#: 21 -0.00950623 -0.0126739 -0.0940046 -0.0916834
#: 22 -0.0126739 -0.0158148 -0.0916834 -0.0877409
#: 23 -0.0158148 -0.0189557 -0.0877409 -0.0837984
#: 24 -0.0189557 -0.022038 -0.0837984 -0.0778046
#: 25 -0.022038 -0.02512 -0.0778046 -0.0718107
#: 26 -0.02512 -0.0376801 -0.0718107 -0.0712347
#: 27 -0.0376801 -0.05024 -0.0712347 -0.0706577
#: 28 -0.05024 -0.05024 -0.0706577 -0.0607405
#: 29 -0.05024 -0.05024 -0.0607405 -0.0508242
#: 30 -0.05024 -0.05024 -0.0508242 -0.0416708
#: 31 -0.05024 -0.05024 -0.0416708 -0.0325174
#: 32 -0.05024 -0.05024 -0.0325174 -0.024066
#: 33 -0.05024 -0.05024 -0.024066 -0.0156145
#: 34 -0.05024 -0.05024 -0.0156145 -0.00780773
#: 35 -0.05024 -0.05024 -0.00780773 0.0
#: 0 0.05024 0.05024 0.0 -0.0158396
#: 1 0.05024 0.05024 -0.0158396 -0.0329456
#: 2 0.05024 0.05024 -0.0329456 -0.0514288
#: 3 0.05024 0.05024 -0.0514288 -0.0714092
#: 4 0.05024 0.02512 -0.0714092 -0.0729227
#: 5 0.02512 0.0189333 -0.0729227 -0.0850859
#: 6 0.0189333 0.0126448 -0.0850859 -0.0930147
#: 7 0.0126448 0.00636935 -0.0930147 -0.0984564
#: 8 0.00636935 0.0 -0.0984564 -0.100526
#: 9 0.0 -0.0063529 -0.100526 -0.0979815
#: 10 -0.0063529 -0.0126967 -0.0979815 -0.0933447
#: 11 -0.0126967 -0.018975 -0.0933447 -0.0854311
#: 12 -0.018975 -0.02512 -0.0854311 -0.0729227
#: 13 -0.02512 -0.05024 -0.0729227 -0.0714092
#: 14 -0.05024 -0.05024 -0.0714092 -0.0514288
#: 15 -0.05024 -0.05024 -0.0514288 -0.0329456
#: 16 -0.05024 -0.05024 -0.0329456 -0.0158396
#: 17 -0.05024 -0.05024 -0.0158396 0.0
#: 0 0.05024 0.05024 0.0 -0.0080328
#: 1 0.05024 0.05024 -0.0080328 -0.0160656
#: 2 0.05024 0.05024 -0.0160656 -0.0247202
#: 3 0.05024 0.05024 -0.0247202 -0.0333738
#: 4 0.05024 0.05024 -0.0333738 -0.0427027
#: 5 0.05024 0.05024 -0.0427027 -0.0520325
#: 6 0.05024 0.05024 -0.0520325 -0.0620966
#: 7 0.05024 0.05024 -0.0620966 -0.0721607
#: 8 0.05024 0.0376801 -0.0721607 -0.0730972
#: 9 0.0376801 0.02512 -0.0730972 -0.0740337
#: 10 0.02512 0.0220399 -0.0740337 -0.080451
#: 11 0.0220399 0.01896 -0.080451 -0.0868692
#: 12 0.01896 0.0158172 -0.0868692 -0.0908461
#: 13 0.0158172 0.0126741 -0.0908461 -0.0948219
#: 14 0.0126741 0.00953388 -0.0948219 -0.0975389
#: 15 0.00953388 0.00639367 -0.0975389 -0.100255
#: 16 0.00639367 0.00319672 -0.100255 -0.101197
#: 17 0.00319672 0.0 -0.101197 -0.102139
#: 18 0.0 -0.0031836 -0.102139 -0.100888
#: 19 -0.0031836 -0.00636721 -0.100888 -0.099638
#: 20 -0.00636721 -0.00954342 -0.099638 -0.0973225
#: 21 -0.00954342 -0.0127199 -0.0973225 -0.0950069
#: 22 -0.0127199 -0.0158572 -0.0950069 -0.0910349
#: 23 -0.0158572 -0.0189943 -0.0910349 -0.0870628
#: 24 -0.0189943 -0.0220571 -0.0870628 -0.0805483
#: 25 -0.0220571 -0.02512 -0.0805483 -0.0740337
#: 26 -0.02512 -0.0376801 -0.0740337 -0.0730972
#: 27 -0.0376801 -0.05024 -0.0730972 -0.0721607
#: 28 -0.05024 -0.05024 -0.0721607 -0.0620966
#: 29 -0.05024 -0.05024 -0.0620966 -0.0520325
#: 30 -0.05024 -0.05024 -0.0520325 -0.0427027
#: 31 -0.05024 -0.05024 -0.0427027 -0.0333738
#: 32 -0.05024 -0.05024 -0.0333738 -0.0247202
#: 33 -0.05024 -0.05024 -0.0247202 -0.0160656
#: 34 -0.05024 -0.05024 -0.0160656 -0.0080328
#: 35 -0.05024 -0.05024 -0.0080328 0.0
#: 0 0.05024 0.05024 0.0 -0.0162916
#: 1 0.05024 0.05024 -0.0162916 -0.0338011
#: 2 0.05024 0.05024 -0.0338011 -0.0526361
#: 3 0.05024 0.05024 -0.0526361 -0.0729132
#: 4 0.05024 0.02512 -0.0729132 -0.0751448
#: 5 0.02512 0.0189848 -0.0751448 -0.0885382
#: 6 0.0189848 0.0127046 -0.0885382 -0.0965357
#: 7 0.0127046 0.00641584 -0.0965357 -0.101935
#: 8 0.00641584 0.0 -0.101935 -0.103722
#: 9 0.0 -0.00637722 -0.103722 -0.101151
#: 10 -0.00637722 -0.0127358 -0.101151 -0.0964651
#: 11 -0.0127358 -0.0190072 -0.0964651 -0.0885019
#: 12 -0.0190072 -0.02512 -0.0885019 -0.0751448
#: 13 -0.02512 -0.05024 -0.0751448 -0.0729132
#: 14 -0.05024 -0.05024 -0.0729132 -0.0526361
#: 15 -0.05024 -0.05024 -0.0526361 -0.0338011
#: 16 -0.05024 -0.05024 -0.0338011 -0.0162916
#: 17 -0.05024 -0.05024 -0.0162916 0.0
#: 0 0.05024 0.05024 0.0 -0.00825882
#: 1 0.05024 0.05024 -0.00825882 -0.0165176
#: 2 0.05024 0.05024 -0.0165176 -0.0253735
#: 3 0.05024 0.05024 -0.0253735 -0.0342293
#: 4 0.05024 0.05024 -0.0342293 -0.0437346
#: 5 0.05024 0.05024 -0.0437346 -0.0532398
#: 6 0.05024 0.05024 -0.0532398 -0.0634527
#: 7 0.05024 0.05024 -0.0634527 -0.0736647
#: 8 0.05024 0.0376801 -0.0736647 -0.0749607
#: 9 0.0376801 0.02512 -0.0749607 -0.0762568
#: 10 0.02512 0.0220647 -0.0762568 -0.0832319
#: 11 0.0220647 0.0190096 -0.0832319 -0.0902081
#: 12 0.0190096 0.0158725 -0.0902081 -0.0942278
#: 13 0.0158725 0.0127351 -0.0942278 -0.0982485
#: 14 0.0127351 0.00958681 -0.0982485 -0.100932
#: 15 0.00958681 0.00643826 -0.100932 -0.103617
#: 16 0.00643826 0.00321913 -0.103617 -0.104461
#: 17 0.00321913 0.0 -0.104461 -0.105304
#: 18 0.0 -0.00319338 -0.105304 -0.103985
#: 19 -0.00319338 -0.006387 -0.103985 -0.102666
#: 20 -0.006387 -0.00956941 -0.102666 -0.100295
#: 21 -0.00956941 -0.0127518 -0.100295 -0.0979233
#: 22 -0.0127518 -0.0158858 -0.0979233 -0.0939322
#: 23 -0.0158858 -0.0190198 -0.0939322 -0.089941
#: 24 -0.0190198 -0.0220699 -0.089941 -0.0830984
#: 25 -0.0220699 -0.02512 -0.0830984 -0.0762568
#: 26 -0.02512 -0.0376801 -0.0762568 -0.0749607
#: 27 -0.0376801 -0.05024 -0.0749607 -0.0736647
#: 28 -0.05024 -0.05024 -0.0736647 -0.0634527
#: 29 -0.05024 -0.05024 -0.0634527 -0.0532398
#: 30 -0.05024 -0.05024 -0.0532398 -0.0437346
#: 31 -0.05024 -0.05024 -0.0437346 -0.0342293
#: 32 -0.05024 -0.05024 -0.0342293 -0.0253735
#: 33 -0.05024 -0.05024 -0.0253735 -0.0165176
#: 34 -0.05024 -0.05024 -0.0165176 -0.00825882
#: 35 -0.05024 -0.05024 -0.00825882 0.0
#: slice #: 3
#: 0 0.05024 0.05024 0.0 -0.0080328
#: 1 0.05024 0.05024 -0.0080328 -0.0160656
#: 2 0.05024 0.05024 -0.0160656 -0.0247202
#: 3 0.05024 0.05024 -0.0247202 -0.0333738
#: 4 0.05024 0.05024 -0.0333738 -0.0427027
#: 5 0.05024 0.05024 -0.0427027 -0.0520325
#: 6 0.05024 0.05024 -0.0520325 -0.0620966
#: 7 0.05024 0.05024 -0.0620966 -0.0721607
#: 8 0.05024 0.0376801 -0.0721607 -0.0730972
#: 9 0.0376801 0.02512 -0.0730972 -0.0740337
#: 10 0.02512 0.0220399 -0.0740337 -0.080451
#: 11 0.0220399 0.01896 -0.080451 -0.0868692
#: 12 0.01896 0.0158172 -0.0868692 -0.0908461
#: 13 0.0158172 0.0126741 -0.0908461 -0.0948219
#: 14 0.0126741 0.00953388 -0.0948219 -0.0975389
#: 15 0.00953388 0.00639367 -0.0975389 -0.100255
#: 16 0.00639367 0.00319672 -0.100255 -0.101197
#: 17 0.00319672 0.0 -0.101197 -0.102139
#: 18 0.0 -0.0031836 -0.102139 -0.100888
#: 19 -0.0031836 -0.00636721 -0.100888 -0.099638
#: 20 -0.00636721 -0.00954342 -0.099638 -0.0973225
#: 21 -0.00954342 -0.0127199 -0.0973225 -0.0950069
#: 22 -0.0127199 -0.0158572 -0.0950069 -0.0910349
#: 23 -0.0158572 -0.0189943 -0.0910349 -0.0870628
#: 24 -0.0189943 -0.0220571 -0.0870628 -0.0805483
#: 25 -0.0220571 -0.02512 -0.0805483 -0.0740337
#: 26 -0.02512 -0.0376801 -0.0740337 -0.0730972
#: 27 -0.0376801 -0.05024 -0.0730972 -0.0721607
#: 28 -0.05024 -0.05024 -0.0721607 -0.0620966
#: 29 -0.05024 -0.05024 -0.0620966 -0.0520325
#: 30 -0.05024 -0.05024 -0.0520325 -0.0427027
#: 31 -0.05024 -0.05024 -0.0427027 -0.0333738
#: 32 -0.05024 -0.05024 -0.0333738 -0.0247202
#: 33 -0.05024 -0.05024 -0.0247202 -0.0160656
#: 34 -0.05024 -0.05024 -0.0160656 -0.0080328
#: 35 -0.05024 -0.05024 -0.0080328 0.0
#: 0 0.05024 0.05024 0.0 -0.0162916
#: 1 0.05024 0.05024 -0.0162916 -0.0338011
#: 2 0.05024 0.05024 -0.0338011 -0.0526361
#: 3 0.05024 0.05024 -0.0526361 -0.0729132
#: 4 0.05024 0.02512 -0.0729132 -0.0751448
#: 5 0.02512 0.0189848 -0.0751448 -0.0885382
#: 6 0.0189848 0.0127046 -0.0885382 -0.0965357
#: 7 0.0127046 0.00641584 -0.0965357 -0.101935
#: 8 0.00641584 0.0 -0.101935 -0.103722
#: 9 0.0 -0.00637722 -0.103722 -0.101151
#: 10 -0.00637722 -0.0127358 -0.101151 -0.0964651
#: 11 -0.0127358 -0.0190072 -0.0964651 -0.0885019
#: 12 -0.0190072 -0.02512 -0.0885019 -0.0751448
#: 13 -0.02512 -0.05024 -0.0751448 -0.0729132
#: 14 -0.05024 -0.05024 -0.0729132 -0.0526361
#: 15 -0.05024 -0.05024 -0.0526361 -0.0338011
#: 16 -0.05024 -0.05024 -0.0338011 -0.0162916
#: 17 -0.05024 -0.05024 -0.0162916 0.0
#: 0 0.05024 0.05024 0.0 -0.00825882
#: 1 0.05024 0.05024 -0.00825882 -0.0165176
#: 2 0.05024 0.05024 -0.0165176 -0.0253735
#: 3 0.05024 0.05024 -0.0253735 -0.0342293
#: 4 0.05024 0.05024 -0.0342293 -0.0437346
#: 5 0.05024 0.05024 -0.0437346 -0.0532398
#: 6 0.05024 0.05024 -0.0532398 -0.0634527
#: 7 0.05024 0.05024 -0.0634527 -0.0736647
#: 8 0.05024 0.0376801 -0.0736647 -0.0749607
#: 9 0.0376801 0.02512 -0.0749607 -0.0762568
#: 10 0.02512 0.0220647 -0.0762568 -0.0832319
#: 11 0.0220647 0.0190096 -0.0832319 -0.0902081
#: 12 0.0190096 0.0158725 -0.0902081 -0.0942278
#: 13 0.0158725 0.0127351 -0.0942278 -0.0982485
#: 14 0.0127351 0.00958681 -0.0982485 -0.100932
#: 15 0.00958681 0.00643826 -0.100932 -0.103617
#: 16 0.00643826 0.00321913 -0.103617 -0.104461
#: 17 0.00321913 0.0 -0.104461 -0.105304
#: 18 0.0 -0.00319338 -0.105304 -0.103985
#: 19 -0.00319338 -0.006387 -0.103985 -0.102666
#: 20 -0.006387 -0.00956941 -0.102666 -0.100295
#: 21 -0.00956941 -0.0127518 -0.100295 -0.0979233
#: 22 -0.0127518 -0.0158858 -0.0979233 -0.0939322
#: 23 -0.0158858 -0.0190198 -0.0939322 -0.089941
#: 24 -0.0190198 -0.0220699 -0.089941 -0.0830984
#: 25 -0.0220699 -0.02512 -0.0830984 -0.0762568
#: 26 -0.02512 -0.0376801 -0.0762568 -0.0749607
#: 27 -0.0376801 -0.05024 -0.0749607 -0.0736647
#: 28 -0.05024 -0.05024 -0.0736647 -0.0634527
#: 29 -0.05024 -0.05024 -0.0634527 -0.0532398
#: 30 -0.05024 -0.05024 -0.0532398 -0.0437346
#: 31 -0.05024 -0.05024 -0.0437346 -0.0342293
#: 32 -0.05024 -0.05024 -0.0342293 -0.0253735
#: 33 -0.05024 -0.05024 -0.0253735 -0.0165176
#: 34 -0.05024 -0.05024 -0.0165176 -0.00825882
#: 35 -0.05024 -0.05024 -0.00825882 0.0
#: 0 0.05024 0.05024 0.0 -0.0167437
#: 1 0.05024 0.05024 -0.0167437 -0.0346575
#: 2 0.05024 0.05024 -0.0346575 -0.0538435
#: 3 0.05024 0.05024 -0.0538435 -0.0744162
#: 4 0.05024 0.02512 -0.0744162 -0.0773687
#: 5 0.02512 0.0190203 -0.0773687 -0.0916204
#: 6 0.0190203 0.0127499 -0.0916204 -0.099679
#: 7 0.0127499 0.00644684 -0.099679 -0.105052
#: 8 0.00644684 0.0 -0.105052 -0.106876
#: 9 0.0 -0.00639248 -0.106876 -0.104074
#: 10 -0.00639248 -0.0127602 -0.104074 -0.0992231
#: 11 -0.0127602 -0.019026 -0.0992231 -0.0912466
#: 12 -0.019026 -0.02512 -0.0912466 -0.0773687
#: 13 -0.02512 -0.05024 -0.0773687 -0.0744162
#: 14 -0.05024 -0.05024 -0.0744162 -0.0538435
#: 15 -0.05024 -0.05024 -0.0538435 -0.0346575
#: 16 -0.05024 -0.05024 -0.0346575 -0.0167437
#: 17 -0.05024 -0.05024 -0.0167437 0.0
#: 0 0.05024 0.05024 0.0 -0.00848484
#: 1 0.05024 0.05024 -0.00848484 -0.0169697
#: 2 0.05024 0.05024 -0.0169697 -0.0260267
#: 3 0.05024 0.05024 -0.0260267 -0.0350847
#: 4 0.05024 0.05024 -0.0350847 -0.0447664
#: 5 0.05024 0.05024 -0.0447664 -0.0544481
#: 6 0.05024 0.05024 -0.0544481 -0.0648079
#: 7 0.05024 0.05024 -0.0648079 -0.0751677
#: 8 0.05024 0.0376801 -0.0751677 -0.0768232
#: 9 0.0376801 0.02512 -0.0768232 -0.0784798
#: 10 0.02512 0.0220757 -0.0784798 -0.0857573
#: 11 0.0220757 0.019031 -0.0857573 -0.0930338
#: 12 0.019031 0.0158978 -0.0930338 -0.0970716
#: 13 0.0158978 0.0127647 -0.0970716 -0.101109
#: 14 0.0127647 0.00961018 -0.101109 -0.103798
#: 15 0.00961018 0.00645566 -0.103798 -0.106487
#: 16 0.00645566 0.00322771 -0.106487 -0.107469
#: 17 0.00322771 0.0 -0.107469 -0.108449
#: 18 0.0 -0.0031991 -0.108449 -0.106965
#: 19 -0.0031991 -0.00639796 -0.106965 -0.105482
#: 20 -0.00639796 -0.00958323 -0.105482 -0.103003
#: 21 -0.00958323 -0.0127685 -0.103003 -0.100523
#: 22 -0.0127685 -0.0159004 -0.100523 -0.0965376
#: 23 -0.0159004 -0.0190322 -0.0965376 -0.0925531
#: 24 -0.0190322 -0.0220761 -0.0925531 -0.0855169
#: 25 -0.0220761 -0.02512 -0.0855169 -0.0784798
#: 26 -0.02512 -0.0376801 -0.0784798 -0.0768232
#: 27 -0.0376801 -0.05024 -0.0768232 -0.0751677
#: 28 -0.05024 -0.05024 -0.0751677 -0.0648079
#: 29 -0.05024 -0.05024 -0.0648079 -0.0544481
#: 30 -0.05024 -0.05024 -0.0544481 -0.0447664
#: 31 -0.05024 -0.05024 -0.0447664 -0.0350847
#: 32 -0.05024 -0.05024 -0.0350847 -0.0260267
#: 33 -0.05024 -0.05024 -0.0260267 -0.0169697
#: 34 -0.05024 -0.05024 -0.0169697 -0.00848484
#: 35 -0.05024 -0.05024 -0.00848484 0.0
#: slice #: 4
#: 0 0.05024 0.05024 0.0 -0.00825882
#: 1 0.05024 0.05024 -0.00825882 -0.0165176
#: 2 0.05024 0.05024 -0.0165176 -0.0253735
#: 3 0.05024 0.05024 -0.0253735 -0.0342293
#: 4 0.05024 0.05024 -0.0342293 -0.0437346
#: 5 0.05024 0.05024 -0.0437346 -0.0532398
#: 6 0.05024 0.05024 -0.0532398 -0.0634527
#: 7 0.05024 0.05024 -0.0634527 -0.0736647
#: 8 0.05024 0.0376801 -0.0736647 -0.0749607
#: 9 0.0376801 0.02512 -0.0749607 -0.0762568
#: 10 0.02512 0.0220647 -0.0762568 -0.0832319
#: 11 0.0220647 0.0190096 -0.0832319 -0.0902081
#: 12 0.0190096 0.0158725 -0.0902081 -0.0942278
#: 13 0.0158725 0.0127351 -0.0942278 -0.0982485
#: 14 0.0127351 0.00958681 -0.0982485 -0.100932
#: 15 0.00958681 0.00643826 -0.100932 -0.103617
#: 16 0.00643826 0.00321913 -0.103617 -0.104461
#: 17 0.00321913 0.0 -0.104461 -0.105304
#: 18 0.0 -0.00319338 -0.105304 -0.103985
#: 19 -0.00319338 -0.006387 -0.103985 -0.102666
#: 20 -0.006387 -0.00956941 -0.102666 -0.100295
#: 21 -0.00956941 -0.0127518 -0.100295 -0.0979233
#: 22 -0.0127518 -0.0158858 -0.0979233 -0.0939322
#: 23 -0.0158858 -0.0190198 -0.0939322 -0.089941
#: 24 -0.0190198 -0.0220699 -0.089941 -0.0830984
#: 25 -0.0220699 -0.02512 -0.0830984 -0.0762568
#: 26 -0.02512 -0.0376801 -0.0762568 -0.0749607
#: 27 -0.0376801 -0.05024 -0.0749607 -0.0736647
#: 28 -0.05024 -0.05024 -0.0736647 -0.0634527
#: 29 -0.05024 -0.05024 -0.0634527 -0.0532398
#: 30 -0.05024 -0.05024 -0.0532398 -0.0437346
#: 31 -0.05024 -0.05024 -0.0437346 -0.0342293
#: 32 -0.05024 -0.05024 -0.0342293 -0.0253735
#: 33 -0.05024 -0.05024 -0.0253735 -0.0165176
#: 34 -0.05024 -0.05024 -0.0165176 -0.00825882
#: 35 -0.05024 -0.05024 -0.00825882 0.0
#: 0 0.05024 0.05024 0.0 -0.0167437
#: 1 0.05024 0.05024 -0.0167437 -0.0346575
#: 2 0.05024 0.05024 -0.0346575 -0.0538435
#: 3 0.05024 0.05024 -0.0538435 -0.0744162
#: 4 0.05024 0.02512 -0.0744162 -0.0773687
#: 5 0.02512 0.0190203 -0.0773687 -0.0916204
#: 6 0.0190203 0.0127499 -0.0916204 -0.099679
#: 7 0.0127499 0.00644684 -0.099679 -0.105052
#: 8 0.00644684 0.0 -0.105052 -0.106876
#: 9 0.0 -0.00639248 -0.106876 -0.104074
#: 10 -0.00639248 -0.0127602 -0.104074 -0.0992231
#: 11 -0.0127602 -0.019026 -0.0992231 -0.0912466
#: 12 -0.019026 -0.02512 -0.0912466 -0.0773687
#: 13 -0.02512 -0.05024 -0.0773687 -0.0744162
#: 14 -0.05024 -0.05024 -0.0744162 -0.0538435
#: 15 -0.05024 -0.05024 -0.0538435 -0.0346575
#: 16 -0.05024 -0.05024 -0.0346575 -0.0167437
#: 17 -0.05024 -0.05024 -0.0167437 0.0
#: 0 0.05024 0.05024 0.0 -0.00848484
#: 1 0.05024 0.05024 -0.00848484 -0.0169697
#: 2 0.05024 0.05024 -0.0169697 -0.0260267
#: 3 0.05024 0.05024 -0.0260267 -0.0350847
#: 4 0.05024 0.05024 -0.0350847 -0.0447664
#: 5 0.05024 0.05024 -0.0447664 -0.0544481
#: 6 0.05024 0.05024 -0.0544481 -0.0648079
#: 7 0.05024 0.05024 -0.0648079 -0.0751677
#: 8 0.05024 0.0376801 -0.0751677 -0.0768232
#: 9 0.0376801 0.02512 -0.0768232 -0.0784798
#: 10 0.02512 0.0220757 -0.0784798 -0.0857573
#: 11 0.0220757 0.019031 -0.0857573 -0.0930338
#: 12 0.019031 0.0158978 -0.0930338 -0.0970716
#: 13 0.0158978 0.0127647 -0.0970716 -0.101109
#: 14 0.0127647 0.00961018 -0.101109 -0.103798
#: 15 0.00961018 0.00645566 -0.103798 -0.106487
#: 16 0.00645566 0.00322771 -0.106487 -0.107469
#: 17 0.00322771 0.0 -0.107469 -0.108449
#: 18 0.0 -0.0031991 -0.108449 -0.106965
#: 19 -0.0031991 -0.00639796 -0.106965 -0.105482
#: 20 -0.00639796 -0.00958323 -0.105482 -0.103003
#: 21 -0.00958323 -0.0127685 -0.103003 -0.100523
#: 22 -0.0127685 -0.0159004 -0.100523 -0.0965376
#: 23 -0.0159004 -0.0190322 -0.0965376 -0.0925531
#: 24 -0.0190322 -0.0220761 -0.0925531 -0.0855169
#: 25 -0.0220761 -0.02512 -0.0855169 -0.0784798
#: 26 -0.02512 -0.0376801 -0.0784798 -0.0768232
#: 27 -0.0376801 -0.05024 -0.0768232 -0.0751677
#: 28 -0.05024 -0.05024 -0.0751677 -0.0648079
#: 29 -0.05024 -0.05024 -0.0648079 -0.0544481
#: 30 -0.05024 -0.05024 -0.0544481 -0.0447664
#: 31 -0.05024 -0.05024 -0.0447664 -0.0350847
#: 32 -0.05024 -0.05024 -0.0350847 -0.0260267
#: 33 -0.05024 -0.05024 -0.0260267 -0.0169697
#: 34 -0.05024 -0.05024 -0.0169697 -0.00848484
#: 35 -0.05024 -0.05024 -0.00848484 0.0
#: 0 0.05024 0.05024 0.0 -0.0171957
#: 1 0.05024 0.05024 -0.0171957 -0.0355129
#: 2 0.05024 0.05024 -0.0355129 -0.0550518
#: 3 0.05024 0.05024 -0.0550518 -0.0759192
#: 4 0.05024 0.02512 -0.0759192 -0.0795908
#: 5 0.02512 0.0190334 -0.0795908 -0.0942717
#: 6 0.0190334 0.0127683 -0.0942717 -0.102324
#: 7 0.0127683 0.00645709 -0.102324 -0.107774
#: 8 0.00645709 0.0 -0.107774 -0.110018
#: 9 0.0 -0.00640059 -0.110018 -0.106829
#: 10 -0.00640059 -0.0127721 -0.106829 -0.101732
#: 11 -0.0127721 -0.0190349 -0.101732 -0.0937891
#: 12 -0.0190349 -0.02512 -0.0937891 -0.0795908
#: 13 -0.02512 -0.05024 -0.0795908 -0.0759192
#: 14 -0.05024 -0.05024 -0.0759192 -0.0550518
#: 15 -0.05024 -0.05024 -0.0550518 -0.0355129
#: 16 -0.05024 -0.05024 -0.0355129 -0.0171957
#: 17 -0.05024 -0.05024 -0.0171957 0.0
#: 0 0.05024 0.05024 0.0 -0.00871086
#: 1 0.05024 0.05024 -0.00871086 -0.0174217
#: 2 0.05024 0.05024 -0.0174217 -0.0266809
#: 3 0.05024 0.05024 -0.0266809 -0.0359411
#: 4 0.05024 0.05024 -0.0359411 -0.0457983
#: 5 0.05024 0.05024 -0.0457983 -0.0556555
#: 6 0.05024 0.05024 -0.0556555 -0.0661631
#: 7 0.05024 0.05024 -0.0661631 -0.0766716
#: 8 0.05024 0.0376801 -0.0766716 -0.0786867
#: 9 0.0376801 0.02512 -0.0786867 -0.0807028
#: 10 0.02512 0.0220778 -0.0807028 -0.0881052
#: 11 0.0220778 0.0190356 -0.0881052 -0.0955086
#: 12 0.0190356 0.0159037 -0.0955086 -0.0995245
#: 13 0.0159037 0.0127718 -0.0995245 -0.103539
#: 14 0.0127718 0.00961518 -0.103539 -0.106299
#: 15 0.00961518 0.00645852 -0.106299 -0.109059
#: 16 0.00645852 0.00322914 -0.109059 -0.110323
#: 17 0.00322914 0.0 -0.110323 -0.111587
#: 18 0.0 -0.00320148 -0.111587 -0.109881
#: 19 -0.00320148 -0.00640321 -0.109881 -0.108175
#: 20 -0.00640321 -0.00958967 -0.108175 -0.105558
#: 21 -0.00958967 -0.0127759 -0.105558 -0.102942
#: 22 -0.0127759 -0.0159068 -0.102942 -0.0989828
#: 23 -0.0159068 -0.0190375 -0.0989828 -0.0950241
#: 24 -0.0190375 -0.0220788 -0.0950241 -0.087863
#: 25 -0.0220788 -0.02512 -0.087863 -0.0807028
#: 26 -0.02512 -0.0376801 -0.0807028 -0.0786867
#: 27 -0.0376801 -0.05024 -0.0786867 -0.0766716
#: 28 -0.05024 -0.05024 -0.0766716 -0.0661631
#: 29 -0.05024 -0.05024 -0.0661631 -0.0556555
#: 30 -0.05024 -0.05024 -0.0556555 -0.0457983
#: 31 -0.05024 -0.05024 -0.0457983 -0.0359411
#: 32 -0.05024 -0.05024 -0.0359411 -0.0266809
#: 33 -0.05024 -0.05024 -0.0266809 -0.0174217
#: 34 -0.05024 -0.05024 -0.0174217 -0.00871086
#: 35 -0.05024 -0.05024 -0.00871086 0.0
#: slice #: 5
#: 0 0.05024 0.05024 0.0 -0.00848484
#: 1 0.05024 0.05024 -0.00848484 -0.0169697
#: 2 0.05024 0.05024 -0.0169697 -0.0260267
#: 3 0.05024 0.05024 -0.0260267 -0.0350847
#: 4 0.05024 0.05024 -0.0350847 -0.0447664
#: 5 0.05024 0.05024 -0.0447664 -0.0544481
#: 6 0.05024 0.05024 -0.0544481 -0.0648079
#: 7 0.05024 0.05024 -0.0648079 -0.0751677
#: 8 0.05024 0.0376801 -0.0751677 -0.0768232
#: 9 0.0376801 0.02512 -0.0768232 -0.0784798
#: 10 0.02512 0.0220757 -0.0784798 -0.0857573
#: 11 0.0220757 0.019031 -0.0857573 -0.0930338
#: 12 0.019031 0.0158978 -0.0930338 -0.0970716
#: 13 0.0158978 0.0127647 -0.0970716 -0.101109
#: 14 0.0127647 0.00961018 -0.101109 -0.103798
#: 15 0.00961018 0.00645566 -0.103798 -0.106487
#: 16 0.00645566 0.00322771 -0.106487 -0.107469
#: 17 0.00322771 0.0 -0.107469 -0.108449
#: 18 0.0 -0.0031991 -0.108449 -0.106965
#: 19 -0.0031991 -0.00639796 -0.106965 -0.105482
#: 20 -0.00639796 -0.00958323 -0.105482 -0.103003
#: 21 -0.00958323 -0.0127685 -0.103003 -0.100523
#: 22 -0.0127685 -0.0159004 -0.100523 -0.0965376
#: 23 -0.0159004 -0.0190322 -0.0965376 -0.0925531
#: 24 -0.0190322 -0.0220761 -0.0925531 -0.0855169
#: 25 -0.0220761 -0.02512 -0.0855169 -0.0784798
#: 26 -0.02512 -0.0376801 -0.0784798 -0.0768232
#: 27 -0.0376801 -0.05024 -0.0768232 -0.0751677
#: 28 -0.05024 -0.05024 -0.0751677 -0.0648079
#: 29 -0.05024 -0.05024 -0.0648079 -0.0544481
#: 30 -0.05024 -0.05024 -0.0544481 -0.0447664
#: 31 -0.05024 -0.05024 -0.0447664 -0.0350847
#: 32 -0.05024 -0.05024 -0.0350847 -0.0260267
#: 33 -0.05024 -0.05024 -0.0260267 -0.0169697
#: 34 -0.05024 -0.05024 -0.0169697 -0.00848484
#: 35 -0.05024 -0.05024 -0.00848484 0.0
#: 0 0.05024 0.05024 0.0 -0.0171957
#: 1 0.05024 0.05024 -0.0171957 -0.0355129
#: 2 0.05024 0.05024 -0.0355129 -0.0550518
#: 3 0.05024 0.05024 -0.0550518 -0.0759192
#: 4 0.05024 0.02512 -0.0759192 -0.0795908
#: 5 0.02512 0.0190334 -0.0795908 -0.0942717
#: 6 0.0190334 0.0127683 -0.0942717 -0.102324
#: 7 0.0127683 0.00645709 -0.102324 -0.107774
#: 8 0.00645709 0.0 -0.107774 -0.110018
#: 9 0.0 -0.00640059 -0.110018 -0.106829
#: 10 -0.00640059 -0.0127721 -0.106829 -0.101732
#: 11 -0.0127721 -0.0190349 -0.101732 -0.0937891
#: 12 -0.0190349 -0.02512 -0.0937891 -0.0795908
#: 13 -0.02512 -0.05024 -0.0795908 -0.0759192
#: 14 -0.05024 -0.05024 -0.0759192 -0.0550518
#: 15 -0.05024 -0.05024 -0.0550518 -0.0355129
#: 16 -0.05024 -0.05024 -0.0355129 -0.0171957
#: 17 -0.05024 -0.05024 -0.0171957 0.0
#: 0 0.05024 0.05024 0.0 -0.00871086
#: 1 0.05024 0.05024 -0.00871086 -0.0174217
#: 2 0.05024 0.05024 -0.0174217 -0.0266809
#: 3 0.05024 0.05024 -0.0266809 -0.0359411
#: 4 0.05024 0.05024 -0.0359411 -0.0457983
#: 5 0.05024 0.05024 -0.0457983 -0.0556555
#: 6 0.05024 0.05024 -0.0556555 -0.0661631
#: 7 0.05024 0.05024 -0.0661631 -0.0766716
#: 8 0.05024 0.0376801 -0.0766716 -0.0786867
#: 9 0.0376801 0.02512 -0.0786867 -0.0807028
#: 10 0.02512 0.0220778 -0.0807028 -0.0881052
#: 11 0.0220778 0.0190356 -0.0881052 -0.0955086
#: 12 0.0190356 0.0159037 -0.0955086 -0.0995245
#: 13 0.0159037 0.0127718 -0.0995245 -0.103539
#: 14 0.0127718 0.00961518 -0.103539 -0.106299
#: 15 0.00961518 0.00645852 -0.106299 -0.109059
#: 16 0.00645852 0.00322914 -0.109059 -0.110323
#: 17 0.00322914 0.0 -0.110323 -0.111587
#: 18 0.0 -0.00320148 -0.111587 -0.109881
#: 19 -0.00320148 -0.00640321 -0.109881 -0.108175
#: 20 -0.00640321 -0.00958967 -0.108175 -0.105558
#: 21 -0.00958967 -0.0127759 -0.105558 -0.102942
#: 22 -0.0127759 -0.0159068 -0.102942 -0.0989828
#: 23 -0.0159068 -0.0190375 -0.0989828 -0.0950241
#: 24 -0.0190375 -0.0220788 -0.0950241 -0.087863
#: 25 -0.0220788 -0.02512 -0.087863 -0.0807028
#: 26 -0.02512 -0.0376801 -0.0807028 -0.0786867
#: 27 -0.0376801 -0.05024 -0.0786867 -0.0766716
#: 28 -0.05024 -0.05024 -0.0766716 -0.0661631
#: 29 -0.05024 -0.05024 -0.0661631 -0.0556555
#: 30 -0.05024 -0.05024 -0.0556555 -0.0457983
#: 31 -0.05024 -0.05024 -0.0457983 -0.0359411
#: 32 -0.05024 -0.05024 -0.0359411 -0.0266809
#: 33 -0.05024 -0.05024 -0.0266809 -0.0174217
#: 34 -0.05024 -0.05024 -0.0174217 -0.00871086
#: 35 -0.05024 -0.05024 -0.00871086 0.0
#: 0 0.05024 0.05024 0.0 -0.0176477
#: 1 0.05024 0.05024 -0.0176477 -0.0363684
#: 2 0.05024 0.05024 -0.0363684 -0.0562601
#: 3 0.05024 0.05024 -0.0562601 -0.0774231
#: 4 0.05024 0.02512 -0.0774231 -0.0818138
#: 5 0.02512 0.0190358 -0.0818138 -0.096694
#: 6 0.0190358 0.0127721 -0.096694 -0.10468
#: 7 0.0127721 0.00645852 -0.10468 -0.110314
#: 8 0.00645852 0.0 -0.110314 -0.113154
#: 9 0.0 -0.0064044 -0.113154 -0.10949
#: 10 -0.0064044 -0.0127773 -0.10949 -0.104107
#: 11 -0.0127773 -0.0190387 -0.104107 -0.0962267
#: 12 -0.0190387 -0.02512 -0.0962267 -0.0818138
#: 13 -0.02512 -0.05024 -0.0818138 -0.0774231
#: 14 -0.05024 -0.05024 -0.0774231 -0.0562601
#: 15 -0.05024 -0.05024 -0.0562601 -0.0363684
#: 16 -0.05024 -0.05024 -0.0363684 -0.0176477
#: 17 -0.05024 -0.05024 -0.0176477 0.0
#: 0 0.05024 0.05024 0.0 -0.00893688
#: 1 0.05024 0.05024 -0.00893688 -0.0178728
#: 2 0.05024 0.05024 -0.0178728 -0.0273352
#: 3 0.05024 0.05024 -0.0273352 -0.0367966
#: 4 0.05024 0.05024 -0.0367966 -0.0468302
#: 5 0.05024 0.05024 -0.0468302 -0.0568638
#: 6 0.05024 0.05024 -0.0568638 -0.0675192
#: 7 0.05024 0.05024 -0.0675192 -0.0781746
#: 8 0.05024 0.0376801 -0.0781746 -0.0805502
#: 9 0.0376801 0.02512 -0.0805502 -0.0829248
#: 10 0.02512 0.022078 -0.0829248 -0.0904016
#: 11 0.022078 0.0190361 -0.0904016 -0.0978785
#: 12 0.0190361 0.0159042 -0.0978785 -0.10185
#: 13 0.0159042 0.0127723 -0.10185 -0.105822
#: 14 0.0127723 0.00961542 -0.105822 -0.108695
#: 15 0.00961542 0.00645852 -0.108695 -0.111568
#: 16 0.00645852 0.00322914 -0.111568 -0.113145
#: 17 0.00322914 0.0 -0.113145 -0.114721
#: 18 0.0 -0.00320268 -0.114721 -0.112763
#: 19 -0.00320268 -0.00640535 -0.112763 -0.110806
#: 20 -0.00640535 -0.00959206 -0.110806 -0.108039
#: 21 -0.00959206 -0.012779 -0.108039 -0.105272
#: 22 -0.012779 -0.0159094 -0.105272 -0.101351
#: 23 -0.0159094 -0.0190399 -0.101351 -0.0974293
#: 24 -0.0190399 -0.0220799 -0.0974293 -0.0901766
#: 25 -0.0220799 -0.02512 -0.0901766 -0.0829248
#: 26 -0.02512 -0.0376801 -0.0829248 -0.0805502
#: 27 -0.0376801 -0.05024 -0.0805502 -0.0781746
#: 28 -0.05024 -0.05024 -0.0781746 -0.0675192
#: 29 -0.05024 -0.05024 -0.0675192 -0.0568638
#: 30 -0.05024 -0.05024 -0.0568638 -0.0468302
#: 31 -0.05024 -0.05024 -0.0468302 -0.0367966
#: 32 -0.05024 -0.05024 -0.0367966 -0.0273352
#: 33 -0.05024 -0.05024 -0.0273352 -0.0178728
#: 34 -0.05024 -0.05024 -0.0178728 -0.00893688
#: 35 -0.05024 -0.05024 -0.00893688 0.0
#: slice #: 6
#: 0 0.05024 0.05024 0.0 -0.00871086
#: 1 0.05024 0.05024 -0.00871086 -0.0174217
#: 2 0.05024 0.05024 -0.0174217 -0.0266809
#: 3 0.05024 0.05024 -0.0266809 -0.0359411
#: 4 0.05024 0.05024 -0.0359411 -0.0457983
#: 5 0.05024 0.05024 -0.0457983 -0.0556555
#: 6 0.05024 0.05024 -0.0556555 -0.0661631
#: 7 0.05024 0.05024 -0.0661631 -0.0766716
#: 8 0.05024 0.0376801 -0.0766716 -0.0786867
#: 9 0.0376801 0.02512 -0.0786867 -0.0807028
#: 10 0.02512 0.0220778 -0.0807028 -0.0881052
#: 11 0.0220778 0.0190356 -0.0881052 -0.0955086
#: 12 0.0190356 0.0159037 -0.0955086 -0.0995245
#: 13 0.0159037 0.0127718 -0.0995245 -0.103539
#: 14 0.0127718 0.00961518 -0.103539 -0.106299
#: 15 0.00961518 0.00645852 -0.106299 -0.109059
#: 16 0.00645852 0.00322914 -0.109059 -0.110323
#: 17 0.00322914 0.0 -0.110323 -0.111587
#: 18 0.0 -0.00320148 -0.111587 -0.109881
#: 19 -0.00320148 -0.00640321 -0.109881 -0.108175
#: 20 -0.00640321 -0.00958967 -0.108175 -0.105558
#: 21 -0.00958967 -0.0127759 -0.105558 -0.102942
#: 22 -0.0127759 -0.0159068 -0.102942 -0.0989828
#: 23 -0.0159068 -0.0190375 -0.0989828 -0.0950241
#: 24 -0.0190375 -0.0220788 -0.0950241 -0.087863
#: 25 -0.0220788 -0.02512 -0.087863 -0.0807028
#: 26 -0.02512 -0.0376801 -0.0807028 -0.0786867
#: 27 -0.0376801 -0.05024 -0.0786867 -0.0766716
#: 28 -0.05024 -0.05024 -0.0766716 -0.0661631
#: 29 -0.05024 -0.05024 -0.0661631 -0.0556555
#: 30 -0.05024 -0.05024 -0.0556555 -0.0457983
#: 31 -0.05024 -0.05024 -0.0457983 -0.0359411
#: 32 -0.05024 -0.05024 -0.0359411 -0.0266809
#: 33 -0.05024 -0.05024 -0.0266809 -0.0174217
#: 34 -0.05024 -0.05024 -0.0174217 -0.00871086
#: 35 -0.05024 -0.05024 -0.00871086 0.0
#: 0 0.05024 0.05024 0.0 -0.0176477
#: 1 0.05024 0.05024 -0.0176477 -0.0363684
#: 2 0.05024 0.05024 -0.0363684 -0.0562601
#: 3 0.05024 0.05024 -0.0562601 -0.0774231
#: 4 0.05024 0.02512 -0.0774231 -0.0818138
#: 5 0.02512 0.0190358 -0.0818138 -0.096694
#: 6 0.0190358 0.0127721 -0.096694 -0.10468
#: 7 0.0127721 0.00645852 -0.10468 -0.110314
#: 8 0.00645852 0.0 -0.110314 -0.113154
#: 9 0.0 -0.0064044 -0.113154 -0.10949
#: 10 -0.0064044 -0.0127773 -0.10949 -0.104107
#: 11 -0.0127773 -0.0190387 -0.104107 -0.0962267
#: 12 -0.0190387 -0.02512 -0.0962267 -0.0818138
#: 13 -0.02512 -0.05024 -0.0818138 -0.0774231
#: 14 -0.05024 -0.05024 -0.0774231 -0.0562601
#: 15 -0.05024 -0.05024 -0.0562601 -0.0363684
#: 16 -0.05024 -0.05024 -0.0363684 -0.0176477
#: 17 -0.05024 -0.05024 -0.0176477 0.0
#: 0 0.05024 0.05024 0.0 -0.00893688
#: 1 0.05024 0.05024 -0.00893688 -0.0178728
#: 2 0.05024 0.05024 -0.0178728 -0.0273352
#: 3 0.05024 0.05024 -0.0273352 -0.0367966
#: 4 0.05024 0.05024 -0.0367966 -0.0468302
#: 5 0.05024 0.05024 -0.0468302 -0.0568638
#: 6 0.05024 0.05024 -0.0568638 -0.0675192
#: 7 0.05024 0.05024 -0.0675192 -0.0781746
#: 8 0.05024 0.0376801 -0.0781746 -0.0805502
#: 9 0.0376801 0.02512 -0.0805502 -0.0829248
#: 10 0.02512 0.022078 -0.0829248 -0.0904016
#: 11 0.022078 0.0190361 -0.0904016 -0.0978785
#: 12 0.0190361 0.0159042 -0.0978785 -0.10185
#: 13 0.0159042 0.0127723 -0.10185 -0.105822
#: 14 0.0127723 0.00961542 -0.105822 -0.108695
#: 15 0.00961542 0.00645852 -0.108695 -0.111568
#: 16 0.00645852 0.00322914 -0.111568 -0.113145
#: 17 0.00322914 0.0 -0.113145 -0.114721
#: 18 0.0 -0.00320268 -0.114721 -0.112763
#: 19 -0.00320268 -0.00640535 -0.112763 -0.110806
#: 20 -0.00640535 -0.00959206 -0.110806 -0.108039
#: 21 -0.00959206 -0.012779 -0.108039 -0.105272
#: 22 -0.012779 -0.0159094 -0.105272 -0.101351
#: 23 -0.0159094 -0.0190399 -0.101351 -0.0974293
#: 24 -0.0190399 -0.0220799 -0.0974293 -0.0901766
#: 25 -0.0220799 -0.02512 -0.0901766 -0.0829248
#: 26 -0.02512 -0.0376801 -0.0829248 -0.0805502
#: 27 -0.0376801 -0.05024 -0.0805502 -0.0781746
#: 28 -0.05024 -0.05024 -0.0781746 -0.0675192
#: 29 -0.05024 -0.05024 -0.0675192 -0.0568638
#: 30 -0.05024 -0.05024 -0.0568638 -0.0468302
#: 31 -0.05024 -0.05024 -0.0468302 -0.0367966
#: 32 -0.05024 -0.05024 -0.0367966 -0.0273352
#: 33 -0.05024 -0.05024 -0.0273352 -0.0178728
#: 34 -0.05024 -0.05024 -0.0178728 -0.00893688
#: 35 -0.05024 -0.05024 -0.00893688 0.0
#: 0 0.05024 0.05024 0.0 -0.0180988
#: 1 0.05024 0.05024 -0.0180988 -0.0372248
#: 2 0.05024 0.05024 -0.0372248 -0.0574675
#: 3 0.05024 0.05024 -0.0574675 -0.0789261
#: 4 0.05024 0.02512 -0.0789261 -0.0840368
#: 5 0.02512 0.0190361 -0.0840368 -0.0990572
#: 6 0.0190361 0.0127723 -0.0990572 -0.106952
#: 7 0.0127723 0.00645852 -0.106952 -0.112821
#: 8 0.00645852 0.0 -0.112821 -0.116288
#: 9 0.0 -0.00640583 -0.116288 -0.112109
#: 10 -0.00640583 -0.0127795 -0.112109 -0.10642
#: 11 -0.0127795 -0.0190401 -0.10642 -0.0986185
#: 12 -0.0190401 -0.02512 -0.0986185 -0.0840368
#: 13 -0.02512 -0.05024 -0.0840368 -0.0789261
#: 14 -0.05024 -0.05024 -0.0789261 -0.0574675
#: 15 -0.05024 -0.05024 -0.0574675 -0.0372248
#: 16 -0.05024 -0.05024 -0.0372248 -0.0180988
#: 17 -0.05024 -0.05024 -0.0180988 0.0
#: 0 0.05024 0.05024 0.0 -0.00916195
#: 1 0.05024 0.05024 -0.00916195 -0.0183249
#: 2 0.05024 0.05024 -0.0183249 -0.0279894
#: 3 0.05024 0.05024 -0.0279894 -0.037653
#: 4 0.05024 0.05024 -0.037653 -0.0478621
#: 5 0.05024 0.05024 -0.0478621 -0.0580711
#: 6 0.05024 0.05024 -0.0580711 -0.0688744
#: 7 0.05024 0.05024 -0.0688744 -0.0796776
#: 8 0.05024 0.0376801 -0.0796776 -0.0824137
#: 9 0.0376801 0.02512 -0.0824137 -0.0851488
#: 10 0.02512 0.022078 -0.0851488 -0.0926924
#: 11 0.022078 0.0190361 -0.0926924 -0.100236
#: 12 0.0190361 0.0159042 -0.100236 -0.104159
#: 13 0.0159042 0.0127723 -0.104159 -0.108083
#: 14 0.0127723 0.00961542 -0.108083 -0.111077
#: 15 0.00961542 0.00645852 -0.111077 -0.114073
#: 16 0.00645852 0.00322914 -0.114073 -0.115964
#: 17 0.00322914 0.0 -0.115964 -0.117855
#: 18 0.0 -0.00320292 -0.117855 -0.115633
#: 19 -0.00320292 -0.00640607 -0.115633 -0.113411
#: 20 -0.00640607 -0.00959301 -0.113411 -0.110489
#: 21 -0.00959301 -0.01278 -0.110489 -0.107567
#: 22 -0.01278 -0.0159101 -0.107567 -0.103688
#: 23 -0.0159101 -0.0190403 -0.103688 -0.0998087
#: 24 -0.0190403 -0.0220802 -0.0998087 -0.0924788
#: 25 -0.0220802 -0.02512 -0.0924788 -0.0851488
#: 26 -0.02512 -0.0376801 -0.0851488 -0.0824137
#: 27 -0.0376801 -0.05024 -0.0824137 -0.0796776
#: 28 -0.05024 -0.05024 -0.0796776 -0.0688744
#: 29 -0.05024 -0.05024 -0.0688744 -0.0580711
#: 30 -0.05024 -0.05024 -0.0580711 -0.0478621
#: 31 -0.05024 -0.05024 -0.0478621 -0.037653
#: 32 -0.05024 -0.05024 -0.037653 -0.0279894
#: 33 -0.05024 -0.05024 -0.0279894 -0.0183249
#: 34 -0.05024 -0.05024 -0.0183249 -0.00916195
#: 35 -0.05024 -0.05024 -0.00916195 0.0
#: slice #: 7
#: 0 0.05024 0.05024 0.0 -0.00893688
#: 1 0.05024 0.05024 -0.00893688 -0.0178728
#: 2 0.05024 0.05024 -0.0178728 -0.0273352
#: 3 0.05024 0.05024 -0.0273352 -0.0367966
#: 4 0.05024 0.05024 -0.0367966 -0.0468302
#: 5 0.05024 0.05024 -0.0468302 -0.0568638
#: 6 0.05024 0.05024 -0.0568638 -0.0675192
#: 7 0.05024 0.05024 -0.0675192 -0.0781746
#: 8 0.05024 0.0376801 -0.0781746 -0.0805502
#: 9 0.0376801 0.02512 -0.0805502 -0.0829248
#: 10 0.02512 0.022078 -0.0829248 -0.0904016
#: 11 0.022078 0.0190361 -0.0904016 -0.0978785
#: 12 0.0190361 0.0159042 -0.0978785 -0.10185
#: 13 0.0159042 0.0127723 -0.10185 -0.105822
#: 14 0.0127723 0.00961542 -0.105822 -0.108695
#: 15 0.00961542 0.00645852 -0.108695 -0.111568
#: 16 0.00645852 0.00322914 -0.111568 -0.113145
#: 17 0.00322914 0.0 -0.113145 -0.114721
#: 18 0.0 -0.00320268 -0.114721 -0.112763
#: 19 -0.00320268 -0.00640535 -0.112763 -0.110806
#: 20 -0.00640535 -0.00959206 -0.110806 -0.108039
#: 21 -0.00959206 -0.012779 -0.108039 -0.105272
#: 22 -0.012779 -0.0159094 -0.105272 -0.101351
#: 23 -0.0159094 -0.0190399 -0.101351 -0.0974293
#: 24 -0.0190399 -0.0220799 -0.0974293 -0.0901766
#: 25 -0.0220799 -0.02512 -0.0901766 -0.0829248
#: 26 -0.02512 -0.0376801 -0.0829248 -0.0805502
#: 27 -0.0376801 -0.05024 -0.0805502 -0.0781746
#: 28 -0.05024 -0.05024 -0.0781746 -0.0675192
#: 29 -0.05024 -0.05024 -0.0675192 -0.0568638
#: 30 -0.05024 -0.05024 -0.0568638 -0.0468302
#: 31 -0.05024 -0.05024 -0.0468302 -0.0367966
#: 32 -0.05024 -0.05024 -0.0367966 -0.0273352
#: 33 -0.05024 -0.05024 -0.0273352 -0.0178728
#: 34 -0.05024 -0.05024 -0.0178728 -0.00893688
#: 35 -0.05024 -0.05024 -0.00893688 0.0
#: 0 0.05024 0.05024 0.0 -0.0180988
#: 1 0.05024 0.05024 -0.0180988 -0.0372248
#: 2 0.05024 0.05024 -0.0372248 -0.0574675
#: 3 0.05024 0.05024 -0.0574675 -0.0789261
#: 4 0.05024 0.02512 -0.0789261 -0.0840368
#: 5 0.02512 0.0190361 -0.0840368 -0.0990572
#: 6 0.0190361 0.0127723 -0.0990572 -0.106952
#: 7 0.0127723 0.00645852 -0.106952 -0.112821
#: 8 0.00645852 0.0 -0.112821 -0.116288
#: 9 0.0 -0.00640583 -0.116288 -0.112109
#: 10 -0.00640583 -0.0127795 -0.112109 -0.10642
#: 11 -0.0127795 -0.0190401 -0.10642 -0.0986185
#: 12 -0.0190401 -0.02512 -0.0986185 -0.0840368
#: 13 -0.02512 -0.05024 -0.0840368 -0.0789261
#: 14 -0.05024 -0.05024 -0.0789261 -0.0574675
#: 15 -0.05024 -0.05024 -0.0574675 -0.0372248
#: 16 -0.05024 -0.05024 -0.0372248 -0.0180988
#: 17 -0.05024 -0.05024 -0.0180988 0.0
#: 0 0.05024 0.05024 0.0 -0.00916195
#: 1 0.05024 0.05024 -0.00916195 -0.0183249
#: 2 0.05024 0.05024 -0.0183249 -0.0279894
#: 3 0.05024 0.05024 -0.0279894 -0.037653
#: 4 0.05024 0.05024 -0.037653 -0.0478621
#: 5 0.05024 0.05024 -0.0478621 -0.0580711
#: 6 0.05024 0.05024 -0.0580711 -0.0688744
#: 7 0.05024 0.05024 -0.0688744 -0.0796776
#: 8 0.05024 0.0376801 -0.0796776 -0.0824137
#: 9 0.0376801 0.02512 -0.0824137 -0.0851488
#: 10 0.02512 0.022078 -0.0851488 -0.0926924
#: 11 0.022078 0.0190361 -0.0926924 -0.100236
#: 12 0.0190361 0.0159042 -0.100236 -0.104159
#: 13 0.0159042 0.0127723 -0.104159 -0.108083
#: 14 0.0127723 0.00961542 -0.108083 -0.111077
#: 15 0.00961542 0.00645852 -0.111077 -0.114073
#: 16 0.00645852 0.00322914 -0.114073 -0.115964
#: 17 0.00322914 0.0 -0.115964 -0.117855
#: 18 0.0 -0.00320292 -0.117855 -0.115633
#: 19 -0.00320292 -0.00640607 -0.115633 -0.113411
#: 20 -0.00640607 -0.00959301 -0.113411 -0.110489
#: 21 -0.00959301 -0.01278 -0.110489 -0.107567
#: 22 -0.01278 -0.0159101 -0.107567 -0.103688
#: 23 -0.0159101 -0.0190403 -0.103688 -0.0998087
#: 24 -0.0190403 -0.0220802 -0.0998087 -0.0924788
#: 25 -0.0220802 -0.02512 -0.0924788 -0.0851488
#: 26 -0.02512 -0.0376801 -0.0851488 -0.0824137
#: 27 -0.0376801 -0.05024 -0.0824137 -0.0796776
#: 28 -0.05024 -0.05024 -0.0796776 -0.0688744
#: 29 -0.05024 -0.05024 -0.0688744 -0.0580711
#: 30 -0.05024 -0.05024 -0.0580711 -0.0478621
#: 31 -0.05024 -0.05024 -0.0478621 -0.037653
#: 32 -0.05024 -0.05024 -0.037653 -0.0279894
#: 33 -0.05024 -0.05024 -0.0279894 -0.0183249
#: 34 -0.05024 -0.05024 -0.0183249 -0.00916195
#: 35 -0.05024 -0.05024 -0.00916195 0.0
#: 0 0.05024 0.05024 0.0 -0.0185509
#: 1 0.05024 0.05024 -0.0185509 -0.0380812
#: 2 0.05024 0.05024 -0.0380812 -0.0586748
#: 3 0.05024 0.05024 -0.0586748 -0.08043
#: 4 0.05024 0.02512 -0.08043 -0.0862598
#: 5 0.02512 0.0190361 -0.0862598 -0.101415
#: 6 0.0190361 0.0127726 -0.101415 -0.109212
#: 7 0.0127726 0.00645852 -0.109212 -0.115324
#: 8 0.00645852 0.0 -0.115324 -0.119422
#: 9 0.0 -0.00640631 -0.119422 -0.114707
#: 10 -0.00640631 -0.0127802 -0.114707 -0.108705
#: 11 -0.0127802 -0.0190406 -0.108705 -0.100993
#: 12 -0.0190406 -0.02512 -0.100993 -0.0862598
#: 13 -0.02512 -0.05024 -0.0862598 -0.08043
#: 14 -0.05024 -0.05024 -0.08043 -0.0586748
#: 15 -0.05024 -0.05024 -0.0586748 -0.0380812
#: 16 -0.05024 -0.05024 -0.0380812 -0.0185509
#: 17 -0.05024 -0.05024 -0.0185509 0.0
#: 0 0.05024 0.05024 0.0 -0.00938892
#: 1 0.05024 0.05024 -0.00938892 -0.0187769
#: 2 0.05024 0.05024 -0.0187769 -0.0286427
#: 3 0.05024 0.05024 -0.0286427 -0.0385084
#: 4 0.05024 0.05024 -0.0385084 -0.0488939
#: 5 0.05024 0.05024 -0.0488939 -0.0592794
#: 6 0.05024 0.05024 -0.0592794 -0.0702305
#: 7 0.05024 0.05024 -0.0702305 -0.0811815
#: 8 0.05024 0.0376801 -0.0811815 -0.0842762
#: 9 0.0376801 0.02512 -0.0842762 -0.0873709
#: 10 0.02512 0.022078 -0.0873709 -0.0949812
#: 11 0.022078 0.0190361 -0.0949812 -0.102592
#: 12 0.0190361 0.0159044 -0.102592 -0.106466
#: 13 0.0159044 0.0127726 -0.106466 -0.11034
#: 14 0.0127726 0.00961542 -0.11034 -0.113458
#: 15 0.00961542 0.00645852 -0.113458 -0.116575
#: 16 0.00645852 0.00322914 -0.116575 -0.118781
#: 17 0.00322914 0.0 -0.118781 -0.120988
#: 18 0.0 -0.00320339 -0.120988 -0.118495
#: 19 -0.00320339 -0.00640655 -0.118495 -0.116002
#: 20 -0.00640655 -0.00959349 -0.116002 -0.112922
#: 21 -0.00959349 -0.0127804 -0.112922 -0.109842
#: 22 -0.0127804 -0.0159106 -0.109842 -0.106009
#: 23 -0.0159106 -0.0190408 -0.106009 -0.102177
#: 24 -0.0190408 -0.0220804 -0.102177 -0.0947733
#: 25 -0.0220804 -0.02512 -0.0947733 -0.0873709
#: 26 -0.02512 -0.0376801 -0.0873709 -0.0842762
#: 27 -0.0376801 -0.05024 -0.0842762 -0.0811815
#: 28 -0.05024 -0.05024 -0.0811815 -0.0702305
#: 29 -0.05024 -0.05024 -0.0702305 -0.0592794
#: 30 -0.05024 -0.05024 -0.0592794 -0.0488939
#: 31 -0.05024 -0.05024 -0.0488939 -0.0385084
#: 32 -0.05024 -0.05024 -0.0385084 -0.0286427
#: 33 -0.05024 -0.05024 -0.0286427 -0.0187769
#: 34 -0.05024 -0.05024 -0.0187769 -0.00938892
#: 35 -0.05024 -0.05024 -0.00938892 0.0
#: slice #: 8
#: 0 0.05024 0.05024 0.0 -0.00916195
#: 1 0.05024 0.05024 -0.00916195 -0.0183249
#: 2 0.05024 0.05024 -0.0183249 -0.0279894
#: 3 0.05024 0.05024 -0.0279894 -0.037653
#: 4 0.05024 0.05024 -0.037653 -0.0478621
#: 5 0.05024 0.05024 -0.0478621 -0.0580711
#: 6 0.05024 0.05024 -0.0580711 -0.0688744
#: 7 0.05024 0.05024 -0.0688744 -0.0796776
#: 8 0.05024 0.0376801 -0.0796776 -0.0824137
#: 9 0.0376801 0.02512 -0.0824137 -0.0851488
#: 10 0.02512 0.022078 -0.0851488 -0.0926924
#: 11 0.022078 0.0190361 -0.0926924 -0.100236
#: 12 0.0190361 0.0159042 -0.100236 -0.104159
#: 13 0.0159042 0.0127723 -0.104159 -0.108083
#: 14 0.0127723 0.00961542 -0.108083 -0.111077
#: 15 0.00961542 0.00645852 -0.111077 -0.114073
#: 16 0.00645852 0.00322914 -0.114073 -0.115964
#: 17 0.00322914 0.0 -0.115964 -0.117855
#: 18 0.0 -0.00320292 -0.117855 -0.115633
#: 19 -0.00320292 -0.00640607 -0.115633 -0.113411
#: 20 -0.00640607 -0.00959301 -0.113411 -0.110489
#: 21 -0.00959301 -0.01278 -0.110489 -0.107567
#: 22 -0.01278 -0.0159101 -0.107567 -0.103688
#: 23 -0.0159101 -0.0190403 -0.103688 -0.0998087
#: 24 -0.0190403 -0.0220802 -0.0998087 -0.0924788
#: 25 -0.0220802 -0.02512 -0.0924788 -0.0851488
#: 26 -0.02512 -0.0376801 -0.0851488 -0.0824137
#: 27 -0.0376801 -0.05024 -0.0824137 -0.0796776
#: 28 -0.05024 -0.05024 -0.0796776 -0.0688744
#: 29 -0.05024 -0.05024 -0.0688744 -0.0580711
#: 30 -0.05024 -0.05024 -0.0580711 -0.0478621
#: 31 -0.05024 -0.05024 -0.0478621 -0.037653
#: 32 -0.05024 -0.05024 -0.037653 -0.0279894
#: 33 -0.05024 -0.05024 -0.0279894 -0.0183249
#: 34 -0.05024 -0.05024 -0.0183249 -0.00916195
#: 35 -0.05024 -0.05024 -0.00916195 0.0
#: 0 0.05024 0.05024 0.0 -0.0185509
#: 1 0.05024 0.05024 -0.0185509 -0.0380812
#: 2 0.05024 0.05024 -0.0380812 -0.0586748
#: 3 0.05024 0.05024 -0.0586748 -0.08043
#: 4 0.05024 0.02512 -0.08043 -0.0862598
#: 5 0.02512 0.0190361 -0.0862598 -0.101415
#: 6 0.0190361 0.0127726 -0.101415 -0.109212
#: 7 0.0127726 0.00645852 -0.109212 -0.115324
#: 8 0.00645852 0.0 -0.115324 -0.119422
#: 9 0.0 -0.00640631 -0.119422 -0.114707
#: 10 -0.00640631 -0.0127802 -0.114707 -0.108705
#: 11 -0.0127802 -0.0190406 -0.108705 -0.100993
#: 12 -0.0190406 -0.02512 -0.100993 -0.0862598
#: 13 -0.02512 -0.05024 -0.0862598 -0.08043
#: 14 -0.05024 -0.05024 -0.08043 -0.0586748
#: 15 -0.05024 -0.05024 -0.0586748 -0.0380812
#: 16 -0.05024 -0.05024 -0.0380812 -0.0185509
#: 17 -0.05024 -0.05024 -0.0185509 0.0
#: 0 0.05024 0.05024 0.0 -0.00938892
#: 1 0.05024 0.05024 -0.00938892 -0.0187769
#: 2 0.05024 0.05024 -0.0187769 -0.0286427
#: 3 0.05024 0.05024 -0.0286427 -0.0385084
#: 4 0.05024 0.05024 -0.0385084 -0.0488939
#: 5 0.05024 0.05024 -0.0488939 -0.0592794
#: 6 0.05024 0.05024 -0.0592794 -0.0702305
#: 7 0.05024 0.05024 -0.0702305 -0.0811815
#: 8 0.05024 0.0376801 -0.0811815 -0.0842762
#: 9 0.0376801 0.02512 -0.0842762 -0.0873709
#: 10 0.02512 0.022078 -0.0873709 -0.0949812
#: 11 0.022078 0.0190361 -0.0949812 -0.102592
#: 12 0.0190361 0.0159044 -0.102592 -0.106466
#: 13 0.0159044 0.0127726 -0.106466 -0.11034
#: 14 0.0127726 0.00961542 -0.11034 -0.113458
#: 15 0.00961542 0.00645852 -0.113458 -0.116575
#: 16 0.00645852 0.00322914 -0.116575 -0.118781
#: 17 0.00322914 0.0 -0.118781 -0.120988
#: 18 0.0 -0.00320339 -0.120988 -0.118495
#: 19 -0.00320339 -0.00640655 -0.118495 -0.116002
#: 20 -0.00640655 -0.00959349 -0.116002 -0.112922
#: 21 -0.00959349 -0.0127804 -0.112922 -0.109842
#: 22 -0.0127804 -0.0159106 -0.109842 -0.106009
#: 23 -0.0159106 -0.0190408 -0.106009 -0.102177
#: 24 -0.0190408 -0.0220804 -0.102177 -0.0947733
#: 25 -0.0220804 -0.02512 -0.0947733 -0.0873709
#: 26 -0.02512 -0.0376801 -0.0873709 -0.0842762
#: 27 -0.0376801 -0.05024 -0.0842762 -0.0811815
#: 28 -0.05024 -0.05024 -0.0811815 -0.0702305
#: 29 -0.05024 -0.05024 -0.0702305 -0.0592794
#: 30 -0.05024 -0.05024 -0.0592794 -0.0488939
#: 31 -0.05024 -0.05024 -0.0488939 -0.0385084
#: 32 -0.05024 -0.05024 -0.0385084 -0.0286427
#: 33 -0.05024 -0.05024 -0.0286427 -0.0187769
#: 34 -0.05024 -0.05024 -0.0187769 -0.00938892
#: 35 -0.05024 -0.05024 -0.00938892 0.0
#: 0 0.05024 0.05024 0.0 -0.0190029
#: 1 0.05024 0.05024 -0.0190029 -0.0389357
#: 2 0.05024 0.05024 -0.0389357 -0.0598841
#: 3 0.05024 0.05024 -0.0598841 -0.081933
#: 4 0.05024 0.02512 -0.081933 -0.0884809
#: 5 0.02512 0.0190361 -0.0884809 -0.103766
#: 6 0.0190361 0.0127726 -0.103766 -0.111464
#: 7 0.0127726 0.00645852 -0.111464 -0.117823
#: 8 0.00645852 0.0 -0.117823 -0.122555
#: 9 0.0 -0.00640631 -0.122555 -0.117295
#: 10 -0.00640631 -0.0127802 -0.117295 -0.110978
#: 11 -0.0127802 -0.0190406 -0.110978 -0.103358
#: 12 -0.0190406 -0.02512 -0.103358 -0.0884809
#: 13 -0.02512 -0.05024 -0.0884809 -0.081933
#: 14 -0.05024 -0.05024 -0.081933 -0.0598841
#: 15 -0.05024 -0.05024 -0.0598841 -0.0389357
#: 16 -0.05024 -0.05024 -0.0389357 -0.0190029
#: 17 -0.05024 -0.05024 -0.0190029 0.0
#: 0 0.05024 0.05024 0.0 -0.00961399
#: 1 0.05024 0.05024 -0.00961399 -0.0192289
#: 2 0.05024 0.05024 -0.0192289 -0.0292959
#: 3 0.05024 0.05024 -0.0292959 -0.0393639
#: 4 0.05024 0.05024 -0.0393639 -0.0499258
#: 5 0.05024 0.05024 -0.0499258 -0.0604877
#: 6 0.05024 0.05024 -0.0604877 -0.0715857
#: 7 0.05024 0.05024 -0.0715857 -0.0826845
#: 8 0.05024 0.0376801 -0.0826845 -0.0861387
#: 9 0.0376801 0.02512 -0.0861387 -0.089592
#: 10 0.02512 0.022078 -0.089592 -0.0972662
#: 11 0.022078 0.0190361 -0.0972662 -0.10494
#: 12 0.0190361 0.0159044 -0.10494 -0.108764
#: 13 0.0159044 0.0127728 -0.108764 -0.112587
#: 14 0.0127728 0.00961566 -0.112587 -0.115829
#: 15 0.00961566 0.00645852 -0.115829 -0.11907
#: 16 0.00645852 0.00322914 -0.11907 -0.121596
#: 17 0.00322914 0.0 -0.121596 -0.124122
#: 18 0.0 -0.00320315 -0.124122 -0.121356
#: 19 -0.00320315 -0.00640631 -0.121356 -0.118589
#: 20 -0.00640631 -0.00959325 -0.118589 -0.115352
#: 21 -0.00959325 -0.0127802 -0.115352 -0.112114
#: 22 -0.0127802 -0.0159101 -0.112114 -0.108327
#: 23 -0.0159101 -0.0190403 -0.108327 -0.104539
#: 24 -0.0190403 -0.0220802 -0.104539 -0.0970659
#: 25 -0.0220802 -0.02512 -0.0970659 -0.089592
#: 26 -0.02512 -0.0376801 -0.089592 -0.0861387
#: 27 -0.0376801 -0.05024 -0.0861387 -0.0826845
#: 28 -0.05024 -0.05024 -0.0826845 -0.0715857
#: 29 -0.05024 -0.05024 -0.0715857 -0.0604877
#: 30 -0.05024 -0.05024 -0.0604877 -0.0499258
#: 31 -0.05024 -0.05024 -0.0499258 -0.0393639
#: 32 -0.05024 -0.05024 -0.0393639 -0.0292959
#: 33 -0.05024 -0.05024 -0.0292959 -0.0192289
#: 34 -0.05024 -0.05024 -0.0192289 -0.00961399
#: 35 -0.05024 -0.05024 -0.00961399 0.0
#: slice #: 9
#: 0 0.05024 0.05024 0.0 -0.00938892
#: 1 0.05024 0.05024 -0.00938892 -0.0187769
#: 2 0.05024 0.05024 -0.0187769 -0.0286427
#: 3 0.05024 0.05024 -0.0286427 -0.0385084
#: 4 0.05024 0.05024 -0.0385084 -0.0488939
#: 5 0.05024 0.05024 -0.0488939 -0.0592794
#: 6 0.05024 0.05024 -0.0592794 -0.0702305
#: 7 0.05024 0.05024 -0.0702305 -0.0811815
#: 8 0.05024 0.0376801 -0.0811815 -0.0842762
#: 9 0.0376801 0.02512 -0.0842762 -0.0873709
#: 10 0.02512 0.022078 -0.0873709 -0.0949812
#: 11 0.022078 0.0190361 -0.0949812 -0.102592
#: 12 0.0190361 0.0159044 -0.102592 -0.106466
#: 13 0.0159044 0.0127726 -0.106466 -0.11034
#: 14 0.0127726 0.00961542 -0.11034 -0.113458
#: 15 0.00961542 0.00645852 -0.113458 -0.116575
#: 16 0.00645852 0.00322914 -0.116575 -0.118781
#: 17 0.00322914 0.0 -0.118781 -0.120988
#: 18 0.0 -0.00320339 -0.120988 -0.118495
#: 19 -0.00320339 -0.00640655 -0.118495 -0.116002
#: 20 -0.00640655 -0.00959349 -0.116002 -0.112922
#: 21 -0.00959349 -0.0127804 -0.112922 -0.109842
#: 22 -0.0127804 -0.0159106 -0.109842 -0.106009
#: 23 -0.0159106 -0.0190408 -0.106009 -0.102177
#: 24 -0.0190408 -0.0220804 -0.102177 -0.0947733
#: 25 -0.0220804 -0.02512 -0.0947733 -0.0873709
#: 26 -0.02512 -0.0376801 -0.0873709 -0.0842762
#: 27 -0.0376801 -0.05024 -0.0842762 -0.0811815
#: 28 -0.05024 -0.05024 -0.0811815 -0.0702305
#: 29 -0.05024 -0.05024 -0.0702305 -0.0592794
#: 30 -0.05024 -0.05024 -0.0592794 -0.0488939
#: 31 -0.05024 -0.05024 -0.0488939 -0.0385084
#: 32 -0.05024 -0.05024 -0.0385084 -0.0286427
#: 33 -0.05024 -0.05024 -0.0286427 -0.0187769
#: 34 -0.05024 -0.05024 -0.0187769 -0.00938892
#: 35 -0.05024 -0.05024 -0.00938892 0.0
#: 0 0.05024 0.05024 0.0 -0.0190029
#: 1 0.05024 0.05024 -0.0190029 -0.0389357
#: 2 0.05024 0.05024 -0.0389357 -0.0598841
#: 3 0.05024 0.05024 -0.0598841 -0.081933
#: 4 0.05024 0.02512 -0.081933 -0.0884809
#: 5 0.02512 0.0190361 -0.0884809 -0.103766
#: 6 0.0190361 0.0127726 -0.103766 -0.111464
#: 7 0.0127726 0.00645852 -0.111464 -0.117823
#: 8 0.00645852 0.0 -0.117823 -0.122555
#: 9 0.0 -0.00640631 -0.122555 -0.117295
#: 10 -0.00640631 -0.0127802 -0.117295 -0.110978
#: 11 -0.0127802 -0.0190406 -0.110978 -0.103358
#: 12 -0.0190406 -0.02512 -0.103358 -0.0884809
#: 13 -0.02512 -0.05024 -0.0884809 -0.081933
#: 14 -0.05024 -0.05024 -0.081933 -0.0598841
#: 15 -0.05024 -0.05024 -0.0598841 -0.0389357
#: 16 -0.05024 -0.05024 -0.0389357 -0.0190029
#: 17 -0.05024 -0.05024 -0.0190029 0.0
#: 0 0.05024 0.05024 0.0 -0.00961399
#: 1 0.05024 0.05024 -0.00961399 -0.0192289
#: 2 0.05024 0.05024 -0.0192289 -0.0292959
#: 3 0.05024 0.05024 -0.0292959 -0.0393639
#: 4 0.05024 0.05024 -0.0393639 -0.0499258
#: 5 0.05024 0.05024 -0.0499258 -0.0604877
#: 6 0.05024 0.05024 -0.0604877 -0.0715857
#: 7 0.05024 0.05024 -0.0715857 -0.0826845
#: 8 0.05024 0.0376801 -0.0826845 -0.0861387
#: 9 0.0376801 0.02512 -0.0861387 -0.089592
#: 10 0.02512 0.022078 -0.089592 -0.0972662
#: 11 0.022078 0.0190361 -0.0972662 -0.10494
#: 12 0.0190361 0.0159044 -0.10494 -0.108764
#: 13 0.0159044 0.0127728 -0.108764 -0.112587
#: 14 0.0127728 0.00961566 -0.112587 -0.115829
#: 15 0.00961566 0.00645852 -0.115829 -0.11907
#: 16 0.00645852 0.00322914 -0.11907 -0.121596
#: 17 0.00322914 0.0 -0.121596 -0.124122
#: 18 0.0 -0.00320315 -0.124122 -0.121356
#: 19 -0.00320315 -0.00640631 -0.121356 -0.118589
#: 20 -0.00640631 -0.00959325 -0.118589 -0.115352
#: 21 -0.00959325 -0.0127802 -0.115352 -0.112114
#: 22 -0.0127802 -0.0159101 -0.112114 -0.108327
#: 23 -0.0159101 -0.0190403 -0.108327 -0.104539
#: 24 -0.0190403 -0.0220802 -0.104539 -0.0970659
#: 25 -0.0220802 -0.02512 -0.0970659 -0.089592
#: 26 -0.02512 -0.0376801 -0.089592 -0.0861387
#: 27 -0.0376801 -0.05024 -0.0861387 -0.0826845
#: 28 -0.05024 -0.05024 -0.0826845 -0.0715857
#: 29 -0.05024 -0.05024 -0.0715857 -0.0604877
#: 30 -0.05024 -0.05024 -0.0604877 -0.0499258
#: 31 -0.05024 -0.05024 -0.0499258 -0.0393639
#: 32 -0.05024 -0.05024 -0.0393639 -0.0292959
#: 33 -0.05024 -0.05024 -0.0292959 -0.0192289
#: 34 -0.05024 -0.05024 -0.0192289 -0.00961399
#: 35 -0.05024 -0.05024 -0.00961399 0.0
#: 0 0.05024 0.05024 0.0 -0.019454
#: 1 0.05024 0.05024 -0.019454 -0.0397921
#: 2 0.05024 0.05024 -0.0397921 -0.0610914
#: 3 0.05024 0.05024 -0.0610914 -0.083436
#: 4 0.05024 0.02512 -0.083436 -0.0907011
#: 5 0.02512 0.0190363 -0.0907011 -0.106105
#: 6 0.0190363 0.012773 -0.106105 -0.113699
#: 7 0.012773 0.00645876 -0.113699 -0.120309
#: 8 0.00645876 0.0 -0.120309 -0.125686
#: 9 0.0 -0.00640583 -0.125686 -0.11988
#: 10 -0.00640583 -0.0127795 -0.11988 -0.113247
#: 11 -0.0127795 -0.0190399 -0.113247 -0.105718
#: 12 -0.0190399 -0.02512 -0.105718 -0.0907011
#: 13 -0.02512 -0.05024 -0.0907011 -0.083436
#: 14 -0.05024 -0.05024 -0.083436 -0.0610914
#: 15 -0.05024 -0.05024 -0.0610914 -0.0397921
#: 16 -0.05024 -0.05024 -0.0397921 -0.019454
#: 17 -0.05024 -0.05024 -0.019454 0.0
#: 0 0.05024 0.05024 0.0 -0.00984001
#: 1 0.05024 0.05024 -0.00984001 -0.01968
#: 2 0.05024 0.05024 -0.01968 -0.0299501
#: 3 0.05024 0.05024 -0.0299501 -0.0402203
#: 4 0.05024 0.05024 -0.0402203 -0.0509577
#: 5 0.05024 0.05024 -0.0509577 -0.0616951
#: 6 0.05024 0.05024 -0.0616951 -0.0729418
#: 7 0.05024 0.05024 -0.0729418 -0.0841885
#: 8 0.05024 0.0376801 -0.0841885 -0.0879993
#: 9 0.0376801 0.02512 -0.0879993 -0.0918102
#: 10 0.02512 0.022078 -0.0918102 -0.0995398
#: 11 0.022078 0.0190363 -0.0995398 -0.10727
#: 12 0.0190363 0.0159049 -0.10727 -0.111041
#: 13 0.0159049 0.0127733 -0.111041 -0.114811
#: 14 0.0127733 0.0096159 -0.114811 -0.118179
#: 15 0.0096159 0.00645876 -0.118179 -0.121548
#: 16 0.00645876 0.00322938 -0.121548 -0.124398
#: 17 0.00322938 0.0 -0.124398 -0.12725
#: 18 0.0 -0.00320268 -0.12725 -0.12421
#: 19 -0.00320268 -0.00640535 -0.12421 -0.121171
#: 20 -0.00640535 -0.00959206 -0.121171 -0.117776
#: 21 -0.00959206 -0.0127788 -0.117776 -0.11438
#: 22 -0.0127788 -0.0159092 -0.11438 -0.110639
#: 23 -0.0159092 -0.0190394 -0.110639 -0.106896
#: 24 -0.0190394 -0.0220797 -0.106896 -0.0993528
#: 25 -0.0220797 -0.02512 -0.0993528 -0.0918102
#: 26 -0.02512 -0.0376801 -0.0918102 -0.0879993
#: 27 -0.0376801 -0.05024 -0.0879993 -0.0841885
#: 28 -0.05024 -0.05024 -0.0841885 -0.0729418
#: 29 -0.05024 -0.05024 -0.0729418 -0.0616951
#: 30 -0.05024 -0.05024 -0.0616951 -0.0509577
#: 31 -0.05024 -0.05024 -0.0509577 -0.0402203
#: 32 -0.05024 -0.05024 -0.0402203 -0.0299501
#: 33 -0.05024 -0.05024 -0.0299501 -0.01968
#: 34 -0.05024 -0.05024 -0.01968 -0.00984001
#: 35 -0.05024 -0.05024 -0.00984001 0.0
#: slice #: 10
#: 0 0.05024 0.05024 0.0 -0.00961399
#: 1 0.05024 0.05024 -0.00961399 -0.0192289
#: 2 0.05024 0.05024 -0.0192289 -0.0292959
#: 3 0.05024 0.05024 -0.0292959 -0.0393639
#: 4 0.05024 0.05024 -0.0393639 -0.0499258
#: 5 0.05024 0.05024 -0.0499258 -0.0604877
#: 6 0.05024 0.05024 -0.0604877 -0.0715857
#: 7 0.05024 0.05024 -0.0715857 -0.0826845
#: 8 0.05024 0.0376801 -0.0826845 -0.0861387
#: 9 0.0376801 0.02512 -0.0861387 -0.089592
#: 10 0.02512 0.022078 -0.089592 -0.0972662
#: 11 0.022078 0.0190361 -0.0972662 -0.10494
#: 12 0.0190361 0.0159044 -0.10494 -0.108764
#: 13 0.0159044 0.0127728 -0.108764 -0.112587
#: 14 0.0127728 0.00961566 -0.112587 -0.115829
#: 15 0.00961566 0.00645852 -0.115829 -0.11907
#: 16 0.00645852 0.00322914 -0.11907 -0.121596
#: 17 0.00322914 0.0 -0.121596 -0.124122
#: 18 0.0 -0.00320315 -0.124122 -0.121356
#: 19 -0.00320315 -0.00640631 -0.121356 -0.118589
#: 20 -0.00640631 -0.00959325 -0.118589 -0.115352
#: 21 -0.00959325 -0.0127802 -0.115352 -0.112114
#: 22 -0.0127802 -0.0159101 -0.112114 -0.108327
#: 23 -0.0159101 -0.0190403 -0.108327 -0.104539
#: 24 -0.0190403 -0.0220802 -0.104539 -0.0970659
#: 25 -0.0220802 -0.02512 -0.0970659 -0.089592
#: 26 -0.02512 -0.0376801 -0.089592 -0.0861387
#: 27 -0.0376801 -0.05024 -0.0861387 -0.0826845
#: 28 -0.05024 -0.05024 -0.0826845 -0.0715857
#: 29 -0.05024 -0.05024 -0.0715857 -0.0604877
#: 30 -0.05024 -0.05024 -0.0604877 -0.0499258
#: 31 -0.05024 -0.05024 -0.0499258 -0.0393639
#: 32 -0.05024 -0.05024 -0.0393639 -0.0292959
#: 33 -0.05024 -0.05024 -0.0292959 -0.0192289
#: 34 -0.05024 -0.05024 -0.0192289 -0.00961399
#: 35 -0.05024 -0.05024 -0.00961399 0.0
#: 0 0.05024 0.05024 0.0 -0.019454
#: 1 0.05024 0.05024 -0.019454 -0.0397921
#: 2 0.05024 0.05024 -0.0397921 -0.0610914
#: 3 0.05024 0.05024 -0.0610914 -0.083436
#: 4 0.05024 0.02512 -0.083436 -0.0907011
#: 5 0.02512 0.0190363 -0.0907011 -0.106105
#: 6 0.0190363 0.012773 -0.106105 -0.113699
#: 7 0.012773 0.00645876 -0.113699 -0.120309
#: 8 0.00645876 0.0 -0.120309 -0.125686
#: 9 0.0 -0.00640583 -0.125686 -0.11988
#: 10 -0.00640583 -0.0127795 -0.11988 -0.113247
#: 11 -0.0127795 -0.0190399 -0.113247 -0.105718
#: 12 -0.0190399 -0.02512 -0.105718 -0.0907011
#: 13 -0.02512 -0.05024 -0.0907011 -0.083436
#: 14 -0.05024 -0.05024 -0.083436 -0.0610914
#: 15 -0.05024 -0.05024 -0.0610914 -0.0397921
#: 16 -0.05024 -0.05024 -0.0397921 -0.019454
#: 17 -0.05024 -0.05024 -0.019454 0.0
#: 0 0.05024 0.05024 0.0 -0.00984001
#: 1 0.05024 0.05024 -0.00984001 -0.01968
#: 2 0.05024 0.05024 -0.01968 -0.0299501
#: 3 0.05024 0.05024 -0.0299501 -0.0402203
#: 4 0.05024 0.05024 -0.0402203 -0.0509577
#: 5 0.05024 0.05024 -0.0509577 -0.0616951
#: 6 0.05024 0.05024 -0.0616951 -0.0729418
#: 7 0.05024 0.05024 -0.0729418 -0.0841885
#: 8 0.05024 0.0376801 -0.0841885 -0.0879993
#: 9 0.0376801 0.02512 -0.0879993 -0.0918102
#: 10 0.02512 0.022078 -0.0918102 -0.0995398
#: 11 0.022078 0.0190363 -0.0995398 -0.10727
#: 12 0.0190363 0.0159049 -0.10727 -0.111041
#: 13 0.0159049 0.0127733 -0.111041 -0.114811
#: 14 0.0127733 0.0096159 -0.114811 -0.118179
#: 15 0.0096159 0.00645876 -0.118179 -0.121548
#: 16 0.00645876 0.00322938 -0.121548 -0.124398
#: 17 0.00322938 0.0 -0.124398 -0.12725
#: 18 0.0 -0.00320268 -0.12725 -0.12421
#: 19 -0.00320268 -0.00640535 -0.12421 -0.121171
#: 20 -0.00640535 -0.00959206 -0.121171 -0.117776
#: 21 -0.00959206 -0.0127788 -0.117776 -0.11438
#: 22 -0.0127788 -0.0159092 -0.11438 -0.110639
#: 23 -0.0159092 -0.0190394 -0.110639 -0.106896
#: 24 -0.0190394 -0.0220797 -0.106896 -0.0993528
#: 25 -0.0220797 -0.02512 -0.0993528 -0.0918102
#: 26 -0.02512 -0.0376801 -0.0918102 -0.0879993
#: 27 -0.0376801 -0.05024 -0.0879993 -0.0841885
#: 28 -0.05024 -0.05024 -0.0841885 -0.0729418
#: 29 -0.05024 -0.05024 -0.0729418 -0.0616951
#: 30 -0.05024 -0.05024 -0.0616951 -0.0509577
#: 31 -0.05024 -0.05024 -0.0509577 -0.0402203
#: 32 -0.05024 -0.05024 -0.0402203 -0.0299501
#: 33 -0.05024 -0.05024 -0.0299501 -0.01968
#: 34 -0.05024 -0.05024 -0.01968 -0.00984001
#: 35 -0.05024 -0.05024 -0.00984001 0.0
#: 0 0.05024 0.05024 0.0 -0.019906
#: 1 0.05024 0.05024 -0.019906 -0.0406485
#: 2 0.05024 0.05024 -0.0406485 -0.0622988
#: 3 0.05024 0.05024 -0.0622988 -0.08494
#: 4 0.05024 0.02512 -0.08494 -0.0929155
#: 5 0.02512 0.0190368 -0.0929155 -0.108413
#: 6 0.0190368 0.012774 -0.108413 -0.115894
#: 7 0.012774 0.00645924 -0.115894 -0.122764
#: 8 0.00645924 0.0 -0.122764 -0.12881
#: 9 0.0 -0.00640392 -0.12881 -0.122451
#: 10 -0.00640392 -0.0127764 -0.122451 -0.115501
#: 11 -0.0127764 -0.0190372 -0.115501 -0.108066
#: 12 -0.0190372 -0.02512 -0.108066 -0.0929155
#: 13 -0.02512 -0.05024 -0.0929155 -0.08494
#: 14 -0.05024 -0.05024 -0.08494 -0.0622988
#: 15 -0.05024 -0.05024 -0.0622988 -0.0406485
#: 16 -0.05024 -0.05024 -0.0406485 -0.019906
#: 17 -0.05024 -0.05024 -0.019906 0.0
#: 0 0.05024 0.05024 0.0 -0.010066
#: 1 0.05024 0.05024 -0.010066 -0.0201321
#: 2 0.05024 0.05024 -0.0201321 -0.0306044
#: 3 0.05024 0.05024 -0.0306044 -0.0410757
#: 4 0.05024 0.05024 -0.0410757 -0.0519896
#: 5 0.05024 0.05024 -0.0519896 -0.0629034
#: 6 0.05024 0.05024 -0.0629034 -0.0742979
#: 7 0.05024 0.05024 -0.0742979 -0.0856915
#: 8 0.05024 0.0376801 -0.0856915 -0.0898561
#: 9 0.0376801 0.02512 -0.0898561 -0.0940199
#: 10 0.02512 0.0220788 -0.0940199 -0.101789
#: 11 0.0220788 0.0190375 -0.101789 -0.109556
#: 12 0.0190375 0.0159061 -0.109556 -0.113267
#: 13 0.0159061 0.0127747 -0.113267 -0.116978
#: 14 0.0127747 0.00961709 -0.116978 -0.120479
#: 15 0.00961709 0.00645947 -0.120479 -0.123979
#: 16 0.00645947 0.00322962 -0.123979 -0.127174
#: 17 0.00322962 0.0 -0.127174 -0.13037
#: 18 0.0 -0.00320125 -0.13037 -0.127051
#: 19 -0.00320125 -0.00640249 -0.127051 -0.123732
#: 20 -0.00640249 -0.00958824 -0.123732 -0.120177
#: 21 -0.00958824 -0.0127738 -0.120177 -0.116623
#: 22 -0.0127738 -0.0159044 -0.116623 -0.112929
#: 23 -0.0159044 -0.0190349 -0.112929 -0.109236
#: 24 -0.0190349 -0.0220776 -0.109236 -0.101628
#: 25 -0.0220776 -0.02512 -0.101628 -0.0940199
#: 26 -0.02512 -0.0376801 -0.0940199 -0.0898561
#: 27 -0.0376801 -0.05024 -0.0898561 -0.0856915
#: 28 -0.05024 -0.05024 -0.0856915 -0.0742979
#: 29 -0.05024 -0.05024 -0.0742979 -0.0629034
#: 30 -0.05024 -0.05024 -0.0629034 -0.0519896
#: 31 -0.05024 -0.05024 -0.0519896 -0.0410757
#: 32 -0.05024 -0.05024 -0.0410757 -0.0306044
#: 33 -0.05024 -0.05024 -0.0306044 -0.0201321
#: 34 -0.05024 -0.05024 -0.0201321 -0.010066
#: 35 -0.05024 -0.05024 -0.010066 0.0
#: slice #: 11
#: 0 0.05024 0.05024 0.0 -0.00984001
#: 1 0.05024 0.05024 -0.00984001 -0.01968
#: 2 0.05024 0.05024 -0.01968 -0.0299501
#: 3 0.05024 0.05024 -0.0299501 -0.0402203
#: 4 0.05024 0.05024 -0.0402203 -0.0509577
#: 5 0.05024 0.05024 -0.0509577 -0.0616951
#: 6 0.05024 0.05024 -0.0616951 -0.0729418
#: 7 0.05024 0.05024 -0.0729418 -0.0841885
#: 8 0.05024 0.0376801 -0.0841885 -0.0879993
#: 9 0.0376801 0.02512 -0.0879993 -0.0918102
#: 10 0.02512 0.022078 -0.0918102 -0.0995398
#: 11 0.022078 0.0190363 -0.0995398 -0.10727
#: 12 0.0190363 0.0159049 -0.10727 -0.111041
#: 13 0.0159049 0.0127733 -0.111041 -0.114811
#: 14 0.0127733 0.0096159 -0.114811 -0.118179
#: 15 0.0096159 0.00645876 -0.118179 -0.121548
#: 16 0.00645876 0.00322938 -0.121548 -0.124398
#: 17 0.00322938 0.0 -0.124398 -0.12725
#: 18 0.0 -0.00320268 -0.12725 -0.12421
#: 19 -0.00320268 -0.00640535 -0.12421 -0.121171
#: 20 -0.00640535 -0.00959206 -0.121171 -0.117776
#: 21 -0.00959206 -0.0127788 -0.117776 -0.11438
#: 22 -0.0127788 -0.0159092 -0.11438 -0.110639
#: 23 -0.0159092 -0.0190394 -0.110639 -0.106896
#: 24 -0.0190394 -0.0220797 -0.106896 -0.0993528
#: 25 -0.0220797 -0.02512 -0.0993528 -0.0918102
#: 26 -0.02512 -0.0376801 -0.0918102 -0.0879993
#: 27 -0.0376801 -0.05024 -0.0879993 -0.0841885
#: 28 -0.05024 -0.05024 -0.0841885 -0.0729418
#: 29 -0.05024 -0.05024 -0.0729418 -0.0616951
#: 30 -0.05024 -0.05024 -0.0616951 -0.0509577
#: 31 -0.05024 -0.05024 -0.0509577 -0.0402203
#: 32 -0.05024 -0.05024 -0.0402203 -0.0299501
#: 33 -0.05024 -0.05024 -0.0299501 -0.01968
#: 34 -0.05024 -0.05024 -0.01968 -0.00984001
#: 35 -0.05024 -0.05024 -0.00984001 0.0
#: 0 0.05024 0.05024 0.0 -0.019906
#: 1 0.05024 0.05024 -0.019906 -0.0406485
#: 2 0.05024 0.05024 -0.0406485 -0.0622988
#: 3 0.05024 0.05024 -0.0622988 -0.08494
#: 4 0.05024 0.02512 -0.08494 -0.0929155
#: 5 0.02512 0.0190368 -0.0929155 -0.108413
#: 6 0.0190368 0.012774 -0.108413 -0.115894
#: 7 0.012774 0.00645924 -0.115894 -0.122764
#: 8 0.00645924 0.0 -0.122764 -0.12881
#: 9 0.0 -0.00640392 -0.12881 -0.122451
#: 10 -0.00640392 -0.0127764 -0.122451 -0.115501
#: 11 -0.0127764 -0.0190372 -0.115501 -0.108066
#: 12 -0.0190372 -0.02512 -0.108066 -0.0929155
#: 13 -0.02512 -0.05024 -0.0929155 -0.08494
#: 14 -0.05024 -0.05024 -0.08494 -0.0622988
#: 15 -0.05024 -0.05024 -0.0622988 -0.0406485
#: 16 -0.05024 -0.05024 -0.0406485 -0.019906
#: 17 -0.05024 -0.05024 -0.019906 0.0
#: 0 0.05024 0.05024 0.0 -0.010066
#: 1 0.05024 0.05024 -0.010066 -0.0201321
#: 2 0.05024 0.05024 -0.0201321 -0.0306044
#: 3 0.05024 0.05024 -0.0306044 -0.0410757
#: 4 0.05024 0.05024 -0.0410757 -0.0519896
#: 5 0.05024 0.05024 -0.0519896 -0.0629034
#: 6 0.05024 0.05024 -0.0629034 -0.0742979
#: 7 0.05024 0.05024 -0.0742979 -0.0856915
#: 8 0.05024 0.0376801 -0.0856915 -0.0898561
#: 9 0.0376801 0.02512 -0.0898561 -0.0940199
#: 10 0.02512 0.0220788 -0.0940199 -0.101789
#: 11 0.0220788 0.0190375 -0.101789 -0.109556
#: 12 0.0190375 0.0159061 -0.109556 -0.113267
#: 13 0.0159061 0.0127747 -0.113267 -0.116978
#: 14 0.0127747 0.00961709 -0.116978 -0.120479
#: 15 0.00961709 0.00645947 -0.120479 -0.123979
#: 16 0.00645947 0.00322962 -0.123979 -0.127174
#: 17 0.00322962 0.0 -0.127174 -0.13037
#: 18 0.0 -0.00320125 -0.13037 -0.127051
#: 19 -0.00320125 -0.00640249 -0.127051 -0.123732
#: 20 -0.00640249 -0.00958824 -0.123732 -0.120177
#: 21 -0.00958824 -0.0127738 -0.120177 -0.116623
#: 22 -0.0127738 -0.0159044 -0.116623 -0.112929
#: 23 -0.0159044 -0.0190349 -0.112929 -0.109236
#: 24 -0.0190349 -0.0220776 -0.109236 -0.101628
#: 25 -0.0220776 -0.02512 -0.101628 -0.0940199
#: 26 -0.02512 -0.0376801 -0.0940199 -0.0898561
#: 27 -0.0376801 -0.05024 -0.0898561 -0.0856915
#: 28 -0.05024 -0.05024 -0.0856915 -0.0742979
#: 29 -0.05024 -0.05024 -0.0742979 -0.0629034
#: 30 -0.05024 -0.05024 -0.0629034 -0.0519896
#: 31 -0.05024 -0.05024 -0.0519896 -0.0410757
#: 32 -0.05024 -0.05024 -0.0410757 -0.0306044
#: 33 -0.05024 -0.05024 -0.0306044 -0.0201321
#: 34 -0.05024 -0.05024 -0.0201321 -0.010066
#: 35 -0.05024 -0.05024 -0.010066 0.0
#: 0 0.05024 0.05024 0.0 -0.0203581
#: 1 0.05024 0.05024 -0.0203581 -0.0415039
#: 2 0.05024 0.05024 -0.0415039 -0.0635071
#: 3 0.05024 0.05024 -0.0635071 -0.0864439
#: 4 0.05024 0.02512 -0.0864439 -0.0951109
#: 5 0.02512 0.0190389 -0.0951109 -0.110644
#: 6 0.0190389 0.0127766 -0.110644 -0.117999
#: 7 0.0127766 0.00645995 -0.117999 -0.125142
#: 8 0.00645995 0.0 -0.125142 -0.131916
#: 9 0.0 -0.00639915 -0.131916 -0.124969
#: 10 -0.00639915 -0.0127678 -0.124969 -0.117698
#: 11 -0.0127678 -0.0190296 -0.117698 -0.110367
#: 12 -0.0190296 -0.02512 -0.110367 -0.0951109
#: 13 -0.02512 -0.05024 -0.0951109 -0.0864439
#: 14 -0.05024 -0.05024 -0.0864439 -0.0635071
#: 15 -0.05024 -0.05024 -0.0635071 -0.0415039
#: 16 -0.05024 -0.05024 -0.0415039 -0.0203581
#: 17 -0.05024 -0.05024 -0.0203581 0.0
#: 0 0.05024 0.05024 0.0 -0.0102921
#: 1 0.05024 0.05024 -0.0102921 -0.0205841
#: 2 0.05024 0.05024 -0.0205841 -0.0312586
#: 3 0.05024 0.05024 -0.0312586 -0.0419321
#: 4 0.05024 0.05024 -0.0419321 -0.0530214
#: 5 0.05024 0.05024 -0.0530214 -0.0641108
#: 6 0.05024 0.05024 -0.0641108 -0.0756531
#: 7 0.05024 0.05024 -0.0756531 -0.0871954
#: 8 0.05024 0.0376801 -0.0871954 -0.0916986
#: 9 0.0376801 0.02512 -0.0916986 -0.0962029
#: 10 0.02512 0.0220802 -0.0962029 -0.103969
#: 11 0.0220802 0.0190403 -0.103969 -0.111733
#: 12 0.0190403 0.0159094 -0.111733 -0.115376
#: 13 0.0159094 0.0127785 -0.115376 -0.11902
#: 14 0.0127785 0.00961947 -0.11902 -0.122663
#: 15 0.00961947 0.00646043 -0.122663 -0.126305
#: 16 0.00646043 0.00323009 -0.126305 -0.129884
#: 17 0.00323009 0.0 -0.129884 -0.133462
#: 18 0.0 -0.00319767 -0.133462 -0.129834
#: 19 -0.00319767 -0.00639558 -0.129834 -0.126207
#: 20 -0.00639558 -0.0095787 -0.126207 -0.12249
#: 21 -0.0095787 -0.0127616 -0.12249 -0.118773
#: 22 -0.0127616 -0.015893 -0.118773 -0.115135
#: 23 -0.015893 -0.0190246 -0.115135 -0.111498
#: 24 -0.0190246 -0.0220723 -0.111498 -0.10385
#: 25 -0.0220723 -0.02512 -0.10385 -0.0962029
#: 26 -0.02512 -0.0376801 -0.0962029 -0.0916986
#: 27 -0.0376801 -0.05024 -0.0916986 -0.0871954
#: 28 -0.05024 -0.05024 -0.0871954 -0.0756531
#: 29 -0.05024 -0.05024 -0.0756531 -0.0641108
#: 30 -0.05024 -0.05024 -0.0641108 -0.0530214
#: 31 -0.05024 -0.05024 -0.0530214 -0.0419321
#: 32 -0.05024 -0.05024 -0.0419321 -0.0312586
#: 33 -0.05024 -0.05024 -0.0312586 -0.0205841
#: 34 -0.05024 -0.05024 -0.0205841 -0.0102921
#: 35 -0.05024 -0.05024 -0.0102921 0.0
#: slice #: 12
#: 0 0.05024 0.05024 0.0 -0.010066
#: 1 0.05024 0.05024 -0.010066 -0.0201321
#: 2 0.05024 0.05024 -0.0201321 -0.0306044
#: 3 0.05024 0.05024 -0.0306044 -0.0410757
#: 4 0.05024 0.05024 -0.0410757 -0.0519896
#: 5 0.05024 0.05024 -0.0519896 -0.0629034
#: 6 0.05024 0.05024 -0.0629034 -0.0742979
#: 7 0.05024 0.05024 -0.0742979 -0.0856915
#: 8 0.05024 0.0376801 -0.0856915 -0.0898561
#: 9 0.0376801 0.02512 -0.0898561 -0.0940199
#: 10 0.02512 0.0220788 -0.0940199 -0.101789
#: 11 0.0220788 0.0190375 -0.101789 -0.109556
#: 12 0.0190375 0.0159061 -0.109556 -0.113267
#: 13 0.0159061 0.0127747 -0.113267 -0.116978
#: 14 0.0127747 0.00961709 -0.116978 -0.120479
#: 15 0.00961709 0.00645947 -0.120479 -0.123979
#: 16 0.00645947 0.00322962 -0.123979 -0.127174
#: 17 0.00322962 0.0 -0.127174 -0.13037
#: 18 0.0 -0.00320125 -0.13037 -0.127051
#: 19 -0.00320125 -0.00640249 -0.127051 -0.123732
#: 20 -0.00640249 -0.00958824 -0.123732 -0.120177
#: 21 -0.00958824 -0.0127738 -0.120177 -0.116623
#: 22 -0.0127738 -0.0159044 -0.116623 -0.112929
#: 23 -0.0159044 -0.0190349 -0.112929 -0.109236
#: 24 -0.0190349 -0.0220776 -0.109236 -0.101628
#: 25 -0.0220776 -0.02512 -0.101628 -0.0940199
#: 26 -0.02512 -0.0376801 -0.0940199 -0.0898561
#: 27 -0.0376801 -0.05024 -0.0898561 -0.0856915
#: 28 -0.05024 -0.05024 -0.0856915 -0.0742979
#: 29 -0.05024 -0.05024 -0.0742979 -0.0629034
#: 30 -0.05024 -0.05024 -0.0629034 -0.0519896
#: 31 -0.05024 -0.05024 -0.0519896 -0.0410757
#: 32 -0.05024 -0.05024 -0.0410757 -0.0306044
#: 33 -0.05024 -0.05024 -0.0306044 -0.0201321
#: 34 -0.05024 -0.05024 -0.0201321 -0.010066
#: 35 -0.05024 -0.05024 -0.010066 0.0
#: 0 0.05024 0.05024 0.0 -0.0203581
#: 1 0.05024 0.05024 -0.0203581 -0.0415039
#: 2 0.05024 0.05024 -0.0415039 -0.0635071
#: 3 0.05024 0.05024 -0.0635071 -0.0864439
#: 4 0.05024 0.02512 -0.0864439 -0.0951109
#: 5 0.02512 0.0190389 -0.0951109 -0.110644
#: 6 0.0190389 0.0127766 -0.110644 -0.117999
#: 7 0.0127766 0.00645995 -0.117999 -0.125142
#: 8 0.00645995 0.0 -0.125142 -0.131916
#: 9 0.0 -0.00639915 -0.131916 -0.124969
#: 10 -0.00639915 -0.0127678 -0.124969 -0.117698
#: 11 -0.0127678 -0.0190296 -0.117698 -0.110367
#: 12 -0.0190296 -0.02512 -0.110367 -0.0951109
#: 13 -0.02512 -0.05024 -0.0951109 -0.0864439
#: 14 -0.05024 -0.05024 -0.0864439 -0.0635071
#: 15 -0.05024 -0.05024 -0.0635071 -0.0415039
#: 16 -0.05024 -0.05024 -0.0415039 -0.0203581
#: 17 -0.05024 -0.05024 -0.0203581 0.0
#: 0 0.05024 0.05024 0.0 -0.0102921
#: 1 0.05024 0.05024 -0.0102921 -0.0205841
#: 2 0.05024 0.05024 -0.0205841 -0.0312586
#: 3 0.05024 0.05024 -0.0312586 -0.0419321
#: 4 0.05024 0.05024 -0.0419321 -0.0530214
#: 5 0.05024 0.05024 -0.0530214 -0.0641108
#: 6 0.05024 0.05024 -0.0641108 -0.0756531
#: 7 0.05024 0.05024 -0.0756531 -0.0871954
#: 8 0.05024 0.0376801 -0.0871954 -0.0916986
#: 9 0.0376801 0.02512 -0.0916986 -0.0962029
#: 10 0.02512 0.0220802 -0.0962029 -0.103969
#: 11 0.0220802 0.0190403 -0.103969 -0.111733
#: 12 0.0190403 0.0159094 -0.111733 -0.115376
#: 13 0.0159094 0.0127785 -0.115376 -0.11902
#: 14 0.0127785 0.00961947 -0.11902 -0.122663
#: 15 0.00961947 0.00646043 -0.122663 -0.126305
#: 16 0.00646043 0.00323009 -0.126305 -0.129884
#: 17 0.00323009 0.0 -0.129884 -0.133462
#: 18 0.0 -0.00319767 -0.133462 -0.129834
#: 19 -0.00319767 -0.00639558 -0.129834 -0.126207
#: 20 -0.00639558 -0.0095787 -0.126207 -0.12249
#: 21 -0.0095787 -0.0127616 -0.12249 -0.118773
#: 22 -0.0127616 -0.015893 -0.118773 -0.115135
#: 23 -0.015893 -0.0190246 -0.115135 -0.111498
#: 24 -0.0190246 -0.0220723 -0.111498 -0.10385
#: 25 -0.0220723 -0.02512 -0.10385 -0.0962029
#: 26 -0.02512 -0.0376801 -0.0962029 -0.0916986
#: 27 -0.0376801 -0.05024 -0.0916986 -0.0871954
#: 28 -0.05024 -0.05024 -0.0871954 -0.0756531
#: 29 -0.05024 -0.05024 -0.0756531 -0.0641108
#: 30 -0.05024 -0.05024 -0.0641108 -0.0530214
#: 31 -0.05024 -0.05024 -0.0530214 -0.0419321
#: 32 -0.05024 -0.05024 -0.0419321 -0.0312586
#: 33 -0.05024 -0.05024 -0.0312586 -0.0205841
#: 34 -0.05024 -0.05024 -0.0205841 -0.0102921
#: 35 -0.05024 -0.05024 -0.0102921 0.0
#: 0 0.05024 0.05024 0.0 -0.0208101
#: 1 0.05024 0.05024 -0.0208101 -0.0423594
#: 2 0.05024 0.05024 -0.0423594 -0.0647154
#: 3 0.05024 0.05024 -0.0647154 -0.0879469
#: 4 0.05024 0.02512 -0.0879469 -0.0972567
#: 5 0.02512 0.0190439 -0.0972567 -0.112704
#: 6 0.0190439 0.0127833 -0.112704 -0.119914
#: 7 0.0127833 0.00645971 -0.119914 -0.127355
#: 8 0.00645971 0.0 -0.127355 -0.134969
#: 9 0.0 -0.00639153 -0.134969 -0.127324
#: 10 -0.00639153 -0.012753 -0.127324 -0.119724
#: 11 -0.012753 -0.0190163 -0.119724 -0.112519
#: 12 -0.0190163 -0.02512 -0.112519 -0.0972567
#: 13 -0.02512 -0.05024 -0.0972567 -0.0879469
#: 14 -0.05024 -0.05024 -0.0879469 -0.0647154
#: 15 -0.05024 -0.05024 -0.0647154 -0.0423594
#: 16 -0.05024 -0.05024 -0.0423594 -0.0208101
#: 17 -0.05024 -0.05024 -0.0208101 0.0
#: 0 0.05024 0.05024 0.0 -0.0105181
#: 1 0.05024 0.05024 -0.0105181 -0.0210361
#: 2 0.05024 0.05024 -0.0210361 -0.0319118
#: 3 0.05024 0.05024 -0.0319118 -0.0427876
#: 4 0.05024 0.05024 -0.0427876 -0.0540533
#: 5 0.05024 0.05024 -0.0540533 -0.0653191
#: 6 0.05024 0.05024 -0.0653191 -0.0770082
#: 7 0.05024 0.05024 -0.0770082 -0.0886984
#: 8 0.05024 0.0376801 -0.0886984 -0.093504
#: 9 0.0376801 0.02512 -0.093504 -0.0983095
#: 10 0.02512 0.0220838 -0.0983095 -0.105992
#: 11 0.0220838 0.0190477 -0.105992 -0.113675
#: 12 0.0190477 0.0159178 -0.113675 -0.117242
#: 13 0.0159178 0.0127881 -0.117242 -0.12081
#: 14 0.0127881 0.00962353 -0.12081 -0.124606
#: 15 0.00962353 0.006459 -0.124606 -0.128404
#: 16 0.006459 0.00322962 -0.128404 -0.13244
#: 17 0.00322962 0.0 -0.13244 -0.136476
#: 18 0.0 -0.00319386 -0.136476 -0.132459
#: 19 -0.00319386 -0.00638747 -0.132459 -0.128442
#: 20 -0.00638747 -0.00956583 -0.128442 -0.124558
#: 21 -0.00956583 -0.0127442 -0.124558 -0.120676
#: 22 -0.0127442 -0.0158763 -0.120676 -0.117108
#: 23 -0.0158763 -0.0190082 -0.117108 -0.113542
#: 24 -0.0190082 -0.0220642 -0.113542 -0.105926
#: 25 -0.0220642 -0.02512 -0.105926 -0.0983095
#: 26 -0.02512 -0.0376801 -0.0983095 -0.093504
#: 27 -0.0376801 -0.05024 -0.093504 -0.0886984
#: 28 -0.05024 -0.05024 -0.0886984 -0.0770082
#: 29 -0.05024 -0.05024 -0.0770082 -0.0653191
#: 30 -0.05024 -0.05024 -0.0653191 -0.0540533
#: 31 -0.05024 -0.05024 -0.0540533 -0.0427876
#: 32 -0.05024 -0.05024 -0.0427876 -0.0319118
#: 33 -0.05024 -0.05024 -0.0319118 -0.0210361
#: 34 -0.05024 -0.05024 -0.0210361 -0.0105181
#: 35 -0.05024 -0.05024 -0.0105181 0.0
#: slice #: 13
#: 0 0.05024 0.05024 0.0 -0.0102921
#: 1 0.05024 0.05024 -0.0102921 -0.0205841
#: 2 0.05024 0.05024 -0.0205841 -0.0312586
#: 3 0.05024 0.05024 -0.0312586 -0.0419321
#: 4 0.05024 0.05024 -0.0419321 -0.0530214
#: 5 0.05024 0.05024 -0.0530214 -0.0641108
#: 6 0.05024 0.05024 -0.0641108 -0.0756531
#: 7 0.05024 0.05024 -0.0756531 -0.0871954
#: 8 0.05024 0.0376801 -0.0871954 -0.0916986
#: 9 0.0376801 0.02512 -0.0916986 -0.0962029
#: 10 0.02512 0.0220802 -0.0962029 -0.103969
#: 11 0.0220802 0.0190403 -0.103969 -0.111733
#: 12 0.0190403 0.0159094 -0.111733 -0.115376
#: 13 0.0159094 0.0127785 -0.115376 -0.11902
#: 14 0.0127785 0.00961947 -0.11902 -0.122663
#: 15 0.00961947 0.00646043 -0.122663 -0.126305
#: 16 0.00646043 0.00323009 -0.126305 -0.129884
#: 17 0.00323009 0.0 -0.129884 -0.133462
#: 18 0.0 -0.00319767 -0.133462 -0.129834
#: 19 -0.00319767 -0.00639558 -0.129834 -0.126207
#: 20 -0.00639558 -0.0095787 -0.126207 -0.12249
#: 21 -0.0095787 -0.0127616 -0.12249 -0.118773
#: 22 -0.0127616 -0.015893 -0.118773 -0.115135
#: 23 -0.015893 -0.0190246 -0.115135 -0.111498
#: 24 -0.0190246 -0.0220723 -0.111498 -0.10385
#: 25 -0.0220723 -0.02512 -0.10385 -0.0962029
#: 26 -0.02512 -0.0376801 -0.0962029 -0.0916986
#: 27 -0.0376801 -0.05024 -0.0916986 -0.0871954
#: 28 -0.05024 -0.05024 -0.0871954 -0.0756531
#: 29 -0.05024 -0.05024 -0.0756531 -0.0641108
#: 30 -0.05024 -0.05024 -0.0641108 -0.0530214
#: 31 -0.05024 -0.05024 -0.0530214 -0.0419321
#: 32 -0.05024 -0.05024 -0.0419321 -0.0312586
#: 33 -0.05024 -0.05024 -0.0312586 -0.0205841
#: 34 -0.05024 -0.05024 -0.0205841 -0.0102921
#: 35 -0.05024 -0.05024 -0.0102921 0.0
#: 0 0.05024 0.05024 0.0 -0.0208101
#: 1 0.05024 0.05024 -0.0208101 -0.0423594
#: 2 0.05024 0.05024 -0.0423594 -0.0647154
#: 3 0.05024 0.05024 -0.0647154 -0.0879469
#: 4 0.05024 0.02512 -0.0879469 -0.0972567
#: 5 0.02512 0.0190439 -0.0972567 -0.112704
#: 6 0.0190439 0.0127833 -0.112704 -0.119914
#: 7 0.0127833 0.00645971 -0.119914 -0.127355
#: 8 0.00645971 0.0 -0.127355 -0.134969
#: 9 0.0 -0.00639153 -0.134969 -0.127324
#: 10 -0.00639153 -0.012753 -0.127324 -0.119724
#: 11 -0.012753 -0.0190163 -0.119724 -0.112519
#: 12 -0.0190163 -0.02512 -0.112519 -0.0972567
#: 13 -0.02512 -0.05024 -0.0972567 -0.0879469
#: 14 -0.05024 -0.05024 -0.0879469 -0.0647154
#: 15 -0.05024 -0.05024 -0.0647154 -0.0423594
#: 16 -0.05024 -0.05024 -0.0423594 -0.0208101
#: 17 -0.05024 -0.05024 -0.0208101 0.0
#: 0 0.05024 0.05024 0.0 -0.0105181
#: 1 0.05024 0.05024 -0.0105181 -0.0210361
#: 2 0.05024 0.05024 -0.0210361 -0.0319118
#: 3 0.05024 0.05024 -0.0319118 -0.0427876
#: 4 0.05024 0.05024 -0.0427876 -0.0540533
#: 5 0.05024 0.05024 -0.0540533 -0.0653191
#: 6 0.05024 0.05024 -0.0653191 -0.0770082
#: 7 0.05024 0.05024 -0.0770082 -0.0886984
#: 8 0.05024 0.0376801 -0.0886984 -0.093504
#: 9 0.0376801 0.02512 -0.093504 -0.0983095
#: 10 0.02512 0.0220838 -0.0983095 -0.105992
#: 11 0.0220838 0.0190477 -0.105992 -0.113675
#: 12 0.0190477 0.0159178 -0.113675 -0.117242
#: 13 0.0159178 0.0127881 -0.117242 -0.12081
#: 14 0.0127881 0.00962353 -0.12081 -0.124606
#: 15 0.00962353 0.006459 -0.124606 -0.128404
#: 16 0.006459 0.00322962 -0.128404 -0.13244
#: 17 0.00322962 0.0 -0.13244 -0.136476
#: 18 0.0 -0.00319386 -0.136476 -0.132459
#: 19 -0.00319386 -0.00638747 -0.132459 -0.128442
#: 20 -0.00638747 -0.00956583 -0.128442 -0.124558
#: 21 -0.00956583 -0.0127442 -0.124558 -0.120676
#: 22 -0.0127442 -0.0158763 -0.120676 -0.117108
#: 23 -0.0158763 -0.0190082 -0.117108 -0.113542
#: 24 -0.0190082 -0.0220642 -0.113542 -0.105926
#: 25 -0.0220642 -0.02512 -0.105926 -0.0983095
#: 26 -0.02512 -0.0376801 -0.0983095 -0.093504
#: 27 -0.0376801 -0.05024 -0.093504 -0.0886984
#: 28 -0.05024 -0.05024 -0.0886984 -0.0770082
#: 29 -0.05024 -0.05024 -0.0770082 -0.0653191
#: 30 -0.05024 -0.05024 -0.0653191 -0.0540533
#: 31 -0.05024 -0.05024 -0.0540533 -0.0427876
#: 32 -0.05024 -0.05024 -0.0427876 -0.0319118
#: 33 -0.05024 -0.05024 -0.0319118 -0.0210361
#: 34 -0.05024 -0.05024 -0.0210361 -0.0105181
#: 35 -0.05024 -0.05024 -0.0105181 0.0
#: 0 0.05024 0.05024 0.0 -0.0212622
#: 1 0.05024 0.05024 -0.0212622 -0.0432158
#: 2 0.05024 0.05024 -0.0432158 -0.0659227
#: 3 0.05024 0.05024 -0.0659227 -0.0894499
#: 4 0.05024 0.02512 -0.0894499 -0.0992556
#: 5 0.02512 0.0190539 -0.0992556 -0.114408
#: 6 0.0190539 0.0128009 -0.114408 -0.121479
#: 7 0.0128009 0.00645018 -0.121479 -0.129239
#: 8 0.00645018 0.0 -0.129239 -0.137592
#: 9 0.0 -0.0064137 -0.137592 -0.129209
#: 10 -0.0064137 -0.012779 -0.129209 -0.121346
#: 11 -0.012779 -0.0190349 -0.121346 -0.114295
#: 12 -0.0190349 -0.02512 -0.114295 -0.0992556
#: 13 -0.02512 -0.05024 -0.0992556 -0.0894499
#: 14 -0.05024 -0.05024 -0.0894499 -0.0659227
#: 15 -0.05024 -0.05024 -0.0659227 -0.0432158
#: 16 -0.05024 -0.05024 -0.0432158 -0.0212622
#: 17 -0.05024 -0.05024 -0.0212622 0.0
#: 0 0.05024 0.05024 0.0 -0.0107431
#: 1 0.05024 0.05024 -0.0107431 -0.0214872
#: 2 0.05024 0.05024 -0.0214872 -0.0325651
#: 3 0.05024 0.05024 -0.0325651 -0.043643
#: 4 0.05024 0.05024 -0.043643 -0.0550852
#: 5 0.05024 0.05024 -0.0550852 -0.0665274
#: 6 0.05024 0.05024 -0.0665274 -0.0783644
#: 7 0.05024 0.05024 -0.0783644 -0.0902023
#: 8 0.05024 0.0376801 -0.0902023 -0.0952024
#: 9 0.0376801 0.02512 -0.0952024 -0.100202
#: 10 0.02512 0.02209 -0.100202 -0.107671
#: 11 0.02209 0.0190601 -0.107671 -0.115139
#: 12 0.0190601 0.0159369 -0.115139 -0.118644
#: 13 0.0159369 0.0128138 -0.118644 -0.122149
#: 14 0.0128138 0.00962758 -0.122149 -0.126112
#: 15 0.00962758 0.00644135 -0.126112 -0.130075
#: 16 0.00644135 0.00322056 -0.130075 -0.134393
#: 17 0.00322056 0.0 -0.134393 -0.138709
#: 18 0.0 -0.00322008 -0.138709 -0.134343
#: 19 -0.00322008 -0.00643992 -0.134343 -0.129976
#: 20 -0.00643992 -0.00962687 -0.129976 -0.125997
#: 21 -0.00962687 -0.0128138 -0.125997 -0.122018
#: 22 -0.0128138 -0.0159378 -0.122018 -0.118533
#: 23 -0.0159378 -0.0190616 -0.118533 -0.115049
#: 24 -0.0190616 -0.0220909 -0.115049 -0.107625
#: 25 -0.0220909 -0.02512 -0.107625 -0.100202
#: 26 -0.02512 -0.0376801 -0.100202 -0.0952024
#: 27 -0.0376801 -0.05024 -0.0952024 -0.0902023
#: 28 -0.05024 -0.05024 -0.0902023 -0.0783644
#: 29 -0.05024 -0.05024 -0.0783644 -0.0665274
#: 30 -0.05024 -0.05024 -0.0665274 -0.0550852
#: 31 -0.05024 -0.05024 -0.0550852 -0.043643
#: 32 -0.05024 -0.05024 -0.043643 -0.0325651
#: 33 -0.05024 -0.05024 -0.0325651 -0.0214872
#: 34 -0.05024 -0.05024 -0.0214872 -0.0107431
#: 35 -0.05024 -0.05024 -0.0107431 0.0
#: slice #: 14
#: 0 0.05024 0.05024 0.0 -0.0105181
#: 1 0.05024 0.05024 -0.0105181 -0.0210361
#: 2 0.05024 0.05024 -0.0210361 -0.0319118
#: 3 0.05024 0.05024 -0.0319118 -0.0427876
#: 4 0.05024 0.05024 -0.0427876 -0.0540533
#: 5 0.05024 0.05024 -0.0540533 -0.0653191
#: 6 0.05024 0.05024 -0.0653191 -0.0770082
#: 7 0.05024 0.05024 -0.0770082 -0.0886984
#: 8 0.05024 0.0376801 -0.0886984 -0.093504
#: 9 0.0376801 0.02512 -0.093504 -0.0983095
#: 10 0.02512 0.0220838 -0.0983095 -0.105992
#: 11 0.0220838 0.0190477 -0.105992 -0.113675
#: 12 0.0190477 0.0159178 -0.113675 -0.117242
#: 13 0.0159178 0.0127881 -0.117242 -0.12081
#: 14 0.0127881 0.00962353 -0.12081 -0.124606
#: 15 0.00962353 0.006459 -0.124606 -0.128404
#: 16 0.006459 0.00322962 -0.128404 -0.13244
#: 17 0.00322962 0.0 -0.13244 -0.136476
#: 18 0.0 -0.00319386 -0.136476 -0.132459
#: 19 -0.00319386 -0.00638747 -0.132459 -0.128442
#: 20 -0.00638747 -0.00956583 -0.128442 -0.124558
#: 21 -0.00956583 -0.0127442 -0.124558 -0.120676
#: 22 -0.0127442 -0.0158763 -0.120676 -0.117108
#: 23 -0.0158763 -0.0190082 -0.117108 -0.113542
#: 24 -0.0190082 -0.0220642 -0.113542 -0.105926
#: 25 -0.0220642 -0.02512 -0.105926 -0.0983095
#: 26 -0.02512 -0.0376801 -0.0983095 -0.093504
#: 27 -0.0376801 -0.05024 -0.093504 -0.0886984
#: 28 -0.05024 -0.05024 -0.0886984 -0.0770082
#: 29 -0.05024 -0.05024 -0.0770082 -0.0653191
#: 30 -0.05024 -0.05024 -0.0653191 -0.0540533
#: 31 -0.05024 -0.05024 -0.0540533 -0.0427876
#: 32 -0.05024 -0.05024 -0.0427876 -0.0319118
#: 33 -0.05024 -0.05024 -0.0319118 -0.0210361
#: 34 -0.05024 -0.05024 -0.0210361 -0.0105181
#: 35 -0.05024 -0.05024 -0.0105181 0.0
#: 0 0.05024 0.05024 0.0 -0.0212622
#: 1 0.05024 0.05024 -0.0212622 -0.0432158
#: 2 0.05024 0.05024 -0.0432158 -0.0659227
#: 3 0.05024 0.05024 -0.0659227 -0.0894499
#: 4 0.05024 0.02512 -0.0894499 -0.0992556
#: 5 0.02512 0.0190539 -0.0992556 -0.114408
#: 6 0.0190539 0.0128009 -0.114408 -0.121479
#: 7 0.0128009 0.00645018 -0.121479 -0.129239
#: 8 0.00645018 0.0 -0.129239 -0.137592
#: 9 0.0 -0.0064137 -0.137592 -0.129209
#: 10 -0.0064137 -0.012779 -0.129209 -0.121346
#: 11 -0.012779 -0.0190349 -0.121346 -0.114295
#: 12 -0.0190349 -0.02512 -0.114295 -0.0992556
#: 13 -0.02512 -0.05024 -0.0992556 -0.0894499
#: 14 -0.05024 -0.05024 -0.0894499 -0.0659227
#: 15 -0.05024 -0.05024 -0.0659227 -0.0432158
#: 16 -0.05024 -0.05024 -0.0432158 -0.0212622
#: 17 -0.05024 -0.05024 -0.0212622 0.0
#: 0 0.05024 0.05024 0.0 -0.0107431
#: 1 0.05024 0.05024 -0.0107431 -0.0214872
#: 2 0.05024 0.05024 -0.0214872 -0.0325651
#: 3 0.05024 0.05024 -0.0325651 -0.043643
#: 4 0.05024 0.05024 -0.043643 -0.0550852
#: 5 0.05024 0.05024 -0.0550852 -0.0665274
#: 6 0.05024 0.05024 -0.0665274 -0.0783644
#: 7 0.05024 0.05024 -0.0783644 -0.0902023
#: 8 0.05024 0.0376801 -0.0902023 -0.0952024
#: 9 0.0376801 0.02512 -0.0952024 -0.100202
#: 10 0.02512 0.02209 -0.100202 -0.107671
#: 11 0.02209 0.0190601 -0.107671 -0.115139
#: 12 0.0190601 0.0159369 -0.115139 -0.118644
#: 13 0.0159369 0.0128138 -0.118644 -0.122149
#: 14 0.0128138 0.00962758 -0.122149 -0.126112
#: 15 0.00962758 0.00644135 -0.126112 -0.130075
#: 16 0.00644135 0.00322056 -0.130075 -0.134393
#: 17 0.00322056 0.0 -0.134393 -0.138709
#: 18 0.0 -0.00322008 -0.138709 -0.134343
#: 19 -0.00322008 -0.00643992 -0.134343 -0.129976
#: 20 -0.00643992 -0.00962687 -0.129976 -0.125997
#: 21 -0.00962687 -0.0128138 -0.125997 -0.122018
#: 22 -0.0128138 -0.0159378 -0.122018 -0.118533
#: 23 -0.0159378 -0.0190616 -0.118533 -0.115049
#: 24 -0.0190616 -0.0220909 -0.115049 -0.107625
#: 25 -0.0220909 -0.02512 -0.107625 -0.100202
#: 26 -0.02512 -0.0376801 -0.100202 -0.0952024
#: 27 -0.0376801 -0.05024 -0.0952024 -0.0902023
#: 28 -0.05024 -0.05024 -0.0902023 -0.0783644
#: 29 -0.05024 -0.05024 -0.0783644 -0.0665274
#: 30 -0.05024 -0.05024 -0.0665274 -0.0550852
#: 31 -0.05024 -0.05024 -0.0550852 -0.043643
#: 32 -0.05024 -0.05024 -0.043643 -0.0325651
#: 33 -0.05024 -0.05024 -0.0325651 -0.0214872
#: 34 -0.05024 -0.05024 -0.0214872 -0.0107431
#: 35 -0.05024 -0.05024 -0.0107431 0.0
#: 0 0.05024 0.05024 0.0 -0.0217133
#: 1 0.05024 0.05024 -0.0217133 -0.0440712
#: 2 0.05024 0.05024 -0.0440712 -0.067131
#: 3 0.05024 0.05024 -0.067131 -0.0909538
#: 4 0.05024 0.02512 -0.0909538 -0.100758
#: 5 0.02512 0.019031 -0.100758 -0.115566
#: 6 0.019031 0.0127788 -0.115566 -0.122603
#: 7 0.0127788 0.00641489 -0.122603 -0.130586
#: 8 0.00641489 0.0 -0.130586 -0.139159
#: 9 0.0 -0.00644922 -0.139159 -0.130361
#: 10 -0.00644922 -0.0128009 -0.130361 -0.122428
#: 11 -0.0128009 -0.0190549 -0.122428 -0.115491
#: 12 -0.0190549 -0.02512 -0.115491 -0.10084
#: 13 -0.02512 -0.05024 -0.10084 -0.0909538
#: 14 -0.05024 -0.05024 -0.0909538 -0.067131
#: 15 -0.05024 -0.05024 -0.067131 -0.0440712
#: 16 -0.05024 -0.05024 -0.0440712 -0.0217133
#: 17 -0.05024 -0.05024 -0.0217133 0.0
#: 0 0.05024 0.05024 0.0 -0.0109701
#: 1 0.05024 0.05024 -0.0109701 -0.0219393
#: 2 0.05024 0.05024 -0.0219393 -0.0332193
#: 3 0.05024 0.05024 -0.0332193 -0.0444994
#: 4 0.05024 0.05024 -0.0444994 -0.0561171
#: 5 0.05024 0.05024 -0.0561171 -0.0677347
#: 6 0.05024 0.05024 -0.0677347 -0.0797205
#: 7 0.05024 0.05024 -0.0797205 -0.0917053
#: 8 0.05024 0.0376801 -0.0917053 -0.096509
#: 9 0.0376801 0.02512 -0.096509 -0.101314
#: 10 0.02512 0.0220609 -0.101314 -0.108653
#: 11 0.0220609 0.019002 -0.108653 -0.115993
#: 12 0.019002 0.015873 -0.115993 -0.119526
#: 13 0.015873 0.0127437 -0.119526 -0.123058
#: 14 0.0127437 0.00956607 -0.123058 -0.127077
#: 15 0.00956607 0.00638843 -0.127077 -0.131096
#: 16 0.00638843 0.00319433 -0.131096 -0.135352
#: 17 0.00319433 0.0 -0.135352 -0.139609
#: 18 0.0 -0.00322914 -0.139609 -0.135178
#: 19 -0.00322914 -0.00645828 -0.135178 -0.130746
#: 20 -0.00645828 -0.00962305 -0.130746 -0.126792
#: 21 -0.00962305 -0.0127881 -0.126792 -0.122839
#: 22 -0.0127881 -0.015918 -0.122839 -0.119386
#: 23 -0.015918 -0.019048 -0.119386 -0.115932
#: 24 -0.019048 -0.022084 -0.115932 -0.108705
#: 25 -0.022084 -0.02512 -0.108705 -0.101478
#: 26 -0.02512 -0.0376801 -0.101478 -0.096591
#: 27 -0.0376801 -0.05024 -0.096591 -0.0917053
#: 28 -0.05024 -0.05024 -0.0917053 -0.0797205
#: 29 -0.05024 -0.05024 -0.0797205 -0.0677347
#: 30 -0.05024 -0.05024 -0.0677347 -0.0561171
#: 31 -0.05024 -0.05024 -0.0561171 -0.0444994
#: 32 -0.05024 -0.05024 -0.0444994 -0.0332193
#: 33 -0.05024 -0.05024 -0.0332193 -0.0219393
#: 34 -0.05024 -0.05024 -0.0219393 -0.0109701
#: 35 -0.05024 -0.05024 -0.0109701 0.0
#: slice #: 15
#: 0 0.05024 0.05024 0.0 -0.0107431
#: 1 0.05024 0.05024 -0.0107431 -0.0214872
#: 2 0.05024 0.05024 -0.0214872 -0.0325651
#: 3 0.05024 0.05024 -0.0325651 -0.043643
#: 4 0.05024 0.05024 -0.043643 -0.0550852
#: 5 0.05024 0.05024 -0.0550852 -0.0665274
#: 6 0.05024 0.05024 -0.0665274 -0.0783644
#: 7 0.05024 0.05024 -0.0783644 -0.0902023
#: 8 0.05024 0.0376801 -0.0902023 -0.0952024
#: 9 0.0376801 0.02512 -0.0952024 -0.100202
#: 10 0.02512 0.02209 -0.100202 -0.107671
#: 11 0.02209 0.0190601 -0.107671 -0.115139
#: 12 0.0190601 0.0159369 -0.115139 -0.118644
#: 13 0.0159369 0.0128138 -0.118644 -0.122149
#: 14 0.0128138 0.00962758 -0.122149 -0.126112
#: 15 0.00962758 0.00644135 -0.126112 -0.130075
#: 16 0.00644135 0.00322056 -0.130075 -0.134393
#: 17 0.00322056 0.0 -0.134393 -0.138709
#: 18 0.0 -0.00322008 -0.138709 -0.134343
#: 19 -0.00322008 -0.00643992 -0.134343 -0.129976
#: 20 -0.00643992 -0.00962687 -0.129976 -0.125997
#: 21 -0.00962687 -0.0128138 -0.125997 -0.122018
#: 22 -0.0128138 -0.0159378 -0.122018 -0.118533
#: 23 -0.0159378 -0.0190616 -0.118533 -0.115049
#: 24 -0.0190616 -0.0220909 -0.115049 -0.107625
#: 25 -0.0220909 -0.02512 -0.107625 -0.100202
#: 26 -0.02512 -0.0376801 -0.100202 -0.0952024
#: 27 -0.0376801 -0.05024 -0.0952024 -0.0902023
#: 28 -0.05024 -0.05024 -0.0902023 -0.0783644
#: 29 -0.05024 -0.05024 -0.0783644 -0.0665274
#: 30 -0.05024 -0.05024 -0.0665274 -0.0550852
#: 31 -0.05024 -0.05024 -0.0550852 -0.043643
#: 32 -0.05024 -0.05024 -0.043643 -0.0325651
#: 33 -0.05024 -0.05024 -0.0325651 -0.0214872
#: 34 -0.05024 -0.05024 -0.0214872 -0.0107431
#: 35 -0.05024 -0.05024 -0.0107431 0.0
#: 0 0.05024 0.05024 0.0 -0.0217133
#: 1 0.05024 0.05024 -0.0217133 -0.0440712
#: 2 0.05024 0.05024 -0.0440712 -0.067131
#: 3 0.05024 0.05024 -0.067131 -0.0909538
#: 4 0.05024 0.02512 -0.0909538 -0.100758
#: 5 0.02512 0.019031 -0.100758 -0.115566
#: 6 0.019031 0.0127788 -0.115566 -0.122603
#: 7 0.0127788 0.00641489 -0.122603 -0.130586
#: 8 0.00641489 0.0 -0.130586 -0.139159
#: 9 0.0 -0.00644922 -0.139159 -0.130361
#: 10 -0.00644922 -0.0128009 -0.130361 -0.122428
#: 11 -0.0128009 -0.0190549 -0.122428 -0.115491
#: 12 -0.0190549 -0.02512 -0.115491 -0.10084
#: 13 -0.02512 -0.05024 -0.10084 -0.0909538
#: 14 -0.05024 -0.05024 -0.0909538 -0.067131
#: 15 -0.05024 -0.05024 -0.067131 -0.0440712
#: 16 -0.05024 -0.05024 -0.0440712 -0.0217133
#: 17 -0.05024 -0.05024 -0.0217133 0.0
#: 0 0.05024 0.05024 0.0 -0.0109701
#: 1 0.05024 0.05024 -0.0109701 -0.0219393
#: 2 0.05024 0.05024 -0.0219393 -0.0332193
#: 3 0.05024 0.05024 -0.0332193 -0.0444994
#: 4 0.05024 0.05024 -0.0444994 -0.0561171
#: 5 0.05024 0.05024 -0.0561171 -0.0677347
#: 6 0.05024 0.05024 -0.0677347 -0.0797205
#: 7 0.05024 0.05024 -0.0797205 -0.0917053
#: 8 0.05024 0.0376801 -0.0917053 -0.096509
#: 9 0.0376801 0.02512 -0.096509 -0.101314
#: 10 0.02512 0.0220609 -0.101314 -0.108653
#: 11 0.0220609 0.019002 -0.108653 -0.115993
#: 12 0.019002 0.015873 -0.115993 -0.119526
#: 13 0.015873 0.0127437 -0.119526 -0.123058
#: 14 0.0127437 0.00956607 -0.123058 -0.127077
#: 15 0.00956607 0.00638843 -0.127077 -0.131096
#: 16 0.00638843 0.00319433 -0.131096 -0.135352
#: 17 0.00319433 0.0 -0.135352 -0.139609
#: 18 0.0 -0.00322914 -0.139609 -0.135178
#: 19 -0.00322914 -0.00645828 -0.135178 -0.130746
#: 20 -0.00645828 -0.00962305 -0.130746 -0.126792
#: 21 -0.00962305 -0.0127881 -0.126792 -0.122839
#: 22 -0.0127881 -0.015918 -0.122839 -0.119386
#: 23 -0.015918 -0.019048 -0.119386 -0.115932
#: 24 -0.019048 -0.022084 -0.115932 -0.108705
#: 25 -0.022084 -0.02512 -0.108705 -0.101478
#: 26 -0.02512 -0.0376801 -0.101478 -0.096591
#: 27 -0.0376801 -0.05024 -0.096591 -0.0917053
#: 28 -0.05024 -0.05024 -0.0917053 -0.0797205
#: 29 -0.05024 -0.05024 -0.0797205 -0.0677347
#: 30 -0.05024 -0.05024 -0.0677347 -0.0561171
#: 31 -0.05024 -0.05024 -0.0561171 -0.0444994
#: 32 -0.05024 -0.05024 -0.0444994 -0.0332193
#: 33 -0.05024 -0.05024 -0.0332193 -0.0219393
#: 34 -0.05024 -0.05024 -0.0219393 -0.0109701
#: 35 -0.05024 -0.05024 -0.0109701 0.0
#: 0 0.05024 0.05024 0.0 -0.0221653
#: 1 0.05024 0.05024 -0.0221653 -0.0449266
#: 2 0.05024 0.05024 -0.0449266 -0.0683393
#: 3 0.05024 0.05024 -0.0683393 -0.0924578
#: 4 0.05024 0.02512 -0.0924578 -0.101771
#: 5 0.02512 0.0190096 -0.101771 -0.116139
#: 6 0.0190096 0.0127523 -0.116139 -0.123217
#: 7 0.0127523 0.006392 -0.123217 -0.131253
#: 8 0.006392 0.0 -0.131253 -0.139669
#: 9 0.0 -0.00645924 -0.139669 -0.130912
#: 10 -0.00645924 -0.0127833 -0.130912 -0.123018
#: 11 -0.0127833 -0.0190444 -0.123018 -0.116075
#: 12 -0.0190444 -0.02512 -0.116075 -0.101853
#: 13 -0.02512 -0.05024 -0.101853 -0.0924578
#: 14 -0.05024 -0.05024 -0.0924578 -0.0683393
#: 15 -0.05024 -0.05024 -0.0683393 -0.0449266
#: 16 -0.05024 -0.05024 -0.0449266 -0.0221653
#: 17 -0.05024 -0.05024 -0.0221653 0.0
#: 0 0.05024 0.05024 0.0 -0.0111952
#: 1 0.05024 0.05024 -0.0111952 -0.0223913
#: 2 0.05024 0.05024 -0.0223913 -0.0338736
#: 3 0.05024 0.05024 -0.0338736 -0.0453548
#: 4 0.05024 0.05024 -0.0453548 -0.0571489
#: 5 0.05024 0.05024 -0.0571489 -0.068943
#: 6 0.05024 0.05024 -0.068943 -0.0810766
#: 7 0.05024 0.05024 -0.0810766 -0.0932093
#: 8 0.05024 0.0376801 -0.0932093 -0.0977192
#: 9 0.0376801 0.02512 -0.0977192 -0.102229
#: 10 0.02512 0.0220685 -0.102229 -0.109258
#: 11 0.0220685 0.0190172 -0.109258 -0.116285
#: 12 0.0190172 0.0158892 -0.116285 -0.11983
#: 13 0.0158892 0.0127609 -0.11983 -0.123375
#: 14 0.0127609 0.00957823 -0.123375 -0.127393
#: 15 0.00957823 0.00639582 -0.127393 -0.13141
#: 16 0.00639582 0.00319791 -0.13141 -0.13557
#: 17 0.00319791 0.0 -0.13557 -0.139729
#: 18 0.0 -0.00323009 -0.139729 -0.135404
#: 19 -0.00323009 -0.00645995 -0.135404 -0.131079
#: 20 -0.00645995 -0.00961924 -0.131079 -0.127138
#: 21 -0.00961924 -0.0127785 -0.127138 -0.123198
#: 22 -0.0127785 -0.0159097 -0.123198 -0.119707
#: 23 -0.0159097 -0.0190406 -0.119707 -0.116217
#: 24 -0.0190406 -0.0220804 -0.116217 -0.109223
#: 25 -0.0220804 -0.02512 -0.109223 -0.102229
#: 26 -0.02512 -0.0376801 -0.102229 -0.0977192
#: 27 -0.0376801 -0.05024 -0.0977192 -0.0932093
#: 28 -0.05024 -0.05024 -0.0932093 -0.0810766
#: 29 -0.05024 -0.05024 -0.0810766 -0.068943
#: 30 -0.05024 -0.05024 -0.068943 -0.0571489
#: 31 -0.05024 -0.05024 -0.0571489 -0.0453548
#: 32 -0.05024 -0.05024 -0.0453548 -0.0338736
#: 33 -0.05024 -0.05024 -0.0338736 -0.0223913
#: 34 -0.05024 -0.05024 -0.0223913 -0.0111952
#: 35 -0.05024 -0.05024 -0.0111952 0.0
#: slice #: 16
#: 0 0.05024 0.05024 0.0 -0.0109701
#: 1 0.05024 0.05024 -0.0109701 -0.0219393
#: 2 0.05024 0.05024 -0.0219393 -0.0332193
#: 3 0.05024 0.05024 -0.0332193 -0.0444994
#: 4 0.05024 0.05024 -0.0444994 -0.0561171
#: 5 0.05024 0.05024 -0.0561171 -0.0677347
#: 6 0.05024 0.05024 -0.0677347 -0.0797205
#: 7 0.05024 0.05024 -0.0797205 -0.0917053
#: 8 0.05024 0.0376801 -0.0917053 -0.096509
#: 9 0.0376801 0.02512 -0.096509 -0.101314
#: 10 0.02512 0.0220609 -0.101314 -0.108653
#: 11 0.0220609 0.019002 -0.108653 -0.115993
#: 12 0.019002 0.015873 -0.115993 -0.119526
#: 13 0.015873 0.0127437 -0.119526 -0.123058
#: 14 0.0127437 0.00956607 -0.123058 -0.127077
#: 15 0.00956607 0.00638843 -0.127077 -0.131096
#: 16 0.00638843 0.00319433 -0.131096 -0.135352
#: 17 0.00319433 0.0 -0.135352 -0.139609
#: 18 0.0 -0.00322914 -0.139609 -0.135178
#: 19 -0.00322914 -0.00645828 -0.135178 -0.130746
#: 20 -0.00645828 -0.00962305 -0.130746 -0.126792
#: 21 -0.00962305 -0.0127881 -0.126792 -0.122839
#: 22 -0.0127881 -0.015918 -0.122839 -0.119386
#: 23 -0.015918 -0.019048 -0.119386 -0.115932
#: 24 -0.019048 -0.022084 -0.115932 -0.108705
#: 25 -0.022084 -0.02512 -0.108705 -0.101478
#: 26 -0.02512 -0.0376801 -0.101478 -0.096591
#: 27 -0.0376801 -0.05024 -0.096591 -0.0917053
#: 28 -0.05024 -0.05024 -0.0917053 -0.0797205
#: 29 -0.05024 -0.05024 -0.0797205 -0.0677347
#: 30 -0.05024 -0.05024 -0.0677347 -0.0561171
#: 31 -0.05024 -0.05024 -0.0561171 -0.0444994
#: 32 -0.05024 -0.05024 -0.0444994 -0.0332193
#: 33 -0.05024 -0.05024 -0.0332193 -0.0219393
#: 34 -0.05024 -0.05024 -0.0219393 -0.0109701
#: 35 -0.05024 -0.05024 -0.0109701 0.0
#: 0 0.05024 0.05024 0.0 -0.0221653
#: 1 0.05024 0.05024 -0.0221653 -0.0449266
#: 2 0.05024 0.05024 -0.0449266 -0.0683393
#: 3 0.05024 0.05024 -0.0683393 -0.0924578
#: 4 0.05024 0.02512 -0.0924578 -0.101771
#: 5 0.02512 0.0190096 -0.101771 -0.116139
#: 6 0.0190096 0.0127523 -0.116139 -0.123217
#: 7 0.0127523 0.006392 -0.123217 -0.131253
#: 8 0.006392 0.0 -0.131253 -0.139669
#: 9 0.0 -0.00645924 -0.139669 -0.130912
#: 10 -0.00645924 -0.0127833 -0.130912 -0.123018
#: 11 -0.0127833 -0.0190444 -0.123018 -0.116075
#: 12 -0.0190444 -0.02512 -0.116075 -0.101853
#: 13 -0.02512 -0.05024 -0.101853 -0.0924578
#: 14 -0.05024 -0.05024 -0.0924578 -0.0683393
#: 15 -0.05024 -0.05024 -0.0683393 -0.0449266
#: 16 -0.05024 -0.05024 -0.0449266 -0.0221653
#: 17 -0.05024 -0.05024 -0.0221653 0.0
#: 0 0.05024 0.05024 0.0 -0.0111952
#: 1 0.05024 0.05024 -0.0111952 -0.0223913
#: 2 0.05024 0.05024 -0.0223913 -0.0338736
#: 3 0.05024 0.05024 -0.0338736 -0.0453548
#: 4 0.05024 0.05024 -0.0453548 -0.0571489
#: 5 0.05024 0.05024 -0.0571489 -0.068943
#: 6 0.05024 0.05024 -0.068943 -0.0810766
#: 7 0.05024 0.05024 -0.0810766 -0.0932093
#: 8 0.05024 0.0376801 -0.0932093 -0.0977192
#: 9 0.0376801 0.02512 -0.0977192 -0.102229
#: 10 0.02512 0.0220685 -0.102229 -0.109258
#: 11 0.0220685 0.0190172 -0.109258 -0.116285
#: 12 0.0190172 0.0158892 -0.116285 -0.11983
#: 13 0.0158892 0.0127609 -0.11983 -0.123375
#: 14 0.0127609 0.00957823 -0.123375 -0.127393
#: 15 0.00957823 0.00639582 -0.127393 -0.13141
#: 16 0.00639582 0.00319791 -0.13141 -0.13557
#: 17 0.00319791 0.0 -0.13557 -0.139729
#: 18 0.0 -0.00323009 -0.139729 -0.135404
#: 19 -0.00323009 -0.00645995 -0.135404 -0.131079
#: 20 -0.00645995 -0.00961924 -0.131079 -0.127138
#: 21 -0.00961924 -0.0127785 -0.127138 -0.123198
#: 22 -0.0127785 -0.0159097 -0.123198 -0.119707
#: 23 -0.0159097 -0.0190406 -0.119707 -0.116217
#: 24 -0.0190406 -0.0220804 -0.116217 -0.109223
#: 25 -0.0220804 -0.02512 -0.109223 -0.102229
#: 26 -0.02512 -0.0376801 -0.102229 -0.0977192
#: 27 -0.0376801 -0.05024 -0.0977192 -0.0932093
#: 28 -0.05024 -0.05024 -0.0932093 -0.0810766
#: 29 -0.05024 -0.05024 -0.0810766 -0.068943
#: 30 -0.05024 -0.05024 -0.068943 -0.0571489
#: 31 -0.05024 -0.05024 -0.0571489 -0.0453548
#: 32 -0.05024 -0.05024 -0.0453548 -0.0338736
#: 33 -0.05024 -0.05024 -0.0338736 -0.0223913
#: 34 -0.05024 -0.05024 -0.0223913 -0.0111952
#: 35 -0.05024 -0.05024 -0.0111952 0.0
#: 0 0.05024 0.05024 0.0 -0.0226164
#: 1 0.05024 0.05024 -0.0226164 -0.045783
#: 2 0.05024 0.05024 -0.045783 -0.0695467
#: 3 0.05024 0.05024 -0.0695467 -0.0939608
#: 4 0.05024 0.02512 -0.0939608 -0.102605
#: 5 0.02512 0.0190225 -0.102605 -0.116294
#: 6 0.0190225 0.0127668 -0.116294 -0.123395
#: 7 0.0127668 0.00639915 -0.123395 -0.131442
#: 8 0.00639915 0.0 -0.131442 -0.13975
#: 9 0.0 -0.00645947 -0.13975 -0.131132
#: 10 -0.00645947 -0.0127766 -0.131132 -0.123255
#: 11 -0.0127766 -0.0190392 -0.123255 -0.116251
#: 12 -0.0190392 -0.02512 -0.116251 -0.102605
#: 13 -0.02512 -0.05024 -0.102605 -0.0939608
#: 14 -0.05024 -0.05024 -0.0939608 -0.0695467
#: 15 -0.05024 -0.05024 -0.0695467 -0.045783
#: 16 -0.05024 -0.05024 -0.045783 -0.0226164
#: 17 -0.05024 -0.05024 -0.0226164 0.0
#: 0 0.05024 0.05024 0.0 -0.0114212
#: 1 0.05024 0.05024 -0.0114212 -0.0228424
#: 2 0.05024 0.05024 -0.0228424 -0.0345268
#: 3 0.05024 0.05024 -0.0345268 -0.0462112
#: 4 0.05024 0.05024 -0.0462112 -0.0581808
#: 5 0.05024 0.05024 -0.0581808 -0.0701504
#: 6 0.05024 0.05024 -0.0701504 -0.0824308
#: 7 0.05024 0.05024 -0.0824308 -0.0947123
#: 8 0.05024 0.0376801 -0.0947123 -0.0988464
#: 9 0.0376801 0.02512 -0.0988464 -0.102981
#: 10 0.02512 0.0220737 -0.102981 -0.109641
#: 11 0.0220737 0.0190277 -0.109641 -0.116302
#: 12 0.0190277 0.0159001 -0.116302 -0.119859
#: 13 0.0159001 0.0127728 -0.119859 -0.123415
#: 14 0.0127728 0.00958776 -0.123415 -0.127444
#: 15 0.00958776 0.00640249 -0.127444 -0.131474
#: 16 0.00640249 0.00320125 -0.131474 -0.135622
#: 17 0.00320125 0.0 -0.135622 -0.139771
#: 18 0.0 -0.00322962 -0.139771 -0.135478
#: 19 -0.00322962 -0.006459 -0.135478 -0.131186
#: 20 -0.006459 -0.00961685 -0.131186 -0.127249
#: 21 -0.00961685 -0.0127747 -0.127249 -0.123312
#: 22 -0.0127747 -0.0159061 -0.123312 -0.119799
#: 23 -0.0159061 -0.0190375 -0.119799 -0.116285
#: 24 -0.0190375 -0.0220788 -0.116285 -0.109633
#: 25 -0.0220788 -0.02512 -0.109633 -0.102981
#: 26 -0.02512 -0.0376801 -0.102981 -0.0988464
#: 27 -0.0376801 -0.05024 -0.0988464 -0.0947123
#: 28 -0.05024 -0.05024 -0.0947123 -0.0824308
#: 29 -0.05024 -0.05024 -0.0824308 -0.0701504
#: 30 -0.05024 -0.05024 -0.0701504 -0.0581808
#: 31 -0.05024 -0.05024 -0.0581808 -0.0462112
#: 32 -0.05024 -0.05024 -0.0462112 -0.0345268
#: 33 -0.05024 -0.05024 -0.0345268 -0.0228424
#: 34 -0.05024 -0.05024 -0.0228424 -0.0114212
#: 35 -0.05024 -0.05024 -0.0114212 0.0
#: slice #: 17
#: 0 0.05024 0.05024 0.0 -0.0111952
#: 1 0.05024 0.05024 -0.0111952 -0.0223913
#: 2 0.05024 0.05024 -0.0223913 -0.0338736
#: 3 0.05024 0.05024 -0.0338736 -0.0453548
#: 4 0.05024 0.05024 -0.0453548 -0.0571489
#: 5 0.05024 0.05024 -0.0571489 -0.068943
#: 6 0.05024 0.05024 -0.068943 -0.0810766
#: 7 0.05024 0.05024 -0.0810766 -0.0932093
#: 8 0.05024 0.0376801 -0.0932093 -0.0977192
#: 9 0.0376801 0.02512 -0.0977192 -0.102229
#: 10 0.02512 0.0220685 -0.102229 -0.109258
#: 11 0.0220685 0.0190172 -0.109258 -0.116285
#: 12 0.0190172 0.0158892 -0.116285 -0.11983
#: 13 0.0158892 0.0127609 -0.11983 -0.123375
#: 14 0.0127609 0.00957823 -0.123375 -0.127393
#: 15 0.00957823 0.00639582 -0.127393 -0.13141
#: 16 0.00639582 0.00319791 -0.13141 -0.13557
#: 17 0.00319791 0.0 -0.13557 -0.139729
#: 18 0.0 -0.00323009 -0.139729 -0.135404
#: 19 -0.00323009 -0.00645995 -0.135404 -0.131079
#: 20 -0.00645995 -0.00961924 -0.131079 -0.127138
#: 21 -0.00961924 -0.0127785 -0.127138 -0.123198
#: 22 -0.0127785 -0.0159097 -0.123198 -0.119707
#: 23 -0.0159097 -0.0190406 -0.119707 -0.116217
#: 24 -0.0190406 -0.0220804 -0.116217 -0.109223
#: 25 -0.0220804 -0.02512 -0.109223 -0.102229
#: 26 -0.02512 -0.0376801 -0.102229 -0.0977192
#: 27 -0.0376801 -0.05024 -0.0977192 -0.0932093
#: 28 -0.05024 -0.05024 -0.0932093 -0.0810766
#: 29 -0.05024 -0.05024 -0.0810766 -0.068943
#: 30 -0.05024 -0.05024 -0.068943 -0.0571489
#: 31 -0.05024 -0.05024 -0.0571489 -0.0453548
#: 32 -0.05024 -0.05024 -0.0453548 -0.0338736
#: 33 -0.05024 -0.05024 -0.0338736 -0.0223913
#: 34 -0.05024 -0.05024 -0.0223913 -0.0111952
#: 35 -0.05024 -0.05024 -0.0111952 0.0
#: 0 0.05024 0.05024 0.0 -0.0226164
#: 1 0.05024 0.05024 -0.0226164 -0.045783
#: 2 0.05024 0.05024 -0.045783 -0.0695467
#: 3 0.05024 0.05024 -0.0695467 -0.0939608
#: 4 0.05024 0.02512 -0.0939608 -0.102605
#: 5 0.02512 0.0190225 -0.102605 -0.116294
#: 6 0.0190225 0.0127668 -0.116294 -0.123395
#: 7 0.0127668 0.00639915 -0.123395 -0.131442
#: 8 0.00639915 0.0 -0.131442 -0.13975
#: 9 0.0 -0.00645947 -0.13975 -0.131132
#: 10 -0.00645947 -0.0127766 -0.131132 -0.123255
#: 11 -0.0127766 -0.0190392 -0.123255 -0.116251
#: 12 -0.0190392 -0.02512 -0.116251 -0.102605
#: 13 -0.02512 -0.05024 -0.102605 -0.0939608
#: 14 -0.05024 -0.05024 -0.0939608 -0.0695467
#: 15 -0.05024 -0.05024 -0.0695467 -0.045783
#: 16 -0.05024 -0.05024 -0.045783 -0.0226164
#: 17 -0.05024 -0.05024 -0.0226164 0.0
#: 0 0.05024 0.05024 0.0 -0.0114212
#: 1 0.05024 0.05024 -0.0114212 -0.0228424
#: 2 0.05024 0.05024 -0.0228424 -0.0345268
#: 3 0.05024 0.05024 -0.0345268 -0.0462112
#: 4 0.05024 0.05024 -0.0462112 -0.0581808
#: 5 0.05024 0.05024 -0.0581808 -0.0701504
#: 6 0.05024 0.05024 -0.0701504 -0.0824308
#: 7 0.05024 0.05024 -0.0824308 -0.0947123
#: 8 0.05024 0.0376801 -0.0947123 -0.0988464
#: 9 0.0376801 0.02512 -0.0988464 -0.102981
#: 10 0.02512 0.0220737 -0.102981 -0.109641
#: 11 0.0220737 0.0190277 -0.109641 -0.116302
#: 12 0.0190277 0.0159001 -0.116302 -0.119859
#: 13 0.0159001 0.0127728 -0.119859 -0.123415
#: 14 0.0127728 0.00958776 -0.123415 -0.127444
#: 15 0.00958776 0.00640249 -0.127444 -0.131474
#: 16 0.00640249 0.00320125 -0.131474 -0.135622
#: 17 0.00320125 0.0 -0.135622 -0.139771
#: 18 0.0 -0.00322962 -0.139771 -0.135478
#: 19 -0.00322962 -0.006459 -0.135478 -0.131186
#: 20 -0.006459 -0.00961685 -0.131186 -0.127249
#: 21 -0.00961685 -0.0127747 -0.127249 -0.123312
#: 22 -0.0127747 -0.0159061 -0.123312 -0.119799
#: 23 -0.0159061 -0.0190375 -0.119799 -0.116285
#: 24 -0.0190375 -0.0220788 -0.116285 -0.109633
#: 25 -0.0220788 -0.02512 -0.109633 -0.102981
#: 26 -0.02512 -0.0376801 -0.102981 -0.0988464
#: 27 -0.0376801 -0.05024 -0.0988464 -0.0947123
#: 28 -0.05024 -0.05024 -0.0947123 -0.0824308
#: 29 -0.05024 -0.05024 -0.0824308 -0.0701504
#: 30 -0.05024 -0.05024 -0.0701504 -0.0581808
#: 31 -0.05024 -0.05024 -0.0581808 -0.0462112
#: 32 -0.05024 -0.05024 -0.0462112 -0.0345268
#: 33 -0.05024 -0.05024 -0.0345268 -0.0228424
#: 34 -0.05024 -0.05024 -0.0228424 -0.0114212
#: 35 -0.05024 -0.05024 -0.0114212 0.0
#: 0 0.05024 0.05024 0.0 -0.0230684
#: 1 0.05024 0.05024 -0.0230684 -0.0466394
#: 2 0.05024 0.05024 -0.0466394 -0.0707541
#: 3 0.05024 0.05024 -0.0707541 -0.0954638
#: 4 0.05024 0.02512 -0.0954638 -0.103356
#: 5 0.02512 0.0190301 -0.103356 -0.116274
#: 6 0.0190301 0.0127754 -0.116274 -0.123385
#: 7 0.0127754 0.00640392 -0.123385 -0.131461
#: 8 0.00640392 0.0 -0.131461 -0.139777
#: 9 0.0 -0.00645876 -0.139777 -0.131189
#: 10 -0.00645876 -0.012774 -0.131189 -0.123312
#: 11 -0.012774 -0.019037 -0.123312 -0.116277
#: 12 -0.019037 -0.02512 -0.116277 -0.103356
#: 13 -0.02512 -0.05024 -0.103356 -0.0954638
#: 14 -0.05024 -0.05024 -0.0954638 -0.0707541
#: 15 -0.05024 -0.05024 -0.0707541 -0.0466394
#: 16 -0.05024 -0.05024 -0.0466394 -0.0230684
#: 17 -0.05024 -0.05024 -0.0230684 0.0
#: 0 0.05024 0.05024 0.0 -0.0116472
#: 1 0.05024 0.05024 -0.0116472 -0.0232944
#: 2 0.05024 0.05024 -0.0232944 -0.0351801
#: 3 0.05024 0.05024 -0.0351801 -0.0470667
#: 4 0.05024 0.05024 -0.0470667 -0.0592127
#: 5 0.05024 0.05024 -0.0592127 -0.0713587
#: 6 0.05024 0.05024 -0.0713587 -0.083787
#: 7 0.05024 0.05024 -0.083787 -0.0962162
#: 8 0.05024 0.0376801 -0.0962162 -0.0999746
#: 9 0.0376801 0.02512 -0.0999746 -0.103733
#: 10 0.02512 0.0220761 -0.103733 -0.109989
#: 11 0.0220761 0.0190322 -0.109989 -0.116245
#: 12 0.0190322 0.0159051 -0.116245 -0.119801
#: 13 0.0159051 0.012778 -0.119801 -0.123356
#: 14 0.012778 0.00959182 -0.123356 -0.127402
#: 15 0.00959182 0.00640559 -0.127402 -0.131448
#: 16 0.00640559 0.00320292 -0.131448 -0.135616
#: 17 0.00320292 0.0 -0.135616 -0.139785
#: 18 0.0 -0.00322914 -0.139785 -0.135489
#: 19 -0.00322914 -0.00645852 -0.135489 -0.131193
#: 20 -0.00645852 -0.0096159 -0.131193 -0.127253
#: 21 -0.0096159 -0.0127733 -0.127253 -0.123312
#: 22 -0.0127733 -0.0159049 -0.123312 -0.11979
#: 23 -0.0159049 -0.0190365 -0.11979 -0.116269
#: 24 -0.0190365 -0.0220783 -0.116269 -0.110001
#: 25 -0.0220783 -0.02512 -0.110001 -0.103732
#: 26 -0.02512 -0.0376801 -0.103732 -0.0999746
#: 27 -0.0376801 -0.05024 -0.0999746 -0.0962162
#: 28 -0.05024 -0.05024 -0.0962162 -0.083787
#: 29 -0.05024 -0.05024 -0.083787 -0.0713587
#: 30 -0.05024 -0.05024 -0.0713587 -0.0592127
#: 31 -0.05024 -0.05024 -0.0592127 -0.0470667
#: 32 -0.05024 -0.05024 -0.0470667 -0.0351801
#: 33 -0.05024 -0.05024 -0.0351801 -0.0232944
#: 34 -0.05024 -0.05024 -0.0232944 -0.0116472
#: 35 -0.05024 -0.05024 -0.0116472 0.0
#: slice #: 18
#: 0 0.05024 0.05024 0.0 -0.0114212
#: 1 0.05024 0.05024 -0.0114212 -0.0228424
#: 2 0.05024 0.05024 -0.0228424 -0.0345268
#: 3 0.05024 0.05024 -0.0345268 -0.0462112
#: 4 0.05024 0.05024 -0.0462112 -0.0581808
#: 5 0.05024 0.05024 -0.0581808 -0.0701504
#: 6 0.05024 0.05024 -0.0701504 -0.0824308
#: 7 0.05024 0.05024 -0.0824308 -0.0947123
#: 8 0.05024 0.0376801 -0.0947123 -0.0988464
#: 9 0.0376801 0.02512 -0.0988464 -0.102981
#: 10 0.02512 0.0220737 -0.102981 -0.109641
#: 11 0.0220737 0.0190277 -0.109641 -0.116302
#: 12 0.0190277 0.0159001 -0.116302 -0.119859
#: 13 0.0159001 0.0127728 -0.119859 -0.123415
#: 14 0.0127728 0.00958776 -0.123415 -0.127444
#: 15 0.00958776 0.00640249 -0.127444 -0.131474
#: 16 0.00640249 0.00320125 -0.131474 -0.135622
#: 17 0.00320125 0.0 -0.135622 -0.139771
#: 18 0.0 -0.00322962 -0.139771 -0.135478
#: 19 -0.00322962 -0.006459 -0.135478 -0.131186
#: 20 -0.006459 -0.00961685 -0.131186 -0.127249
#: 21 -0.00961685 -0.0127747 -0.127249 -0.123312
#: 22 -0.0127747 -0.0159061 -0.123312 -0.119799
#: 23 -0.0159061 -0.0190375 -0.119799 -0.116285
#: 24 -0.0190375 -0.0220788 -0.116285 -0.109633
#: 25 -0.0220788 -0.02512 -0.109633 -0.102981
#: 26 -0.02512 -0.0376801 -0.102981 -0.0988464
#: 27 -0.0376801 -0.05024 -0.0988464 -0.0947123
#: 28 -0.05024 -0.05024 -0.0947123 -0.0824308
#: 29 -0.05024 -0.05024 -0.0824308 -0.0701504
#: 30 -0.05024 -0.05024 -0.0701504 -0.0581808
#: 31 -0.05024 -0.05024 -0.0581808 -0.0462112
#: 32 -0.05024 -0.05024 -0.0462112 -0.0345268
#: 33 -0.05024 -0.05024 -0.0345268 -0.0228424
#: 34 -0.05024 -0.05024 -0.0228424 -0.0114212
#: 35 -0.05024 -0.05024 -0.0114212 0.0
#: 0 0.05024 0.05024 0.0 -0.0230684
#: 1 0.05024 0.05024 -0.0230684 -0.0466394
#: 2 0.05024 0.05024 -0.0466394 -0.0707541
#: 3 0.05024 0.05024 -0.0707541 -0.0954638
#: 4 0.05024 0.02512 -0.0954638 -0.103356
#: 5 0.02512 0.0190301 -0.103356 -0.116274
#: 6 0.0190301 0.0127754 -0.116274 -0.123385
#: 7 0.0127754 0.00640392 -0.123385 -0.131461
#: 8 0.00640392 0.0 -0.131461 -0.139777
#: 9 0.0 -0.00645876 -0.139777 -0.131189
#: 10 -0.00645876 -0.012774 -0.131189 -0.123312
#: 11 -0.012774 -0.019037 -0.123312 -0.116277
#: 12 -0.019037 -0.02512 -0.116277 -0.103356
#: 13 -0.02512 -0.05024 -0.103356 -0.0954638
#: 14 -0.05024 -0.05024 -0.0954638 -0.0707541
#: 15 -0.05024 -0.05024 -0.0707541 -0.0466394
#: 16 -0.05024 -0.05024 -0.0466394 -0.0230684
#: 17 -0.05024 -0.05024 -0.0230684 0.0
#: 0 0.05024 0.05024 0.0 -0.0116472
#: 1 0.05024 0.05024 -0.0116472 -0.0232944
#: 2 0.05024 0.05024 -0.0232944 -0.0351801
#: 3 0.05024 0.05024 -0.0351801 -0.0470667
#: 4 0.05024 0.05024 -0.0470667 -0.0592127
#: 5 0.05024 0.05024 -0.0592127 -0.0713587
#: 6 0.05024 0.05024 -0.0713587 -0.083787
#: 7 0.05024 0.05024 -0.083787 -0.0962162
#: 8 0.05024 0.0376801 -0.0962162 -0.0999746
#: 9 0.0376801 0.02512 -0.0999746 -0.103733
#: 10 0.02512 0.0220761 -0.103733 -0.109989
#: 11 0.0220761 0.0190322 -0.109989 -0.116245
#: 12 0.0190322 0.0159051 -0.116245 -0.119801
#: 13 0.0159051 0.012778 -0.119801 -0.123356
#: 14 0.012778 0.00959182 -0.123356 -0.127402
#: 15 0.00959182 0.00640559 -0.127402 -0.131448
#: 16 0.00640559 0.00320292 -0.131448 -0.135616
#: 17 0.00320292 0.0 -0.135616 -0.139785
#: 18 0.0 -0.00322914 -0.139785 -0.135489
#: 19 -0.00322914 -0.00645852 -0.135489 -0.131193
#: 20 -0.00645852 -0.0096159 -0.131193 -0.127253
#: 21 -0.0096159 -0.0127733 -0.127253 -0.123312
#: 22 -0.0127733 -0.0159049 -0.123312 -0.11979
#: 23 -0.0159049 -0.0190365 -0.11979 -0.116269
#: 24 -0.0190365 -0.0220783 -0.116269 -0.110001
#: 25 -0.0220783 -0.02512 -0.110001 -0.103732
#: 26 -0.02512 -0.0376801 -0.103732 -0.0999746
#: 27 -0.0376801 -0.05024 -0.0999746 -0.0962162
#: 28 -0.05024 -0.05024 -0.0962162 -0.083787
#: 29 -0.05024 -0.05024 -0.083787 -0.0713587
#: 30 -0.05024 -0.05024 -0.0713587 -0.0592127
#: 31 -0.05024 -0.05024 -0.0592127 -0.0470667
#: 32 -0.05024 -0.05024 -0.0470667 -0.0351801
#: 33 -0.05024 -0.05024 -0.0351801 -0.0232944
#: 34 -0.05024 -0.05024 -0.0232944 -0.0116472
#: 35 -0.05024 -0.05024 -0.0116472 0.0
#: 0 0.05024 0.05024 0.0 -0.0235205
#: 1 0.05024 0.05024 -0.0235205 -0.0474939
#: 2 0.05024 0.05024 -0.0474939 -0.0719624
#: 3 0.05024 0.05024 -0.0719624 -0.0969677
#: 4 0.05024 0.02512 -0.0969677 -0.104109
#: 5 0.02512 0.0190327 -0.104109 -0.116212
#: 6 0.0190327 0.0127788 -0.116212 -0.123317
#: 7 0.0127788 0.00640583 -0.123317 -0.131425
#: 8 0.00640583 0.0 -0.131425 -0.139787
#: 9 0.0 -0.00645852 -0.139787 -0.131175
#: 10 -0.00645852 -0.012773 -0.131175 -0.123288
#: 11 -0.012773 -0.0190363 -0.123288 -0.116246
#: 12 -0.0190363 -0.02512 -0.116246 -0.104108
#: 13 -0.02512 -0.05024 -0.104108 -0.0969677
#: 14 -0.05024 -0.05024 -0.0969677 -0.0719624
#: 15 -0.05024 -0.05024 -0.0719624 -0.0474939
#: 16 -0.05024 -0.05024 -0.0474939 -0.0235205
#: 17 -0.05024 -0.05024 -0.0235205 0.0
#: 0 0.05024 0.05024 0.0 -0.0118732
#: 1 0.05024 0.05024 -0.0118732 -0.0237465
#: 2 0.05024 0.05024 -0.0237465 -0.0358343
#: 3 0.05024 0.05024 -0.0358343 -0.0479221
#: 4 0.05024 0.05024 -0.0479221 -0.0602446
#: 5 0.05024 0.05024 -0.0602446 -0.072566
#: 6 0.05024 0.05024 -0.072566 -0.0851431
#: 7 0.05024 0.05024 -0.0851431 -0.0977192
#: 8 0.05024 0.0376801 -0.0977192 -0.101102
#: 9 0.0376801 0.02512 -0.101102 -0.104485
#: 10 0.02512 0.0220766 -0.104485 -0.110332
#: 11 0.0220766 0.0190332 -0.110332 -0.116178
#: 12 0.0190332 0.0159063 -0.116178 -0.119727
#: 13 0.0159063 0.0127792 -0.119727 -0.123277
#: 14 0.0127792 0.00959277 -0.123277 -0.127339
#: 15 0.00959277 0.00640631 -0.127339 -0.131402
#: 16 0.00640631 0.00320315 -0.131402 -0.135595
#: 17 0.00320315 0.0 -0.135595 -0.139789
#: 18 0.0 -0.00322914 -0.139789 -0.135473
#: 19 -0.00322914 -0.00645852 -0.135473 -0.131158
#: 20 -0.00645852 -0.00961566 -0.131158 -0.127212
#: 21 -0.00961566 -0.0127728 -0.127212 -0.123264
#: 22 -0.0127728 -0.0159044 -0.123264 -0.119743
#: 23 -0.0159044 -0.0190361 -0.119743 -0.116222
#: 24 -0.0190361 -0.022078 -0.116222 -0.110353
#: 25 -0.022078 -0.02512 -0.110353 -0.104484
#: 26 -0.02512 -0.0376801 -0.104484 -0.101102
#: 27 -0.0376801 -0.05024 -0.101102 -0.0977192
#: 28 -0.05024 -0.05024 -0.0977192 -0.0851431
#: 29 -0.05024 -0.05024 -0.0851431 -0.072566
#: 30 -0.05024 -0.05024 -0.072566 -0.0602446
#: 31 -0.05024 -0.05024 -0.0602446 -0.0479221
#: 32 -0.05024 -0.05024 -0.0479221 -0.0358343
#: 33 -0.05024 -0.05024 -0.0358343 -0.0237465
#: 34 -0.05024 -0.05024 -0.0237465 -0.0118732
#: 35 -0.05024 -0.05024 -0.0118732 0.0
#: slice #: 19
#: 0 0.05024 0.05024 0.0 -0.0116472
#: 1 0.05024 0.05024 -0.0116472 -0.0232944
#: 2 0.05024 0.05024 -0.0232944 -0.0351801
#: 3 0.05024 0.05024 -0.0351801 -0.0470667
#: 4 0.05024 0.05024 -0.0470667 -0.0592127
#: 5 0.05024 0.05024 -0.0592127 -0.0713587
#: 6 0.05024 0.05024 -0.0713587 -0.083787
#: 7 0.05024 0.05024 -0.083787 -0.0962162
#: 8 0.05024 0.0376801 -0.0962162 -0.0999746
#: 9 0.0376801 0.02512 -0.0999746 -0.103733
#: 10 0.02512 0.0220761 -0.103733 -0.109989
#: 11 0.0220761 0.0190322 -0.109989 -0.116245
#: 12 0.0190322 0.0159051 -0.116245 -0.119801
#: 13 0.0159051 0.012778 -0.119801 -0.123356
#: 14 0.012778 0.00959182 -0.123356 -0.127402
#: 15 0.00959182 0.00640559 -0.127402 -0.131448
#: 16 0.00640559 0.00320292 -0.131448 -0.135616
#: 17 0.00320292 0.0 -0.135616 -0.139785
#: 18 0.0 -0.00322914 -0.139785 -0.135489
#: 19 -0.00322914 -0.00645852 -0.135489 -0.131193
#: 20 -0.00645852 -0.0096159 -0.131193 -0.127253
#: 21 -0.0096159 -0.0127733 -0.127253 -0.123312
#: 22 -0.0127733 -0.0159049 -0.123312 -0.11979
#: 23 -0.0159049 -0.0190365 -0.11979 -0.116269
#: 24 -0.0190365 -0.0220783 -0.116269 -0.110001
#: 25 -0.0220783 -0.02512 -0.110001 -0.103732
#: 26 -0.02512 -0.0376801 -0.103732 -0.0999746
#: 27 -0.0376801 -0.05024 -0.0999746 -0.0962162
#: 28 -0.05024 -0.05024 -0.0962162 -0.083787
#: 29 -0.05024 -0.05024 -0.083787 -0.0713587
#: 30 -0.05024 -0.05024 -0.0713587 -0.0592127
#: 31 -0.05024 -0.05024 -0.0592127 -0.0470667
#: 32 -0.05024 -0.05024 -0.0470667 -0.0351801
#: 33 -0.05024 -0.05024 -0.0351801 -0.0232944
#: 34 -0.05024 -0.05024 -0.0232944 -0.0116472
#: 35 -0.05024 -0.05024 -0.0116472 0.0
#: 0 0.05024 0.05024 0.0 -0.0235205
#: 1 0.05024 0.05024 -0.0235205 -0.0474939
#: 2 0.05024 0.05024 -0.0474939 -0.0719624
#: 3 0.05024 0.05024 -0.0719624 -0.0969677
#: 4 0.05024 0.02512 -0.0969677 -0.104109
#: 5 0.02512 0.0190327 -0.104109 -0.116212
#: 6 0.0190327 0.0127788 -0.116212 -0.123317
#: 7 0.0127788 0.00640583 -0.123317 -0.131425
#: 8 0.00640583 0.0 -0.131425 -0.139787
#: 9 0.0 -0.00645852 -0.139787 -0.131175
#: 10 -0.00645852 -0.012773 -0.131175 -0.123288
#: 11 -0.012773 -0.0190363 -0.123288 -0.116246
#: 12 -0.0190363 -0.02512 -0.116246 -0.104108
#: 13 -0.02512 -0.05024 -0.104108 -0.0969677
#: 14 -0.05024 -0.05024 -0.0969677 -0.0719624
#: 15 -0.05024 -0.05024 -0.0719624 -0.0474939
#: 16 -0.05024 -0.05024 -0.0474939 -0.0235205
#: 17 -0.05024 -0.05024 -0.0235205 0.0
#: 0 0.05024 0.05024 0.0 -0.0118732
#: 1 0.05024 0.05024 -0.0118732 -0.0237465
#: 2 0.05024 0.05024 -0.0237465 -0.0358343
#: 3 0.05024 0.05024 -0.0358343 -0.0479221
#: 4 0.05024 0.05024 -0.0479221 -0.0602446
#: 5 0.05024 0.05024 -0.0602446 -0.072566
#: 6 0.05024 0.05024 -0.072566 -0.0851431
#: 7 0.05024 0.05024 -0.0851431 -0.0977192
#: 8 0.05024 0.0376801 -0.0977192 -0.101102
#: 9 0.0376801 0.02512 -0.101102 -0.104485
#: 10 0.02512 0.0220766 -0.104485 -0.110332
#: 11 0.0220766 0.0190332 -0.110332 -0.116178
#: 12 0.0190332 0.0159063 -0.116178 -0.119727
#: 13 0.0159063 0.0127792 -0.119727 -0.123277
#: 14 0.0127792 0.00959277 -0.123277 -0.127339
#: 15 0.00959277 0.00640631 -0.127339 -0.131402
#: 16 0.00640631 0.00320315 -0.131402 -0.135595
#: 17 0.00320315 0.0 -0.135595 -0.139789
#: 18 0.0 -0.00322914 -0.139789 -0.135473
#: 19 -0.00322914 -0.00645852 -0.135473 -0.131158
#: 20 -0.00645852 -0.00961566 -0.131158 -0.127212
#: 21 -0.00961566 -0.0127728 -0.127212 -0.123264
#: 22 -0.0127728 -0.0159044 -0.123264 -0.119743
#: 23 -0.0159044 -0.0190361 -0.119743 -0.116222
#: 24 -0.0190361 -0.022078 -0.116222 -0.110353
#: 25 -0.022078 -0.02512 -0.110353 -0.104484
#: 26 -0.02512 -0.0376801 -0.104484 -0.101102
#: 27 -0.0376801 -0.05024 -0.101102 -0.0977192
#: 28 -0.05024 -0.05024 -0.0977192 -0.0851431
#: 29 -0.05024 -0.05024 -0.0851431 -0.072566
#: 30 -0.05024 -0.05024 -0.072566 -0.0602446
#: 31 -0.05024 -0.05024 -0.0602446 -0.0479221
#: 32 -0.05024 -0.05024 -0.0479221 -0.0358343
#: 33 -0.05024 -0.05024 -0.0358343 -0.0237465
#: 34 -0.05024 -0.05024 -0.0237465 -0.0118732
#: 35 -0.05024 -0.05024 -0.0118732 0.0
#: 0 0.05024 0.05024 0.0 -0.0239725
#: 1 0.05024 0.05024 -0.0239725 -0.0483503
#: 2 0.05024 0.05024 -0.0483503 -0.0731707
#: 3 0.05024 0.05024 -0.0731707 -0.0984707
#: 4 0.05024 0.02512 -0.0984707 -0.10486
#: 5 0.02512 0.0190334 -0.10486 -0.116143
#: 6 0.0190334 0.0127792 -0.116143 -0.123237
#: 7 0.0127792 0.00640631 -0.123237 -0.131377
#: 8 0.00640631 0.0 -0.131377 -0.13979
#: 9 0.0 -0.00645852 -0.13979 -0.131133
#: 10 -0.00645852 -0.0127726 -0.131133 -0.12323
#: 11 -0.0127726 -0.0190361 -0.12323 -0.116193
#: 12 -0.0190361 -0.02512 -0.116193 -0.104859
#: 13 -0.02512 -0.05024 -0.104859 -0.0984707
#: 14 -0.05024 -0.05024 -0.0984707 -0.0731707
#: 15 -0.05024 -0.05024 -0.0731707 -0.0483503
#: 16 -0.05024 -0.05024 -0.0483503 -0.0239725
#: 17 -0.05024 -0.05024 -0.0239725 0.0
#: 0 0.05024 0.05024 0.0 -0.0120993
#: 1 0.05024 0.05024 -0.0120993 -0.0241985
#: 2 0.05024 0.05024 -0.0241985 -0.0364885
#: 3 0.05024 0.05024 -0.0364885 -0.0487785
#: 4 0.05024 0.05024 -0.0487785 -0.0612764
#: 5 0.05024 0.05024 -0.0612764 -0.0737743
#: 6 0.05024 0.05024 -0.0737743 -0.0864983
#: 7 0.05024 0.05024 -0.0864983 -0.0992222
#: 8 0.05024 0.0376801 -0.0992222 -0.102229
#: 9 0.0376801 0.02512 -0.102229 -0.105236
#: 10 0.02512 0.0220766 -0.105236 -0.110673
#: 11 0.0220766 0.0190334 -0.110673 -0.11611
#: 12 0.0190334 0.0159063 -0.11611 -0.119653
#: 13 0.0159063 0.0127795 -0.119653 -0.123196
#: 14 0.0127795 0.00959301 -0.123196 -0.127275
#: 15 0.00959301 0.00640631 -0.127275 -0.131352
#: 16 0.00640631 0.00320315 -0.131352 -0.135571
#: 17 0.00320315 0.0 -0.135571 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.135449
#: 19 -0.00322914 -0.00645852 -0.135449 -0.131107
#: 20 -0.00645852 -0.00961542 -0.131107 -0.127151
#: 21 -0.00961542 -0.0127726 -0.127151 -0.123196
#: 22 -0.0127726 -0.0159044 -0.123196 -0.119679
#: 23 -0.0159044 -0.0190361 -0.119679 -0.116162
#: 24 -0.0190361 -0.022078 -0.116162 -0.110699
#: 25 -0.022078 -0.02512 -0.110699 -0.105235
#: 26 -0.02512 -0.0376801 -0.105235 -0.102229
#: 27 -0.0376801 -0.05024 -0.102229 -0.0992222
#: 28 -0.05024 -0.05024 -0.0992222 -0.0864983
#: 29 -0.05024 -0.05024 -0.0864983 -0.0737743
#: 30 -0.05024 -0.05024 -0.0737743 -0.0612764
#: 31 -0.05024 -0.05024 -0.0612764 -0.0487785
#: 32 -0.05024 -0.05024 -0.0487785 -0.0364885
#: 33 -0.05024 -0.05024 -0.0364885 -0.0241985
#: 34 -0.05024 -0.05024 -0.0241985 -0.0120993
#: 35 -0.05024 -0.05024 -0.0120993 0.0
#: slice #: 20
#: 0 0.05024 0.05024 0.0 -0.0118732
#: 1 0.05024 0.05024 -0.0118732 -0.0237465
#: 2 0.05024 0.05024 -0.0237465 -0.0358343
#: 3 0.05024 0.05024 -0.0358343 -0.0479221
#: 4 0.05024 0.05024 -0.0479221 -0.0602446
#: 5 0.05024 0.05024 -0.0602446 -0.072566
#: 6 0.05024 0.05024 -0.072566 -0.0851431
#: 7 0.05024 0.05024 -0.0851431 -0.0977192
#: 8 0.05024 0.0376801 -0.0977192 -0.101102
#: 9 0.0376801 0.02512 -0.101102 -0.104485
#: 10 0.02512 0.0220766 -0.104485 -0.110332
#: 11 0.0220766 0.0190332 -0.110332 -0.116178
#: 12 0.0190332 0.0159063 -0.116178 -0.119727
#: 13 0.0159063 0.0127792 -0.119727 -0.123277
#: 14 0.0127792 0.00959277 -0.123277 -0.127339
#: 15 0.00959277 0.00640631 -0.127339 -0.131402
#: 16 0.00640631 0.00320315 -0.131402 -0.135595
#: 17 0.00320315 0.0 -0.135595 -0.139789
#: 18 0.0 -0.00322914 -0.139789 -0.135473
#: 19 -0.00322914 -0.00645852 -0.135473 -0.131158
#: 20 -0.00645852 -0.00961566 -0.131158 -0.127212
#: 21 -0.00961566 -0.0127728 -0.127212 -0.123264
#: 22 -0.0127728 -0.0159044 -0.123264 -0.119743
#: 23 -0.0159044 -0.0190361 -0.119743 -0.116222
#: 24 -0.0190361 -0.022078 -0.116222 -0.110353
#: 25 -0.022078 -0.02512 -0.110353 -0.104484
#: 26 -0.02512 -0.0376801 -0.104484 -0.101102
#: 27 -0.0376801 -0.05024 -0.101102 -0.0977192
#: 28 -0.05024 -0.05024 -0.0977192 -0.0851431
#: 29 -0.05024 -0.05024 -0.0851431 -0.072566
#: 30 -0.05024 -0.05024 -0.072566 -0.0602446
#: 31 -0.05024 -0.05024 -0.0602446 -0.0479221
#: 32 -0.05024 -0.05024 -0.0479221 -0.0358343
#: 33 -0.05024 -0.05024 -0.0358343 -0.0237465
#: 34 -0.05024 -0.05024 -0.0237465 -0.0118732
#: 35 -0.05024 -0.05024 -0.0118732 0.0
#: 0 0.05024 0.05024 0.0 -0.0239725
#: 1 0.05024 0.05024 -0.0239725 -0.0483503
#: 2 0.05024 0.05024 -0.0483503 -0.0731707
#: 3 0.05024 0.05024 -0.0731707 -0.0984707
#: 4 0.05024 0.02512 -0.0984707 -0.10486
#: 5 0.02512 0.0190334 -0.10486 -0.116143
#: 6 0.0190334 0.0127792 -0.116143 -0.123237
#: 7 0.0127792 0.00640631 -0.123237 -0.131377
#: 8 0.00640631 0.0 -0.131377 -0.13979
#: 9 0.0 -0.00645852 -0.13979 -0.131133
#: 10 -0.00645852 -0.0127726 -0.131133 -0.12323
#: 11 -0.0127726 -0.0190361 -0.12323 -0.116193
#: 12 -0.0190361 -0.02512 -0.116193 -0.104859
#: 13 -0.02512 -0.05024 -0.104859 -0.0984707
#: 14 -0.05024 -0.05024 -0.0984707 -0.0731707
#: 15 -0.05024 -0.05024 -0.0731707 -0.0483503
#: 16 -0.05024 -0.05024 -0.0483503 -0.0239725
#: 17 -0.05024 -0.05024 -0.0239725 0.0
#: 0 0.05024 0.05024 0.0 -0.0120993
#: 1 0.05024 0.05024 -0.0120993 -0.0241985
#: 2 0.05024 0.05024 -0.0241985 -0.0364885
#: 3 0.05024 0.05024 -0.0364885 -0.0487785
#: 4 0.05024 0.05024 -0.0487785 -0.0612764
#: 5 0.05024 0.05024 -0.0612764 -0.0737743
#: 6 0.05024 0.05024 -0.0737743 -0.0864983
#: 7 0.05024 0.05024 -0.0864983 -0.0992222
#: 8 0.05024 0.0376801 -0.0992222 -0.102229
#: 9 0.0376801 0.02512 -0.102229 -0.105236
#: 10 0.02512 0.0220766 -0.105236 -0.110673
#: 11 0.0220766 0.0190334 -0.110673 -0.11611
#: 12 0.0190334 0.0159063 -0.11611 -0.119653
#: 13 0.0159063 0.0127795 -0.119653 -0.123196
#: 14 0.0127795 0.00959301 -0.123196 -0.127275
#: 15 0.00959301 0.00640631 -0.127275 -0.131352
#: 16 0.00640631 0.00320315 -0.131352 -0.135571
#: 17 0.00320315 0.0 -0.135571 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.135449
#: 19 -0.00322914 -0.00645852 -0.135449 -0.131107
#: 20 -0.00645852 -0.00961542 -0.131107 -0.127151
#: 21 -0.00961542 -0.0127726 -0.127151 -0.123196
#: 22 -0.0127726 -0.0159044 -0.123196 -0.119679
#: 23 -0.0159044 -0.0190361 -0.119679 -0.116162
#: 24 -0.0190361 -0.022078 -0.116162 -0.110699
#: 25 -0.022078 -0.02512 -0.110699 -0.105235
#: 26 -0.02512 -0.0376801 -0.105235 -0.102229
#: 27 -0.0376801 -0.05024 -0.102229 -0.0992222
#: 28 -0.05024 -0.05024 -0.0992222 -0.0864983
#: 29 -0.05024 -0.05024 -0.0864983 -0.0737743
#: 30 -0.05024 -0.05024 -0.0737743 -0.0612764
#: 31 -0.05024 -0.05024 -0.0612764 -0.0487785
#: 32 -0.05024 -0.05024 -0.0487785 -0.0364885
#: 33 -0.05024 -0.05024 -0.0364885 -0.0241985
#: 34 -0.05024 -0.05024 -0.0241985 -0.0120993
#: 35 -0.05024 -0.05024 -0.0120993 0.0
#: 0 0.05024 0.05024 0.0 -0.0244246
#: 1 0.05024 0.05024 -0.0244246 -0.0492067
#: 2 0.05024 0.05024 -0.0492067 -0.074378
#: 3 0.05024 0.05024 -0.074378 -0.0999746
#: 4 0.05024 0.02512 -0.0999746 -0.105613
#: 5 0.02512 0.0190334 -0.105613 -0.116076
#: 6 0.0190334 0.0127792 -0.116076 -0.123157
#: 7 0.0127792 0.00640631 -0.123157 -0.131328
#: 8 0.00640631 0.0 -0.131328 -0.139791
#: 9 0.0 -0.00645852 -0.139791 -0.131078
#: 10 -0.00645852 -0.0127726 -0.131078 -0.123158
#: 11 -0.0127726 -0.0190361 -0.123158 -0.11613
#: 12 -0.0190361 -0.02512 -0.11613 -0.105611
#: 13 -0.02512 -0.05024 -0.105611 -0.0999746
#: 14 -0.05024 -0.05024 -0.0999746 -0.074378
#: 15 -0.05024 -0.05024 -0.074378 -0.0492067
#: 16 -0.05024 -0.05024 -0.0492067 -0.0244246
#: 17 -0.05024 -0.05024 -0.0244246 0.0
#: 0 0.05024 0.05024 0.0 -0.0123243
#: 1 0.05024 0.05024 -0.0123243 -0.0246496
#: 2 0.05024 0.05024 -0.0246496 -0.0371418
#: 3 0.05024 0.05024 -0.0371418 -0.049634
#: 4 0.05024 0.05024 -0.049634 -0.0623083
#: 5 0.05024 0.05024 -0.0623083 -0.0749826
#: 6 0.05024 0.05024 -0.0749826 -0.0878544
#: 7 0.05024 0.05024 -0.0878544 -0.100726
#: 8 0.05024 0.0376801 -0.100726 -0.103357
#: 9 0.0376801 0.02512 -0.103357 -0.105989
#: 10 0.02512 0.0220766 -0.105989 -0.111016
#: 11 0.0220766 0.0190332 -0.111016 -0.116044
#: 12 0.0190332 0.0159061 -0.116044 -0.11958
#: 13 0.0159061 0.012779 -0.11958 -0.123116
#: 14 0.012779 0.00959253 -0.123116 -0.12721
#: 15 0.00959253 0.00640607 -0.12721 -0.131303
#: 16 0.00640607 0.00320292 -0.131303 -0.135547
#: 17 0.00320292 0.0 -0.135547 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.13542
#: 19 -0.00322914 -0.00645852 -0.13542 -0.131048
#: 20 -0.00645852 -0.00961542 -0.131048 -0.127084
#: 21 -0.00961542 -0.0127726 -0.127084 -0.123119
#: 22 -0.0127726 -0.0159044 -0.123119 -0.119609
#: 23 -0.0159044 -0.0190361 -0.119609 -0.116097
#: 24 -0.0190361 -0.022078 -0.116097 -0.111043
#: 25 -0.022078 -0.02512 -0.111043 -0.105988
#: 26 -0.02512 -0.0376801 -0.105988 -0.103356
#: 27 -0.0376801 -0.05024 -0.103356 -0.100726
#: 28 -0.05024 -0.05024 -0.100726 -0.0878544
#: 29 -0.05024 -0.05024 -0.0878544 -0.0749826
#: 30 -0.05024 -0.05024 -0.0749826 -0.0623083
#: 31 -0.05024 -0.05024 -0.0623083 -0.049634
#: 32 -0.05024 -0.05024 -0.049634 -0.0371418
#: 33 -0.05024 -0.05024 -0.0371418 -0.0246496
#: 34 -0.05024 -0.05024 -0.0246496 -0.0123243
#: 35 -0.05024 -0.05024 -0.0123243 0.0
#: slice #: 21
#: 0 0.05024 0.05024 0.0 -0.0120993
#: 1 0.05024 0.05024 -0.0120993 -0.0241985
#: 2 0.05024 0.05024 -0.0241985 -0.0364885
#: 3 0.05024 0.05024 -0.0364885 -0.0487785
#: 4 0.05024 0.05024 -0.0487785 -0.0612764
#: 5 0.05024 0.05024 -0.0612764 -0.0737743
#: 6 0.05024 0.05024 -0.0737743 -0.0864983
#: 7 0.05024 0.05024 -0.0864983 -0.0992222
#: 8 0.05024 0.0376801 -0.0992222 -0.102229
#: 9 0.0376801 0.02512 -0.102229 -0.105236
#: 10 0.02512 0.0220766 -0.105236 -0.110673
#: 11 0.0220766 0.0190334 -0.110673 -0.11611
#: 12 0.0190334 0.0159063 -0.11611 -0.119653
#: 13 0.0159063 0.0127795 -0.119653 -0.123196
#: 14 0.0127795 0.00959301 -0.123196 -0.127275
#: 15 0.00959301 0.00640631 -0.127275 -0.131352
#: 16 0.00640631 0.00320315 -0.131352 -0.135571
#: 17 0.00320315 0.0 -0.135571 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.135449
#: 19 -0.00322914 -0.00645852 -0.135449 -0.131107
#: 20 -0.00645852 -0.00961542 -0.131107 -0.127151
#: 21 -0.00961542 -0.0127726 -0.127151 -0.123196
#: 22 -0.0127726 -0.0159044 -0.123196 -0.119679
#: 23 -0.0159044 -0.0190361 -0.119679 -0.116162
#: 24 -0.0190361 -0.022078 -0.116162 -0.110699
#: 25 -0.022078 -0.02512 -0.110699 -0.105235
#: 26 -0.02512 -0.0376801 -0.105235 -0.102229
#: 27 -0.0376801 -0.05024 -0.102229 -0.0992222
#: 28 -0.05024 -0.05024 -0.0992222 -0.0864983
#: 29 -0.05024 -0.05024 -0.0864983 -0.0737743
#: 30 -0.05024 -0.05024 -0.0737743 -0.0612764
#: 31 -0.05024 -0.05024 -0.0612764 -0.0487785
#: 32 -0.05024 -0.05024 -0.0487785 -0.0364885
#: 33 -0.05024 -0.05024 -0.0364885 -0.0241985
#: 34 -0.05024 -0.05024 -0.0241985 -0.0120993
#: 35 -0.05024 -0.05024 -0.0120993 0.0
#: 0 0.05024 0.05024 0.0 -0.0244246
#: 1 0.05024 0.05024 -0.0244246 -0.0492067
#: 2 0.05024 0.05024 -0.0492067 -0.074378
#: 3 0.05024 0.05024 -0.074378 -0.0999746
#: 4 0.05024 0.02512 -0.0999746 -0.105613
#: 5 0.02512 0.0190334 -0.105613 -0.116076
#: 6 0.0190334 0.0127792 -0.116076 -0.123157
#: 7 0.0127792 0.00640631 -0.123157 -0.131328
#: 8 0.00640631 0.0 -0.131328 -0.139791
#: 9 0.0 -0.00645852 -0.139791 -0.131078
#: 10 -0.00645852 -0.0127726 -0.131078 -0.123158
#: 11 -0.0127726 -0.0190361 -0.123158 -0.11613
#: 12 -0.0190361 -0.02512 -0.11613 -0.105611
#: 13 -0.02512 -0.05024 -0.105611 -0.0999746
#: 14 -0.05024 -0.05024 -0.0999746 -0.074378
#: 15 -0.05024 -0.05024 -0.074378 -0.0492067
#: 16 -0.05024 -0.05024 -0.0492067 -0.0244246
#: 17 -0.05024 -0.05024 -0.0244246 0.0
#: 0 0.05024 0.05024 0.0 -0.0123243
#: 1 0.05024 0.05024 -0.0123243 -0.0246496
#: 2 0.05024 0.05024 -0.0246496 -0.0371418
#: 3 0.05024 0.05024 -0.0371418 -0.049634
#: 4 0.05024 0.05024 -0.049634 -0.0623083
#: 5 0.05024 0.05024 -0.0623083 -0.0749826
#: 6 0.05024 0.05024 -0.0749826 -0.0878544
#: 7 0.05024 0.05024 -0.0878544 -0.100726
#: 8 0.05024 0.0376801 -0.100726 -0.103357
#: 9 0.0376801 0.02512 -0.103357 -0.105989
#: 10 0.02512 0.0220766 -0.105989 -0.111016
#: 11 0.0220766 0.0190332 -0.111016 -0.116044
#: 12 0.0190332 0.0159061 -0.116044 -0.11958
#: 13 0.0159061 0.012779 -0.11958 -0.123116
#: 14 0.012779 0.00959253 -0.123116 -0.12721
#: 15 0.00959253 0.00640607 -0.12721 -0.131303
#: 16 0.00640607 0.00320292 -0.131303 -0.135547
#: 17 0.00320292 0.0 -0.135547 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.13542
#: 19 -0.00322914 -0.00645852 -0.13542 -0.131048
#: 20 -0.00645852 -0.00961542 -0.131048 -0.127084
#: 21 -0.00961542 -0.0127726 -0.127084 -0.123119
#: 22 -0.0127726 -0.0159044 -0.123119 -0.119609
#: 23 -0.0159044 -0.0190361 -0.119609 -0.116097
#: 24 -0.0190361 -0.022078 -0.116097 -0.111043
#: 25 -0.022078 -0.02512 -0.111043 -0.105988
#: 26 -0.02512 -0.0376801 -0.105988 -0.103356
#: 27 -0.0376801 -0.05024 -0.103356 -0.100726
#: 28 -0.05024 -0.05024 -0.100726 -0.0878544
#: 29 -0.05024 -0.05024 -0.0878544 -0.0749826
#: 30 -0.05024 -0.05024 -0.0749826 -0.0623083
#: 31 -0.05024 -0.05024 -0.0623083 -0.049634
#: 32 -0.05024 -0.05024 -0.049634 -0.0371418
#: 33 -0.05024 -0.05024 -0.0371418 -0.0246496
#: 34 -0.05024 -0.05024 -0.0246496 -0.0123243
#: 35 -0.05024 -0.05024 -0.0123243 0.0
#: 0 0.05024 0.05024 0.0 -0.0248756
#: 1 0.05024 0.05024 -0.0248756 -0.0500622
#: 2 0.05024 0.05024 -0.0500622 -0.0755863
#: 3 0.05024 0.05024 -0.0755863 -0.101478
#: 4 0.05024 0.02512 -0.101478 -0.106364
#: 5 0.02512 0.019033 -0.106364 -0.116014
#: 6 0.019033 0.0127785 -0.116014 -0.123078
#: 7 0.0127785 0.00640559 -0.123078 -0.13128
#: 8 0.00640559 0.0 -0.13128 -0.139791
#: 9 0.0 -0.00645852 -0.139791 -0.131019
#: 10 -0.00645852 -0.0127726 -0.131019 -0.12308
#: 11 -0.0127726 -0.0190361 -0.12308 -0.116065
#: 12 -0.0190361 -0.02512 -0.116065 -0.106363
#: 13 -0.02512 -0.05024 -0.106363 -0.101478
#: 14 -0.05024 -0.05024 -0.101478 -0.0755863
#: 15 -0.05024 -0.05024 -0.0755863 -0.0500622
#: 16 -0.05024 -0.05024 -0.0500622 -0.0248756
#: 17 -0.05024 -0.05024 -0.0248756 0.0
#: 0 0.05024 0.05024 0.0 -0.0125513
#: 1 0.05024 0.05024 -0.0125513 -0.0251017
#: 2 0.05024 0.05024 -0.0251017 -0.037796
#: 3 0.05024 0.05024 -0.037796 -0.0504904
#: 4 0.05024 0.05024 -0.0504904 -0.0633402
#: 5 0.05024 0.05024 -0.0633402 -0.07619
#: 6 0.05024 0.05024 -0.07619 -0.0892096
#: 7 0.05024 0.05024 -0.0892096 -0.102229
#: 8 0.05024 0.0376801 -0.102229 -0.104485
#: 9 0.0376801 0.02512 -0.104485 -0.10674
#: 10 0.02512 0.0220761 -0.10674 -0.111362
#: 11 0.0220761 0.0190325 -0.111362 -0.115982
#: 12 0.0190325 0.0159054 -0.115982 -0.119512
#: 13 0.0159054 0.012778 -0.119512 -0.123041
#: 14 0.012778 0.00959158 -0.123041 -0.127149
#: 15 0.00959158 0.00640512 -0.127149 -0.131257
#: 16 0.00640512 0.00320244 -0.131257 -0.135524
#: 17 0.00320244 0.0 -0.135524 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.13539
#: 19 -0.00322914 -0.00645852 -0.13539 -0.130989
#: 20 -0.00645852 -0.00961542 -0.130989 -0.127015
#: 21 -0.00961542 -0.0127726 -0.127015 -0.123041
#: 22 -0.0127726 -0.0159044 -0.123041 -0.119537
#: 23 -0.0159044 -0.0190361 -0.119537 -0.116034
#: 24 -0.0190361 -0.022078 -0.116034 -0.111386
#: 25 -0.022078 -0.02512 -0.111386 -0.106739
#: 26 -0.02512 -0.0376801 -0.106739 -0.104484
#: 27 -0.0376801 -0.05024 -0.104484 -0.102229
#: 28 -0.05024 -0.05024 -0.102229 -0.0892096
#: 29 -0.05024 -0.05024 -0.0892096 -0.07619
#: 30 -0.05024 -0.05024 -0.07619 -0.0633402
#: 31 -0.05024 -0.05024 -0.0633402 -0.0504904
#: 32 -0.05024 -0.05024 -0.0504904 -0.037796
#: 33 -0.05024 -0.05024 -0.037796 -0.0251017
#: 34 -0.05024 -0.05024 -0.0251017 -0.0125513
#: 35 -0.05024 -0.05024 -0.0125513 0.0
#: slice #: 22
#: 0 0.05024 0.05024 0.0 -0.0123243
#: 1 0.05024 0.05024 -0.0123243 -0.0246496
#: 2 0.05024 0.05024 -0.0246496 -0.0371418
#: 3 0.05024 0.05024 -0.0371418 -0.049634
#: 4 0.05024 0.05024 -0.049634 -0.0623083
#: 5 0.05024 0.05024 -0.0623083 -0.0749826
#: 6 0.05024 0.05024 -0.0749826 -0.0878544
#: 7 0.05024 0.05024 -0.0878544 -0.100726
#: 8 0.05024 0.0376801 -0.100726 -0.103357
#: 9 0.0376801 0.02512 -0.103357 -0.105989
#: 10 0.02512 0.0220766 -0.105989 -0.111016
#: 11 0.0220766 0.0190332 -0.111016 -0.116044
#: 12 0.0190332 0.0159061 -0.116044 -0.11958
#: 13 0.0159061 0.012779 -0.11958 -0.123116
#: 14 0.012779 0.00959253 -0.123116 -0.12721
#: 15 0.00959253 0.00640607 -0.12721 -0.131303
#: 16 0.00640607 0.00320292 -0.131303 -0.135547
#: 17 0.00320292 0.0 -0.135547 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.13542
#: 19 -0.00322914 -0.00645852 -0.13542 -0.131048
#: 20 -0.00645852 -0.00961542 -0.131048 -0.127084
#: 21 -0.00961542 -0.0127726 -0.127084 -0.123119
#: 22 -0.0127726 -0.0159044 -0.123119 -0.119609
#: 23 -0.0159044 -0.0190361 -0.119609 -0.116097
#: 24 -0.0190361 -0.022078 -0.116097 -0.111043
#: 25 -0.022078 -0.02512 -0.111043 -0.105988
#: 26 -0.02512 -0.0376801 -0.105988 -0.103356
#: 27 -0.0376801 -0.05024 -0.103356 -0.100726
#: 28 -0.05024 -0.05024 -0.100726 -0.0878544
#: 29 -0.05024 -0.05024 -0.0878544 -0.0749826
#: 30 -0.05024 -0.05024 -0.0749826 -0.0623083
#: 31 -0.05024 -0.05024 -0.0623083 -0.049634
#: 32 -0.05024 -0.05024 -0.049634 -0.0371418
#: 33 -0.05024 -0.05024 -0.0371418 -0.0246496
#: 34 -0.05024 -0.05024 -0.0246496 -0.0123243
#: 35 -0.05024 -0.05024 -0.0123243 0.0
#: 0 0.05024 0.05024 0.0 -0.0248756
#: 1 0.05024 0.05024 -0.0248756 -0.0500622
#: 2 0.05024 0.05024 -0.0500622 -0.0755863
#: 3 0.05024 0.05024 -0.0755863 -0.101478
#: 4 0.05024 0.02512 -0.101478 -0.106364
#: 5 0.02512 0.019033 -0.106364 -0.116014
#: 6 0.019033 0.0127785 -0.116014 -0.123078
#: 7 0.0127785 0.00640559 -0.123078 -0.13128
#: 8 0.00640559 0.0 -0.13128 -0.139791
#: 9 0.0 -0.00645852 -0.139791 -0.131019
#: 10 -0.00645852 -0.0127726 -0.131019 -0.12308
#: 11 -0.0127726 -0.0190361 -0.12308 -0.116065
#: 12 -0.0190361 -0.02512 -0.116065 -0.106363
#: 13 -0.02512 -0.05024 -0.106363 -0.101478
#: 14 -0.05024 -0.05024 -0.101478 -0.0755863
#: 15 -0.05024 -0.05024 -0.0755863 -0.0500622
#: 16 -0.05024 -0.05024 -0.0500622 -0.0248756
#: 17 -0.05024 -0.05024 -0.0248756 0.0
#: 0 0.05024 0.05024 0.0 -0.0125513
#: 1 0.05024 0.05024 -0.0125513 -0.0251017
#: 2 0.05024 0.05024 -0.0251017 -0.037796
#: 3 0.05024 0.05024 -0.037796 -0.0504904
#: 4 0.05024 0.05024 -0.0504904 -0.0633402
#: 5 0.05024 0.05024 -0.0633402 -0.07619
#: 6 0.05024 0.05024 -0.07619 -0.0892096
#: 7 0.05024 0.05024 -0.0892096 -0.102229
#: 8 0.05024 0.0376801 -0.102229 -0.104485
#: 9 0.0376801 0.02512 -0.104485 -0.10674
#: 10 0.02512 0.0220761 -0.10674 -0.111362
#: 11 0.0220761 0.0190325 -0.111362 -0.115982
#: 12 0.0190325 0.0159054 -0.115982 -0.119512
#: 13 0.0159054 0.012778 -0.119512 -0.123041
#: 14 0.012778 0.00959158 -0.123041 -0.127149
#: 15 0.00959158 0.00640512 -0.127149 -0.131257
#: 16 0.00640512 0.00320244 -0.131257 -0.135524
#: 17 0.00320244 0.0 -0.135524 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.13539
#: 19 -0.00322914 -0.00645852 -0.13539 -0.130989
#: 20 -0.00645852 -0.00961542 -0.130989 -0.127015
#: 21 -0.00961542 -0.0127726 -0.127015 -0.123041
#: 22 -0.0127726 -0.0159044 -0.123041 -0.119537
#: 23 -0.0159044 -0.0190361 -0.119537 -0.116034
#: 24 -0.0190361 -0.022078 -0.116034 -0.111386
#: 25 -0.022078 -0.02512 -0.111386 -0.106739
#: 26 -0.02512 -0.0376801 -0.106739 -0.104484
#: 27 -0.0376801 -0.05024 -0.104484 -0.102229
#: 28 -0.05024 -0.05024 -0.102229 -0.0892096
#: 29 -0.05024 -0.05024 -0.0892096 -0.07619
#: 30 -0.05024 -0.05024 -0.07619 -0.0633402
#: 31 -0.05024 -0.05024 -0.0633402 -0.0504904
#: 32 -0.05024 -0.05024 -0.0504904 -0.037796
#: 33 -0.05024 -0.05024 -0.037796 -0.0251017
#: 34 -0.05024 -0.05024 -0.0251017 -0.0125513
#: 35 -0.05024 -0.05024 -0.0125513 0.0
#: 0 0.05024 0.05024 0.0 -0.0253277
#: 1 0.05024 0.05024 -0.0253277 -0.0509176
#: 2 0.05024 0.05024 -0.0509176 -0.0767946
#: 3 0.05024 0.05024 -0.0767946 -0.102981
#: 4 0.05024 0.02512 -0.102981 -0.107116
#: 5 0.02512 0.0190315 -0.107116 -0.115953
#: 6 0.0190315 0.0127766 -0.115953 -0.123008
#: 7 0.0127766 0.00640416 -0.123008 -0.131238
#: 8 0.00640416 0.0 -0.131238 -0.139791
#: 9 0.0 -0.00645828 -0.139791 -0.13096
#: 10 -0.00645828 -0.0127721 -0.13096 -0.123004
#: 11 -0.0127721 -0.0190358 -0.123004 -0.116002
#: 12 -0.0190358 -0.02512 -0.116002 -0.107116
#: 13 -0.02512 -0.05024 -0.107116 -0.102981
#: 14 -0.05024 -0.05024 -0.102981 -0.0767946
#: 15 -0.05024 -0.05024 -0.0767946 -0.0509176
#: 16 -0.05024 -0.05024 -0.0509176 -0.0253277
#: 17 -0.05024 -0.05024 -0.0253277 0.0
#: 0 0.05024 0.05024 0.0 -0.0127764
#: 1 0.05024 0.05024 -0.0127764 -0.0255537
#: 2 0.05024 0.05024 -0.0255537 -0.0384493
#: 3 0.05024 0.05024 -0.0384493 -0.0513458
#: 4 0.05024 0.05024 -0.0513458 -0.0643721
#: 5 0.05024 0.05024 -0.0643721 -0.0773983
#: 6 0.05024 0.05024 -0.0773983 -0.0905657
#: 7 0.05024 0.05024 -0.0905657 -0.103733
#: 8 0.05024 0.0376801 -0.103733 -0.105613
#: 9 0.0376801 0.02512 -0.105613 -0.107491
#: 10 0.02512 0.0220752 -0.107491 -0.111709
#: 11 0.0220752 0.0190303 -0.111709 -0.115925
#: 12 0.0190303 0.0159028 -0.115925 -0.119451
#: 13 0.0159028 0.0127752 -0.119451 -0.122975
#: 14 0.0127752 0.0095892 -0.122975 -0.127097
#: 15 0.0095892 0.00640321 -0.127097 -0.131219
#: 16 0.00640321 0.00320148 -0.131219 -0.135505
#: 17 0.00320148 0.0 -0.135505 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.13536
#: 19 -0.00322914 -0.00645804 -0.13536 -0.130929
#: 20 -0.00645804 -0.00961494 -0.130929 -0.126948
#: 21 -0.00961494 -0.0127718 -0.126948 -0.122967
#: 22 -0.0127718 -0.0159037 -0.122967 -0.119469
#: 23 -0.0159037 -0.0190356 -0.119469 -0.115971
#: 24 -0.0190356 -0.0220778 -0.115971 -0.111732
#: 25 -0.0220778 -0.02512 -0.111732 -0.107491
#: 26 -0.02512 -0.0376801 -0.107491 -0.105613
#: 27 -0.0376801 -0.05024 -0.105613 -0.103733
#: 28 -0.05024 -0.05024 -0.103733 -0.0905657
#: 29 -0.05024 -0.05024 -0.0905657 -0.0773983
#: 30 -0.05024 -0.05024 -0.0773983 -0.0643721
#: 31 -0.05024 -0.05024 -0.0643721 -0.0513458
#: 32 -0.05024 -0.05024 -0.0513458 -0.0384493
#: 33 -0.05024 -0.05024 -0.0384493 -0.0255537
#: 34 -0.05024 -0.05024 -0.0255537 -0.0127764
#: 35 -0.05024 -0.05024 -0.0127764 0.0
#: slice #: 23
#: 0 0.05024 0.05024 0.0 -0.0125513
#: 1 0.05024 0.05024 -0.0125513 -0.0251017
#: 2 0.05024 0.05024 -0.0251017 -0.037796
#: 3 0.05024 0.05024 -0.037796 -0.0504904
#: 4 0.05024 0.05024 -0.0504904 -0.0633402
#: 5 0.05024 0.05024 -0.0633402 -0.07619
#: 6 0.05024 0.05024 -0.07619 -0.0892096
#: 7 0.05024 0.05024 -0.0892096 -0.102229
#: 8 0.05024 0.0376801 -0.102229 -0.104485
#: 9 0.0376801 0.02512 -0.104485 -0.10674
#: 10 0.02512 0.0220761 -0.10674 -0.111362
#: 11 0.0220761 0.0190325 -0.111362 -0.115982
#: 12 0.0190325 0.0159054 -0.115982 -0.119512
#: 13 0.0159054 0.012778 -0.119512 -0.123041
#: 14 0.012778 0.00959158 -0.123041 -0.127149
#: 15 0.00959158 0.00640512 -0.127149 -0.131257
#: 16 0.00640512 0.00320244 -0.131257 -0.135524
#: 17 0.00320244 0.0 -0.135524 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.13539
#: 19 -0.00322914 -0.00645852 -0.13539 -0.130989
#: 20 -0.00645852 -0.00961542 -0.130989 -0.127015
#: 21 -0.00961542 -0.0127726 -0.127015 -0.123041
#: 22 -0.0127726 -0.0159044 -0.123041 -0.119537
#: 23 -0.0159044 -0.0190361 -0.119537 -0.116034
#: 24 -0.0190361 -0.022078 -0.116034 -0.111386
#: 25 -0.022078 -0.02512 -0.111386 -0.106739
#: 26 -0.02512 -0.0376801 -0.106739 -0.104484
#: 27 -0.0376801 -0.05024 -0.104484 -0.102229
#: 28 -0.05024 -0.05024 -0.102229 -0.0892096
#: 29 -0.05024 -0.05024 -0.0892096 -0.07619
#: 30 -0.05024 -0.05024 -0.07619 -0.0633402
#: 31 -0.05024 -0.05024 -0.0633402 -0.0504904
#: 32 -0.05024 -0.05024 -0.0504904 -0.037796
#: 33 -0.05024 -0.05024 -0.037796 -0.0251017
#: 34 -0.05024 -0.05024 -0.0251017 -0.0125513
#: 35 -0.05024 -0.05024 -0.0125513 0.0
#: 0 0.05024 0.05024 0.0 -0.0253277
#: 1 0.05024 0.05024 -0.0253277 -0.0509176
#: 2 0.05024 0.05024 -0.0509176 -0.0767946
#: 3 0.05024 0.05024 -0.0767946 -0.102981
#: 4 0.05024 0.02512 -0.102981 -0.107116
#: 5 0.02512 0.0190315 -0.107116 -0.115953
#: 6 0.0190315 0.0127766 -0.115953 -0.123008
#: 7 0.0127766 0.00640416 -0.123008 -0.131238
#: 8 0.00640416 0.0 -0.131238 -0.139791
#: 9 0.0 -0.00645828 -0.139791 -0.13096
#: 10 -0.00645828 -0.0127721 -0.13096 -0.123004
#: 11 -0.0127721 -0.0190358 -0.123004 -0.116002
#: 12 -0.0190358 -0.02512 -0.116002 -0.107116
#: 13 -0.02512 -0.05024 -0.107116 -0.102981
#: 14 -0.05024 -0.05024 -0.102981 -0.0767946
#: 15 -0.05024 -0.05024 -0.0767946 -0.0509176
#: 16 -0.05024 -0.05024 -0.0509176 -0.0253277
#: 17 -0.05024 -0.05024 -0.0253277 0.0
#: 0 0.05024 0.05024 0.0 -0.0127764
#: 1 0.05024 0.05024 -0.0127764 -0.0255537
#: 2 0.05024 0.05024 -0.0255537 -0.0384493
#: 3 0.05024 0.05024 -0.0384493 -0.0513458
#: 4 0.05024 0.05024 -0.0513458 -0.0643721
#: 5 0.05024 0.05024 -0.0643721 -0.0773983
#: 6 0.05024 0.05024 -0.0773983 -0.0905657
#: 7 0.05024 0.05024 -0.0905657 -0.103733
#: 8 0.05024 0.0376801 -0.103733 -0.105613
#: 9 0.0376801 0.02512 -0.105613 -0.107491
#: 10 0.02512 0.0220752 -0.107491 -0.111709
#: 11 0.0220752 0.0190303 -0.111709 -0.115925
#: 12 0.0190303 0.0159028 -0.115925 -0.119451
#: 13 0.0159028 0.0127752 -0.119451 -0.122975
#: 14 0.0127752 0.0095892 -0.122975 -0.127097
#: 15 0.0095892 0.00640321 -0.127097 -0.131219
#: 16 0.00640321 0.00320148 -0.131219 -0.135505
#: 17 0.00320148 0.0 -0.135505 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.13536
#: 19 -0.00322914 -0.00645804 -0.13536 -0.130929
#: 20 -0.00645804 -0.00961494 -0.130929 -0.126948
#: 21 -0.00961494 -0.0127718 -0.126948 -0.122967
#: 22 -0.0127718 -0.0159037 -0.122967 -0.119469
#: 23 -0.0159037 -0.0190356 -0.119469 -0.115971
#: 24 -0.0190356 -0.0220778 -0.115971 -0.111732
#: 25 -0.0220778 -0.02512 -0.111732 -0.107491
#: 26 -0.02512 -0.0376801 -0.107491 -0.105613
#: 27 -0.0376801 -0.05024 -0.105613 -0.103733
#: 28 -0.05024 -0.05024 -0.103733 -0.0905657
#: 29 -0.05024 -0.05024 -0.0905657 -0.0773983
#: 30 -0.05024 -0.05024 -0.0773983 -0.0643721
#: 31 -0.05024 -0.05024 -0.0643721 -0.0513458
#: 32 -0.05024 -0.05024 -0.0513458 -0.0384493
#: 33 -0.05024 -0.05024 -0.0384493 -0.0255537
#: 34 -0.05024 -0.05024 -0.0255537 -0.0127764
#: 35 -0.05024 -0.05024 -0.0127764 0.0
#: 0 0.05024 0.05024 0.0 -0.0257797
#: 1 0.05024 0.05024 -0.0257797 -0.051774
#: 2 0.05024 0.05024 -0.051774 -0.078002
#: 3 0.05024 0.05024 -0.078002 -0.104485
#: 4 0.05024 0.02512 -0.104485 -0.107867
#: 5 0.02512 0.0190277 -0.107867 -0.115906
#: 6 0.0190277 0.0127714 -0.115906 -0.122954
#: 7 0.0127714 0.00640059 -0.122954 -0.131207
#: 8 0.00640059 0.0 -0.131207 -0.139791
#: 9 0.0 -0.00645685 -0.139791 -0.130908
#: 10 -0.00645685 -0.0127685 -0.130908 -0.12295
#: 11 -0.0127685 -0.0190334 -0.12295 -0.115953
#: 12 -0.0190334 -0.02512 -0.115953 -0.107867
#: 13 -0.02512 -0.05024 -0.107867 -0.104485
#: 14 -0.05024 -0.05024 -0.104485 -0.078002
#: 15 -0.05024 -0.05024 -0.078002 -0.051774
#: 16 -0.05024 -0.05024 -0.051774 -0.0257797
#: 17 -0.05024 -0.05024 -0.0257797 0.0
#: 0 0.05024 0.05024 0.0 -0.0130033
#: 1 0.05024 0.05024 -0.0130033 -0.0260057
#: 2 0.05024 0.05024 -0.0260057 -0.0391035
#: 3 0.05024 0.05024 -0.0391035 -0.0522013
#: 4 0.05024 0.05024 -0.0522013 -0.0654039
#: 5 0.05024 0.05024 -0.0654039 -0.0786057
#: 6 0.05024 0.05024 -0.0786057 -0.0919209
#: 7 0.05024 0.05024 -0.0919209 -0.105236
#: 8 0.05024 0.0376801 -0.105236 -0.10674
#: 9 0.0376801 0.02512 -0.10674 -0.108243
#: 10 0.02512 0.0220728 -0.108243 -0.112065
#: 11 0.0220728 0.0190253 -0.112065 -0.115887
#: 12 0.0190253 0.0158963 -0.115887 -0.119411
#: 13 0.0158963 0.0127676 -0.119411 -0.122933
#: 14 0.0127676 0.00958276 -0.122933 -0.127065
#: 15 0.00958276 0.00639796 -0.127065 -0.131196
#: 16 0.00639796 0.0031991 -0.131196 -0.135493
#: 17 0.0031991 0.0 -0.135493 -0.139791
#: 18 0.0 -0.00322795 -0.139791 -0.135339
#: 19 -0.00322795 -0.0064559 -0.135339 -0.130886
#: 20 -0.0064559 -0.00961065 -0.130886 -0.126909
#: 21 -0.00961065 -0.0127652 -0.126909 -0.122932
#: 22 -0.0127652 -0.0158982 -0.122932 -0.119434
#: 23 -0.0158982 -0.019031 -0.119434 -0.115936
#: 24 -0.019031 -0.0220757 -0.115936 -0.11209
#: 25 -0.0220757 -0.02512 -0.11209 -0.108243
#: 26 -0.02512 -0.0376801 -0.108243 -0.10674
#: 27 -0.0376801 -0.05024 -0.10674 -0.105236
#: 28 -0.05024 -0.05024 -0.105236 -0.0919209
#: 29 -0.05024 -0.05024 -0.0919209 -0.0786057
#: 30 -0.05024 -0.05024 -0.0786057 -0.0654039
#: 31 -0.05024 -0.05024 -0.0654039 -0.0522013
#: 32 -0.05024 -0.05024 -0.0522013 -0.0391035
#: 33 -0.05024 -0.05024 -0.0391035 -0.0260057
#: 34 -0.05024 -0.05024 -0.0260057 -0.0130033
#: 35 -0.05024 -0.05024 -0.0130033 0.0
#: slice #: 24
#: 0 0.05024 0.05024 0.0 -0.0127764
#: 1 0.05024 0.05024 -0.0127764 -0.0255537
#: 2 0.05024 0.05024 -0.0255537 -0.0384493
#: 3 0.05024 0.05024 -0.0384493 -0.0513458
#: 4 0.05024 0.05024 -0.0513458 -0.0643721
#: 5 0.05024 0.05024 -0.0643721 -0.0773983
#: 6 0.05024 0.05024 -0.0773983 -0.0905657
#: 7 0.05024 0.05024 -0.0905657 -0.103733
#: 8 0.05024 0.0376801 -0.103733 -0.105613
#: 9 0.0376801 0.02512 -0.105613 -0.107491
#: 10 0.02512 0.0220752 -0.107491 -0.111709
#: 11 0.0220752 0.0190303 -0.111709 -0.115925
#: 12 0.0190303 0.0159028 -0.115925 -0.119451
#: 13 0.0159028 0.0127752 -0.119451 -0.122975
#: 14 0.0127752 0.0095892 -0.122975 -0.127097
#: 15 0.0095892 0.00640321 -0.127097 -0.131219
#: 16 0.00640321 0.00320148 -0.131219 -0.135505
#: 17 0.00320148 0.0 -0.135505 -0.139791
#: 18 0.0 -0.00322914 -0.139791 -0.13536
#: 19 -0.00322914 -0.00645804 -0.13536 -0.130929
#: 20 -0.00645804 -0.00961494 -0.130929 -0.126948
#: 21 -0.00961494 -0.0127718 -0.126948 -0.122967
#: 22 -0.0127718 -0.0159037 -0.122967 -0.119469
#: 23 -0.0159037 -0.0190356 -0.119469 -0.115971
#: 24 -0.0190356 -0.0220778 -0.115971 -0.111732
#: 25 -0.0220778 -0.02512 -0.111732 -0.107491
#: 26 -0.02512 -0.0376801 -0.107491 -0.105613
#: 27 -0.0376801 -0.05024 -0.105613 -0.103733
#: 28 -0.05024 -0.05024 -0.103733 -0.0905657
#: 29 -0.05024 -0.05024 -0.0905657 -0.0773983
#: 30 -0.05024 -0.05024 -0.0773983 -0.0643721
#: 31 -0.05024 -0.05024 -0.0643721 -0.0513458
#: 32 -0.05024 -0.05024 -0.0513458 -0.0384493
#: 33 -0.05024 -0.05024 -0.0384493 -0.0255537
#: 34 -0.05024 -0.05024 -0.0255537 -0.0127764
#: 35 -0.05024 -0.05024 -0.0127764 0.0
#: 0 0.05024 0.05024 0.0 -0.0257797
#: 1 0.05024 0.05024 -0.0257797 -0.051774
#: 2 0.05024 0.05024 -0.051774 -0.078002
#: 3 0.05024 0.05024 -0.078002 -0.104485
#: 4 0.05024 0.02512 -0.104485 -0.107867
#: 5 0.02512 0.0190277 -0.107867 -0.115906
#: 6 0.0190277 0.0127714 -0.115906 -0.122954
#: 7 0.0127714 0.00640059 -0.122954 -0.131207
#: 8 0.00640059 0.0 -0.131207 -0.139791
#: 9 0.0 -0.00645685 -0.139791 -0.130908
#: 10 -0.00645685 -0.0127685 -0.130908 -0.12295
#: 11 -0.0127685 -0.0190334 -0.12295 -0.115953
#: 12 -0.0190334 -0.02512 -0.115953 -0.107867
#: 13 -0.02512 -0.05024 -0.107867 -0.104485
#: 14 -0.05024 -0.05024 -0.104485 -0.078002
#: 15 -0.05024 -0.05024 -0.078002 -0.051774
#: 16 -0.05024 -0.05024 -0.051774 -0.0257797
#: 17 -0.05024 -0.05024 -0.0257797 0.0
#: 0 0.05024 0.05024 0.0 -0.0130033
#: 1 0.05024 0.05024 -0.0130033 -0.0260057
#: 2 0.05024 0.05024 -0.0260057 -0.0391035
#: 3 0.05024 0.05024 -0.0391035 -0.0522013
#: 4 0.05024 0.05024 -0.0522013 -0.0654039
#: 5 0.05024 0.05024 -0.0654039 -0.0786057
#: 6 0.05024 0.05024 -0.0786057 -0.0919209
#: 7 0.05024 0.05024 -0.0919209 -0.105236
#: 8 0.05024 0.0376801 -0.105236 -0.10674
#: 9 0.0376801 0.02512 -0.10674 -0.108243
#: 10 0.02512 0.0220728 -0.108243 -0.112065
#: 11 0.0220728 0.0190253 -0.112065 -0.115887
#: 12 0.0190253 0.0158963 -0.115887 -0.119411
#: 13 0.0158963 0.0127676 -0.119411 -0.122933
#: 14 0.0127676 0.00958276 -0.122933 -0.127065
#: 15 0.00958276 0.00639796 -0.127065 -0.131196
#: 16 0.00639796 0.0031991 -0.131196 -0.135493
#: 17 0.0031991 0.0 -0.135493 -0.139791
#: 18 0.0 -0.00322795 -0.139791 -0.135339
#: 19 -0.00322795 -0.0064559 -0.135339 -0.130886
#: 20 -0.0064559 -0.00961065 -0.130886 -0.126909
#: 21 -0.00961065 -0.0127652 -0.126909 -0.122932
#: 22 -0.0127652 -0.0158982 -0.122932 -0.119434
#: 23 -0.0158982 -0.019031 -0.119434 -0.115936
#: 24 -0.019031 -0.0220757 -0.115936 -0.11209
#: 25 -0.0220757 -0.02512 -0.11209 -0.108243
#: 26 -0.02512 -0.0376801 -0.108243 -0.10674
#: 27 -0.0376801 -0.05024 -0.10674 -0.105236
#: 28 -0.05024 -0.05024 -0.105236 -0.0919209
#: 29 -0.05024 -0.05024 -0.0919209 -0.0786057
#: 30 -0.05024 -0.05024 -0.0786057 -0.0654039
#: 31 -0.05024 -0.05024 -0.0654039 -0.0522013
#: 32 -0.05024 -0.05024 -0.0522013 -0.0391035
#: 33 -0.05024 -0.05024 -0.0391035 -0.0260057
#: 34 -0.05024 -0.05024 -0.0260057 -0.0130033
#: 35 -0.05024 -0.05024 -0.0130033 0.0
#: 0 0.05024 0.05024 0.0 -0.0262308
#: 1 0.05024 0.05024 -0.0262308 -0.0526295
#: 2 0.05024 0.05024 -0.0526295 -0.0792093
#: 3 0.05024 0.05024 -0.0792093 -0.105989
#: 4 0.05024 0.02512 -0.105989 -0.108619
#: 5 0.02512 0.0190187 -0.108619 -0.115887
#: 6 0.0190187 0.012759 -0.115887 -0.122937
#: 7 0.012759 0.00639224 -0.122937 -0.1312
#: 8 0.00639224 0.0 -0.1312 -0.139791
#: 9 0.0 -0.00644779 -0.139791 -0.130908
#: 10 -0.00644779 -0.0127513 -0.130908 -0.122977
#: 11 -0.0127513 -0.0190206 -0.122977 -0.115969
#: 12 -0.0190206 -0.02512 -0.115969 -0.108619
#: 13 -0.02512 -0.05024 -0.108619 -0.105989
#: 14 -0.05024 -0.05024 -0.105989 -0.0792093
#: 15 -0.05024 -0.05024 -0.0792093 -0.0526295
#: 16 -0.05024 -0.05024 -0.0526295 -0.0262308
#: 17 -0.05024 -0.05024 -0.0262308 0.0
#: 0 0.05024 0.05024 0.0 -0.0132284
#: 1 0.05024 0.05024 -0.0132284 -0.0264568
#: 2 0.05024 0.05024 -0.0264568 -0.0397577
#: 3 0.05024 0.05024 -0.0397577 -0.0530577
#: 4 0.05024 0.05024 -0.0530577 -0.0664358
#: 5 0.05024 0.05024 -0.0664358 -0.079814
#: 6 0.05024 0.05024 -0.079814 -0.093277
#: 7 0.05024 0.05024 -0.093277 -0.10674
#: 8 0.05024 0.0376801 -0.10674 -0.107867
#: 9 0.0376801 0.02512 -0.107867 -0.108994
#: 10 0.02512 0.0220661 -0.108994 -0.112441
#: 11 0.0220661 0.0190122 -0.112441 -0.115887
#: 12 0.0190122 0.0158813 -0.115887 -0.119414
#: 13 0.0158813 0.0127504 -0.119414 -0.122941
#: 14 0.0127504 0.00956845 -0.122941 -0.127072
#: 15 0.00956845 0.00638652 -0.127072 -0.131203
#: 16 0.00638652 0.00319338 -0.131203 -0.135497
#: 17 0.00319338 0.0 -0.135497 -0.139791
#: 18 0.0 -0.00322008 -0.139791 -0.13536
#: 19 -0.00322008 -0.00643992 -0.13536 -0.130929
#: 20 -0.00643992 -0.00958872 -0.130929 -0.126975
#: 21 -0.00958872 -0.0127375 -0.126975 -0.123021
#: 22 -0.0127375 -0.0158739 -0.123021 -0.119512
#: 23 -0.0158739 -0.0190103 -0.119512 -0.116001
#: 24 -0.0190103 -0.0220652 -0.116001 -0.112498
#: 25 -0.0220652 -0.02512 -0.112498 -0.108994
#: 26 -0.02512 -0.0376801 -0.108994 -0.107867
#: 27 -0.0376801 -0.05024 -0.107867 -0.10674
#: 28 -0.05024 -0.05024 -0.10674 -0.093277
#: 29 -0.05024 -0.05024 -0.093277 -0.079814
#: 30 -0.05024 -0.05024 -0.079814 -0.0664358
#: 31 -0.05024 -0.05024 -0.0664358 -0.0530577
#: 32 -0.05024 -0.05024 -0.0530577 -0.0397577
#: 33 -0.05024 -0.05024 -0.0397577 -0.0264568
#: 34 -0.05024 -0.05024 -0.0264568 -0.0132284
#: 35 -0.05024 -0.05024 -0.0132284 0.0
#: slice #: 25
#: 0 0.05024 0.05024 0.0 -0.0130033
#: 1 0.05024 0.05024 -0.0130033 -0.0260057
#: 2 0.05024 0.05024 -0.0260057 -0.0391035
#: 3 0.05024 0.05024 -0.0391035 -0.0522013
#: 4 0.05024 0.05024 -0.0522013 -0.0654039
#: 5 0.05024 0.05024 -0.0654039 -0.0786057
#: 6 0.05024 0.05024 -0.0786057 -0.0919209
#: 7 0.05024 0.05024 -0.0919209 -0.105236
#: 8 0.05024 0.0376801 -0.105236 -0.10674
#: 9 0.0376801 0.02512 -0.10674 -0.108243
#: 10 0.02512 0.0220728 -0.108243 -0.112065
#: 11 0.0220728 0.0190253 -0.112065 -0.115887
#: 12 0.0190253 0.0158963 -0.115887 -0.119411
#: 13 0.0158963 0.0127676 -0.119411 -0.122933
#: 14 0.0127676 0.00958276 -0.122933 -0.127065
#: 15 0.00958276 0.00639796 -0.127065 -0.131196
#: 16 0.00639796 0.0031991 -0.131196 -0.135493
#: 17 0.0031991 0.0 -0.135493 -0.139791
#: 18 0.0 -0.00322795 -0.139791 -0.135339
#: 19 -0.00322795 -0.0064559 -0.135339 -0.130886
#: 20 -0.0064559 -0.00961065 -0.130886 -0.126909
#: 21 -0.00961065 -0.0127652 -0.126909 -0.122932
#: 22 -0.0127652 -0.0158982 -0.122932 -0.119434
#: 23 -0.0158982 -0.019031 -0.119434 -0.115936
#: 24 -0.019031 -0.0220757 -0.115936 -0.11209
#: 25 -0.0220757 -0.02512 -0.11209 -0.108243
#: 26 -0.02512 -0.0376801 -0.108243 -0.10674
#: 27 -0.0376801 -0.05024 -0.10674 -0.105236
#: 28 -0.05024 -0.05024 -0.105236 -0.0919209
#: 29 -0.05024 -0.05024 -0.0919209 -0.0786057
#: 30 -0.05024 -0.05024 -0.0786057 -0.0654039
#: 31 -0.05024 -0.05024 -0.0654039 -0.0522013
#: 32 -0.05024 -0.05024 -0.0522013 -0.0391035
#: 33 -0.05024 -0.05024 -0.0391035 -0.0260057
#: 34 -0.05024 -0.05024 -0.0260057 -0.0130033
#: 35 -0.05024 -0.05024 -0.0130033 0.0
#: 0 0.05024 0.05024 0.0 -0.0262308
#: 1 0.05024 0.05024 -0.0262308 -0.0526295
#: 2 0.05024 0.05024 -0.0526295 -0.0792093
#: 3 0.05024 0.05024 -0.0792093 -0.105989
#: 4 0.05024 0.02512 -0.105989 -0.108619
#: 5 0.02512 0.0190187 -0.108619 -0.115887
#: 6 0.0190187 0.012759 -0.115887 -0.122937
#: 7 0.012759 0.00639224 -0.122937 -0.1312
#: 8 0.00639224 0.0 -0.1312 -0.139791
#: 9 0.0 -0.00644779 -0.139791 -0.130908
#: 10 -0.00644779 -0.0127513 -0.130908 -0.122977
#: 11 -0.0127513 -0.0190206 -0.122977 -0.115969
#: 12 -0.0190206 -0.02512 -0.115969 -0.108619
#: 13 -0.02512 -0.05024 -0.108619 -0.105989
#: 14 -0.05024 -0.05024 -0.105989 -0.0792093
#: 15 -0.05024 -0.05024 -0.0792093 -0.0526295
#: 16 -0.05024 -0.05024 -0.0526295 -0.0262308
#: 17 -0.05024 -0.05024 -0.0262308 0.0
#: 0 0.05024 0.05024 0.0 -0.0132284
#: 1 0.05024 0.05024 -0.0132284 -0.0264568
#: 2 0.05024 0.05024 -0.0264568 -0.0397577
#: 3 0.05024 0.05024 -0.0397577 -0.0530577
#: 4 0.05024 0.05024 -0.0530577 -0.0664358
#: 5 0.05024 0.05024 -0.0664358 -0.079814
#: 6 0.05024 0.05024 -0.079814 -0.093277
#: 7 0.05024 0.05024 -0.093277 -0.10674
#: 8 0.05024 0.0376801 -0.10674 -0.107867
#: 9 0.0376801 0.02512 -0.107867 -0.108994
#: 10 0.02512 0.0220661 -0.108994 -0.112441
#: 11 0.0220661 0.0190122 -0.112441 -0.115887
#: 12 0.0190122 0.0158813 -0.115887 -0.119414
#: 13 0.0158813 0.0127504 -0.119414 -0.122941
#: 14 0.0127504 0.00956845 -0.122941 -0.127072
#: 15 0.00956845 0.00638652 -0.127072 -0.131203
#: 16 0.00638652 0.00319338 -0.131203 -0.135497
#: 17 0.00319338 0.0 -0.135497 -0.139791
#: 18 0.0 -0.00322008 -0.139791 -0.13536
#: 19 -0.00322008 -0.00643992 -0.13536 -0.130929
#: 20 -0.00643992 -0.00958872 -0.130929 -0.126975
#: 21 -0.00958872 -0.0127375 -0.126975 -0.123021
#: 22 -0.0127375 -0.0158739 -0.123021 -0.119512
#: 23 -0.0158739 -0.0190103 -0.119512 -0.116001
#: 24 -0.0190103 -0.0220652 -0.116001 -0.112498
#: 25 -0.0220652 -0.02512 -0.112498 -0.108994
#: 26 -0.02512 -0.0376801 -0.108994 -0.107867
#: 27 -0.0376801 -0.05024 -0.107867 -0.10674
#: 28 -0.05024 -0.05024 -0.10674 -0.093277
#: 29 -0.05024 -0.05024 -0.093277 -0.079814
#: 30 -0.05024 -0.05024 -0.079814 -0.0664358
#: 31 -0.05024 -0.05024 -0.0664358 -0.0530577
#: 32 -0.05024 -0.05024 -0.0530577 -0.0397577
#: 33 -0.05024 -0.05024 -0.0397577 -0.0264568
#: 34 -0.05024 -0.05024 -0.0264568 -0.0132284
#: 35 -0.05024 -0.05024 -0.0132284 0.0
#: 0 0.05024 0.05024 0.0 -0.0266829
#: 1 0.05024 0.05024 -0.0266829 -0.0534849
#: 2 0.05024 0.05024 -0.0534849 -0.0804176
#: 3 0.05024 0.05024 -0.0804176 -0.107491
#: 4 0.05024 0.02512 -0.107491 -0.10937
#: 5 0.02512 0.0189991 -0.10937 -0.115926
#: 6 0.0189991 0.0127337 -0.115926 -0.122989
#: 7 0.0127337 0.00637627 -0.122989 -0.131233
#: 8 0.00637627 0.0 -0.131233 -0.139791
#: 9 0.0 -0.00642014 -0.139791 -0.131017
#: 10 -0.00642014 -0.0127101 -0.131017 -0.123136
#: 11 -0.0127101 -0.0189862 -0.123136 -0.116107
#: 12 -0.0189862 -0.02512 -0.116107 -0.10937
#: 13 -0.02512 -0.05024 -0.10937 -0.107491
#: 14 -0.05024 -0.05024 -0.107491 -0.0804176
#: 15 -0.05024 -0.05024 -0.0804176 -0.0534849
#: 16 -0.05024 -0.05024 -0.0534849 -0.0266829
#: 17 -0.05024 -0.05024 -0.0266829 0.0
#: 0 0.05024 0.05024 0.0 -0.0134544
#: 1 0.05024 0.05024 -0.0134544 -0.0269089
#: 2 0.05024 0.05024 -0.0269089 -0.040411
#: 3 0.05024 0.05024 -0.040411 -0.0539131
#: 4 0.05024 0.05024 -0.0539131 -0.0674677
#: 5 0.05024 0.05024 -0.0674677 -0.0810213
#: 6 0.05024 0.05024 -0.0810213 -0.0946321
#: 7 0.05024 0.05024 -0.0946321 -0.108243
#: 8 0.05024 0.0376801 -0.108243 -0.108994
#: 9 0.0376801 0.02512 -0.108994 -0.109746
#: 10 0.02512 0.022053 -0.109746 -0.112855
#: 11 0.022053 0.018986 -0.112855 -0.115965
#: 12 0.018986 0.0158515 -0.115965 -0.119501
#: 13 0.0158515 0.012717 -0.119501 -0.123037
#: 14 0.012717 0.00954151 -0.123037 -0.127151
#: 15 0.00954151 0.00636578 -0.127151 -0.131264
#: 16 0.00636578 0.00318289 -0.131264 -0.135528
#: 17 0.00318289 0.0 -0.135528 -0.139791
#: 18 0.0 -0.00320005 -0.139791 -0.135448
#: 19 -0.00320005 -0.00640035 -0.135448 -0.131104
#: 20 -0.00640035 -0.00954151 -0.131104 -0.127177
#: 21 -0.00954151 -0.0126824 -0.127177 -0.123251
#: 22 -0.0126824 -0.0158222 -0.123251 -0.119731
#: 23 -0.0158222 -0.0189619 -0.119731 -0.116212
#: 24 -0.0189619 -0.0220408 -0.116212 -0.112979
#: 25 -0.0220408 -0.02512 -0.112979 -0.109746
#: 26 -0.02512 -0.0376801 -0.109746 -0.108994
#: 27 -0.0376801 -0.05024 -0.108994 -0.108243
#: 28 -0.05024 -0.05024 -0.108243 -0.0946321
#: 29 -0.05024 -0.05024 -0.0946321 -0.0810213
#: 30 -0.05024 -0.05024 -0.0810213 -0.0674677
#: 31 -0.05024 -0.05024 -0.0674677 -0.0539131
#: 32 -0.05024 -0.05024 -0.0539131 -0.040411
#: 33 -0.05024 -0.05024 -0.040411 -0.0269089
#: 34 -0.05024 -0.05024 -0.0269089 -0.0134544
#: 35 -0.05024 -0.05024 -0.0134544 0.0
#: slice #: 26
#: 0 0.05024 0.05024 0.0 -0.0132284
#: 1 0.05024 0.05024 -0.0132284 -0.0264568
#: 2 0.05024 0.05024 -0.0264568 -0.0397577
#: 3 0.05024 0.05024 -0.0397577 -0.0530577
#: 4 0.05024 0.05024 -0.0530577 -0.0664358
#: 5 0.05024 0.05024 -0.0664358 -0.079814
#: 6 0.05024 0.05024 -0.079814 -0.093277
#: 7 0.05024 0.05024 -0.093277 -0.10674
#: 8 0.05024 0.0376801 -0.10674 -0.107867
#: 9 0.0376801 0.02512 -0.107867 -0.108994
#: 10 0.02512 0.0220661 -0.108994 -0.112441
#: 11 0.0220661 0.0190122 -0.112441 -0.115887
#: 12 0.0190122 0.0158813 -0.115887 -0.119414
#: 13 0.0158813 0.0127504 -0.119414 -0.122941
#: 14 0.0127504 0.00956845 -0.122941 -0.127072
#: 15 0.00956845 0.00638652 -0.127072 -0.131203
#: 16 0.00638652 0.00319338 -0.131203 -0.135497
#: 17 0.00319338 0.0 -0.135497 -0.139791
#: 18 0.0 -0.00322008 -0.139791 -0.13536
#: 19 -0.00322008 -0.00643992 -0.13536 -0.130929
#: 20 -0.00643992 -0.00958872 -0.130929 -0.126975
#: 21 -0.00958872 -0.0127375 -0.126975 -0.123021
#: 22 -0.0127375 -0.0158739 -0.123021 -0.119512
#: 23 -0.0158739 -0.0190103 -0.119512 -0.116001
#: 24 -0.0190103 -0.0220652 -0.116001 -0.112498
#: 25 -0.0220652 -0.02512 -0.112498 -0.108994
#: 26 -0.02512 -0.0376801 -0.108994 -0.107867
#: 27 -0.0376801 -0.05024 -0.107867 -0.10674
#: 28 -0.05024 -0.05024 -0.10674 -0.093277
#: 29 -0.05024 -0.05024 -0.093277 -0.079814
#: 30 -0.05024 -0.05024 -0.079814 -0.0664358
#: 31 -0.05024 -0.05024 -0.0664358 -0.0530577
#: 32 -0.05024 -0.05024 -0.0530577 -0.0397577
#: 33 -0.05024 -0.05024 -0.0397577 -0.0264568
#: 34 -0.05024 -0.05024 -0.0264568 -0.0132284
#: 35 -0.05024 -0.05024 -0.0132284 0.0
#: 0 0.05024 0.05024 0.0 -0.0266829
#: 1 0.05024 0.05024 -0.0266829 -0.0534849
#: 2 0.05024 0.05024 -0.0534849 -0.0804176
#: 3 0.05024 0.05024 -0.0804176 -0.107491
#: 4 0.05024 0.02512 -0.107491 -0.10937
#: 5 0.02512 0.0189991 -0.10937 -0.115926
#: 6 0.0189991 0.0127337 -0.115926 -0.122989
#: 7 0.0127337 0.00637627 -0.122989 -0.131233
#: 8 0.00637627 0.0 -0.131233 -0.139791
#: 9 0.0 -0.00642014 -0.139791 -0.131017
#: 10 -0.00642014 -0.0127101 -0.131017 -0.123136
#: 11 -0.0127101 -0.0189862 -0.123136 -0.116107
#: 12 -0.0189862 -0.02512 -0.116107 -0.10937
#: 13 -0.02512 -0.05024 -0.10937 -0.107491
#: 14 -0.05024 -0.05024 -0.107491 -0.0804176
#: 15 -0.05024 -0.05024 -0.0804176 -0.0534849
#: 16 -0.05024 -0.05024 -0.0534849 -0.0266829
#: 17 -0.05024 -0.05024 -0.0266829 0.0
#: 0 0.05024 0.05024 0.0 -0.0134544
#: 1 0.05024 0.05024 -0.0134544 -0.0269089
#: 2 0.05024 0.05024 -0.0269089 -0.040411
#: 3 0.05024 0.05024 -0.040411 -0.0539131
#: 4 0.05024 0.05024 -0.0539131 -0.0674677
#: 5 0.05024 0.05024 -0.0674677 -0.0810213
#: 6 0.05024 0.05024 -0.0810213 -0.0946321
#: 7 0.05024 0.05024 -0.0946321 -0.108243
#: 8 0.05024 0.0376801 -0.108243 -0.108994
#: 9 0.0376801 0.02512 -0.108994 -0.109746
#: 10 0.02512 0.022053 -0.109746 -0.112855
#: 11 0.022053 0.018986 -0.112855 -0.115965
#: 12 0.018986 0.0158515 -0.115965 -0.119501
#: 13 0.0158515 0.012717 -0.119501 -0.123037
#: 14 0.012717 0.00954151 -0.123037 -0.127151
#: 15 0.00954151 0.00636578 -0.127151 -0.131264
#: 16 0.00636578 0.00318289 -0.131264 -0.135528
#: 17 0.00318289 0.0 -0.135528 -0.139791
#: 18 0.0 -0.00320005 -0.139791 -0.135448
#: 19 -0.00320005 -0.00640035 -0.135448 -0.131104
#: 20 -0.00640035 -0.00954151 -0.131104 -0.127177
#: 21 -0.00954151 -0.0126824 -0.127177 -0.123251
#: 22 -0.0126824 -0.0158222 -0.123251 -0.119731
#: 23 -0.0158222 -0.0189619 -0.119731 -0.116212
#: 24 -0.0189619 -0.0220408 -0.116212 -0.112979
#: 25 -0.0220408 -0.02512 -0.112979 -0.109746
#: 26 -0.02512 -0.0376801 -0.109746 -0.108994
#: 27 -0.0376801 -0.05024 -0.108994 -0.108243
#: 28 -0.05024 -0.05024 -0.108243 -0.0946321
#: 29 -0.05024 -0.05024 -0.0946321 -0.0810213
#: 30 -0.05024 -0.05024 -0.0810213 -0.0674677
#: 31 -0.05024 -0.05024 -0.0674677 -0.0539131
#: 32 -0.05024 -0.05024 -0.0539131 -0.040411
#: 33 -0.05024 -0.05024 -0.040411 -0.0269089
#: 34 -0.05024 -0.05024 -0.0269089 -0.0134544
#: 35 -0.05024 -0.05024 -0.0134544 0.0
#: 0 0.05024 0.05024 0.0 -0.0271349
#: 1 0.05024 0.05024 -0.0271349 -0.0543413
#: 2 0.05024 0.05024 -0.0543413 -0.0816259
#: 3 0.05024 0.05024 -0.0816259 -0.108994
#: 4 0.05024 0.02512 -0.108994 -0.110122
#: 5 0.02512 0.0189652 -0.110122 -0.116057
#: 6 0.0189652 0.0126922 -0.116057 -0.123144
#: 7 0.0126922 0.00635099 -0.123144 -0.13133
#: 8 0.00635099 0.0 -0.13133 -0.139791
#: 9 0.0 -0.00638294 -0.139791 -0.131186
#: 10 -0.00638294 -0.012661 -0.131186 -0.123351
#: 11 -0.012661 -0.0189347 -0.123351 -0.116338
#: 12 -0.0189347 -0.02512 -0.116338 -0.110122
#: 13 -0.02512 -0.05024 -0.110122 -0.108994
#: 14 -0.05024 -0.05024 -0.108994 -0.0816259
#: 15 -0.05024 -0.05024 -0.0816259 -0.0543413
#: 16 -0.05024 -0.05024 -0.0543413 -0.0271349
#: 17 -0.05024 -0.05024 -0.0271349 0.0
#: 0 0.05024 0.05024 0.0 -0.0136805
#: 1 0.05024 0.05024 -0.0136805 -0.0273609
#: 2 0.05024 0.05024 -0.0273609 -0.0410652
#: 3 0.05024 0.05024 -0.0410652 -0.0547695
#: 4 0.05024 0.05024 -0.0547695 -0.0684996
#: 5 0.05024 0.05024 -0.0684996 -0.0822296
#: 6 0.05024 0.05024 -0.0822296 -0.0959883
#: 7 0.05024 0.05024 -0.0959883 -0.109747
#: 8 0.05024 0.0376801 -0.109747 -0.110123
#: 9 0.0376801 0.02512 -0.110123 -0.110498
#: 10 0.02512 0.0220323 -0.110498 -0.113324
#: 11 0.0220323 0.0189443 -0.113324 -0.11615
#: 12 0.0189443 0.0158057 -0.11615 -0.1197
#: 13 0.0158057 0.0126674 -0.1197 -0.123251
#: 14 0.0126674 0.0095017 -0.123251 -0.127322
#: 15 0.0095017 0.00633597 -0.127322 -0.131394
#: 16 0.00633597 0.00316811 -0.131394 -0.135592
#: 17 0.00316811 0.0 -0.135592 -0.139791
#: 18 0.0 -0.00318289 -0.139791 -0.13553
#: 19 -0.00318289 -0.00636554 -0.13553 -0.131269
#: 20 -0.00636554 -0.00950241 -0.131269 -0.12736
#: 21 -0.00950241 -0.0126393 -0.12736 -0.123451
#: 22 -0.0126393 -0.0157733 -0.123451 -0.119957
#: 23 -0.0157733 -0.0189073 -0.119957 -0.116463
#: 24 -0.0189073 -0.0220137 -0.116463 -0.113481
#: 25 -0.0220137 -0.02512 -0.113481 -0.110497
#: 26 -0.02512 -0.0376801 -0.110497 -0.110122
#: 27 -0.0376801 -0.05024 -0.110122 -0.109747
#: 28 -0.05024 -0.05024 -0.109747 -0.0959883
#: 29 -0.05024 -0.05024 -0.0959883 -0.0822296
#: 30 -0.05024 -0.05024 -0.0822296 -0.0684996
#: 31 -0.05024 -0.05024 -0.0684996 -0.0547695
#: 32 -0.05024 -0.05024 -0.0547695 -0.0410652
#: 33 -0.05024 -0.05024 -0.0410652 -0.0273609
#: 34 -0.05024 -0.05024 -0.0273609 -0.0136805
#: 35 -0.05024 -0.05024 -0.0136805 0.0
#: slice #: 27
#: 0 0.05024 0.05024 0.0 -0.0134544
#: 1 0.05024 0.05024 -0.0134544 -0.0269089
#: 2 0.05024 0.05024 -0.0269089 -0.040411
#: 3 0.05024 0.05024 -0.040411 -0.0539131
#: 4 0.05024 0.05024 -0.0539131 -0.0674677
#: 5 0.05024 0.05024 -0.0674677 -0.0810213
#: 6 0.05024 0.05024 -0.0810213 -0.0946321
#: 7 0.05024 0.05024 -0.0946321 -0.108243
#: 8 0.05024 0.0376801 -0.108243 -0.108994
#: 9 0.0376801 0.02512 -0.108994 -0.109746
#: 10 0.02512 0.022053 -0.109746 -0.112855
#: 11 0.022053 0.018986 -0.112855 -0.115965
#: 12 0.018986 0.0158515 -0.115965 -0.119501
#: 13 0.0158515 0.012717 -0.119501 -0.123037
#: 14 0.012717 0.00954151 -0.123037 -0.127151
#: 15 0.00954151 0.00636578 -0.127151 -0.131264
#: 16 0.00636578 0.00318289 -0.131264 -0.135528
#: 17 0.00318289 0.0 -0.135528 -0.139791
#: 18 0.0 -0.00320005 -0.139791 -0.135448
#: 19 -0.00320005 -0.00640035 -0.135448 -0.131104
#: 20 -0.00640035 -0.00954151 -0.131104 -0.127177
#: 21 -0.00954151 -0.0126824 -0.127177 -0.123251
#: 22 -0.0126824 -0.0158222 -0.123251 -0.119731
#: 23 -0.0158222 -0.0189619 -0.119731 -0.116212
#: 24 -0.0189619 -0.0220408 -0.116212 -0.112979
#: 25 -0.0220408 -0.02512 -0.112979 -0.109746
#: 26 -0.02512 -0.0376801 -0.109746 -0.108994
#: 27 -0.0376801 -0.05024 -0.108994 -0.108243
#: 28 -0.05024 -0.05024 -0.108243 -0.0946321
#: 29 -0.05024 -0.05024 -0.0946321 -0.0810213
#: 30 -0.05024 -0.05024 -0.0810213 -0.0674677
#: 31 -0.05024 -0.05024 -0.0674677 -0.0539131
#: 32 -0.05024 -0.05024 -0.0539131 -0.040411
#: 33 -0.05024 -0.05024 -0.040411 -0.0269089
#: 34 -0.05024 -0.05024 -0.0269089 -0.0134544
#: 35 -0.05024 -0.05024 -0.0134544 0.0
#: 0 0.05024 0.05024 0.0 -0.0271349
#: 1 0.05024 0.05024 -0.0271349 -0.0543413
#: 2 0.05024 0.05024 -0.0543413 -0.0816259
#: 3 0.05024 0.05024 -0.0816259 -0.108994
#: 4 0.05024 0.02512 -0.108994 -0.110122
#: 5 0.02512 0.0189652 -0.110122 -0.116057
#: 6 0.0189652 0.0126922 -0.116057 -0.123144
#: 7 0.0126922 0.00635099 -0.123144 -0.13133
#: 8 0.00635099 0.0 -0.13133 -0.139791
#: 9 0.0 -0.00638294 -0.139791 -0.131186
#: 10 -0.00638294 -0.012661 -0.131186 -0.123351
#: 11 -0.012661 -0.0189347 -0.123351 -0.116338
#: 12 -0.0189347 -0.02512 -0.116338 -0.110122
#: 13 -0.02512 -0.05024 -0.110122 -0.108994
#: 14 -0.05024 -0.05024 -0.108994 -0.0816259
#: 15 -0.05024 -0.05024 -0.0816259 -0.0543413
#: 16 -0.05024 -0.05024 -0.0543413 -0.0271349
#: 17 -0.05024 -0.05024 -0.0271349 0.0
#: 0 0.05024 0.05024 0.0 -0.0136805
#: 1 0.05024 0.05024 -0.0136805 -0.0273609
#: 2 0.05024 0.05024 -0.0273609 -0.0410652
#: 3 0.05024 0.05024 -0.0410652 -0.0547695
#: 4 0.05024 0.05024 -0.0547695 -0.0684996
#: 5 0.05024 0.05024 -0.0684996 -0.0822296
#: 6 0.05024 0.05024 -0.0822296 -0.0959883
#: 7 0.05024 0.05024 -0.0959883 -0.109747
#: 8 0.05024 0.0376801 -0.109747 -0.110123
#: 9 0.0376801 0.02512 -0.110123 -0.110498
#: 10 0.02512 0.0220323 -0.110498 -0.113324
#: 11 0.0220323 0.0189443 -0.113324 -0.11615
#: 12 0.0189443 0.0158057 -0.11615 -0.1197
#: 13 0.0158057 0.0126674 -0.1197 -0.123251
#: 14 0.0126674 0.0095017 -0.123251 -0.127322
#: 15 0.0095017 0.00633597 -0.127322 -0.131394
#: 16 0.00633597 0.00316811 -0.131394 -0.135592
#: 17 0.00316811 0.0 -0.135592 -0.139791
#: 18 0.0 -0.00318289 -0.139791 -0.13553
#: 19 -0.00318289 -0.00636554 -0.13553 -0.131269
#: 20 -0.00636554 -0.00950241 -0.131269 -0.12736
#: 21 -0.00950241 -0.0126393 -0.12736 -0.123451
#: 22 -0.0126393 -0.0157733 -0.123451 -0.119957
#: 23 -0.0157733 -0.0189073 -0.119957 -0.116463
#: 24 -0.0189073 -0.0220137 -0.116463 -0.113481
#: 25 -0.0220137 -0.02512 -0.113481 -0.110497
#: 26 -0.02512 -0.0376801 -0.110497 -0.110122
#: 27 -0.0376801 -0.05024 -0.110122 -0.109747
#: 28 -0.05024 -0.05024 -0.109747 -0.0959883
#: 29 -0.05024 -0.05024 -0.0959883 -0.0822296
#: 30 -0.05024 -0.05024 -0.0822296 -0.0684996
#: 31 -0.05024 -0.05024 -0.0684996 -0.0547695
#: 32 -0.05024 -0.05024 -0.0547695 -0.0410652
#: 33 -0.05024 -0.05024 -0.0410652 -0.0273609
#: 34 -0.05024 -0.05024 -0.0273609 -0.0136805
#: 35 -0.05024 -0.05024 -0.0136805 0.0
#: 0 0.05024 0.05024 0.0 -0.0275869
#: 1 0.05024 0.05024 -0.0275869 -0.0551977
#: 2 0.05024 0.05024 -0.0551977 -0.0828333
#: 3 0.05024 0.05024 -0.0828333 -0.110498
#: 4 0.05024 0.02512 -0.110498 -0.110874
#: 5 0.02512 0.0189269 -0.110874 -0.116242
#: 6 0.0189269 0.01265 -0.116242 -0.123374
#: 7 0.01265 0.00632381 -0.123374 -0.131481
#: 8 0.00632381 0.0 -0.131481 -0.139791
#: 9 0.0 -0.00639677 -0.139791 -0.131146
#: 10 -0.00639677 -0.0126743 -0.131146 -0.123343
#: 11 -0.0126743 -0.0189085 -0.123343 -0.11649
#: 12 -0.0189085 -0.02512 -0.11649 -0.110873
#: 13 -0.02512 -0.05024 -0.110873 -0.110498
#: 14 -0.05024 -0.05024 -0.110498 -0.0828333
#: 15 -0.05024 -0.05024 -0.0828333 -0.0551977
#: 16 -0.05024 -0.05024 -0.0551977 -0.0275869
#: 17 -0.05024 -0.05024 -0.0275869 0.0
#: 0 0.05024 0.05024 0.0 -0.0139065
#: 1 0.05024 0.05024 -0.0139065 -0.027813
#: 2 0.05024 0.05024 -0.027813 -0.0417185
#: 3 0.05024 0.05024 -0.0417185 -0.055625
#: 4 0.05024 0.05024 -0.055625 -0.0695314
#: 5 0.05024 0.05024 -0.0695314 -0.0834379
#: 6 0.05024 0.05024 -0.0834379 -0.0973444
#: 7 0.05024 0.05024 -0.0973444 -0.11125
#: 8 0.05024 0.0376801 -0.11125 -0.11125
#: 9 0.0376801 0.02512 -0.11125 -0.11125
#: 10 0.02512 0.0220146 -0.11125 -0.113793
#: 11 0.0220146 0.0189095 -0.113793 -0.116336
#: 12 0.0189095 0.0157709 -0.116336 -0.119916
#: 13 0.0157709 0.0126324 -0.119916 -0.123496
#: 14 0.0126324 0.00947189 -0.123496 -0.127532
#: 15 0.00947189 0.00631142 -0.127532 -0.131568
#: 16 0.00631142 0.00315571 -0.131568 -0.13568
#: 17 0.00315571 0.0 -0.13568 -0.139791
#: 18 0.0 -0.00321388 -0.139791 -0.135407
#: 19 -0.00321388 -0.00642776 -0.135407 -0.131024
#: 20 -0.00642776 -0.00956845 -0.131024 -0.12713
#: 21 -0.00956845 -0.0127091 -0.12713 -0.123236
#: 22 -0.0127091 -0.0158095 -0.123236 -0.119876
#: 23 -0.0158095 -0.0189099 -0.119876 -0.116517
#: 24 -0.0189099 -0.0220151 -0.116517 -0.113883
#: 25 -0.0220151 -0.02512 -0.113883 -0.11125
#: 26 -0.02512 -0.0376801 -0.11125 -0.11125
#: 27 -0.0376801 -0.05024 -0.11125 -0.11125
#: 28 -0.05024 -0.05024 -0.11125 -0.0973444
#: 29 -0.05024 -0.05024 -0.0973444 -0.0834379
#: 30 -0.05024 -0.05024 -0.0834379 -0.0695314
#: 31 -0.05024 -0.05024 -0.0695314 -0.055625
#: 32 -0.05024 -0.05024 -0.055625 -0.0417185
#: 33 -0.05024 -0.05024 -0.0417185 -0.027813
#: 34 -0.05024 -0.05024 -0.027813 -0.0139065
#: 35 -0.05024 -0.05024 -0.0139065 0.0
#: slice #: 28
#: 0 0.05024 0.05024 0.0 -0.0136805
#: 1 0.05024 0.05024 -0.0136805 -0.0273609
#: 2 0.05024 0.05024 -0.0273609 -0.0410652
#: 3 0.05024 0.05024 -0.0410652 -0.0547695
#: 4 0.05024 0.05024 -0.0547695 -0.0684996
#: 5 0.05024 0.05024 -0.0684996 -0.0822296
#: 6 0.05024 0.05024 -0.0822296 -0.0959883
#: 7 0.05024 0.05024 -0.0959883 -0.109747
#: 8 0.05024 0.0376801 -0.109747 -0.110123
#: 9 0.0376801 0.02512 -0.110123 -0.110498
#: 10 0.02512 0.0220323 -0.110498 -0.113324
#: 11 0.0220323 0.0189443 -0.113324 -0.11615
#: 12 0.0189443 0.0158057 -0.11615 -0.1197
#: 13 0.0158057 0.0126674 -0.1197 -0.123251
#: 14 0.0126674 0.0095017 -0.123251 -0.127322
#: 15 0.0095017 0.00633597 -0.127322 -0.131394
#: 16 0.00633597 0.00316811 -0.131394 -0.135592
#: 17 0.00316811 0.0 -0.135592 -0.139791
#: 18 0.0 -0.00318289 -0.139791 -0.13553
#: 19 -0.00318289 -0.00636554 -0.13553 -0.131269
#: 20 -0.00636554 -0.00950241 -0.131269 -0.12736
#: 21 -0.00950241 -0.0126393 -0.12736 -0.123451
#: 22 -0.0126393 -0.0157733 -0.123451 -0.119957
#: 23 -0.0157733 -0.0189073 -0.119957 -0.116463
#: 24 -0.0189073 -0.0220137 -0.116463 -0.113481
#: 25 -0.0220137 -0.02512 -0.113481 -0.110497
#: 26 -0.02512 -0.0376801 -0.110497 -0.110122
#: 27 -0.0376801 -0.05024 -0.110122 -0.109747
#: 28 -0.05024 -0.05024 -0.109747 -0.0959883
#: 29 -0.05024 -0.05024 -0.0959883 -0.0822296
#: 30 -0.05024 -0.05024 -0.0822296 -0.0684996
#: 31 -0.05024 -0.05024 -0.0684996 -0.0547695
#: 32 -0.05024 -0.05024 -0.0547695 -0.0410652
#: 33 -0.05024 -0.05024 -0.0410652 -0.0273609
#: 34 -0.05024 -0.05024 -0.0273609 -0.0136805
#: 35 -0.05024 -0.05024 -0.0136805 0.0
#: 0 0.05024 0.05024 0.0 -0.0275869
#: 1 0.05024 0.05024 -0.0275869 -0.0551977
#: 2 0.05024 0.05024 -0.0551977 -0.0828333
#: 3 0.05024 0.05024 -0.0828333 -0.110498
#: 4 0.05024 0.02512 -0.110498 -0.110874
#: 5 0.02512 0.0189269 -0.110874 -0.116242
#: 6 0.0189269 0.01265 -0.116242 -0.123374
#: 7 0.01265 0.00632381 -0.123374 -0.131481
#: 8 0.00632381 0.0 -0.131481 -0.139791
#: 9 0.0 -0.00639677 -0.139791 -0.131146
#: 10 -0.00639677 -0.0126743 -0.131146 -0.123343
#: 11 -0.0126743 -0.0189085 -0.123343 -0.11649
#: 12 -0.0189085 -0.02512 -0.11649 -0.110873
#: 13 -0.02512 -0.05024 -0.110873 -0.110498
#: 14 -0.05024 -0.05024 -0.110498 -0.0828333
#: 15 -0.05024 -0.05024 -0.0828333 -0.0551977
#: 16 -0.05024 -0.05024 -0.0551977 -0.0275869
#: 17 -0.05024 -0.05024 -0.0275869 0.0
#: 0 0.05024 0.05024 0.0 -0.0139065
#: 1 0.05024 0.05024 -0.0139065 -0.027813
#: 2 0.05024 0.05024 -0.027813 -0.0417185
#: 3 0.05024 0.05024 -0.0417185 -0.055625
#: 4 0.05024 0.05024 -0.055625 -0.0695314
#: 5 0.05024 0.05024 -0.0695314 -0.0834379
#: 6 0.05024 0.05024 -0.0834379 -0.0973444
#: 7 0.05024 0.05024 -0.0973444 -0.11125
#: 8 0.05024 0.0376801 -0.11125 -0.11125
#: 9 0.0376801 0.02512 -0.11125 -0.11125
#: 10 0.02512 0.0220146 -0.11125 -0.113793
#: 11 0.0220146 0.0189095 -0.113793 -0.116336
#: 12 0.0189095 0.0157709 -0.116336 -0.119916
#: 13 0.0157709 0.0126324 -0.119916 -0.123496
#: 14 0.0126324 0.00947189 -0.123496 -0.127532
#: 15 0.00947189 0.00631142 -0.127532 -0.131568
#: 16 0.00631142 0.00315571 -0.131568 -0.13568
#: 17 0.00315571 0.0 -0.13568 -0.139791
#: 18 0.0 -0.00321388 -0.139791 -0.135407
#: 19 -0.00321388 -0.00642776 -0.135407 -0.131024
#: 20 -0.00642776 -0.00956845 -0.131024 -0.12713
#: 21 -0.00956845 -0.0127091 -0.12713 -0.123236
#: 22 -0.0127091 -0.0158095 -0.123236 -0.119876
#: 23 -0.0158095 -0.0189099 -0.119876 -0.116517
#: 24 -0.0189099 -0.0220151 -0.116517 -0.113883
#: 25 -0.0220151 -0.02512 -0.113883 -0.11125
#: 26 -0.02512 -0.0376801 -0.11125 -0.11125
#: 27 -0.0376801 -0.05024 -0.11125 -0.11125
#: 28 -0.05024 -0.05024 -0.11125 -0.0973444
#: 29 -0.05024 -0.05024 -0.0973444 -0.0834379
#: 30 -0.05024 -0.05024 -0.0834379 -0.0695314
#: 31 -0.05024 -0.05024 -0.0695314 -0.055625
#: 32 -0.05024 -0.05024 -0.055625 -0.0417185
#: 33 -0.05024 -0.05024 -0.0417185 -0.027813
#: 34 -0.05024 -0.05024 -0.027813 -0.0139065
#: 35 -0.05024 -0.05024 -0.0139065 0.0
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.1411, 
    farPlane=64.4937, width=0.93251, height=0.234016, viewOffsetX=3.10881, 
    viewOffsetY=-2.83248)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.8784, 
    farPlane=61.8035, width=0.94964, height=0.238315, cameraPosition=(26.9875, 
    28.9319, 45.5851), cameraUpVector=(-0.533583, 0.657912, -0.531451), 
    cameraTarget=(8.66498, 5.71749, 2.42852), viewOffsetX=3.16592, 
    viewOffsetY=-2.88451)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.3536, 
    farPlane=62.3284, width=7.907, height=1.98429, viewOffsetX=4.86271, 
    viewOffsetY=-2.52298)
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.273, 
    farPlane=62.4091, width=7.8912, height=1.98032, cameraPosition=(27.022, 
    29.6405, 45.1893), cameraUpVector=(-0.440171, 0.681996, -0.584065), 
    cameraTarget=(8.69946, 6.42604, 2.03274), viewOffsetX=4.85299, 
    viewOffsetY=-2.51793)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.3851, 
    farPlane=69.9692, width=8.69693, height=2.18252, cameraPosition=(55.8474, 
    -24.7375, 14.1047), cameraUpVector=(0.324326, 0.58558, -0.742906), 
    cameraTarget=(19.226, 10.8371, 2.68375), viewOffsetX=5.34851, 
    viewOffsetY=-2.77502)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43.3115, 
    farPlane=71.0428, width=21.4691, height=5.38774, viewOffsetX=3.74086, 
    viewOffsetY=-1.87245)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43.2082, 
    farPlane=71.1461, width=21.4179, height=5.37489, viewOffsetX=9.08259, 
    viewOffsetY=-6.65764)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.9445, 
    farPlane=69.4099, width=1.37607, height=0.345329, viewOffsetX=8.77207, 
    viewOffsetY=-4.85982)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: Processing Contour:  10
#: slice #: 0
#: 0 0.05024 0.05024 0.0 -0.00758076
#: 1 0.05024 0.05024 -0.00758076 -0.0151625
#: 2 0.05024 0.05024 -0.0151625 -0.0234118
#: 3 0.05024 0.05024 -0.0234118 -0.031662
#: 4 0.05024 0.05024 -0.031662 -0.0406389
#: 5 0.05024 0.05024 -0.0406389 -0.0496159
#: 6 0.05024 0.05024 -0.0496159 -0.0593843
#: 7 0.05024 0.05024 -0.0593843 -0.0691538
#: 8 0.05024 0.0376801 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 10 0.02512 0.0220258 -0.0691538 -0.0747337
#: 11 0.0220258 0.0189316 -0.0747337 -0.0803137
#: 12 0.0189316 0.0157847 -0.0803137 -0.0842819
#: 13 0.0157847 0.0126379 -0.0842819 -0.0882502
#: 14 0.0126379 0.00950575 -0.0882502 -0.0909357
#: 15 0.00950575 0.00637341 -0.0909357 -0.0936213
#: 16 0.00637341 0.0031867 -0.0936213 -0.0943747
#: 17 0.0031867 0.0 -0.0943747 -0.0951271
#: 18 0.0 -0.00315881 -0.0951271 -0.0939579
#: 19 -0.00315881 -0.00631762 -0.0939579 -0.0927887
#: 20 -0.00631762 -0.00948238 -0.0927887 -0.0904884
#: 21 -0.00948238 -0.0126469 -0.0904884 -0.0881882
#: 22 -0.0126469 -0.0157919 -0.0881882 -0.0842257
#: 23 -0.0157919 -0.0189366 -0.0842257 -0.0802622
#: 24 -0.0189366 -0.0220284 -0.0802622 -0.074708
#: 25 -0.0220284 -0.02512 -0.074708 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 27 -0.0376801 -0.05024 -0.0691538 -0.0691538
#: 28 -0.05024 -0.05024 -0.0691538 -0.0593843
#: 29 -0.05024 -0.05024 -0.0593843 -0.0496159
#: 30 -0.05024 -0.05024 -0.0496159 -0.0406389
#: 31 -0.05024 -0.05024 -0.0406389 -0.031662
#: 32 -0.05024 -0.05024 -0.031662 -0.0234118
#: 33 -0.05024 -0.05024 -0.0234118 -0.0151625
#: 34 -0.05024 -0.05024 -0.0151625 -0.00758076
#: 35 -0.05024 -0.05024 -0.00758076 0.0
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: found a nan
#: 0 0.05024 0.05024 0.0 -0.0153885
#: 1 0.05024 0.05024 -0.0153885 -0.0320902
#: 2 0.05024 0.05024 -0.0320902 -0.0502195
#: 3 0.05024 0.05024 -0.0502195 -0.0699053
#: 4 0.05024 0.02512 -0.0699053 -0.0704823
#: 5 0.02512 0.0189192 -0.0704823 -0.081809
#: 6 0.0189192 0.0126266 -0.081809 -0.0897284
#: 7 0.0126266 0.0063591 -0.0897284 -0.0951395
#: 8 0.0063591 0.0 -0.0951395 -0.0970201
#: 9 0.0 -0.00632811 -0.0970201 -0.0945578
#: 10 -0.00632811 -0.0126605 -0.0945578 -0.0899363
#: 11 -0.0126605 -0.0189462 -0.0899363 -0.0820303
#: 12 -0.0189462 -0.02512 -0.0820303 -0.0704823
#: 13 -0.02512 -0.05024 -0.0704823 -0.0699053
#: 14 -0.05024 -0.05024 -0.0699053 -0.0502195
#: 15 -0.05024 -0.05024 -0.0502195 -0.0320902
#: 16 -0.05024 -0.05024 -0.0320902 -0.0153885
#: 17 -0.05024 -0.05024 -0.0153885 0.0
#: 0 0.05024 0.05024 0.0 -0.00780773
#: 1 0.05024 0.05024 -0.00780773 -0.0156145
#: 2 0.05024 0.05024 -0.0156145 -0.024066
#: 3 0.05024 0.05024 -0.024066 -0.0325174
#: 4 0.05024 0.05024 -0.0325174 -0.0416708
#: 5 0.05024 0.05024 -0.0416708 -0.0508242
#: 6 0.05024 0.05024 -0.0508242 -0.0607405
#: 7 0.05024 0.05024 -0.0607405 -0.0706577
#: 8 0.05024 0.0376801 -0.0706577 -0.0712347
#: 9 0.0376801 0.02512 -0.0712347 -0.0718107
#: 10 0.02512 0.0220134 -0.0718107 -0.0775576
#: 11 0.0220134 0.0189068 -0.0775576 -0.0833035
#: 12 0.0189068 0.0157609 -0.0833035 -0.0872545
#: 13 0.0157609 0.0126152 -0.0872545 -0.0912066
#: 14 0.0126152 0.00948 -0.0912066 -0.0939322
#: 15 0.00948 0.00634503 -0.0939322 -0.0966578
#: 16 0.00634503 0.0031724 -0.0966578 -0.097785
#: 17 0.0031724 0.0 -0.097785 -0.0989122
#: 18 0.0 -0.00316954 -0.0989122 -0.0976191
#: 19 -0.00316954 -0.00633883 -0.0976191 -0.0963259
#: 20 -0.00633883 -0.00950623 -0.0963259 -0.0940046
#: 21 -0.00950623 -0.0126739 -0.0940046 -0.0916834
#: 22 -0.0126739 -0.0158148 -0.0916834 -0.0877409
#: 23 -0.0158148 -0.0189557 -0.0877409 -0.0837984
#: 24 -0.0189557 -0.022038 -0.0837984 -0.0778046
#: 25 -0.022038 -0.02512 -0.0778046 -0.0718107
#: 26 -0.02512 -0.0376801 -0.0718107 -0.0712347
#: 27 -0.0376801 -0.05024 -0.0712347 -0.0706577
#: 28 -0.05024 -0.05024 -0.0706577 -0.0607405
#: 29 -0.05024 -0.05024 -0.0607405 -0.0508242
#: 30 -0.05024 -0.05024 -0.0508242 -0.0416708
#: 31 -0.05024 -0.05024 -0.0416708 -0.0325174
#: 32 -0.05024 -0.05024 -0.0325174 -0.024066
#: 33 -0.05024 -0.05024 -0.024066 -0.0156145
#: 34 -0.05024 -0.05024 -0.0156145 -0.00780773
#: 35 -0.05024 -0.05024 -0.00780773 0.0
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: Processing Contour:  10
#: slice #: 0
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 27 -0.0376801 -0.05024 -0.0691538 -0.0691538
#: 27 -0.0376801 -0.05024 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 27 -0.0376801 -0.05024 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 27 -0.0376801 -0.05024 -0.0691538 -0.0691538
#: 27 -0.0376801 -0.05024 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 8 0.05024 0.0376801 -0.0691538 -0.0691538
#: 8 0.05024 0.0376801 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 8 0.05024 0.0376801 -0.0691538 -0.0691538
#: 8 0.05024 0.0376801 -0.0691538 -0.0691538
#: 8 0.05024 0.0376801 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 8 0.05024 0.0376801 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 8 0.05024 0.0376801 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 9 0.0376801 0.02512 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
#: 26 -0.02512 -0.0376801 -0.0691538 -0.0691538
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#* Command successfully aborted.
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1087, in CalculateDomainJIntegral
#*     
#* dqdX,intLcL,slicePos[sliceCnt],dudXElLabels=GetdqdX(root,frame,allNodes,
#* nSetQ0,nSetQ0p5,nSetQ1,nodeLabelTip,nSetSlice,elSetSlice,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 841, 
#* in GetdqdX
#*     
#* ENQ2,intLcL,posz=GetqLinear(nSetQ0,nodeSetName,firstCrackNodeLabel,root,
#* allNodes,elSetName,isSymm)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 604, 
#* in GetqLinear
#*     mb.append((yb[i]-yb[i+1])/(xb[i]-xb[i+1]))
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#* UnboundLocalError: local variable 'slicePos' referenced before assignment
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1061, in CalculateDomainJIntegral
#*     fobj.write(',%f' % (slicePos[i]))
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#* SyntaxError: ('invalid syntax', 
#* ('E:\\Dropbox\\Research\\Source\\Abaqus-J-integral\\code\\JCore.py', 1062, 
#* 28, '\t\tfor contourId in contours:\t\n'))
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 21, in <module>
#*     from JCore import *
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: No modules to remove
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: Processing Contour:  0
#: slice #: 0
#: slice #: 1
#: slice #: 2
#* IndexError: index out of bounds
#* File "E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py", 
#* line 107, in <module>
#*     
#* CalculateDomainJIntegral(stepNumber,frameNumbers,contours,slices,SetPrefix,
#* nodeLabelTip,isSymm,odb,partInstance)
#* File "E:\Dropbox\Research\Source\Abaqus-J-integral\code\JCore.py", line 
#* 1122, in CalculateDomainJIntegral
#*     JAll[sliceCnt]=2*Jbar/intLcL
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
#: Processing Contour:  0
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
#: Processing Contour:  1
#: slice #: 0
#: slice #: 1
#: slice #: 2
#: slice #: 3
#: slice #: 4
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter_homo.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
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
#: slice #: 20
#: slice #: 21
#: slice #: 22
#: slice #: 23
#: slice #: 24
#: slice #: 25
#: slice #: 26
#: slice #: 27
#: slice #: 28
