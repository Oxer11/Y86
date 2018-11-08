# -*- coding: UTF-8 -*-

from cc_stat import *

def ALU(ALUA, ALUB, ALUfun):
	if ALUfun == 0:
		return ALUA+ALUB
	elif ALUfun == 1:
		return ALUA-ALUB
	elif ALUfun == 2:
		return ALUA&ALUB
	elif ALUfun == 3:
		return ALUA^ALUB
	else:
		raise Exception("Invalid ALUfun: %d"%(ALUfun))
		

def Execute(lst, cur, CC):
	cur.regM['stat'] = lst.regE['stat']
	cur.regM['icode'] = lst.regE['icode']
	cur.regM['dstM'] = lst.regE['dstM']
	cur.regM['dstE'] = lst.regE['dstE']
	cur.regM['valA'] = lst.regE['valA']
	icode = lst.regE['icode']
	
	ALUB = valB
	if icode in [IOPQ, IRRMOVQ]:
		ALUA = lst.regE['valA']
	elif icode in [IIRMOVQ, IRMMOVQ, IMRMOVQ]:
		ALUA = lst.regE['valC']
	elif icode in [IPUSHQ, ICALL]:
		ALUA = -4
	elif icode in [IPOPQ, IRET]:
		ALUA = 4
	else:
		ALUA = 0
	
	if icode == IOPQ:
		ALUfun = lst.regE['ifun']
	else:
		ALUfun = 0
		
	cur.regM['valE'] = ALU(ALUA, ALUB, ALUfun)
	
	if lst.regW['stat'] == 'AOK' and cur.regM['stat'] == 'AOK':
		if cur.regM['valE']==0: CC.ZF = 1
		if cur.regM['valE']<0 : CC.SF = 1
		if ((ALUA<0) == (ALUB<0)) and ((cur.regM['valE']<0) != (ALUA<0)): CC.OF = 1
		
	cur.regM['Cnd'] = 0
	if icode in [IOPQ, IRRMOVQ]:
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
	
