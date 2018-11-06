# -*- coding: UTF-8 -*-

'''
流水线寄存器，共5个
用5个dictionary存储，支持write操作

write(Regid, NewReg)
更新Regid对应的寄存器的值为NewReg
Regid为'F','D','E','M','W'之一
NewReg为更新的dictionary
'''

from constant import *

class PipeRegister:
	'流水线寄存器'
	
	def __init__(self):
		self.regF = {'predPC':0}
		self.regD = {'stat':'AOK', 'icode':0, 'ifun':0, 'rA':0xF, 'rB':0xF, 'valC':0, 'valP':0}
		self.regE = {'stat':'AOK', 'icode':0, 'ifun':0, 'valC':0, 'valA':0, 'valB':0, 'dstE':0, 'dstM':0, 'srcA':0, 'srcB':0}
		self.regM = {'stat':'AOK', 'icode':0, 'Cnd':0, 'valE':0, 'valA':0, 'dstE':0, 'dstM':0}
		self.regW = {'stat':'AOK', 'icode':0, 'valE':0, 'valA':0, 'dstE':0, 'dstM':0}
		
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

if __name__ == "__main__":
	print '测试PipeRegister类'
	reg = PipeRegister()
	reg.write('D', {'icode':1})
	reg.write('T', {'ifun':0})
	print reg.regD
