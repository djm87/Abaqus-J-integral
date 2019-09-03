# Utilities for J integral calculation
from abaqusConstants import *
from odbAccess import *
from textRepr import *
from shutil import copyfile
from os import getcwd, path
import numpy as np
import pprint
import time
import sys

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def invertMatrix(A):
    u, s, v = np.linalg.svd(A)
    Ainv = np.dot (v.transpose(), np.dot(np.diag(s**-1),u.transpose()))
    return(Ainv)
	
def Ensure_ODB_Is_Closed(odbPath,session):
	keys=session.odbs.keys()
	for key in keys:
		path=os.path.normpath(session.odbs[key].path)
		if not session.odbs[key].closed and odbPath==path:
			session.odbs[key].close()

def Numpy_2_Tuple(nplist): 
	if len(nplist.shape)==1:
		out = tuple(nplist)
	elif len(nplist.shape)==2:
		out = tuple(map(tuple, nplist))
	else:
		raise NameError("Unhandled numpy list to tuple conversion")

	return out

def	CheckFieldExists(frame,fieldName,position):
	try:
		if position=='ELEMENT_NODAL':
			field = frame.fieldOutputs[fieldName].getSubset(position=ELEMENT_NODAL)
		elif position=='INTEGRATION_POINT':
			field = frame.fieldOutputs[fieldName].getSubset(position=INTEGRATION_POINT)
		elif position=='NODAL':
			field = frame.fieldOutputs[fieldName].getSubset(position=NODAL)		
		else:
			print 'please enter ELEMENT_NODAL, INTEGRATION_POINT, or NODAL strings for position'
			raise NameError('invalid position specified')
			
		if not field.values:
			raise NameError('data is not at the position specified')
			
	except NameError:
		print 'Field variable ', fieldName,' at position ', position, ' does not exists'
		raise
	except KeyError:
		print 'Field variable ', fieldName,' at position ', position, ' does not exists'
		raise

def CheckSetExists(root,setName,setType):
	if setType=='element':
		try: 
			elemset = root.elementSets[setName]
			region = " in the element set : " + setName;
		except KeyError: 
			print 'An assembly level elSet named %s does not exist' % (setName)
			raise	
	if setType=='node':		
		try: 
			nodeset = root.nodeSets[setName]
			region = " in the element set : " + setName;
		except KeyError: 
			print 'An assembly level nodeSet named %s does not exist' % (setName)
			raise

def GetElementConnectivities(elements):
	#Adapted from https://gist.github.com/mhogg/b0481d842253d12bb41d
	#For 539370 elements, 2234751 nodes, C3D20 type it takes about 1 minute to run
	# Get neighboring elements attached for each node such that nodes label is the index, sorted
	elemConn = {}
	for elem in elements:
		#elem=elements[elem]
		e     = elem.label
		nconn = elem.connectivity #list of node labels

		for n in nconn:		
			if not elemConn.has_key(n):
				elemConn[n] = []
				elemConn[n].append(e)
			elif not any(x==e for x in elemConn[n]):
				elemConn[n].append(e)
	
	# Now get list of all neighboring elements for each element where element label is the index
	elemNbr = {}
	for elem in elements:
		#elem=elements[539366]
		e     = elem.label
		nconn = elem.connectivity
		if not elemNbr.has_key(e):
			elemNbr[e] = {}
		for n in nconn:
			for ec in elemConn[n]:
				elemNbr[e][ec] = 1

	# Delete element label from its keys of neighbours and convert to a list
	for k in elemNbr.keys():
		del elemNbr[k][k]
		elemNbr[k] = elemNbr[k].keys() 	
	
	return elemConn, elemNbr
			
def GetNumIntegrationPoints(elType):
	if elType=='C3D20':
		nInt=27
	else:
		print 'Unknown element type'
		raise
	return nInt
	