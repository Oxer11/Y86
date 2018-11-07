# -*- coding: UTF-8 -*-

from memory import *
from register import *
from piperegister import *
from cc_stat import *
from Init import *
from Fetch import Fetch
from Decode import Decode
from Execute import Execute
from Memory import Memory
from WriteBack import WriteBack


def Update(cur, lst):
	lst.write('F', cur.regF)
	lst.write('D', cur.regD)
	lst.write('E', cur.regE)
	lst.write('M', cur.regM)
	lst.write('W', cur,regW)

def UpdatePC(reg, f_pc):
	if reg.regM['icode'] == IJXX && !reg.regM['Cnd']:
		f_pc = reg.regM['valA']
	elif reg.regW['icode'] == IRET:
		f_pc = reg.regW['valM']
	else:
		f_pc = reg.regF['predPC']


mem = Memory()
InsCode = {}
Init(InsCode, mem) 
reg = Register()
pipereg = PipeRegister()
tmp_pipereg = PipeRegister()
CC = ConditionCode()
Stat = Status()

PC, f_pc = 0, 0
while Stat.stat=='AOK':
	print 'Current Time:',PC
	tmp_pipereg = PipeRegister()
	Fetch(tmp_pipereg, InsCode[hex(PC)], PC)
	Execute(pipereg, tmp_pipereg)
	Memory(pipereg, tmp_pipereg, mem)
	#转发过程需要用到e_valE和m_valM，所以先执行Execute和Memory，实际电路中是同时执行的
	Decode(pipereg, tmp_pipereg, reg)
	WriteBack(pipereg, Stat, reg)
	UpdatePC(pipereg, f_pc)
	Update(cur=tmp_pipereg, lst=pipireg)
	PC = f_pc
	'''
	判断PC是否合法
	'''
	print 'RegF:',reg.regF
	print 'RegD:',reg.regD
	print 'RegE:',reg.regE
	print 'RegM:',reg.regM
	print 'RegW:',reg.regW
	
	
