def Gauss_Guad_1d(npoints):
	#determines the integration points and weighting coefficients for 
	#Gauss-legendre quadrature for 1d integration which can then be used for n-dim quadrature
	#npoint is the number of integration points
	
	#See https://www.sciencedirect.com/topics/engineering/gauss-quadrature
	if npoints == 3:
		p=np.float64(0.6)
		psqrt=np.sqrt(p)
		points = np.array([-psqrt,0.,psqrt],dtype='float64')
		a=np.float64(5./9.)
		b=np.float64(8./9.)
		weights = np.array([a,b,a],dtype='float64')
	else: 
		raise NameError('unspecified number of quadrature points')
	return [points,weights]
	
def Gauss_Guad_2d(npoints): 
	print 'to be done' 
	raise
	
def Gauss_Guad_3d(npoints):
	#determines the integration points and weighting coefficients for 
	#Gauss-legendre quadrature for 3d integration. this function assumes we have equal 
	#number of quadrature points in each dimension and can be used for 3x3x3 integration schemes
	#The function has been verified only for C3D20 elements with 3x3x3 integration!
	#npoint is the number of integration points
	
	[points_1d,weights_1d]=Gauss_Guad_1d(npoints)

	#print 'points_1d',points_1d
	
	points=np.zeros((npoints*npoints*npoints, 3),dtype='float64')
	weights=np.zeros((npoints*npoints*npoints, 1),dtype='float64')
	
	cnt=0
	for k in range(0,npoints,1): #t dim
		for j in range(0,npoints,1): #s dim
			for i in range(0,npoints,1): #r dim
				points[cnt,0]=points_1d[i]
				points[cnt,1]=points_1d[j]
				points[cnt,2]=points_1d[k]
				weights[cnt]=weights_1d[i]*weights_1d[j]*weights_1d[k]
				#print 'w',weights[cnt]
				#print 'w',points_1d[i],points_1d[j],points_1d[k]
				cnt=cnt+1
	return [points,weights]