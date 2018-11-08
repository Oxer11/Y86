# -*- coding: UTF-8 -*-

from memory import *
from decoder import*


def Init(mem):
	'''
	InsCode为指令集dictionary，
	键为机器码的编号，是一个十六进制字符串
	值为机器码，是一个十六进制字符串
	Init函数，从output.txt文件中读取InsCode，并通过mem.write()操作，将机器码写入内存
	'''
	fname = "/home/linux-mia/Documents/pj/sim/y86-code/asum.yo"
	InsCode = decoder(fname)
	for a, i in InsCode.items():
		addr = int(a, 16)
		length = len(i)/2
		ins = int(i, 16)
		mem.write(addr, ins, length)


if __name__ == "__main__":
	mem = Memory()
	Init(mem)
	e, ins = mem.read(0x18)
	print e, hex(ins)
	e, ins = mem.read(0x42)
	print e, hex(ins)
