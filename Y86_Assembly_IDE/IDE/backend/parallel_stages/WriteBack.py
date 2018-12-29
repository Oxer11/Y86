# -*- coding: UTF-8 -*-
import sys
import os

o_path = os.getcwd() 
sys.path.append(o_path)

from others.cc_stat import *
from memory_sys.register import *
from memory_sys.piperegister import *


def WriteBack(lst, Stat, reg):
	print 'W starts'
	
	if lst.regW['stat'] == 'BUB':
		Stat.stat = 'AOK'
	else:
		Stat.stat = lst.regW['stat']

	if Stat.stat != 'AOK':
		print 'W is over'
		return
    
	reg.write(lst.regW['dstE'], lst.regW['valE'])
	reg.write(lst.regW['dstM'], lst.regW['valM'])
	
	print 'W is over'


if __name__ == "__main__":
    pipereg = PipeRegister()
    reg = Register()
    Stat = Status()

    pipereg.regW['stat'] = 'HLT'
    pipereg.regW['valE'] = 0xdead1
    pipereg.regW['valM'] = 0xdead2
    pipereg.regW['dstE'] = 10
    pipereg.regW['dstM'] = 15
    WriteBack(pipereg, Stat, reg)
    print Stat.stat, hex(reg.reg[10]), hex(reg.reg[11])
