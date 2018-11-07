# -*- coding: UTF-8 -*-

'''
条件码
ZF, SF, OF三个bool类型变量，分别为零标志，符号标志，溢出标志

程序状态
stat为表示程序状态的字符串，共五种：
'AOK':正常操作
'HLT':处理器执行halt指令
'ADR':遇到非法地址
'INS':遇到非法指令
'BUB':bubble

'''

class ConditionCode:
	‘控制码’
	def __init__(self):
		self.ZF, self.SF, self.OF = 1, 0, 0


class Status:
	‘程序状态’
	def __init__(self):
		self.stat = 'AOK'
