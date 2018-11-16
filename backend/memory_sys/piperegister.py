# -*- coding: UTF-8 -*-
import sys
import os

o_path = os.getcwd() 
sys.path.append(o_path)


'''

流水线寄存器，共5个

用5个dictionary存储，支持write操作



write(Regid, NewReg)

更新Regid对应的寄存器的值为NewReg

Regid为'F','D','E','M','W'之一

NewReg为更新的dictionary

'''



from others.constant import *



class PipeRegister:

	'流水线寄存器'

	

	def __init__(self):

		self.regF = {'predPC':0}

		self.regD = {'stat':'AOK', 'icode':1, 'ifun':0, 'rA':RNONE, 'rB':RNONE, 'valC':0, 'valP':0}

		self.regE = {'stat':'AOK', 'icode':1, 'ifun':0, 'valC':0, 'valA':0, 'valB':0, 'dstE':RNONE, 'dstM':RNONE, 'srcA':RNONE, 'srcB':RNONE}

		self.regM = {'stat':'AOK', 'icode':1, 'Cnd':0, 'valE':0, 'valA':0, 'dstE':RNONE, 'dstM':RNONE}

		self.regW = {'stat':'AOK', 'icode':1, 'valE':0, 'valM':0, 'dstE':RNONE, 'dstM':RNONE}

		

	def write(self, Regid, NewReg):

		if Regid=='F':

			self.regF.update(NewReg)

		elif Regid=='D':

			self.regD.update(NewReg)

		elif Regid=='E':

			self.regE.update(NewReg)

		elif Regid=='M':

			self.regM.update(NewReg)

		elif Regid=='W':

			self.regW.update(NewReg)

		else:

			raise Exception("Invalid Regid: %c"%(Regid))

		return

	def get_ins(self):
		dic = {0x00:'halt', 0x10:'nop', 0x20:'rrmovq', 0x21:'cmovle', 0x22:'cmovl', 0x23:'cmove', 0x24:'cmovne',\
		0x25:'cmovge', 0x26:'cmovg', 0x30:'irmovq', 0x40:'rmmovq', 0x50:'mrmovq', 0x60:'addq', 0x61:'subq', 0x62:'andq',\
		0x63:'xorq', 0x70:'jmp', 0x71:'jle', 0x72:'jl', 0x73:'je', 0x74:'jne', 0x75:'jge', 0x76:'jg', 0x80:'call', 0x90:'ret',\
		0xA0:'pushq', 0xB0:'popq', 0xC0:'iaddq'}
		ins = []

		if self.regD['stat'] == 'INS':ins.append('<bad>')
		else: ins.append(dic[self.regD['icode']*16+self.regD['ifun']])
		if self.regE['stat'] == 'INS':ins.append('<bad>')
		else: ins.append(dic[self.regE['icode']*16+self.regE['ifun']])
		if self.regM['stat'] == 'INS':ins.append('<bad>')
		else: ins.append(dic[self.regM['icode']*16])
		if self.regW['stat'] == 'INS':ins.append('<bad>')
		else: ins.append(dic[self.regW['icode']*16])

		return ins

	def print_(self):
		dic_reg = {0:'%rax', 1:'%rcx', 2:'%rdx', 3:'%rbx', 4:'%rsp', 5:'%rbp', 6:'%rsi', 7:'%rdi', 8:'%r8', 9:'%r9', 10:'%r10',\
		11:'%r11', 12:'%r12', 13:'%r13', 14:'%14', 15:'----'}
		ins = self.get_ins()
		print 'F: predPC = %#x'%(self.regF['predPC'])
		print 'D: instr = %s, rA = %s, rB = %s, valC = %#x, valP = %#x, Stat = %s'%(ins[0], dic_reg[self.regD['rA']], \
		dic_reg[self.regD['rB']], self.regD['valC'], self.regD['valP'], self.regD['stat'])
		print 'E: instr = %s, valC = %#x, valA = %#x, valB = %#x'%(ins[1], self.regE['valC'], self.regE['valA'], self.regE['valB'])
		print 'srcA = %s, srcB = %s, dstE = %s, dstM = %s, Stat = %s'%(dic_reg[self.regE['srcA']], dic_reg[self.regE['srcB']], dic_reg[self.regE['dstE']], \
		dic_reg[self.regE['dstM']], self.regE['stat'])
		print 'M: instr = %s, Cnd = %d, valE = %#x, valA = %#x'%(ins[2], self.regM['Cnd'], self.regM['valE'], self.regM['valA'])
		print 'dstE = %s, dstM = %s, Stat = %s'%(dic_reg[self.regM['dstE']], dic_reg[self.regM['dstM']], self.regM['stat'])
		print 'W: instr = %s, valE = %#x, valM = %#x, dstE = %s, dstM = %s, Stat = %s'%(ins[3], self.regW['valE'], self.regW['valM'],\
		dic_reg[self.regW['dstE']], dic_reg[self.regW['dstM']], self.regW['stat'])



if __name__ == "__main__":

	print '测试PipeRegister类'

	reg = PipeRegister()

	reg.write('D', {'icode':1})

	reg.write('T', {'ifun':0})

	print reg.regD
