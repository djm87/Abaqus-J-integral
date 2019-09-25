# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2019 replay file
# Internal Version: 2018_09_24-14.41.51 157541
# Run by dansa on Wed Sep 25 10:25:27 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=156.25, 
    height=239.25927734375)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='J-Indenter-All-structured.odb')
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter-All-structured.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       137
#: Number of Node Sets:          1278
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.3097, 
    farPlane=65.3251, width=3.13182, height=4.62546, viewOffsetX=1.79651, 
    viewOffsetY=-2.43903)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    DEFORMED, ))
#: 
#: Node: SPECIMEN-1.1780
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.24600e+01,  2.13520e+00,  2.78150e+00,      -      
#: Scale:                             1.00000e+00,  1.00000e+00,  1.00000e+00,      -      
#: Deformed coordinates (unscaled):   1.24600e+01,  2.13520e+00,  2.78150e+00,      -      
#: Deformed coordinates (scaled):     1.24600e+01,  2.13520e+00,  2.78150e+00,      -      
#: Displacement (unscaled):           0.00000e+00,  0.00000e+00,  0.00000e+00,  0.00000e+00
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.2189, 
    farPlane=64.4165, width=0.0309255, height=0.0456746, viewOffsetX=1.70868, 
    viewOffsetY=-3.79587)
import os
os.chdir(r"E:\Dropbox\Research\Source\Abaqus-J-integral\Example 3")
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: No modules to remove
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter-All-structured_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       137
#: Number of Node Sets:          1278
#: Number of Steps:              1
#: Starting to build element and node sets...
#: =================================================================
#: time report
#: ++++++++++++
#: time building sets 127.654000044
#: time in J integral Surface 0.0
#: time in J integral Volume 0.0
#: time in J to KI 0.0
session.viewports['Viewport: 1'].view.setValues(nearPlane=40.1443, 
    farPlane=64.4911, width=0.320544, height=0.456793, viewOffsetX=1.70226, 
    viewOffsetY=-3.70835)
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter-All-structured_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.686, 
    farPlane=64.9488, width=1.83402, height=2.61359, viewOffsetX=1.45738, 
    viewOffsetY=-2.76316)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter-All-structured_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       137
#: Number of Node Sets:          1278
#: Number of Steps:              1
#: Starting to build element and node sets...
#: =================================================================
#: time report
#: ++++++++++++
#: time building sets 196.92599988
#: time in J integral Surface 0.0
#: time in J integral Volume 0.0
#: time in J to KI 0.0
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter-All-structured_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.182, 
    farPlane=65.4528, width=3.99827, height=5.69776, viewOffsetX=1.45248, 
    viewOffsetY=-3.29055)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.4305, 
    farPlane=61.825, width=4.53385, height=6.461, cameraPosition=(21.0552, 
    12.1806, 54.2257), cameraUpVector=(-0.390852, 0.852676, -0.346667), 
    cameraTarget=(9.19258, 6.60332, 3.5771), viewOffsetX=1.64705, 
    viewOffsetY=-3.73133)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43.5028, 
    farPlane=62.7527, width=7.77904, height=11.0856, viewOffsetX=1.54751, 
    viewOffsetY=-3.26605)
session.viewports['Viewport: 1'].view.setValues(nearPlane=41.8862, 
    farPlane=62.2482, width=7.48997, height=10.6736, cameraPosition=(-6.73733, 
    2.73403, 52.3015), cameraUpVector=(-0.0354214, 0.959063, -0.28097), 
    cameraTarget=(9.45867, 6.99511, 2.73702), viewOffsetX=1.49, 
    viewOffsetY=-3.14468)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43.1899, 
    farPlane=64.247, width=7.72309, height=11.0058, cameraPosition=(30.8231, 
    8.9058, 51.7193), cameraUpVector=(-0.317336, 0.911337, -0.262228), 
    cameraTarget=(9.1988, 6.81721, 4.1259), viewOffsetX=1.53637, 
    viewOffsetY=-3.24255)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.5233, 
    farPlane=62.7554, width=7.96152, height=11.3456, cameraPosition=(16.1816, 
    0.581684, 55.4867), cameraUpVector=(-0.162452, 0.966022, -0.201022), 
    cameraTarget=(8.9097, 6.70565, 4.04037), viewOffsetX=1.5838, 
    viewOffsetY=-3.34266)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43.6609, 
    farPlane=63.6179, width=10.1288, height=14.4342, viewOffsetX=1.56657, 
    viewOffsetY=-2.75016)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(session.views['Left'])
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=34.6257, 
    farPlane=64.3949, width=9.02196, height=12.8568, cameraPosition=(49.092, 
    26.3717, 24.1129), cameraUpVector=(-0.240288, 0.90291, -0.356391))
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=39.9921, 
    farPlane=59.0285, width=2.67109, height=3.80646, viewOffsetX=0.84841, 
    viewOffsetY=-2.24554)
session.viewports['Viewport: 1'].view.setValues(nearPlane=36.6217, 
    farPlane=60.4028, width=2.44598, height=3.48567, cameraPosition=(54.3521, 
    22.1156, 9.85306), cameraUpVector=(-0.28587, 0.950517, -0.121641), 
    cameraTarget=(7.74685, 7.14815, 2.42356), viewOffsetX=0.77691, 
    viewOffsetY=-2.05629)
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter-All-structured_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       137
#: Number of Node Sets:          1278
#: Number of Steps:              1
#: Starting to build element and node sets...
#: =================================================================
#: Building Slice Element sets
#: Time= 66.6130001545
#: Building Q node sets
#: Time= 1056.25199986
#: Building interface sets
#: Time= 1935.77099991
#: time report
#: ++++++++++++
#: time building sets 3182.171
#: time in J integral Surface 0.0
#: time in J integral Volume 0.0
#: time in J to KI 0.0
