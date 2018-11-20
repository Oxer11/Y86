# -*- coding: UTF-8 -*-

from encoder.encoder import *
from memory_sys.memory import *
from memory_sys.register import *
from memory_sys.piperegister import *
from others.cc_stat import *
from others.Init import *
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

def Step(MAXCLOCK, breakpoint={}):
	global PC, CC, Stat, CLK
	while Stat.stat=='AOK' and CLK<MAXCLOCK:
		if breakpoint.has_key(PC):
			print 'Breakpoint '+hex(PC)
			break
		print ''
		print 'Cycle %d. CC=Z=%d S=%d O=%d, Stat=%s'%(CLK, CC.ZF, CC.SF, CC.OF, Stat.stat)
		pipereg.print_()
		print ''
		if pipereg.regW['stat'] in ['HLT', 'INS', 'ADR']:
			Stat.stat = pipereg.regW['stat']
			break

		WriteBack(pipereg, Stat, reg)
		Memory_(pipereg, tmp_pipereg, mem)
		CC = Execute(pipereg, tmp_pipereg, CC)
		#转发过程需要用到e_valE和m_valM，所以先执行Execute和Memory，实际电路中是同时执行的
		Decode(pipereg, tmp_pipereg, reg)
		Fetch(pipereg, tmp_pipereg, InsCode, PC)
		Update(cur=tmp_pipereg, lst=pipereg)
		PC = UpdatePC(pipereg)
		CLK += 1
	print reg.reg
	print 'CC.ZF=%d SF=%d OF=%d, Stat=%s'%(CC.ZF, CC.SF, CC.OF, Stat.stat)
	
	
print 'If you want to input a .yo file, please input 1'
print 'If you want to input a .ys file, please input 2'
print 'If you want to execute interactively, please input 3'
mode = raw_input()

mem = Memory()
reg = Register()
pipereg = PipeRegister()
CC = ConditionCode()
Stat = Status()
tmp_pipereg = PipeRegister()
labels = {}
Codes = []
InsCode = {}
breakpoint = {}
CLK = 0
PC, f_pc, maxPC= 0, 0, 0

if mode == '1':
	print 'Please input the address of the .yo file'
	fname = raw_input()
	InsCode = Init(mem, fname) 
	with open(fname) as fi:
		for line in fi:
			Codes.append(line)
	for addr, ins in InsCode.items():
		length = len(ins)/2
		mem.load(addr, ins, length)
		if addr + length > maxPC:
			maxPC = addr + length

elif mode == '2':
	print 'Please input the address of the .ys file'
	fname = raw_input()
	AssemblyCode = []
	i = 0
	with open(fname) as fi:
		for line in fi:
			AssemblyCode.append(line)
			i += 1
	Codes, maxPC = encoder(AssemblyCode, labels, maxPC)
	fout = fname[0:len(fname)-2] + 'yo'
	fo = open(fout, "w")
	i = 0
	for line in AssemblyCode:
		fo.write(Codes[i])
		i += 1
	fo.close()
	InsCode = Init(mem, fout)
	
print 'Please input your commands.'
cmd = raw_input(">>")
while 1:
	if cmd[0] == '-':
		if cmd == '-quit': break
		if cmd == '-step': 
			if Stat.stat == 'NON': Stat.stat = 'AOK'
			Step(CLK+1)
		if cmd == '-continue': 
			if Stat.stat == 'NON': Stat.stat = 'AOK'
			Step(MAXCLOCK, breakpoint)
		if cmd[0:6] == '-break':
			breakpoint.update({int(cmd[6:len(cmd)].strip(),16):1})
			print 'Breakpoint '+ cmd[6:len(cmd)].strip()
		if cmd == '-show':
			for line in Codes:
				print line.rstrip()
	else:
		AssemblyCode = []
		while (len(cmd) > 0):
			AssemblyCode.append(cmd)
			cmd = raw_input()

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
		
	cmd = raw_input(">>")
	
	
