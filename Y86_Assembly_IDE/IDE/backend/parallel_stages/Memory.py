# -*- coding: UTF-8 -*-
import sys
import os

o_path = os.getcwd() 
sys.path.append(o_path)

from memory_sys.memory import *
from others.Global import *

def Memory_(lst, cur, mem, M_over):
	#add_CR('<div>M starts</div>')
	add_THREAD('M')
	cur.regW['stat'] = lst.regM['stat']
	cur.regW['icode'] = lst.regM['icode']
	cur.regW['ifun'] = lst.regM['ifun']
	if lst.regM['stat'] not in ['AOK','BUB'] or lst.regW['stat'] not in ['AOK','BUB']:
		#add_CR('<div>M is over</div>')
		add_THREAD('M')
		M_over.set()
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
	
	#add_CR('<div>M is over</div>')
	add_THREAD('M')
	M_over.set()
