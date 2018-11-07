# -*- coding: UTF-8 -*-

from memory import *

def Memory(lst, cur, mem):
	cur.regW['stat'] = lst.regM['stat']
	cur.regW['icode'] = lst.regM['icode']
	cur.regW['dstE'] = lst.regM['dstE']
	cur.regW['dstM'] = lst.regM['dstM']
	cur.regW['valE'] = lst.regM['valE']
	
	icode = lst.regM['icode']
	
	if icode == IMRMOVQ:
		cur.regW['valM'] = mem.read(lst.regM['valE'])
	elif icode in [IPOPQ, IRET]:
		cur.regW['valM'] = mem.read(lst.regM['valA'])
	else:
		cur.regW['valM'] = 0
		
	if icode in [IRMMOVQ, IPUSHQ, ICALL]:
		mem.write(lst.regM['valE'], lst.regM['valA'])
