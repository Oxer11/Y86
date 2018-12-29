# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import sys
sys.path.append("./IDE/backend")

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
from others.Global import *
from js.WriteCode import WriteCode
from js.WriteStat import WriteStat
from js.WriteStage import WriteStage
from js.WriteDisplay import WriteDisplay
from js.WriteStack import WriteStack
from js.WriteReg import WriteReg

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
	global PC, CC, Stat, NUM_INS, NUM_BUB
	dep, STEP = 0, 0
	while Stat.stat=='AOK' and STEP<MAXSTEP:
		if [PC,'y',1] in breakpoints:
			print 'Breakpoint %d, '%(breakpoints.index([PC,'y',1])+1)+hex(PC)
			break
		if (OP == 2) and (dep == -1): break
		print ''
		print 'Cycle %d. CC=Z=%d S=%d O=%d, Stat=%s'%(get_CLK(), CC.ZF, CC.SF, CC.OF, Stat.stat)
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
		add_CLK(1)
		if (OP != 1) or (dep == 0): STEP += 1
		
	print reg.reg
	print 'CC.ZF=%d SF=%d OF=%d, Stat=%s'%(CC.ZF, CC.SF, CC.OF, Stat.stat)


def OUTPUT(results):

	results.update({"Codes":WriteCode(Codes, PC)})
	
	ins_lst = pipereg.get_ins()
	results.update({"Stage":WriteStage(pipereg, ins_lst)})
	
	if NUM_INS !=0 : CPI = (NUM_INS+NUM_BUB+0.0)/NUM_INS
	else: CPI = 0.00 
	results.update({"Stat":WriteStat(get_CLK(), Stat.stat, CPI, CC.ZF, CC.SF, CC.OF)})
	
	dis = []
	for i in range(0, len(Display)):
		sep = Display[i].find(' ')
		arg1 = Display[i][0:sep].strip()
		arg2 = Display[i][sep+1:len(Display[i])].strip()
		if arg1 == 'REG': 
			dis.append((arg2,hex(reg.reg[reg.map[arg2]])))
		if arg1 == 'MEM': 
			dis.append((arg2,hex(mem.display(int(arg2,16)))))
		if arg1 == 'STACK':
			dis.append((arg2,hex(mem.display(reg.reg[RRSP]-8*int(arg2,10)))))
	results.update({"Display":WriteDisplay(dis)})
	
	rsp, rbp = reg.read(4, 5)
	stack = {}
	for i in range(rsp, rbp+1, 8):
		stack.update({hex(i):hex(mem.display(i))})
	results.update({"Stack":WriteStack(stack, rsp, rbp)})
	
	REG = []
	for i in range(0, 0xF):
		val, V = reg.read(i, RNONE)
		REG.append((reg.map[i],hex(val)))
	results.update({'Register':WriteReg(REG)})
	


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
CMD_RESULTS = ""
NUM_INS, NUM_BUB = 0, 0
PC, f_pc, maxPC = 0, 0, 0
	
@csrf_exempt
def index(request):
#print request.method
#	print request.POST
	global mem, reg, pipereg, CC, Stat, tmp_pipereg, labels, Codes, InsCode, breakpoints, NUM_INS, NUM_BUB, PC, f_pc, maxPC
	if request.method == 'GET':
		return render(request, 'IDE/main.html', {})
	elif request.method == 'POST':
		results = {}
		CMD_RESULTS = ""
		if request.POST.get("type") == 'code':
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
			set_CLK(0)
			NUM_INS, NUM_BUB = 0, 0
			PC, f_pc, maxPC= 0, 0, 0
			AssemblyCode = request.POST.get("content").encode('ascii')
			AssemblyCode = AssemblyCode.split('\n')
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
			Code = ""
			for line in Codes:
				Code = Code + line.rstrip() + "\n"
			results.update({'Code':Code})
		
		elif request.POST.get("type") == 'command':
			cmd = request.POST.get("content").encode('ascii')
			cmd = cmd.strip()
			CMD_RESULTS = "<div>" + cmd 
			if len(cmd)==0 : cmd = lst_cmd
			sep = cmd.find(' ')
			if sep == -1: sep = len(cmd)
			CMD = cmd[0:sep]
			arg = cmd[sep:len(cmd)].strip()
			
			#Others
			if (CMD == 'clear'): 
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
				set_CLK(0)
				NUM_INS, NUM_BUB = 0, 0
				PC, f_pc, maxPC= 0, 0, 0
	
	
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
				if arg1 == 'CACHE':
					sep=arg3.find(' ')
					arg4=arg3[sep+1:].strip()
					arg3=arg3[0:sep].strip()
					if mem.set_cacfg(int(arg2),int(arg3),int(arg4))==1:
						CMD_RESULTS = CMD_RESULTS + "<div>Invalid S,B or E</div>"
	
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
				addr = mem.display(rsp)
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
				CMD_RESULTS = CMD_RESULTS + "<div>" + 'Breakpoint %d at '%(len(breakpoints)) + arg + "</div>"
	
			if (CMD == 'info') and (arg == 'breakpoints'):
				CMD_RESULTS = CMD_RESULTS + "<div>" + 'Num'.ljust(8)+'Type'.ljust(15)+'Enb'.ljust(4)+'Address' + "</div>"
				for i in range(0,len(breakpoints)):
					if breakpoints[i][2]!=0:
						CMD_RESULTS = CMD_RESULTS + "<div>" + str(i+1).ljust(8)+'breakpoint'.ljust(15)+breakpoints[i][1].ljust(4)+hex(breakpoints[i][0]) + "</div>"
				
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
			
			lst_cmd = cmd	
		
		print 'miss,hit:',mem.get_hm()
		OUTPUT(results)
		CMD_RESULTS = CMD_RESULTS + "</div>"
		results.update({"CMD":CMD_RESULTS})
		return JsonResponse(results)
   	return ""
