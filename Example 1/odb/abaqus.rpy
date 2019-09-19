# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2019 replay file
# Internal Version: 2018_09_24-14.41.51 157541
# Run by dansa on Thu Sep 19 08:11:38 2019
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.3936, 
    farPlane=19.7595, width=2.36631, height=0.935838, viewOffsetX=0.891292, 
    viewOffsetY=-1.97368)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.4063, 
    farPlane=19.7468, width=2.36873, height=0.936797, viewOffsetX=0.980123, 
    viewOffsetY=-2.29592)
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.1395, 
    farPlane=21.0136, width=16.0277, height=6.33869, viewOffsetX=0.520002, 
    viewOffsetY=-0.926524)
import os
os.chdir(r"E:\Dropbox\Research\Source\Abaqus-J-integral\Example 1")
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
#: Starting to build element and node sets...
#: =================================================================
#: Starting calculations for the Material force at the interface...
#: =================================================================
#: Processing slice #: 0
#: ___Contour:  14
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 2
#: ___Contour:  14
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 4
#: ___Contour:  14
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 6
#: ___Contour:  14
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 8
#: ___Contour:  14
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 10
#: ___Contour:  14
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 12
#: ___Contour:  14
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 14
#: ___Contour:  14
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 16
#: ___Contour:  14
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 18
#: ___Contour:  14
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Starting calculations for the J Integral...
#: ===========================================
#: Processing slice #: 0
#: ___Contour:  14
#: J far = 0.829812943159
#: J tip = 0.829812943159
#: ___Contour:  12
#: J far = 0.722527658552
#: J tip = 0.722527658552
#: ___Contour:  10
#: J far = 0.722334805651
#: J tip = 0.722334805651
#: ___Contour:  8
#: J far = 0.722652648139
#: J tip = 0.722652648139
#: ___Contour:  6
#: J far = 0.722656531105
#: J tip = 0.722656531105
#: ___Contour:  4
#: J far = 0.722655773714
#: J tip = 0.722655773714
#: ___Contour:  2
#: J far = 0.72259369237
#: J tip = 0.72259369237
#: ___Contour:  0
#: J far = 0.694327437049
#: J tip = 0.694327437049
#: Processing slice #: 2
#: ___Contour:  14
#: J far = 0.868648769226
#: J tip = 0.868648769226
#: ___Contour:  12
#: J far = 0.724243863368
#: J tip = 0.724243863368
#: ___Contour:  10
#: J far = 0.724039326359
#: J tip = 0.724039326359
#: ___Contour:  8
#: J far = 0.724382210141
#: J tip = 0.724382210141
#: ___Contour:  6
#: J far = 0.724384838032
#: J tip = 0.724384838032
#: ___Contour:  4
#: J far = 0.724384330108
#: J tip = 0.724384330108
#: ___Contour:  2
#: J far = 0.724322864768
#: J tip = 0.724322864768
#: ___Contour:  0
#: J far = 0.695775588607
#: J tip = 0.695775588607
#: Processing slice #: 4
#: ___Contour:  14
#: J far = 0.913656287101
#: J tip = 0.913656287101
#: ___Contour:  12
#: J far = 0.725278695108
#: J tip = 0.725278695108
#: ___Contour:  10
#: J far = 0.725068712338
#: J tip = 0.725068712338
#: ___Contour:  8
#: J far = 0.725435634921
#: J tip = 0.725435634921
#: ___Contour:  6
#: J far = 0.725438109561
#: J tip = 0.725438109561
#: ___Contour:  4
#: J far = 0.725435914297
#: J tip = 0.725435914297
#: ___Contour:  2
#: J far = 0.725368531191
#: J tip = 0.725368531191
#: ___Contour:  0
#: J far = 0.696755820242
#: J tip = 0.696755820242
#: Processing slice #: 6
#: ___Contour:  14
#: J far = 0.959155443164
#: J tip = 0.959155443164
#: ___Contour:  12
#: J far = 0.727300076408
#: J tip = 0.727300076408
#: ___Contour:  10
#: J far = 0.727085283251
#: J tip = 0.727085283251
#: ___Contour:  8
#: J far = 0.727480040189
#: J tip = 0.727480040189
#: ___Contour:  6
#: J far = 0.727482321162
#: J tip = 0.727482321162
#: ___Contour:  4
#: J far = 0.727479673852
#: J tip = 0.727479673852
#: ___Contour:  2
#: J far = 0.727421177788
#: J tip = 0.727421177788
#: ___Contour:  0
#: J far = 0.698707991248
#: J tip = 0.698707991248
#: Processing slice #: 8
#: ___Contour:  14
#: J far = 0.997583345475
#: J tip = 0.997583345475
#: ___Contour:  12
#: J far = 0.730802904097
#: J tip = 0.730802904097
#: ___Contour:  10
#: J far = 0.73058079242
#: J tip = 0.73058079242
#: ___Contour:  8
#: J far = 0.731008048869
#: J tip = 0.731008048869
#: ___Contour:  6
#: J far = 0.731010179345
#: J tip = 0.731010179345
#: ___Contour:  4
#: J far = 0.731007625025
#: J tip = 0.731007625025
#: ___Contour:  2
#: J far = 0.730951774478
#: J tip = 0.730951774478
#: ___Contour:  0
#: J far = 0.702086001493
#: J tip = 0.702086001493
#: Processing slice #: 10
#: ___Contour:  14
#: J far = 1.01714382725
#: J tip = 1.01714382725
#: ___Contour:  12
#: J far = 0.736539273761
#: J tip = 0.736539273761
#: ___Contour:  10
#: J far = 0.736323658157
#: J tip = 0.736323658157
#: ___Contour:  8
#: J far = 0.736755619464
#: J tip = 0.736755619464
#: ___Contour:  6
#: J far = 0.736757863021
#: J tip = 0.736757863021
#: ___Contour:  4
#: J far = 0.736754944284
#: J tip = 0.736754944284
#: ___Contour:  2
#: J far = 0.736704869811
#: J tip = 0.736704869811
#: ___Contour:  0
#: J far = 0.707594504098
#: J tip = 0.707594504098
#: Processing slice #: 12
#: ___Contour:  14
#: J far = 1.00991670094
#: J tip = 1.00991670094
#: ___Contour:  12
#: J far = 0.745916708925
#: J tip = 0.745916708925
#: ___Contour:  10
#: J far = 0.745691745669
#: J tip = 0.745691745669
#: ___Contour:  8
#: J far = 0.746130427803
#: J tip = 0.746130427803
#: ___Contour:  6
#: J far = 0.746132863321
#: J tip = 0.746132863321
#: ___Contour:  4
#: J far = 0.746128718032
#: J tip = 0.746128718032
#: ___Contour:  2
#: J far = 0.746089136234
#: J tip = 0.746089136234
#: ___Contour:  0
#: J far = 0.716587335792
#: J tip = 0.716587335792
#: Processing slice #: 14
#: ___Contour:  14
#: J far = 0.982120134588
#: J tip = 0.982120134588
#: ___Contour:  12
#: J far = 0.761470352715
#: J tip = 0.761470352715
#: ___Contour:  10
#: J far = 0.761242168548
#: J tip = 0.761242168548
#: ___Contour:  8
#: J far = 0.761665742064
#: J tip = 0.761665742064
#: ___Contour:  6
#: J far = 0.761668044076
#: J tip = 0.761668044076
#: ___Contour:  4
#: J far = 0.761662457704
#: J tip = 0.761662457704
#: ___Contour:  2
#: J far = 0.761633306017
#: J tip = 0.761633306017
#: ___Contour:  0
#: J far = 0.731497223472
#: J tip = 0.731497223472
#: Processing slice #: 16
#: ___Contour:  14
#: J far = 0.958884865211
#: J tip = 0.958884865211
#: ___Contour:  12
#: J far = 0.787351603453
#: J tip = 0.787351603453
#: ___Contour:  10
#: J far = 0.787111617908
#: J tip = 0.787111617908
#: ___Contour:  8
#: J far = 0.787537156716
#: J tip = 0.787537156716
#: ___Contour:  6
#: J far = 0.787539729922
#: J tip = 0.787539729922
#: ___Contour:  4
#: J far = 0.787532826228
#: J tip = 0.787532826228
#: ___Contour:  2
#: J far = 0.78750408151
#: J tip = 0.78750408151
#: ___Contour:  0
#: J far = 0.756349334456
#: J tip = 0.756349334456
#: Processing slice #: 18
#: ___Contour:  14
#: J far = 0.953720944395
#: J tip = 0.953720944395
#: ___Contour:  12
#: J far = 0.827054710619
#: J tip = 0.827054710619
#: ___Contour:  10
#: J far = 0.826801463192
#: J tip = 0.826801463192
#: ___Contour:  8
#: J far = 0.827228736217
#: J tip = 0.827228736217
#: ___Contour:  6
#: J far = 0.827225895768
#: J tip = 0.827225895768
#: ___Contour:  4
#: J far = 0.827220730722
#: J tip = 0.827220730722
#: ___Contour:  2
#: J far = 0.827195942211
#: J tip = 0.827195942211
#: ___Contour:  0
#: J far = 0.794524252333
#: J tip = 0.794524252333
#: Starting calculations of KI from J...
#: =================================================================
#: the stress intensity factor is being calculated assuming
#: only mode I and plane strain.
#: (10L, 8L)
#: time report
#: ++++++++++++
#: time building sets 21.6779999733
#: time in J integral Surface 0.34500002861
#: time in J integral Volume 105.118999958
#: time in J to KI 0.244000196457
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlane_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.4536, 
    farPlane=20.6995, width=12.3662, height=4.89062)
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.5285, 
    farPlane=20.6246, width=12.4471, height=4.92264)
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.5292, 
    farPlane=20.6239, width=12.4479, height=4.92294)
