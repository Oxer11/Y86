# -*- coding: UTF-8 -*-

import sys
import os

o_path = os.getcwd() 
sys.path.append(o_path)

'''
系统内存，大小为MEMORYSIZE，指令码存储在[insbeg, insend)地址中
用list存储，每个位置代表1个byte，对应两位十六进制数，用字符串表示
支持read和write操作
read(addr)
读取内存中地址addr中存储的值，其中addr为一个十六进制整数
返回值为dataout
dataout是十六进制整数
write(addr, datain)
向内存中地址addr写入datain，其中addr，datain均为十六进制整数
'''

from others.constant import *
from others.Global import*

miss, hit = 0, 0
s=2
b=6
t=4
S=4
B=64
E=4
class Memory:
	'系统内存'
	
	def __init__(self):
		global miss,hit,S,B,E,s,b,t
		
		miss, hit = 0, 0
		self.main_m = ['00']*MEMORYSIZE
		self.cache_m=[[{'lst':0,'write':0,'valid':0,'tag':0,'block':['00']*B} for i in range(0,E)] for j in range(0,S)]
		#self.insbeg = -1
		#self.insend = -1
		
	def	read(self, addr):
		global miss,hit,S,B,E,s,b,t
		dataout = ''
		
		if (addr not in range(0,MEMORYSIZE)) or (addr+7 not in range(0,MEMORYSIZE)):
			raise Exception("Invalid addr: [%d, %d)"%(addr, addr+8))
		else:
			si=(addr>>b)%(1<<s)
			bo=addr%(1<<b)
			t=addr>>(s+b)
			
			i=0
			while i<E:
				if self.cache_m[si][i]['tag']==t and self.cache_m[si][i]['valid']==1:
					break
				i+=1
			#hit	
			if i<E:
				add_CLK(VISIT_C)
				hit += 1
				add_CR("<div>Hit when read "+hex(addr)+"</div>")
				self.cache_m[si][i]['lst']=get_CLK()
				for j in range(0,8):
					dataout = self.cache_m[si][i]['block'][bo+j]+dataout
			#miss
			else:
				add_CLK(VISIT_M)
				miss += 1
				add_CR("<div>Miss when read "+hex(addr)+"</div>")
				min_id=0
				min=MAXCLOCK
				i=0
				while i<E:
					if self.cache_m[si][i]['valid']==0:
						break
					else:
						if self.cache_m[si][i]['lst']<min:
							min_id=i
							min=self.cache_m[si][i]['lst']
					i+=1
				
				if i==E:
					i=min_id
					
				if self.cache_m[si][i]['write'] == 1 and self.cache_m[si][i]['valid'] == 1:
					w_addr = (self.cache_m[si][i]['tag']<<s+si)<<b
					for j in range(0,B):
						self.main_m[w_addr+j] = self.cache_m[si][i]['block'][j]
				
				for j in range(0,B):
					self.cache_m[si][i]['block'][j] = self.main_m[addr-bo+j]
				self.cache_m[si][i]['write'] = 0
				self.cache_m[si][i]['tag'] = t
				self.cache_m[si][i]['valid'] = 1
				self.cache_m[si][i]['lst']=get_CLK()
				
				for j in range(0,8):
					dataout = self.cache_m[si][i]['block'][bo+j]+dataout
		
		if dataout[0] in ['8','9','a','b','c','d','e','f']:
			ret = -1 * ((0xffffffffffffffff ^ long(dataout, 16)) + 1)
		else:
			ret = long(dataout, 16)
		
		return ret
		
	def write(self, addr, datain, length = 8):	
		global miss,hit,S,B,E,s,b,t
		if (addr not in range(0,MEMORYSIZE)) or (addr+length-1 not in range(0,MEMORYSIZE)):
			raise Exception("Invalid addr: [%d, %d)"%(addr, addr+8))
		
		else:
			si=(addr>>b)%(1<<s)
			bo=addr%(1<<b)
			t=addr>>(s+b)
			
			i=0
			while i<E:
				if self.cache_m[si][i]['tag']==t and self.cache_m[si][i]['valid']==1:
					break
				i+=1
			#hit
			if i<E:
				add_CLK(VISIT_C)
				hit += 1
				add_CR("<div>Hit when write to "+hex(addr)+"</div>")
				for j in range(0,length):
					self.cache_m[si][i]['block'][bo+j] = hex(datain%256/16)[2]+hex(datain%16)[2]
					datain /= 256
				self.cache_m[si][i]['write'] = 1
				self.cache_m[si][i]['lst']=get_CLK()
			#miss
			else:
				add_CLK(VISIT_M)
				miss += 1
				add_CR("<div>Miss when write to "+hex(addr)+"</div>")
				min_id=0
				min=MAXCLOCK
				i=0
				while i<E:
					if self.cache_m[si][i]['valid']==0:
						break
					else:
						if self.cache_m[si][i]['lst']<min:
							min_id=i
							min=self.cache_m[si][i]['lst']
					i+=1
				
				if i==E:
					i=min_id
					
				if self.cache_m[si][i]['write'] == 1 and self.cache_m[si][i]['valid'] == 1:
					w_addr = (self.cache_m[si][i]['tag']<<s+si)<<b
					for j in range(0,B):
						self.main_m[w_addr+j] = self.cache_m[si][i]['block'][j]
						
				for j in range(0,B):
					self.cache_m[si][i]['block'][j] = self.main_m[addr-bo+j]
				self.cache_m[si][i]['write'] = 1
				self.cache_m[si][i]['tag'] = t
				self.cache_m[si][i]['valid'] = 1
				self.cache_m[si][i]['lst']=get_CLK()
				for j in range(0,length):
					self.cache_m[si][i]['block'][bo+j] = hex(datain%256/16)[2]+hex(datain%16)[2]
					datain /= 256
	
	def load(self, addr, datain, length = 8):
		if (addr not in range(0,MEMORYSIZE)) or (addr+length-1 not in range(0,MEMORYSIZE)):
			raise Exception("Invalid addr: [%d, %d)"%(addr, addr+8))
		else:
			for i in range(0,length):
				self.main_m[addr+i] = datain[2*i]+datain[2*i+1]
	
	def display(self, addr):
		global miss,hit,S,B,E,s,b,t
		dataout = ''
		
		if (addr not in range(0,MEMORYSIZE)) or (addr+7 not in range(0,MEMORYSIZE)):
			raise Exception("Invalid addr: [%d, %d)"%(addr, addr+8))
		else:
			si=(addr>>b)%(1<<s)
			bo=addr%(1<<b)
			t=addr>>(s+b)
			
			i=0
			while i<E:
				if self.cache_m[si][i]['tag']==t and self.cache_m[si][i]['valid']==1:
					break
				i+=1
			#hit
			if i<E:
				for j in range(0,8):
					dataout = self.cache_m[si][i]['block'][bo+j]+dataout
			#miss
			else:				
				for j in range(0,8):
					dataout = self.main_m[addr+j]+dataout
		
		if dataout[0] in ['8','9','a','b','c','d','e','f']:
			ret = -1 * ((0xffffffffffffffff ^ long(dataout, 16)) + 1)
		else:
			ret = long(dataout, 16)
		return ret
	
	def get_hm(self):
		global hit
		global miss
		return hit,miss
	
	def set_cacfg(self,S_,B_,E_):
		global S,B,E,s,b,t
		if S_<=0 or B_<=0 or E_<=0:
			return 1
		temp_s=math.log(S_,2)
		temp_b=math.log(B_,2)
		if temp_s==int(temp_s) and temp_b==int(temp_b) and temp_b>2 and temp_s>0 and temp_s+temp_b<12:
			s=int(temp_s)
			b=int(temp_b)
			t=12-s-b
			S=S_
			B=B_
		else:
			return 1
	
		if E_<=1<<t:
			E=E_
		else:
			E=1<<t
			
		self.cache_m=[[{'lst':0,'write':0,'valid':0,'tag':0,'block':['00']*B} for i in range(0,E)] for j in range(0,S)]
	
		return 0
	
	def valid(self,addr):
		return (addr in range(0,MEMORYSIZE)) and (addr+7 in range(0,MEMORYSIZE)) #and not (addr in range(self.insbeg, self.insend)) and not (addr+7 in range(self.insbeg, self.insend))
			
if __name__ == "__main__":
	print '测试Memory类'
	main_m = Memory()
	main_m.write(0x0, 0x0123456789abcdef)
	main_m.write(0x8, 0x0123456789abcdef)
	error, val = main_m.read(0x4)
	print error, hex(val)
