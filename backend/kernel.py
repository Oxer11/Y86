# -*- coding: UTF-8 -*-

from memory import *
from register import *
from piperegister import *
from cc_stat import *
from Init import *
from fetch import Fetch
from decode import Decode
from execute import Execute
from memory import Memory
from writeback import WriteBack


def Update(cur, lst):
	lst.write('F', cur.regF)
	lst.write('D', cur.regD)
	lst.write('E', cur.regE)
	lst.write('M', cur.regM)
	lst.write('W', cur,regW)

mem = Memory()
InsCode = {}
Init(InsCode, mem) 
reg = Register()
pipereg = PipeRegister()
tmp_pipereg = PipeRegister()
CC = ConditionCode()
Stat = Status()

PC = 0
while Stat.stat=='AOK':
	print 'Current Time:',PC
	tmp_pipereg = PipeRegister()
	Fetch(tmp_pipereg, InsCode[hex(PC)], PC)
	Decode(pipereg, tmp_pipereg, reg)
	Execute(pipereg, tmp_pipereg)
	Memory(pipereg, tmp_pipereg)
	WriteBack(pipereg, tmp_pipereg)
	PC = pipereg.regF['predPC']
	Update(cur=tmp_pipereg, lst=pipireg)
	print 'RegF:',reg.regF
	print 'RegD:',reg.regD
	print 'RegE:',reg.regE
	print 'RegM:',reg.regM
	print 'RegW:',reg.regW
	
	
