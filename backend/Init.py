# -*- coding: UTF-8 -*-

from memory import *

def Init(InsCode, mem):
	'''
	InsCode为指令集dictionary，
	键为机器码的编号，是一个十六进制字符串
	值为机器码，是一个十六进制字符串
	Init函数，从output.txt文件中读取InsCode，并通过mem.write()操作，将机器码写入内存
	'''
	fi = open("output.txt", "r")
	
	fi.close()