session.viewports['Viewport: 1'].view.setValues(viewOffsetX=0.870731, 
    viewOffsetY=-1.27997)
session.viewports['Viewport: 1'].view.setValues(nearPlane=12.1049, 
    farPlane=20.0482, width=5.49604, height=2.1736, viewOffsetX=1.12695, 
    viewOffsetY=-1.96223)
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlane_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       12
#: Number of Node Sets:          830
#: Number of Steps:              1
#: Starting to build element and node sets...
#: =================================================================
#: Starting calculations for the Material force at the interface...
#: =================================================================
#: Processing slice #: 0
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 1
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 2
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 3
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 4
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 5
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 6
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 7
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 8
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 9
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 10
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 11
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 12
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 13
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 14
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 15
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 16
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 17
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 18
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 19
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Processing slice #: 20
#: ___Contour:  12
#: ___Contour:  10
#: ___Contour:  8
#: ___Contour:  6
#: ___Contour:  4
#: ___Contour:  2
#: ___Contour:  0
#: Starting calculations for the J Integral...
#: ===========================================
#: Processing slice #: 0
#: ___Contour:  12
#: J far = 0.000722527658552
#: J tip = 0.000722527658552
#: ___Contour:  10
#: J far = 0.000722334805651
#: J tip = 0.000722334805651
#: ___Contour:  8
#: J far = 0.000722652648139
#: J tip = 0.000722652648139
#: ___Contour:  6
#: J far = 0.000722656531105
#: J tip = 0.000722656531105
#: ___Contour:  4
#: J far = 0.000722655773714
#: J tip = 0.000722655773714
#: ___Contour:  2
#: J far = 0.00072259369237
#: J tip = 0.00072259369237
#: ___Contour:  0
#: J far = 0.000694327437049
#: J tip = 0.000694327437049
#: Processing slice #: 1
#: ___Contour:  12
#: J far = 0.000723743670862
#: J tip = 0.000723743670862
#: ___Contour:  10
#: J far = 0.000723543317272
#: J tip = 0.000723543317272
#: ___Contour:  8
#: J far = 0.000723874112713
#: J tip = 0.000723874112713
#: ___Contour:  6
#: J far = 0.000723877058543
#: J tip = 0.000723877058543
#: ___Contour:  4
#: J far = 0.000723877318754
#: J tip = 0.000723877318754
#: ___Contour:  2
#: J far = 0.000723818251115
#: J tip = 0.000723818251115
#: ___Contour:  0
#: J far = 0.000695357075075
#: J tip = 0.000695357075075
#: Processing slice #: 2
#: ___Contour:  12
#: J far = 0.000724243863368
#: J tip = 0.000724243863368
#: ___Contour:  10
#: J far = 0.000724039326359
#: J tip = 0.000724039326359
#: ___Contour:  8
#: J far = 0.000724382210141
#: J tip = 0.000724382210141
#: ___Contour:  6
#: J far = 0.000724384838032
#: J tip = 0.000724384838032
#: ___Contour:  4
#: J far = 0.000724384330108
#: J tip = 0.000724384330108
#: ___Contour:  2
#: J far = 0.000724322864768
#: J tip = 0.000724322864768
#: ___Contour:  0
#: J far = 0.000695775588607
#: J tip = 0.000695775588607
#: Processing slice #: 3
#: ___Contour:  12
#: J far = 0.000724682028811
#: J tip = 0.000724682028811
#: ___Contour:  10
#: J far = 0.000724474826012
#: J tip = 0.000724474826012
#: ___Contour:  8
#: J far = 0.000724829044068
#: J tip = 0.000724829044068
#: ___Contour:  6
#: J far = 0.000724831725798
#: J tip = 0.000724831725798
#: ___Contour:  4
#: J far = 0.000724829925733
#: J tip = 0.000724829925733
#: ___Contour:  2
#: J far = 0.00072476234708
#: J tip = 0.00072476234708
#: ___Contour:  0
#: J far = 0.000696181198029
#: J tip = 0.000696181198029
#: Processing slice #: 4
#: ___Contour:  12
#: J far = 0.000725278695108
#: J tip = 0.000725278695108
#: ___Contour:  10
#: J far = 0.000725068712338
#: J tip = 0.000725068712338
#: ___Contour:  8
#: J far = 0.000725435634921
#: J tip = 0.000725435634921
#: ___Contour:  6
#: J far = 0.000725438109561
#: J tip = 0.000725438109561
#: ___Contour:  4
#: J far = 0.000725435914297
#: J tip = 0.000725435914297
#: ___Contour:  2
#: J far = 0.000725368531191
#: J tip = 0.000725368531191
#: ___Contour:  0
#: J far = 0.000696755820242
#: J tip = 0.000696755820242
#: Processing slice #: 5
#: ___Contour:  12
#: J far = 0.000726134035316
#: J tip = 0.000726134035316
#: ___Contour:  10
#: J far = 0.000725921439856
#: J tip = 0.000725921439856
#: ___Contour:  8
#: J far = 0.000726301946564
#: J tip = 0.000726301946564
#: ___Contour:  6
#: J far = 0.000726304241379
#: J tip = 0.000726304241379
#: ___Contour:  4
#: J far = 0.000726301812431
#: J tip = 0.000726301812431
#: ___Contour:  2
#: J far = 0.000726240687968
#: J tip = 0.000726240687968
#: ___Contour:  0
#: J far = 0.000697581536089
#: J tip = 0.000697581536089
#: Processing slice #: 6
#: ___Contour:  12
#: J far = 0.000727300076408
#: J tip = 0.000727300076408
#: ___Contour:  10
#: J far = 0.000727085283251
#: J tip = 0.000727085283251
#: ___Contour:  8
#: J far = 0.000727480040189
#: J tip = 0.000727480040189
#: ___Contour:  6
#: J far = 0.000727482321162
#: J tip = 0.000727482321162
#: ___Contour:  4
#: J far = 0.000727479673852
#: J tip = 0.000727479673852
#: ___Contour:  2
#: J far = 0.000727421177788
#: J tip = 0.000727421177788
#: ___Contour:  0
#: J far = 0.000698707991248
#: J tip = 0.000698707991248
#: Processing slice #: 7
#: ___Contour:  12
#: J far = 0.000728830746201
#: J tip = 0.000728830746201
#: ___Contour:  10
#: J far = 0.000728613228262
#: J tip = 0.000728613228262
#: ___Contour:  8
#: J far = 0.000729023394885
#: J tip = 0.000729023394885
#: ___Contour:  6
#: J far = 0.00072902570459
#: J tip = 0.00072902570459
#: ___Contour:  4
#: J far = 0.000729023028768
#: J tip = 0.000729023028768
#: ___Contour:  2
#: J far = 0.000728966061281
#: J tip = 0.000728966061281
#: ___Contour:  0
#: J far = 0.000700184901176
#: J tip = 0.000700184901176
#: Processing slice #: 8
#: ___Contour:  12
#: J far = 0.000730802904097
#: J tip = 0.000730802904097
#: ___Contour:  10
#: J far = 0.00073058079242
#: J tip = 0.00073058079242
#: ___Contour:  8
#: J far = 0.000731008048869
#: J tip = 0.000731008048869
#: ___Contour:  6
#: J far = 0.000731010179345
#: J tip = 0.000731010179345
#: ___Contour:  4
#: J far = 0.000731007625025
#: J tip = 0.000731007625025
#: ___Contour:  2
#: J far = 0.000730951774478
#: J tip = 0.000730951774478
#: ___Contour:  0
#: J far = 0.000702086001493
#: J tip = 0.000702086001493
#: Processing slice #: 9
#: ___Contour:  12
#: J far = 0.000733324186665
#: J tip = 0.000733324186665
#: ___Contour:  10
#: J far = 0.000733098185836
#: J tip = 0.000733098185836
#: ___Contour:  8
#: J far = 0.000733536653991
#: J tip = 0.000733536653991
#: ___Contour:  6
#: J far = 0.000733538800149
#: J tip = 0.000733538800149
#: ___Contour:  4
#: J far = 0.0007335362313
#: J tip = 0.0007335362313
#: ___Contour:  2
#: J far = 0.000733481941922
#: J tip = 0.000733481941922
#: ___Contour:  0
#: J far = 0.000704509398342
#: J tip = 0.000704509398342
#: Processing slice #: 10
#: ___Contour:  12
#: J far = 0.000736539273761
#: J tip = 0.000736539273761
#: ___Contour:  10
#: J far = 0.000736323658157
#: J tip = 0.000736323658157
#: ___Contour:  8
#: J far = 0.000736755619464
#: J tip = 0.000736755619464
#: ___Contour:  6
#: J far = 0.000736757863021
#: J tip = 0.000736757863021
#: ___Contour:  4
#: J far = 0.000736754944284
#: J tip = 0.000736754944284
#: ___Contour:  2
#: J far = 0.000736704869811
#: J tip = 0.000736704869811
#: ___Contour:  0
#: J far = 0.000707594504098
#: J tip = 0.000707594504098
#: Processing slice #: 11
#: ___Contour:  12
#: J far = 0.000740647552936
#: J tip = 0.000740647552936
#: ___Contour:  10
#: J far = 0.000740423501249
#: J tip = 0.000740423501249
#: ___Contour:  8
#: J far = 0.00074086499694
#: J tip = 0.00074086499694
#: ___Contour:  6
#: J far = 0.000740867380491
#: J tip = 0.000740867380491
#: ___Contour:  4
#: J far = 0.000740863656763
#: J tip = 0.000740863656763
#: ___Contour:  2
#: J far = 0.000740821350034
#: J tip = 0.000740821350034
#: ___Contour:  0
#: J far = 0.000711534603565
#: J tip = 0.000711534603565
#: Processing slice #: 12
#: ___Contour:  12
#: J far = 0.000745916708925
#: J tip = 0.000745916708925
#: ___Contour:  10
#: J far = 0.000745691745669
#: J tip = 0.000745691745669
#: ___Contour:  8
#: J far = 0.000746130427803
#: J tip = 0.000746130427803
#: ___Contour:  6
#: J far = 0.000746132863321
#: J tip = 0.000746132863321
#: ___Contour:  4
#: J far = 0.000746128718032
#: J tip = 0.000746128718032
#: ___Contour:  2
#: J far = 0.000746089136234
#: J tip = 0.000746089136234
#: ___Contour:  0
#: J far = 0.000716587335792
#: J tip = 0.000716587335792
#: Processing slice #: 13
#: ___Contour:  12
#: J far = 0.000752704669596
#: J tip = 0.000752704669596
#: ___Contour:  10
#: J far = 0.000752479081657
#: J tip = 0.000752479081657
#: ___Contour:  8
#: J far = 0.000752909018698
#: J tip = 0.000752909018698
#: ___Contour:  6
#: J far = 0.000752911445949
#: J tip = 0.000752911445949
#: ___Contour:  4
#: J far = 0.000752906960665
#: J tip = 0.000752906960665
#: ___Contour:  2
#: J far = 0.00075287072013
#: J tip = 0.00075287072013
#: ___Contour:  0
#: J far = 0.0007230928812
#: J tip = 0.0007230928812
#: Processing slice #: 14
#: ___Contour:  12
#: J far = 0.000761470352715
#: J tip = 0.000761470352715
#: ___Contour:  10
#: J far = 0.000761242168548
#: J tip = 0.000761242168548
#: ___Contour:  8
#: J far = 0.000761665742064
#: J tip = 0.000761665742064
#: ___Contour:  6
#: J far = 0.000761668044076
#: J tip = 0.000761668044076
#: ___Contour:  4
#: J far = 0.000761662457704
#: J tip = 0.000761662457704
#: ___Contour:  2
#: J far = 0.000761633306017
#: J tip = 0.000761633306017
#: ___Contour:  0
#: J far = 0.000731497223472
#: J tip = 0.000731497223472
#: Processing slice #: 15
#: ___Contour:  12
#: J far = 0.000772794142563
#: J tip = 0.000772794142563
#: ___Contour:  10
#: J far = 0.000772561444844
#: J tip = 0.000772561444844
#: ___Contour:  8
#: J far = 0.000772983091629
#: J tip = 0.000772983091629
#: ___Contour:  6
#: J far = 0.000772985500705
#: J tip = 0.000772985500705
#: ___Contour:  4
#: J far = 0.000772978674849
#: J tip = 0.000772978674849
#: ___Contour:  2
#: J far = 0.000772950709703
#: J tip = 0.000772950709703
#: ___Contour:  0
#: J far = 0.000742365234905
#: J tip = 0.000742365234905
#: Processing slice #: 16
#: ___Contour:  12
#: J far = 0.000787351603453
#: J tip = 0.000787351603453
#: ___Contour:  10
#: J far = 0.000787111617908
#: J tip = 0.000787111617908
#: ___Contour:  8
#: J far = 0.000787537156716
#: J tip = 0.000787537156716
#: ___Contour:  6
#: J far = 0.000787539729922
#: J tip = 0.000787539729922
#: ___Contour:  4
#: J far = 0.000787532826228
#: J tip = 0.000787532826228
#: ___Contour:  2
#: J far = 0.00078750408151
#: J tip = 0.00078750408151
#: ___Contour:  0
#: J far = 0.000756349334456
#: J tip = 0.000756349334456
#: Processing slice #: 17
#: ___Contour:  12
#: J far = 0.000805631237052
#: J tip = 0.000805631237052
#: ___Contour:  10
#: J far = 0.000805381912321
#: J tip = 0.000805381912321
#: ___Contour:  8
#: J far = 0.00080581392754
#: J tip = 0.00080581392754
#: ___Contour:  6
#: J far = 0.000805817105825
#: J tip = 0.000805817105825
#: ___Contour:  4
#: J far = 0.000805811107278
#: J tip = 0.000805811107278
#: ___Contour:  2
#: J far = 0.000805780671096
#: J tip = 0.000805780671096
#: ___Contour:  0
#: J far = 0.000773907882301
#: J tip = 0.000773907882301
#: Processing slice #: 18
#: ___Contour:  12
#: J far = 0.000827054710619
#: J tip = 0.000827054710619
#: ___Contour:  10
#: J far = 0.000826801463192
#: J tip = 0.000826801463192
#: ___Contour:  8
#: J far = 0.000827228736217
#: J tip = 0.000827228736217
#: ___Contour:  6
#: J far = 0.000827225895768
#: J tip = 0.000827225895768
#: ___Contour:  4
#: J far = 0.000827220730722
#: J tip = 0.000827220730722
#: ___Contour:  2
#: J far = 0.000827195942211
#: J tip = 0.000827195942211
#: ___Contour:  0
#: J far = 0.000794524252333
#: J tip = 0.000794524252333
#: Processing slice #: 19
#: ___Contour:  12
#: J far = 0.000840973366395
#: J tip = 0.000840973366395
#: ___Contour:  10
#: J far = 0.000840728393634
#: J tip = 0.000840728393634
#: ___Contour:  8
#: J far = 0.000841149439954
#: J tip = 0.000841149439954
#: ___Contour:  6
#: J far = 0.000841157470059
#: J tip = 0.000841157470059
#: ___Contour:  4
#: J far = 0.000841104477325
#: J tip = 0.000841104477325
#: ___Contour:  2
#: J far = 0.000840889884006
#: J tip = 0.000840889884006
#: ___Contour:  0
#: J far = 0.000807893971884
#: J tip = 0.000807893971884
#: Processing slice #: 20
#: ___Contour:  12
#: J far = 0.000802850632884
#: J tip = 0.000802850632884
#: ___Contour:  10
#: J far = 0.000802559384172
#: J tip = 0.000802559384172
#: ___Contour:  8
#: J far = 0.000802968966841
#: J tip = 0.000802968966841
#: ___Contour:  6
#: J far = 0.000802964684696
#: J tip = 0.000802964684696
#: ___Contour:  4
#: J far = 0.000803042636705
#: J tip = 0.000803042636705
#: ___Contour:  2
#: J far = 0.00080333793585
#: J tip = 0.00080333793585
#: ___Contour:  0
#: J far = 0.000771953064443
#: J tip = 0.000771953064443
#: Starting calculations of KI from J...
#: =================================================================
#: the stress intensity factor is being calculated assuming
#: only mode I and plane strain.
#: (21L, 7L)
#: time report
#: ++++++++++++
#: time building sets 22.5230000019
#: time in J integral Surface 0.559000015259
#: time in J integral Volume 171.657999992
#: time in J to KI 0.378999948502
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlane_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       12
#: Number of Node Sets:          830
#: Number of Steps:              1
#: Starting to build element and node sets...
#: =================================================================
#* Command successfully aborted.
execfile(
    'E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/Evaluate_J.py', 
    __main__.__dict__)
