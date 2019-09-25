def CalculateDomainJIntegral(Junit,JInt,stepNumber,frameNumbers,contours,slices,SetPrefix,nodeLabelTip,isSymm,odb,partInstance,JFnamePrefix): 
	##This routine calculates the so called domain J integral
	##Assumptions: C3D20 elements, small strains, crack extension direction [0,1,0], straight crackfront
	##Assumptions: nodeLabelTip is not at zero (used when reconstructing the crack front)
	##output: J(s) - energy release rate along the crack front (file)
	##==============================================================================================================
	
	print 'Starting calculations for the J Integral...'
	print '==========================================='
	print '' 
	
	##Initialize Abaqus variables
	##=============================
	#Get components of odb
	root=odb.rootAssembly
	#Get elements
	part=root.instances[partInstance]
	elements=part.elements

	#Get nodes
	allNodes = root.instances[partInstance].nodes 
	
	#Get the frames in the step 
	steps=odb.steps

	# Get the step keys
	allSteps = steps.keys()

	# Get current step object and the number of increments (frameLen) in step
	step = steps[allSteps[stepNumber]]

	# Get frames in step
	frames=step.frames

	#Initialize J data container and slice position so we can later write to file
	J=np.zeros((len(frameNumbers),len(slices),len(contours)),dtype='float64')

	slicePosition=np.zeros((len(slices)),dtype='float64')
	
	#Sort slice and contour lists
	contours.sort(reverse = True) #starts with largest contour first to save computations
	slices.sort()	

	##loop over specified frames and compute J
	##======================
	for frame in range(0,len(frameNumbers),1):
		frameId=frameNumbers[frame]
		##Get the frame and time
		##======================
		cframe = frames[frameId]
		TTAU = cframe.frameValue
		
		#Check that the necessary field variables exist at the appropriate locations
		##==========================================
		CheckFieldExists(cframe,'U','NODAL') #displacements
		CheckFieldExists(cframe,'S','INTEGRATION_POINT') #stress 
				
		##loop over the slices and contours specified
		##==========================================
		for slice in range(0,len(slices),1):
			sliceId=slices[slice]
			print 'Processing slice #:',sliceId
			
			#Get slice position and the crack length for the slice
			nSetSlice=SetPrefix+'-contour-'+str(contours[-1])+'-slice-'+str(sliceId)
			CheckSetExists(root,nSetSlice,'node')
			slicePosition[slice],L,Lc,rPoszRelTol,CFPosz=GetCrackFrontInterface(root,allNodes,nSetSlice,nodeLabelTip) 
			
			for contour in range(0,len(contours),1):
				contourId=contours[contour]
				print '___Contour: ', contourId
				
				##build the node set and element set names 
				##========================================
				nSetSlice=SetPrefix+'-contour-'+str(contourId)+'-slice-'+str(sliceId)
				nSetQ0=nSetSlice+'-Q0'
				nSetQ0p5=nSetSlice+'-Q0p5'
				nSetQ1=nSetSlice+'-Q1'
				elSetSlice=nSetSlice
				
				##Check that node and element sets exist	(ensures only that they exist, not that they are valid..)
				##=====================================
				CheckSetExists(root,nSetQ0,'node')
				CheckSetExists(root,nSetQ0p5,'node')
				CheckSetExists(root,nSetQ1,'node')
				CheckSetExists(root,nSetSlice,'node')
				CheckSetExists(root,elSetSlice,'element')
				
				##For a slice compute all data once and after that just compute a mask based on the elementsets
				##============================================================================================
				#If the largest contour compute all quantities
				t0=time.time()
				if contour==0:
					#Stress Sij 
					S,SElLabels,nEl,nInt = GetStress(root,cframe,elSetSlice)

					#Get du/dX, where X is the reference coordinates and u is displacement in the current frame. 
					#The Jacobian is also computed when calculating the derivatives and is returned here
					dudX,detJac,dudXElLabels = GetdudX(root,partInstance,cframe,allNodes,nSetSlice,elSetSlice)
					
					#Strain energy density defined for linear elasticity as computed for linear elasticity as U=1/2*Sijeij where e is linear strain
					W = GetW(S,dudX,nEl,nInt)
					
					#Get dqdX, a weighting term defined as a pyramid function similar to what Abaqus uses
					dqdX,dqdXElLabels=GetdqdX(root,cframe,allNodes,nSetQ0,nSetQ0p5,nSetQ1,nodeLabelTip,nSetSlice,elSetSlice,L,rPoszRelTol,CFPosz,isSymm)

					#Get the Jacobian for integration
					#detJac=GetdetJac(root,partInstance,frame,allNodes,nSetSlice,elSetSlice)
					
					#Get Gauss integrations weights
					_,wp = Gauss_Guad_3d(3)
					wp = np.reshape(wp,(-1))

					#Initialize the croneker delta evaluation 
					krd2=np.zeros((3),dtype='float64')
					krd2[1]=1
					
					if isSymm:
						factor=Junit*2.0/Lc 
					else:
						factor=Junit*1.0/Lc 
					
					#Create mask with all values true
					mask=np.ones(nEl,dtype=bool)

				else:
					#Compute a mask for sub contours
					els=root.elementSets[elSetSlice].elements[0]
					mask = GetContourMask(els,SElLabels)

					#Get dqdX, a weighting term defined as a pyramid function similar to what Abaqus uses
					dqdXtmp,dqdXElLabels=GetdqdX(root,cframe,allNodes,nSetQ0,nSetQ0p5,nSetQ1,nodeLabelTip,nSetSlice,elSetSlice,L,rPoszRelTol,CFPosz,isSymm)
										
					#dqdX doesn't have the same number of elements need to map back to original array
					dqdXElLabels=np.array(dqdXElLabels)
					SElLabels=np.array(SElLabels)
					for el in range(0,len(els),1):
						elabel=np.array(dqdXElLabels[el])
						ind=np.where(SElLabels==dqdXElLabels[el])
						dqdX[ind,:,:]=dqdXtmp[el,:,:]
					
				##Perform quadrature
				##====================
				Jbar=0
				for el in range(0,nEl,1):
					if mask[el]:	
						for p in range(0,nInt,1):
							Jbar+=np.dot((np.dot(S[el,p,:,:],dudX[el,p,:,1])-W[el,p]*krd2),dqdX[el,p,:])*detJac[el,p]*wp[p]
			
				#Store J
				J[frame][slice][contour]=factor*Jbar
				print 'J far =',J[frame][slice][contour]
				if JInt.shape[0]==len(frameNumbers) and JInt.shape[1]==len(slices) and JInt.shape[2]==len(contours):
					print 'J tip =',J[frame][slice][contour]+JInt[frame][slice][contour]
				#print 'Time for contour comps', time.time()-t0
				
		##Write the computed J values to a file 
		##=====================================
		WriteJToFile(JFnamePrefix,contours,slices,J[frame],slicePosition,TTAU)	
		if JInt.shape[0]==len(frameNumbers) and JInt.shape[1]==len(slices) and JInt.shape[2]==len(contours):
			WriteJToFile(JFnamePrefix+'corrected_',contours,slices,J[frame]+JInt[frame],slicePosition,TTAU)
	if JInt.shape[0]==len(frameNumbers) and JInt.shape[1]==len(slices) and JInt.shape[2]==len(contours):
		return J+JInt
	else:
		return J
		
