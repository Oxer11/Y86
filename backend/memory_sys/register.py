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
