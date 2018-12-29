# -*- coding: UTF-8 -*-
import sys
import os

o_path = os.getcwd() 
sys.path.append(o_path)

from others.little_endian import *
from memory_sys.piperegister import *
from others.constant import *
from others.Global import*

def valid(InsCode):
	icode = int(InsCode[0], 16)
	ifun = int(InsCode[1], 16)

	#检验icode
	if icode not in range(0, 0xD): return 0
	#检验指令格式
	length = len(InsCode)

	if icode in [IHALT, INOP, IRET]:
		if length != 2: return 0
	elif icode in [IRRMOVQ, IOPQ, IPUSHQ, IPOPQ]:
		if length != 4: return 0
	elif icode in [IJXX, ICALL]:
		if length != 18: return 0
	elif icode in [IIRMOVQ, IRMMOVQ, IMRMOVQ, IIADDQ]:
		if length != 20: return 0
	#检验ifun
	if icode in [IOPQ, IJXX, IRRMOVQ]:
		if (icode == IOPQ) and (ifun not in range(0,4)):
			return 0
		elif (icode in [IJXX, IRRMOVQ]) and (ifun not in range(0,7)):
			return 0
	elif ifun != 0:
		return 0

	#检验寄存器
	if icode in [IPUSHQ, IPOPQ]:
		if InsCode[3] != 'f' or InsCode[2] == 'f':
			return 0
	elif icode in [IIRMOVQ, IIADDQ]:
		if InsCode[2] != 'f' or InsCode[3] == 'f':
			return 0
	elif icode in [IRRMOVQ, IOPQ, IRMMOVQ, IMRMOVQ]:
		if InsCode[2] == 'f' or InsCode[3] == 'f':
			return 0
	return 1

def Fetch(lst, cur, InsCode_dic, PC):
	add_CR('<div>F starts</div>')
	if not InsCode_dic.has_key(PC):
		cur.regD['stat'] = 'NON'
		add_CR( '<div>F is over</div>')
		return
	InsCode = InsCode_dic[PC]
	icode = int(InsCode[0], 16)
	
	if not valid(InsCode):
		cur.regD['stat'] = 'INS'
		add_CR( '<div>F is over</div>')
		return
	elif icode == IHALT or lst.regD['stat'] == 'HLT':
		cur.regD['stat'] = 'HLT'
		cur.regD['icode'] = IHALT
	else:
		cur.regD['stat'] = 'AOK'
		cur.regD['icode'] = icode
	
	if icode in [IRRMOVQ, IOPQ, IJXX]:
		cur.regD['ifun'] = int(InsCode[1], 16)
	else:
		cur.regD['ifun'] = 0
	
	if icode in [IRRMOVQ, IIRMOVQ, IRMMOVQ, IMRMOVQ, IOPQ, IPUSHQ, IPOPQ, IIADDQ]:
		cur.regD['rA'], cur.regD['rB'] = int(InsCode[2], 16), int(InsCode[3], 16)
	else:
		cur.regD['rA'], cur.regD['rB'] = RNONE, RNONE
	
	if icode in [IJXX, ICALL]:
		cur.regD['valC'] = int(rearrange(InsCode[2:18]), 16)
	elif icode in [IIRMOVQ, IRMMOVQ, IMRMOVQ, IIADDQ]:
		s = rearrange(InsCode[4:20])
		if s[0] in ['8','9','a','b','c','d','e','f']:
			cur.regD['valC'] = -1 * ((0xffffffffffffffff ^ int(rearrange(InsCode[4:20]), 16)) + 1)
		else:
			cur.regD['valC'] = int(rearrange(InsCode[4:20]), 16)
	else:
		cur.regD['valC'] = 0
		
	if icode in [IHALT, INOP, IRET]:
		cur.regD['valP'] = PC+1
	elif icode in [IRRMOVQ, IOPQ, IPUSHQ, IPOPQ]:
		cur.regD['valP'] = PC+2
	elif icode in [IJXX, ICALL]:
		cur.regD['valP'] = PC+9
	else:
		cur.regD['valP'] = PC+10
	
	if icode in [IRET, IHALT]:
		cur.regF['predPC'] = PC + 1
	elif icode in [IJXX, ICALL]:
		cur.regF['predPC'] = cur.regD['valC']
	else:
		cur.regF['predPC'] = cur.regD['valP']
		
	add_CR( '<div>F is over</div>')