#: Model: E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlane_copy.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       12
#: Number of Node Sets:          830
#: Number of Steps:              1
#: Starting to build element and node sets...
#: =================================================================
#: Starting calculations for the J Integral...
#: ===========================================
#: Processing slice #: 0
#: ___Contour:  12
#: J far = 0.000722527658552
#: ___Contour:  10
#: J far = 0.000722334805651
#: ___Contour:  8
#: J far = 0.000722652648139
#: ___Contour:  6
#: J far = 0.000722656531105
#: ___Contour:  4
#: J far = 0.000722655773714
#: ___Contour:  2
#: J far = 0.00072259369237
#: ___Contour:  0
#: J far = 0.000694327437049
#: Processing slice #: 1
#: ___Contour:  12
#: J far = 0.000723743670862
#: ___Contour:  10
#: J far = 0.000723543317272
#: ___Contour:  8
#: J far = 0.000723874112713
#: ___Contour:  6
#: J far = 0.000723877058543
#: ___Contour:  4
#: J far = 0.000723877318754
#: ___Contour:  2
#: J far = 0.000723818251115
#: ___Contour:  0
#: J far = 0.000695357075075
#: Processing slice #: 2
#: ___Contour:  12
#: J far = 0.000724243863368
#: ___Contour:  10
#: J far = 0.000724039326359
#: ___Contour:  8
#: J far = 0.000724382210141
#: ___Contour:  6
#: J far = 0.000724384838032
#: ___Contour:  4
#: J far = 0.000724384330108
#: ___Contour:  2
#: J far = 0.000724322864768
#: ___Contour:  0
#: J far = 0.000695775588607
#: Processing slice #: 3
#: ___Contour:  12
#: J far = 0.000724682028811
#: ___Contour:  10
#: J far = 0.000724474826012
#: ___Contour:  8
#: J far = 0.000724829044068
#: ___Contour:  6
#: J far = 0.000724831725798
#: ___Contour:  4
#: J far = 0.000724829925733
#: ___Contour:  2
#: J far = 0.00072476234708
#: ___Contour:  0
#: J far = 0.000696181198029
#: Processing slice #: 4
#: ___Contour:  12
#: J far = 0.000725278695108
#: ___Contour:  10
#: J far = 0.000725068712338
#: ___Contour:  8
#: J far = 0.000725435634921
#: ___Contour:  6
#: J far = 0.000725438109561
#: ___Contour:  4
#: J far = 0.000725435914297
#: ___Contour:  2
#: J far = 0.000725368531191
#: ___Contour:  0
#: J far = 0.000696755820242
#: Processing slice #: 5
#: ___Contour:  12
#: J far = 0.000726134035316
#: ___Contour:  10
#: J far = 0.000725921439856
#: ___Contour:  8
#: J far = 0.000726301946564
#: ___Contour:  6
#: J far = 0.000726304241379
#: ___Contour:  4
#: J far = 0.000726301812431
#: ___Contour:  2
#: J far = 0.000726240687968
#: ___Contour:  0
#: J far = 0.000697581536089
#: Processing slice #: 6
#: ___Contour:  12
#: J far = 0.000727300076408
#: ___Contour:  10
#: J far = 0.000727085283251
#: ___Contour:  8
#: J far = 0.000727480040189
#: ___Contour:  6
#: J far = 0.000727482321162
#: ___Contour:  4
#: J far = 0.000727479673852
#: ___Contour:  2
#: J far = 0.000727421177788
#: ___Contour:  0
#: J far = 0.000698707991248
#: Processing slice #: 7
#: ___Contour:  12
#: J far = 0.000728830746201
#: ___Contour:  10
#: J far = 0.000728613228262
#: ___Contour:  8
#: J far = 0.000729023394885
#: ___Contour:  6
#: J far = 0.00072902570459
#: ___Contour:  4
#: J far = 0.000729023028768
#: ___Contour:  2
#: J far = 0.000728966061281
#: ___Contour:  0
#: J far = 0.000700184901176
#: Processing slice #: 8
#: ___Contour:  12
#: J far = 0.000730802904097
#: ___Contour:  10
#: J far = 0.00073058079242
#: ___Contour:  8
#: J far = 0.000731008048869
#: ___Contour:  6
#: J far = 0.000731010179345
#: ___Contour:  4
#: J far = 0.000731007625025
#: ___Contour:  2
#: J far = 0.000730951774478
#: ___Contour:  0
#: J far = 0.000702086001493
#: Processing slice #: 9
#: ___Contour:  12
#: J far = 0.000733324186665
#: ___Contour:  10
#: J far = 0.000733098185836
#: ___Contour:  8
#: J far = 0.000733536653991
#: ___Contour:  6
#: J far = 0.000733538800149
#: ___Contour:  4
#: J far = 0.0007335362313
#: ___Contour:  2
#: J far = 0.000733481941922
#: ___Contour:  0
#: J far = 0.000704509398342
#: Processing slice #: 10
#: ___Contour:  12
#: J far = 0.000736539273761
#: ___Contour:  10
#: J far = 0.000736323658157
#: ___Contour:  8
#: J far = 0.000736755619464
#: ___Contour:  6
#: J far = 0.000736757863021
#: ___Contour:  4
#: J far = 0.000736754944284
#: ___Contour:  2
#: J far = 0.000736704869811
#: ___Contour:  0
#: J far = 0.000707594504098
#: Processing slice #: 11
#: ___Contour:  12
#: J far = 0.000740647552936
#: ___Contour:  10
#: J far = 0.000740423501249
#: ___Contour:  8
#: J far = 0.00074086499694
#: ___Contour:  6
#: J far = 0.000740867380491
#: ___Contour:  4
#: J far = 0.000740863656763
#: ___Contour:  2
#: J far = 0.000740821350034
#: ___Contour:  0
#: J far = 0.000711534603565
#: Processing slice #: 12
#: ___Contour:  12
#: J far = 0.000745916708925
#: ___Contour:  10
#: J far = 0.000745691745669
#: ___Contour:  8
#: J far = 0.000746130427803
#: ___Contour:  6
#: J far = 0.000746132863321
#: ___Contour:  4
#: J far = 0.000746128718032
#: ___Contour:  2
#: J far = 0.000746089136234
#: ___Contour:  0
#: J far = 0.000716587335792
#: Processing slice #: 13
#: ___Contour:  12
#: J far = 0.000752704669596
#: ___Contour:  10
#: J far = 0.000752479081657
#: ___Contour:  8
#: J far = 0.000752909018698
#: ___Contour:  6
#: J far = 0.000752911445949
#: ___Contour:  4
#: J far = 0.000752906960665
#: ___Contour:  2
#: J far = 0.00075287072013
#: ___Contour:  0
#: J far = 0.0007230928812
#: Processing slice #: 14
#: ___Contour:  12
#: J far = 0.000761470352715
#: ___Contour:  10
#: J far = 0.000761242168548
#: ___Contour:  8
#: J far = 0.000761665742064
#: ___Contour:  6
#: J far = 0.000761668044076
#: ___Contour:  4
#: J far = 0.000761662457704
#: ___Contour:  2
#: J far = 0.000761633306017
#: ___Contour:  0
#: J far = 0.000731497223472
#: Processing slice #: 15
#: ___Contour:  12
#: J far = 0.000772794142563
#: ___Contour:  10
#: J far = 0.000772561444844
#: ___Contour:  8
#: J far = 0.000772983091629
#: ___Contour:  6
#: J far = 0.000772985500705
#: ___Contour:  4
#: J far = 0.000772978674849
#: ___Contour:  2
#: J far = 0.000772950709703
#: ___Contour:  0
#: J far = 0.000742365234905
#: Processing slice #: 16
#: ___Contour:  12
#: J far = 0.000787351603453
#: ___Contour:  10
#: J far = 0.000787111617908
#: ___Contour:  8
#: J far = 0.000787537156716
#: ___Contour:  6
#: J far = 0.000787539729922
#: ___Contour:  4
#: J far = 0.000787532826228
#: ___Contour:  2
#: J far = 0.00078750408151
#: ___Contour:  0
#: J far = 0.000756349334456
#: Processing slice #: 17
#: ___Contour:  12
#: J far = 0.000805631237052
#: ___Contour:  10
#: J far = 0.000805381912321
#: ___Contour:  8
#: J far = 0.00080581392754
#: ___Contour:  6
#: J far = 0.000805817105825
#: ___Contour:  4
#: J far = 0.000805811107278
#: ___Contour:  2
#: J far = 0.000805780671096
#: ___Contour:  0
#: J far = 0.000773907882301
#: Processing slice #: 18
#: ___Contour:  12
#: J far = 0.000827054710619
#: ___Contour:  10
#: J far = 0.000826801463192
#: ___Contour:  8
#: J far = 0.000827228736217
#: ___Contour:  6
#: J far = 0.000827225895768
#: ___Contour:  4
#: J far = 0.000827220730722
#: ___Contour:  2
#: J far = 0.000827195942211
#: ___Contour:  0
#: J far = 0.000794524252333
#: Processing slice #: 19
#: ___Contour:  12
#: J far = 0.000840973366395
#: ___Contour:  10
#: J far = 0.000840728393634
#: ___Contour:  8
#: J far = 0.000841149439954
#: ___Contour:  6
#: J far = 0.000841157470059
#: ___Contour:  4
#: J far = 0.000841104477325
#: ___Contour:  2
#: J far = 0.000840889884006
#: ___Contour:  0
#: J far = 0.000807893971884
#: Processing slice #: 20
#: ___Contour:  12
#: J far = 0.000802850632884
#: ___Contour:  10
#: J far = 0.000802559384172
#: ___Contour:  8
#: J far = 0.000802968966841
#: ___Contour:  6
#: J far = 0.000802964684696
#: ___Contour:  4
#: J far = 0.000803042636705
#: ___Contour:  2
#: J far = 0.00080333793585
#: ___Contour:  0
#: J far = 0.000771953064443
#: Starting calculations of KI from J...
#: =================================================================
#: the stress intensity factor is being calculated assuming
#: only mode I and plane strain.
#: (21L, 7L)
#: time report
#: ++++++++++++
#: time building sets 17.5350000858
#: time in J integral Surface 0.0
#: time in J integral Volume 173.309999943
#: time in J to KI 0.37299990654
o3 = session.odbs['E:/Dropbox/Research/Source/Abaqus-J-integral/Example 1/odb/ThroughThicknessCrackInInfinitePlane_copy.odb']
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.4536, 
    farPlane=20.6995, width=12.3662, height=4.89062, viewOffsetX=2.13605, 
    viewOffsetY=-0.48017)
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.524, 
    farPlane=20.6291, width=13.2364, height=5.2348, viewOffsetX=2.34867, 
    viewOffsetY=-0.545167)
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.4669, 
    farPlane=20.6862, width=13.1708, height=5.20886, viewOffsetX=2.48745, 
    viewOffsetY=-0.267817)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.5295, 
    farPlane=21.0281, width=13.2427, height=5.2373, viewOffsetX=2.47268, 
    viewOffsetY=-0.764443)
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.5301, 
    farPlane=21.0274, width=13.2435, height=5.23759, viewOffsetX=2.17978, 
    viewOffsetY=-0.383569)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.467, 
    farPlane=20.6861, width=13.171, height=5.20893, viewOffsetX=2.22425, 
    viewOffsetY=-0.229937)
