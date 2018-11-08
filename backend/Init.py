# -*- coding: UTF-8 -*-

from memory import *
from decoder import *


def Init(mem):
	'''
	InsCode为指令集dictionary，
	键为机器码的编号，是一个十六进制整数
	值为机器码，是一个十六进制字符串
	Init函数，从output.txt文件中读取InsCode，并通过mem.write()操作，将机器码写入内存
	'''
	fname = "/home/oxer/ICS/project/Y86/backend/test/asum.yo"
	InsCode = decoder(fname)
	for addr, i in InsCode.items():
		length = len(i)/2
		ins = int(i, 16)
		mem.write(addr, ins, length)
	return InsCode


if __name__ == "__main__":
	mem = Memory()
	InsCode = {}
	Init(mem)
	e, ins = mem.read(0x18)
	print e, hex(ins)
	e, ins = mem.read(0x42)
	print e, hex(ins)
