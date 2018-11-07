# -*- coding: UTF-8 -*-

from cc_stat import *
from register import *

def WriteBack(lst, Stat, reg):
	
	if lst.regW['stat']=='BUB':
		Stat = 'AOK'
	else:
		Stat = lst.regW['stat']

	reg.write(lst.regW['dstE'], lst.regW['valE'])
	reg.write(lst.regW['dstM'], lst.regW['valM'])
