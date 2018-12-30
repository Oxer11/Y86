# -*- coding: UTF-8 -*-
import sys
import os

o_path = os.getcwd() 
sys.path.append(o_path)

from others.cc_stat import *
from others.constant import *
from others.Global import *

def ALU(ALUA, ALUB, ALUfun):
	if ALUfun == 0:
		ans = ALUA+ALUB
	elif ALUfun == 1:
		ans = ALUB-ALUA
	elif ALUfun == 2:
		ans = ALUA&ALUB
	elif ALUfun == 3:
		ans = ALUA^ALUB
	else:
		raise Exception("Invalid ALUfun: %d"%(ALUfun))
	if ans < MININT:
		ans = MAXINT - MININT + ans + 1
	elif ans > MAXINT:
		ans = MININT - MAXINT + ans - 1
	return ans
		

def Execute(lst, cur, CC, NUM_INS, NUM_BUB, E_over, M_over):
	#add_CR('<div>E starts</div>')
	add_THREAD('E')
	
	cur.regM['stat'] = lst.regE['stat']
	cur.regM['icode'] = lst.regE['icode']
	cur.regM['ifun'] = lst.regE['ifun']
	NUM_INS += 1
	if lst.regE['stat'] in ['BUB']: NUM_BUB += 1
	M_over.wait()
	if lst.regE['stat'] not in ['AOK','BUB'] or lst.regM['stat'] not in ['AOK','BUB'] or lst.regW['stat'] not in ['AOK','BUB'] or cur.regW['stat'] not in ['AOK','BUB']:
		#add_CR('<div>E is over</div>')
		add_THREAD('E')
		E_over.set()
		return CC, NUM_INS, NUM_BUB

	cur.regM['dstM'] = lst.regE['dstM']
	cur.regM['dstE'] = lst.regE['dstE']
	if lst.regE['icode'] in [IRMMOVQ, IPUSHQ] and lst.regM['dstM'] == cur.regE['srcA']:
		cur.regM['valA'] = cur.regW['valM']
	else:
		cur.regM['valA'] = lst.regE['valA']
	icode = lst.regE['icode']
	
	ALUB = lst.regE['valB']
	if icode in [IOPQ, IRRMOVQ]:
		ALUA = lst.regE['valA']
	elif icode in [IIRMOVQ, IRMMOVQ, IMRMOVQ, IIADDQ]:
		ALUA = lst.regE['valC']
	elif icode in [IPUSHQ, ICALL]:
		ALUA = -8
	elif icode in [IPOPQ, IRET]:
		ALUA = 8
	else:
		ALUA = 0
	
	if icode == IOPQ:
		ALUfun = lst.regE['ifun']
	else:
		ALUfun = 0
	
	cur.regM['valE'] = ALU(ALUA, ALUB, ALUfun)
	
	#设置条件码
	if lst.regW['stat'] in ['AOK','BUB'] and cur.regM['stat'] in ['AOK','BUB'] and cur.regM['icode'] in [IOPQ, IIADDQ]:
		if cur.regM['valE']==0: CC.ZF = 1
		else: CC.ZF = 0
		if cur.regM['valE']<0 : CC.SF = 1
		else: CC.SF = 0
		if (ALUfun == 0) and ((ALUA<0) == (ALUB<0)) and ((cur.regM['valE']<0) != (ALUA<0)): CC.OF = 1
		elif (ALUfun == 1) and (ALUA*ALUB<0) and (((ALUB<0) and (cur.regM['valE']>ALUB)) or ((ALUB>0) and (cur.regM['valE']<ALUB))): CC.OF = 1
		else: CC.OF = 0
		
	#设置Cnd
	if icode in [IJXX, IRRMOVQ]:
		if lst.regE['ifun'] == 0:
			cur.regM['Cnd'] = 1
		elif lst.regE['ifun'] == 1:
			cur.regM['Cnd'] = (CC.SF^CC.OF)|CC.ZF
		elif lst.regE['ifun'] == 2:
			cur.regM['Cnd'] = CC.SF^CC.OF
		elif lst.regE['ifun'] == 3:
			cur.regM['Cnd'] = CC.ZF
		elif lst.regE['ifun'] == 4:
			cur.regM['Cnd'] = not CC.ZF
		elif lst.regE['ifun'] == 5:
			cur.regM['Cnd'] = not (CC.SF^CC.OF)
		elif lst.regE['ifun'] == 6:
			cur.regM['Cnd'] = not (CC.SF^CC.OF) and not CC.ZF
		else:
			cur.regM['stat'] = 'INS'
	
	#处理cmov
	if icode == 2 and lst.regE['ifun'] != 0 and not cur.regM['Cnd']:
		cur.regM['dstE'] = RNONE
	
	#add_CR('<div>E is over</div>')
	add_THREAD('E')
	E_over.set()
	
	return CC, NUM_INS, NUM_BUB
	
