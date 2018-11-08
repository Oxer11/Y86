# -*- coding: UTF-8 -*-

from cc_stat import *
from register import *
from piperegister import *


def WriteBack(lst, Stat, reg):
	if lst.regW['stat'] == 'BUB':
		Stat.stat = 'AOK'
	else:
		Stat.stat = lst.regW['stat']
    
	reg.write(lst.regW['dstE'], lst.regW['valE'])
	reg.write(lst.regW['dstM'], lst.regW['valM'])


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
