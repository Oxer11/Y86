# -*- coding: UTF-8 -*-

'''
系统内存，大小为MEMORYSIZE
用list存储，每个位置代表1个byte，对应两位十六进制数，用字符串表示
支持read和write操作
read(addr)
读取内存中地址addr中存储的值，其中addr为一个十六进制整数
返回值为dataout
dataout是十六进制整数
write(addr, datain)
向内存中地址addr写入datain，其中addr，datain均为十六进制整数
'''

from constant import *

class Memory:
	'系统内存'
	
	def __init__(self):
		self.mem = ['00']*MEMORYSIZE
		
	def	read(self, addr):
		dataout = ''
		
		if (addr not in range(0,MEMORYSIZE)) or (addr+7 not in range(0,MEMORYSIZE)):
			raise Exception("Invalid addr: [%d, %d)"%(addr, addr+8))
			
		else:
			for i in range(0,8):
				dataout = self.mem[addr+i]+dataout
		
		return long(dataout, 16)
		
	def write(self, addr, datain, length = 8):
		
		if (addr not in range(0,MEMORYSIZE)) or (addr+length-1 not in range(0,MEMORYSIZE)):
			raise Exception("Invalid addr: [%d, %d)"%(addr, addr+8))
		
		else:
			for i in range(0,length):
				self.mem[addr+i] = hex(datain%256/16)[2]+hex(datain%16)[2]
				datain /= 256
	
	def load(self, addr, datain, length = 8):
		if (addr not in range(0,MEMORYSIZE)) or (addr+length-1 not in range(0,MEMORYSIZE)):
			raise Exception("Invalid addr: [%d, %d)"%(addr, addr+8))
		
		else:
			for i in range(0,length):
				self.mem[addr+i] = datain[2*i]+datain[2*i+1]
				
			
if __name__ == "__main__":
	print '测试Memory类'
	mem = Memory()
	mem.write(0x0, 0x0123456789abcdef)
	mem.write(0x8, 0x0123456789abcdef)
	error, val = mem.read(0x4)
	print error, hex(val)
