# -*- coding: UTF-8 -*-
import sys
import os

o_path = os.getcwd() 
sys.path.append(o_path)

from memory_sys.memory import *
from decoder import *


def Init(mem, fname):
	'''
	InsCode为指令集dictionary，
	键为机器码的编号，是一个十六进制整数
	值为机器码，是一个十六进制字符串
	Init函数，从fname文件中读取InsCode，并通过mem.write()操作，将机器码写入内存
	'''
	InsCode = decoder(fname)
	for addr, ins in InsCode.items():
		length = len(ins)/2
		mem.load(addr, ins, length)
		#if mem.insbeg == -1:
		#	mem.insbeg = addr
		#mem.insend = addr + length
	return InsCode


if __name__ == "__main__":
	mem = Memory()
	InsCode = {}
	Init(mem)
	e, ins = mem.read(0x18)
	print e, hex(ins)
	e, ins = mem.read(0x42)
	print e, hex(ins)
