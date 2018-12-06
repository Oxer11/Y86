# -*- coding: UTF-8 -*-
import sys
import time
import os
sys.path.append("..")
from frontend.js.WriteCode import *
from frontend.js.WriteDisplay import *
from frontend.js.WriteReg import *
from frontend.js.WriteStack import *
from frontend.js.WriteStage import *
from frontend.js.WriteStat import *

from encoder.encoder import *
from memory_sys.memory import *
from memory_sys.register import *
from memory_sys.piperegister import *
from others.cc_stat import *
from others.Init import *
from others.Help import *
from stages.Fetch import Fetch
from stages.Decode import Decode
from stages.Execute import Execute
from stages.Memory import Memory_
from stages.WriteBack import WriteBack


def Update(cur, lst):
	#P1代表处理ret，P2代表加载/使用冒险，P3代表预测错误的分支
	P1 = IRET in [lst.regD['icode'], lst.regE['icode'], lst.regM['icode']]
	P2 = (lst.regE['icode'] in [IMRMOVQ, IPOPQ]) and (lst.regE['dstM'] in [cur.regE['srcA'], cur.regE['srcB']]) and lst.regD['stat'] == 'AOK' and not ((lst.regE['icode'] == IMRMOVQ) and (lst.regD['icode'] in [IRMMOVQ, IPUSHQ]))
	P3 = (lst.regE['icode'] == IJXX) and not cur.regM['Cnd']
	#print P1,' ',P2,' ',P3
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

def Step(MAXSTEP=1, breakpoints=[], OP=0):
	global PC, CC, Stat, CLK, NUM_INS, NUM_BUB
	dep, STEP = 0, 0
	while Stat.stat=='AOK' and STEP<MAXSTEP:
		if [PC,'y',1] in breakpoints:
			print 'Breakpoint %d, '%(breakpoints.index([PC,'y',1])+1)+hex(PC)
			break
		if (OP == 2) and (dep == -1): break
		print ''
		print 'Cycle %d. CC=Z=%d S=%d O=%d, Stat=%s'%(CLK, CC.ZF, CC.SF, CC.OF, Stat.stat)
		pipereg.print_()
		print ''
		if pipereg.regW['stat'] in ['HLT', 'INS', 'ADR']:
			Stat.stat = pipereg.regW['stat']
			break
		if pipereg.regW['icode'] == 8: dep += 1
		if pipereg.regW['icode'] == 9: dep -= 1
		WriteBack(pipereg, Stat, reg)
		Memory_(pipereg, tmp_pipereg, mem)
		CC, NUM_INS, NUM_BUB = Execute(pipereg, tmp_pipereg, CC, NUM_INS, NUM_BUB)
		#转发过程需要用到e_valE和m_valM，所以先执行Execute和Memory，实际电路中是同时执行的
		Decode(pipereg, tmp_pipereg, reg)
		Fetch(pipereg, tmp_pipereg, InsCode, PC)
		Update(cur=tmp_pipereg, lst=pipereg)
		PC = UpdatePC(pipereg)
		CLK += 1
		if (OP != 1) or (dep == 0): STEP += 1
		
	print reg.reg
	print 'CC.ZF=%d SF=%d OF=%d, Stat=%s'%(CC.ZF, CC.SF, CC.OF, Stat.stat)


def OUTPUT():
	ins_lst = pipereg.get_ins()
	WriteStage(pipereg,ins_lst)
	if NUM_INS !=0 : CPI = (NUM_INS+NUM_BUB+0.0)/NUM_INS
	else: CPI = 0.00 
	WriteStat(CLK, Stat.stat, CPI, CC.ZF, CC.SF, CC.OF)
	dis = []
	for i in range(0, len(Display)):
		sep = Display[i].find(' ')
		arg1 = Display[i][0:sep].strip()
		arg2 = Display[i][sep+1:len(Display[i])].strip()
		if arg1 == 'REG': 
			dis.append((arg2,hex(reg.reg[reg.map[arg2]])))
		if arg1 == 'MEM': 
			dis.append((arg2,hex(mem.read(int(arg2,16)))))
		if arg1 == 'STACK':
			dis.append((arg2,hex(mem.read(reg.reg[RRSP]-8*int(arg2,10)))))
	WriteDisplay(dis)
	WriteCode(Codes, PC)
	rsp, rbp = reg.read(4, 5)
	stack = {}
	for i in range(rsp, rbp+1, 8):
		stack.update({hex(i):hex(mem.read(i))})
	WriteStack(stack, rsp, rbp)
	REG = []
	for i in range(0, 0xF):
		val, V = reg.read(i, RNONE)
		REG.append((reg.map[i],hex(val)))
	WriteReg(REG)
	
