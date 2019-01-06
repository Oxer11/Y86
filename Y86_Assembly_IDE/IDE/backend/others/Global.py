# -*- coding: UTF-8 -*-
import sys
import os
import math

o_path = os.getcwd() 
sys.path.append(o_path)

'''
定义CLK,提供修改和读取的接口
定义CMD_RESULTS,提供修改和读取的接口
定义THREAD_LIST,提供修改和读取的接口
'''
Hit_Type = -1
def set_Hit_Type(d):
	global Hit_Type
	Hit_Type = d

def get_Hit_Type():
	global Hit_Type
	return Hit_Type

CLK = 0
def get_CLK():
	global CLK
	return CLK
	
def add_CLK(d):
	global CLK
	CLK += d
	
def set_CLK(cycle):
	global CLK
	CLK = cycle

CMD_RESULTS = ''
def add_CR(s):
	global CMD_RESULTS
	CMD_RESULTS += s
	
def set_CR(s):
	global CMD_RESULTS
	CMD_RESULTS = s
	
def get_CR():
	global CMD_RESULTS
	return CMD_RESULTS
	
THREAD_LIST = ''
def add_THREAD(s):
	global THREAD_LIST
	THREAD_LIST += s

def init_THREAD():
	global THREAD_LIST
	THREAD_LIST = ''

def get_THREAD():
	global THREAD_LIST
	return THREAD_LIST
