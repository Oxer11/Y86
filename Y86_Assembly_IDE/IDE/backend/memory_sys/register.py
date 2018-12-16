# -*- coding: UTF-8 -*-
import sys
import os

o_path = os.getcwd() 
sys.path.append(o_path)

'''
系统寄存器，共16个
用list存储，支持read和write操作

read(srcA, srcB)
读取srcA和srcB寄存器中的值，其中srcA和srcB分别为寄存器标识符，RNONE代表空寄存器
返回值为valA,valB两个整型变量

write(dstW, valW)
向寄存器dstW中写入值valW，其中dstW为寄存器标识符，RNONE代表空寄存器，valW为整型变量
无返回值
'''

from others.constant import *

class Register:
	'系统寄存器'
	
	def __init__(self):
		self.reg = [0]*0xF
		self.map = {0:'%rax', 1:'%rcx', 2:'%rdx', 3:'%rbx', 4:'%rsp', 5:'%rbp', 6:'%rsi', 7:'%rdi', 8:'%r8', 9:'%r9', 10:'%r10', 11:'%r11', 12:'%r12', 13:'%r13', 14:'%r14', 15:'%rnone', '%rax':0, '%rcx':1, '%rdx':2, '%rbx':3, '%rsp':4, '%rbp':5, '%rsi':6, '%rdi':7, '%r8':8, '%r9':9, '%r10':10, '%r11':11, '%r12':12, '%r13':13, '%r14':14, '%rnone':15}
	
	def read(self, srcA, srcB):
	
		if (srcA not in range(0,0x10)):
			raise Exception("Invalid srcA: %d"%(srcA))
		if (srcB not in range(0,0x10)):
			raise Exception("Invalid srcB: %d"%(srcB))
			
		valA, valB = 0, 0
		if (srcA != RNONE):
			valA = self.reg[srcA]
		if (srcB != RNONE):
			valB = self.reg[srcB]
		return valA, valB
		
	def write(self, dstW, valW):
	
		if (dstW not in range(0,0x10)):
			raise Exception("Invalid dstW: %d"%(dstW))
			
		if (dstW != RNONE):
			self.reg[dstW] = valW
		return

if __name__ == "__main__":
	print '测试register类'
	reg = Register()
	reg.write(0x1, 19990611)
	reg.write(0x2, 19990610)
	val = reg.read(0x1, 0x20)
	print reg.reg
