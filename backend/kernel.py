# -*- coding: UTF-8 -*-

from memory import *
from register import *
from piperegister import *
from cc_stat import *
from Init import *
from Fetch import Fetch
from Decode import Decode
from Execute import Execute
from Memory import Memory_
from WriteBack import WriteBack


def Update(cur, lst):
	#P1代表处理ret，P2代表加载/使用冒险，P3代表预测错误的分支
	P1 = IRET in [lst.regD['icode'], lst.regE['icode'], lst.regM['icode']]
	P2 = (lst.regE['icode'] in [IMRMOVQ, IPOPQ]) and (lst.regE['dstM'] in [cur.regE['srcA'], cur.regE['srcB']])
	P3 = (lst.regE['icode'] == IJXX) and not cur.regM['Cnd']
	print P1,' ',P2,' ',P3
	#控制逻辑
	if not P1 and not P2: lst.write('F', cur.regF)
	
	if P2:
		pass
	elif P1 or P3:
		lst.write('D', {'stat':'BUB', 'icode':1, 'ifun':0, 'rA':RNONE, 'rB':RNONE, 'valC':0, 'valP':0})
	else:
		lst.write('D', cur.regD)
		
	if P2 or P3:
		lst.write('E', {'stat':'BUB', 'icode':1, 'ifun':0, 'valC':0, 'valA':0, 'valB':0, 'dstE':RNONE, 'dstM':RNONE, 'srcA':RNONE, 'srcB':RNONE})
	else:
		lst.write('E', cur.regE)
	
	lst.write('M', cur.regM)
	lst.write('W', cur.regW)

def UpdatePC(reg):
	if reg.regM['icode'] == IJXX and not reg.regM['Cnd']:
		f_pc = reg.regM['valA']
	elif reg.regW['icode'] == IRET:
		f_pc = reg.regW['valM']
	else:
		f_pc = reg.regF['predPC']
	return f_pc


mem = Memory()
InsCode = Init(mem) 
reg = Register()
pipereg = PipeRegister()
tmp_pipereg = PipeRegister()
CC = ConditionCode()
Stat = Status()
CLK = 0


PC, f_pc = 0, 0
while Stat.stat=='AOK' and CLK<=MAXCLOCK:
	print 'Current Time:',PC
	print 'Current Instruction:',InsCode[PC]
	tmp_pipereg = PipeRegister()
	WriteBack(pipereg, Stat, reg)
	Memory_(pipereg, tmp_pipereg, mem)
	CC = Execute(pipereg, tmp_pipereg, CC)
	print reg.reg
	#转发过程需要用到e_valE和m_valM，所以先执行Execute和Memory，实际电路中是同时执行的
	Decode(pipereg, tmp_pipereg, reg)
	Fetch(tmp_pipereg, InsCode[PC], PC)
	Update(cur=tmp_pipereg, lst=pipereg)
	PC = UpdatePC(pipereg)
	CLK += 1
	#缺少判断PC是否合法的过程
	
	print 'RegF:',pipereg.regF
	print 'RegD:',pipereg.regD
	print 'RegE:',pipereg.regE
	print 'RegM:',pipereg.regM
	print 'RegW:',pipereg.regW
	print ''
	
