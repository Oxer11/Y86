# -*- coding: UTF-8 -*-

class ConditionCode:
	‘控制码’
	def __init__(self):
		self.ZF, self.SF, self.OF = 1, 0, 0


class Status:
	‘程序状态’
	def __init__(self):
		self.stat = 'AOK'
