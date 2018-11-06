# -*- coding: UTF-8 -*-

from piperegister import *
from register import *

def Decode(lst, cur, reg)
	cur.regE['stat'] = lst.regD['stat']
	if lst.regE['stat'] != 'AOK':
		return
	
	icode = lst.regD['icode']
	
	cur.regE['icode'] = lst.regD['icode']
	cur.regE['ifun'] = lst.regD['ifun']
	cur.regE['valC'] = lst.regD['valC']
	
	if icode in [IRRMOVQ, IRMMOVQ, IOPQ, IPUSHQ]:
		cur.regE['srcA'] = lst.regD['rA']
	elif icode in [IPOPL, IRET]:
		cur.regE['srcA'] = RRSP
	else:
		cur.regE['srcA'] = RNONE
		
	if icode in [IOPQ, IMRMOVQ, IRMMOVQ]:
		cur.regE['srcB'] = lst.regD['rB']
	elif icode in [IRET, ICALL, IPOPQ, IPUSHQ]:
		cur.regE['srcB'] = RRSP
	else:
		cur.regE['srcB'] = RNONE
	
	if icode in [IRRMOVQ, IIRMOVQ, IOPQ]:
		cur.regE['dstE'] = lst.regD['rB']
	elif icode in [IPUSHQ, IPOPQ, ICALL, IRET]:
		cur.regE['dstE'] = RRSP
	else:
		cur.regE['dstE'] = RNONE
	
	''''''''	
	cur.regE['dstW'] = RNONE
	''''''''
	
	cur.regE['valA'], cur.regE['valB'] = reg.read(cur.regE['srcA'], cur.regE['srcB'])
	
	if icode == RCALL:
		cur.regE['valA'] = lst.regD['valP']
	
