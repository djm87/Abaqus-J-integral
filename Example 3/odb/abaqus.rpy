# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2019 replay file
# Internal Version: 2018_09_24-14.41.51 157541
# Run by dansa on Wed Sep 18 23:38:10 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=156.25, 
    height=194.240753173828)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='J-Indenter_Quarter.odb')
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 3/odb/J-Indenter_Quarter.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     2
#: Number of Meshes:             2
#: Number of Element Sets:       135
#: Number of Node Sets:          1280
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=38.4548, 
    farPlane=66.2078, width=21.8226, height=8.6305, viewOffsetX=0.839671, 
    viewOffsetY=0.444494)
session.viewports['Viewport: 1'].view.setValues(nearPlane=38.351, 
    farPlane=66.3116, width=21.7637, height=8.60722, viewOffsetX=1.83161, 
    viewOffsetY=-2.07627)