session.viewports['Viewport: 1'].view.setValues(width=15.4943, height=6.12776, 
    viewOffsetX=2.52023, viewOffsetY=-0.0778426)
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.2095, 
    farPlane=20.6007, width=15.1473, height=5.99052, cameraPosition=(12.4691, 
    9.49135, 11.3725), cameraUpVector=(-0.604313, 0.638369, -0.476751), 
    cameraTarget=(3.26694, 1.40156, 0.964243), viewOffsetX=2.46378, 
    viewOffsetY=-0.0760992)
session.viewports['Viewport: 1'].view.setValues(session.views['Right'])
session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.4536, 
    farPlane=20.6995, width=12.3662, height=4.89062, viewOffsetX=1.20925, 
    viewOffsetY=-0.604659)
#: 
#: Node: PLATE-1.16
#:                                         1             2             3        Magnitude
#: Base coordinates:                  0.00000e+00,  4.00000e+00,  2.00000e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: PLATE-1.14
#:                                         1             2             3        Magnitude
#: Base coordinates:                  6.00000e+00,  4.00000e+00,  2.00000e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Nodes for distance: PLATE-1.16, PLATE-1.14
#:                                        1             2             3        Magnitude
#: Base distance:                     6.00000e+00,  0.00000e+00,  0.00000e+00,  6.00000e+00
#: No deformed coordinates for current plot.
#: 
#: Node: PLATE-1.14
#:                                         1             2             3        Magnitude
#: Base coordinates:                  6.00000e+00,  4.00000e+00,  2.00000e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: PLATE-1.13
#:                                         1             2             3        Magnitude
#: Base coordinates:                  6.00000e+00,  4.00000e+00,  0.00000e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Nodes for distance: PLATE-1.14, PLATE-1.13
#:                                        1             2             3        Magnitude
#: Base distance:                     0.00000e+00,  0.00000e+00, -2.00000e+00,  2.00000e+00
#: No deformed coordinates for current plot.
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.5693, 
    farPlane=20.5838, width=12.6883, height=5.01803, viewOffsetX=1.34464, 
    viewOffsetY=0.148453)
session.viewports['Viewport: 1'].view.setValues(nearPlane=11.5141, 
    farPlane=20.639, width=12.6277, height=4.99408, viewOffsetX=1.42836, 
    viewOffsetY=-0.342584)
#: 
#: Node: PLATE-1.14
#:                                         1             2             3        Magnitude
#: Base coordinates:                  6.00000e+00,  4.00000e+00,  2.00000e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: PLATE-1.139
#:                                         1             2             3        Magnitude
#: Base coordinates:                  6.00000e+00,  5.00002e-02,  2.00000e+00,      -      
#: No deformed coordinates for current plot.
#: 
#: Nodes for distance: PLATE-1.14, PLATE-1.139
#:                                        1             2             3        Magnitude
#: Base distance:                     0.00000e+00, -3.95000e+00,  0.00000e+00,  3.95000e+00
#: No deformed coordinates for current plot.
