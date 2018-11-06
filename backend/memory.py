# -*- coding: UTF-8 -*-

'''
系统内存，大小为MEMORYSIZE
用list存储，每个位置代表4个bit，对应一位十六进制数，用字符串表示
支持read和write操作

read(addr)
读取内存中地址addr中存储的值，其中addr为一个十六进制整数
返回值为error,dataout，
当addr是合法地址时，error等于0；否则，error等于1
dataout是十六进制整数

write(addr, datain)
向内存中地址addr写入datain，其中addr，datain均为十六进制整数
返回值为error
当addr是合法地址时，error等于0；否则，error等于1

'''

from constant import *

class Memory:
	'系统内存'
	
	def __init__(self):
		self.mem = ['0']*MEMORYSIZE
		
	def	read(self, addr):
		error, dataout = 0, ''
		
		if (addr not in range(0,MEMORYSIZE)) or (addr+0xE not in range(0,MEMORYSIZE)):
			error = 1
			raise Exception("Invalid addr: [%d, %d)"%(addr, addr+8))
			
		else:
			for i in range(0,0xF,2):
				dataout = self.mem[addr+i]+self.mem[addr+i+1]+dataout
		
		return error, long(dataout, 16)
		
	def write(self, addr, datain):
		error = 0
		
		if (addr not in range(0,MEMORYSIZE)) or (addr+0xE not in range(0,MEMORYSIZE)):
			error = 1
			raise Exception("Invalid addr: [%d, %d)"%(addr, addr+8))
		
		else:
			for i in range(0,0xF,2):
				self.mem[addr+i:addr+i+1] = [hex(datain%256/16)[2], hex(datain%16)[2]]
				datain /= 256
		
		return error	
			
if __name__ == "__main__":
	print '测试Memory类'
	mem = Memory()
	mem.write(0x0, 0x0123456789abcdef)
	mem.write(-1, 0x0123456789abcdef)
	error, val = mem.read(0x8)
	print error, hex(val)