def CalculateDomainJIntegralInterface(Junit,stepNumber,frameNumbers,contours,slices,SetPrefix,nodeLabelTip,isSymm,odb,partInstance,JIntFnamePrefix): 
	##This routine calculates the material force at surfaces where there is a change in material between elements and integrates
	##the material force over the interface.
	##Assumptions: C3D20 elements, small strains, interface normal [0,1,0], crack extension direction [0,1,0], straight crackfront
	##Assumptions: nodeLabelTip is not at zero (used when reconstructing the crack front)
	##output: J-Interface(s) - energy release rate along the crack front that is due to the interfaces (file)
	##output: Spatial energy densities in the interfaces (file)
	##==============================================================================================================
	
	print 'Starting calculations for the Material force at the interface...'
	print '================================================================='
	print ''
	
	##Initialize Abaqus variables
	##=============================
	#Get components of odb
	root=odb.rootAssembly
	#Get elements
	part=root.instances[partInstance]
	elements=part.elements

	#Get nodes
	allNodes = root.instances[partInstance].nodes 
	
	#Get the frames in the step 
	steps=odb.steps

	# Get the step keys
	allSteps = steps.keys()

	# Get current step object and the number of increments (frameLen) in step
	step = steps[allSteps[stepNumber]]

	# Get frames in step
	frames=step.frames

	#Initialize J data container and slice position so we can later write to file
	JInt=np.zeros((len(frameNumbers),len(slices),len(contours)),dtype='float64')

	slicePosition=np.zeros((len(slices)),dtype='float64')
	
	#Sort slice and contour lists
	contours.sort(reverse = True) #starts with largest contour first to save computations
	slices.sort()	

	#Set the surface normals for the interfaces
	z=np.array([0,1,0])

	##loop over specified frames and compute J
	##======================
	for frame in range(0,len(frameNumbers),1):
		frameId=frameNumbers[frame]
		##Get the frame and time
		##======================
		cframe = frames[frameId]
		TTAU = cframe.frameValue
		
		#Check that the necessary field variables exist at the appropriate locations
		##==========================================
		CheckFieldExists(cframe,'U','NODAL') #displacements
		CheckFieldExists(cframe,'S','INTEGRATION_POINT') #stress 
				
		##loop over the slices and contours specified
		##==========================================
		for slice in range(0,len(slices),1):
			sliceId=slices[slice]
			print 'Processing slice #:',sliceId
			
			#Get slice position and the crack length for the slice
			nSetSlice=SetPrefix+'-contour-'+str(contours[-1])+'-slice-'+str(sliceId)
			CheckSetExists(root,nSetSlice,'node')
			slicePosition[slice],L,Lc,rPoszRelTol,CFPosz=GetCrackFrontInterface(root,allNodes,nSetSlice,nodeLabelTip) 
			
			for contour in range(0,len(contours),1):
				contourId=contours[contour]
				print '___Contour: ', contourId
				
				##build the node set and element set names 
				##========================================
				nSetSlice=SetPrefix+'-contour-'+str(contourId)+'-slice-'+str(sliceId)
				nSetQ0=nSetSlice+'-Q0'
				nSetQ0p5=nSetSlice+'-Q0p5'
				nSetQ1=nSetSlice+'-Q1'
				nSetInterface=nSetSlice+'-interface'
				elSetSlice=nSetSlice
				elSetInterfaceBottom=nSetSlice+'-interfaceBottom'
				elSetInterfaceTop=nSetSlice+'-interfaceTop'
				
				##Check that node and element sets exist	(ensures only that they exist, not that they are valid..)
				##=====================================
				CheckSetExists(root,nSetQ0,'node')
				CheckSetExists(root,nSetQ0p5,'node')
				CheckSetExists(root,nSetQ1,'node')
				CheckSetExists(root,nSetSlice,'node')
				CheckSetExists(root,nSetInterface,'node')
				CheckSetExists(root,elSetSlice,'element')
				CheckSetExists(root,elSetInterfaceBottom,'element')
				CheckSetExists(root,elSetInterfaceTop,'element')
				
				##For a slice compute all data once and after that just compute a mask based on the elementsets
				##============================================================================================
				t00=time.time()
				InterfaceElements=root.elementSets[elSetInterfaceBottom].elements
				if InterfaceElements!=None:
					#If the largest contour compute all quantities
					if contour==0:
						#Get the nodes at the interface
						nodes=root.nodeSets[nSetInterface].nodes[0]
						
						#At the bottom of the interface
						elsm=root.elementSets[elSetInterfaceBottom].elements[0]
						elsp=root.elementSets[elSetInterfaceTop].elements[0]
						nEls=len(elsm)
						elsSetm = root.elementSets[elSetInterfaceBottom].elements[0]
						Sm,surfm,elLabelm=Get2DStress(nodes,elsm,elsp,elSetInterfaceBottom,allNodes,root,cframe)
						dudXm,_ = Get2DdudX(root,partInstance,cframe,allNodes,nSetInterface,elSetInterfaceBottom,surfm)
						Wm = GetW(Sm,dudXm,nEls,9)

						#At the top of the interface
						elsSetp = root.elementSets[elSetInterfaceTop].elements[0]
						Sp,surfp,elLabelp=Get2DStress(nodes,elsp,elsm,elSetInterfaceTop,allNodes,root,cframe)		
						dudXp,elLabelp2 = Get2DdudX(root,partInstance,cframe,allNodes,nSetInterface,elSetInterfaceTop,surfp)
						Wp = GetW(Sp,dudXp,nEls,9)
						
						
						#Average stress 
						S=(Sp+Sm)/2.0
						
						#Take differences across the interface
						dudX=dudXp-dudXm
						W=Wp-Wm
						
						#Get the area Jacobian
						detJac,elLabel = Get2DdetJac(root,cframe,partInstance,surfp,allNodes,elsp)
						
						#Get Q2 along L
						Q2EN=GetqNew2D(nSetQ0,nSetQ0p5,nSetQ1,nSetSlice,nodeLabelTip,root,allNodes,elSetSlice,L,rPoszRelTol,CFPosz)
						elSlice = root.elementSets[elSetSlice].elements[0]
						lz=Convert_Q2_to_Face_integration(Q2EN,surfm,elsm,elSlice,z)													
						
						#Get the Gauss weights (independent on the face so chose random face=1)
						_,wp=Gauss_Guad_Psuedo_2d(3,1)
						
						#Initialize the Kronecker delta evaluation 
						krd2=np.zeros((3),dtype='float64')
						krd2[1]=1
										
						if isSymm:
							factor=Junit*2.0/Lc 
						else:
							factor=Junit*1.0/Lc
						
						#Export spatial data of the material force as energy density
						#Currently exporting J/m^3*m^2/m.. not the density. Fix when units are fixed
						WriteSpatialJint(JIntFnamePrefix,S,dudX,W,detJac,wp,krd2,lz,allNodes,elsm,surfm,slice,TTAU,1.0)	

						#Initialize mask
						mask=np.ones((len(elsm)),dtype='bool')
					else:
						#Compute a mask sub contours
						elsm=root.elementSets[elSetInterfaceBottom].elements[0]
						mask = GetContourMask(elsm,elLabelm)
						
					##Perform quadrature
					##====================
					Jbar=0
					for el in range(0,nEls,1):
						if mask[el]:
							for p in range(0,9,1):
								Jbar+=np.dot(np.dot(S[el,p,:,:],dudX[el,p,:,1])-W[el,p]*krd2,lz[el,p,:])*detJac[el,p]*wp[p]
													
							print elLabelm[el],elLabelp[el],surfm[el],surfm[el],S[el,0,0,0]

					#Store Jint
					JInt[frame][slice][contour]=factor*Jbar
					print 'Jint =',JInt[frame][slice][contour]

		##Write the computed J values to a file 
		##=====================================
		WriteJToFile(JIntFnamePrefix,contours,slices,JInt[frame],slicePosition,TTAU)	
	return JInt