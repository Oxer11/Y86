# -*- coding: UTF-8 -*-
import sys
import os
import math

o_path = os.getcwd() 
sys.path.append(o_path)

'''
定义CLK,提供修改和读取的接口
'''

CLK=0
def get_CLK():
	return CLK
	
def add_CLK(d):
	global CLK
	CLK += d
	
def set_CLK(cycle):
	global CLK
	CLK=cycle