def Welcome():
	print "==============================================================="
	print "|                                                             |"
	print "|                       Y86-simulator                         |"
	print "|                      Y86 Assembly IDE                       |"
	print "|                                                             |"
	print "|       Copyright (c) 2018 Xinyi Zhou and Zuobai Zhang        |"
	print "|                                                             |"
	print "==============================================================="


Welcome()	
Help('')

mem = Memory()
reg = Register()
pipereg = PipeRegister()
CC = ConditionCode()
Stat = Status()
tmp_pipereg = PipeRegister()
labels = {}
Codes = []
InsCode = {}
breakpoints = []
Display = []
CLK = 0
NUM_INS, NUM_BUB = 0, 0
PC, f_pc, maxPC = 0, 0, 0

#cmd = raw_input(">>>")
t = -1
lst_cmd = ''
while 1:
	time.sleep(0.05)
	lst_time=os.path.getmtime('../frontend/instruction.txt')
	if lst_time == t:
		OUTPUT()
		continue
	t=lst_time
	f_ins = open('../frontend/instruction.txt','r')
	lines = f_ins.readlines()
	f_ins.close()
	if len(lines)==0:
		OUTPUT()
		continue
	cmd = lines[-1]
	if cmd=='\n' : cmd = lst_cmd
	sep = cmd.find(' ')
	if sep == -1: sep = len(cmd)
	CMD = cmd[0:sep]
	CMD = CMD.strip()
	arg = cmd[sep:len(cmd)].strip()
	
	#Others
	if (CMD == 'clear') or (CMD == 'load'): 
		mem = Memory()
		reg = Register()
		pipereg = PipeRegister()
		CC = ConditionCode()
		Stat = Status()
		tmp_pipereg = PipeRegister()
		labels = {}
		Codes = []
		InsCode = {}
		breakpoints = []
		CLK = 0
		NUM_INS, NUM_BUB = 0, 0
		PC, f_pc, maxPC= 0, 0, 0
	
	if (CMD == 'q') or (CMD == 'quit'): break
	
	if (CMD == 'h') or (CMD == 'help'): Help(arg)
	
	if (CMD == 'set'):
		sep = arg.find(' ')
		arg1 = arg[0:sep].strip()
		arg2 = arg[sep+1:len(arg)].strip()
		sep = arg2.find(' ')
		arg3 = arg2[sep+1:len(arg)].strip()
		arg2 = arg2[0:sep].strip()
		if arg1 == 'REG': 
			reg.write(reg.map[arg2],int(arg3))
		if arg1 == 'MEM': 
			mem.write(int(arg2,16),int(arg3))
		if arg1 == 'STACK':
			mem.write(reg.reg[RRSP]-8*int(arg2,10),int(arg3))
	
	#Display
	if (CMD == 'display'): Display.append(arg)
	
	if (CMD == 'undisplay'): Display.remove(arg)
	
	#Step
	if (CMD == 's') or (CMD == 'step'): 
		if Stat.stat == 'NON': Stat.stat = 'AOK'
		if len(arg) == 0: Step()
		else: Step(int(arg,10))
		
	if (CMD == 'n') or (CMD == 'next'): 
		if Stat.stat == 'NON': Stat.stat = 'AOK'
		if len(arg) == 0: Step(OP = 1)
		else: Step(int(arg,10), OP = 1)	
		
	if (CMD == 'c') or (CMD == 'continue'): 
		if Stat.stat == 'NON': Stat.stat = 'AOK'
		Step(MAXCLOCK, breakpoints)
	
	if (CMD == 'finish'):
		if Stat.stat == 'NON': Stat.stat = 'AOK'
		Step(MAXCLOCK, OP = 2)
		
	#Jump
	if (CMD == 'j') or (CMD == 'jump'):
		pipereg = PipeRegister()
		if labels.has_key(arg): PC = int(labels[arg],16)
		else: PC = int(arg,16)
		
	if (CMD == 'return'):
		pipereg = PipeRegister()
		rsp, rnone = reg.read(RRSP, RNONE)
		addr = mem.read(rsp)
		reg.write(RRSP, rsp+8)
		PC = addr
	
	if (CMD == 'call'):
		if labels.has_key(arg): addr = int(labels[arg],16)
		else: addr = int(arg,16)
		pipereg = PipeRegister()
		rsp, rnone = reg.read(RRSP, RNONE)
		rsp -= 8 
		mem.write(rsp, PC)
		reg.write(RRSP, rsp)
		PC = addr
	
	#Breakpoints
	
	if (CMD == 'b') or (CMD == 'break'):
		if labels.has_key(arg): breakpoints.append([int(labels[arg],16),'y',1])
		else: breakpoints.append([int(arg,16),'y',1])
		print 'Breakpoint %d at '%(len(breakpoints)) + arg
	
	if (CMD == 'info') and (arg == 'breakpoints'):
		print 'Num'.ljust(8)+'Type'.ljust(15)+'Enb'.ljust(4)+'Address'
		for i in range(0,len(breakpoints)):
			if breakpoints[i][2]!=0:
				print str(i+1).ljust(8)+'breakpoint'.ljust(15)+breakpoints[i][1].ljust(4)+hex(breakpoints[i][0])
				
	if (CMD == 'enable'): 
		if len(arg) == 0:
			for i in range(0,len(breakpoints)):
				breakpoints[i][1] = 'y'
		else: breakpoints[int(arg,10)-1][1] = 'y'
	if (CMD == 'disable'): 
		if len(arg) == 0:
			for i in range(0,len(breakpoints)):
				breakpoints[i][1] = 'n'
		else: breakpoints[int(arg,10)-1][1] = 'n'
	if (CMD == 'delete'): 
		if len(arg) == 0:
			for i in range(0,len(breakpoints)):
				breakpoints[i][2] = 0
		else: breakpoints[int(arg,10)-1][2] = 0

	#I/O
	if (CMD == 'w') or (CMD == 'write'):
		fout = arg
		fo = open(fout, "w")
		for line in Codes:
			fo.write(line.rstrip()+"\n")
		fo.close()
	
	if (CMD == 'list'):
		for line in Codes:
			print line.rstrip()
	
	if (CMD == 'load'):
		if arg[len(arg)-3:len(arg)] == '.yo':
			fname = arg
			InsCode = Init(mem, fname) 
			with open(fname) as fi:
				for line in fi:
					Codes.append(line.rstrip())
			for addr, ins in InsCode.items():
				length = len(ins)/2
				mem.load(addr, ins, length)
				if addr + length > maxPC: maxPC = addr + length
					
		elif arg[len(arg)-3:len(arg)] == '.ys':
			AssemblyCode = []
			fname = arg
			with open(fname) as fi:
				for line in fi:
					AssemblyCode.append(line.rstrip())
			new_Codes, maxPC = encoder(AssemblyCode, labels, maxPC)
			Codes.extend(new_Codes)
			for line in new_Codes:
				beg = line.find(":")
				end = line.find("|")
				if beg == -1: continue
				if end == -1: end = len(line)
				addr = line[0:beg]
				ins = line[beg + 1:end]
				ins = ins.strip()
				if len(ins) == 0: continue
				InsCode[int(addr,16)] = ins
				length = len(ins)/2
				mem.load(int(addr,16), ins, length)
		else:
			print "Please input an address of .yo/.ys file."
	
	if (CMD == 'read'):
		AssemblyCode = []
		ins = raw_input()
		while (len(ins) > 0):
			AssemblyCode.append(ins)
			ins = raw_input()

		new_Codes, maxPC = encoder(AssemblyCode, labels, maxPC)
		Codes.extend(new_Codes)
		for line in new_Codes:
			beg = line.find(":")
			end = line.find("|")
			if beg == -1: continue
			if end == -1: end = len(line)
			addr = line[0:beg]
			ins = line[beg + 1:end]
			ins = ins.strip()
			if len(ins) == 0: continue
			InsCode[int(addr,16)] = ins
			length = len(ins)/2
			mem.load(int(addr,16), ins, length)
	
	OUTPUT()
	
	lst_cmd = cmd	
	#cmd = raw_input(">>>")
	
	
