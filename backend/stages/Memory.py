# -*- coding: UTF-8 -*-
import sys
import os

o_path = os.getcwd() 
sys.path.append(o_path)

from memory_sys.memory import *

def Memory_(lst, cur, mem):
	cur.regW['stat'] = lst.regM['stat']
	cur.regW['icode'] = lst.regM['icode']
	cur.regW['ifun'] = lst.regM['ifun']
	if lst.regM['stat'] not in ['AOK','BUB'] or lst.regW['stat'] not in ['AOK','BUB']:
		return

	cur.regW['dstE'] = lst.regM['dstE']
	cur.regW['dstM'] = lst.regM['dstM']
	cur.regW['valE'] = lst.regM['valE']
	
	icode = lst.regM['icode']
	
	if icode == IMRMOVQ:
		if mem.valid(lst.regM['valE']):
			cur.regW['valM'] = mem.read(lst.regM['valE'])
		else:
			cur.regW['stat'] = 'ADR'
	elif icode in [IPOPQ, IRET]:
		if mem.valid(lst.regM['valA']):
			cur.regW['valM'] = mem.read(lst.regM['valA'])
		else:
			cur.regW['stat'] = 'ADR'
	else:
		cur.regW['valM'] = 0
		
	if icode in [IRMMOVQ, IPUSHQ, ICALL]:
		if mem.valid(lst.regM['valE']):
			mem.write(lst.regM['valE'], lst.regM['valA'])
		else:
			cur.regW['stat'] = 'ADR'
