# -*- coding: UTF-8 -*-
import sys
import os

o_path = os.getcwd() 
sys.path.append(o_path)

from memory_sys.piperegister import *
from memory_sys.register import *
from others.Global import *

def Decode(lst, cur, reg, E_over):
	add_CR('<div>D starts</div>')
	cur.regE['stat'] = lst.regD['stat']	
	icode = lst.regD['icode']	
	cur.regE['icode'] = lst.regD['icode']
	cur.regE['ifun'] = lst.regD['ifun']
	if lst.regD['stat'] not in ['AOK','BUB']:
		add_CR('<div>D is over</div>')
		return

	cur.regE['valC'] = lst.regD['valC']
	
	if icode in [IRRMOVQ, IRMMOVQ, IOPQ, IPUSHQ]:
		cur.regE['srcA'] = lst.regD['rA']
	elif icode in [IPOPQ, IRET]:
		cur.regE['srcA'] = RRSP
	else:
		cur.regE['srcA'] = RNONE
		
	if icode in [IOPQ, IMRMOVQ, IRMMOVQ, IIADDQ]:
		cur.regE['srcB'] = lst.regD['rB']
	elif icode in [IRET, ICALL, IPOPQ, IPUSHQ]:
		cur.regE['srcB'] = RRSP
	else:
		cur.regE['srcB'] = RNONE
	
	if icode in [IRRMOVQ, IIRMOVQ, IOPQ, IIADDQ]:
		cur.regE['dstE'] = lst.regD['rB']
	elif icode in [IPUSHQ, IPOPQ, ICALL, IRET]:
		cur.regE['dstE'] = RRSP
	else:
		cur.regE['dstE'] = RNONE
	
	if icode in [IMRMOVQ, IPOPQ]:
		cur.regE['dstM'] = lst.regD['rA']
	else:
		cur.regE['dstM'] = RNONE
	
	cur.regE['valA'], cur.regE['valB'] = reg.read(cur.regE['srcA'], cur.regE['srcB'])
	
	E_over.wait()
	
	#forward valA
	if icode in [ICALL, IJXX]:
		cur.regE['valA'] = lst.regD['valP']
	elif cur.regE['srcA'] == RNONE:
		pass
	elif cur.regE['srcA'] == cur.regM['dstE']:
		cur.regE['valA'] = cur.regM['valE']
	elif cur.regE['srcA'] == lst.regM['dstM']:
		cur.regE['valA'] = cur.regW['valM']
	elif cur.regE['srcA'] == lst.regM['dstE']:
		cur.regE['valA'] = lst.regM['valE']
	elif cur.regE['srcA'] == lst.regW['dstM']:
		cur.regE['valA'] = lst.regW['valM']
	elif cur.regE['srcA'] == lst.regW['dstE']:
		cur.regE['valA'] = lst.regW['valE']
		
	#forward valB
	if cur.regE['srcB'] == RNONE:
		pass
	elif cur.regE['srcB'] == cur.regM['dstE']:
		cur.regE['valB'] = cur.regM['valE']
	elif cur.regE['srcB'] == lst.regM['dstM']:
		cur.regE['valB'] = cur.regW['valM']
	elif cur.regE['srcB'] == lst.regM['dstE']:
		cur.regE['valB'] = lst.regM['valE']
	elif cur.regE['srcB'] == lst.regW['dstM']:
		cur.regE['valB'] = lst.regW['valM']
	elif cur.regE['srcB'] == lst.regW['dstE']:
		cur.regE['valB'] = lst.regW['valE']
	
	add_CR('<div>D is over</div>')
		
	
