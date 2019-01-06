# -*- coding: utf-8 -*-
'''
<div class="button" style="float:left;">Hit:1</div><div class="button" style="float:right;">Miss:1</div>
						<table>
							<tr><th>Set 1</th></tr>
							<tr class="valid"><td>Tag</td><td>From</td><td>To</td></tr>
							<tr class="valid"><td>0</td><td>0x0</td><td>0x8</td></tr>
						</table>
						<table>
							<tr><th>Set 2</th></tr>
							<tr class="valid"><td>Tag</td><td>From</td><td>To</td></tr>
							<tr class="invalid"><td>0</td><td>0x0</td><td>0x8</td></tr>
						</table>
'''

import sys
import os

o_path = os.getcwd() 
sys.path.append(o_path)

from others.Global import*

def WriteCache(Cache):
	ret = ''
	ret += '''<div class="button" style="float:left;">Hit:'''+str(Cache[1][0])
	ret += '''</div><div class="button" style="float:right;">Miss:'''+str(Cache[1][1])+'''</div>'''
	cache = Cache[0]
	s,t,b = Cache[2][0], Cache[2][1], Cache[2][2]
	for si in range(0,len(cache)):
		ret += '''<table>
				<tr><th>Set '''+str(si+1)+'''</th></tr>
				<tr class="valid"><td>Tag</td><td>From</td><td>To</td></tr>'''
		for j in range(0,len(cache[si])):
			if cache[si][j]['valid'] == 0:
				ret += '''<tr class="invalid"'''
			else:
				ret += '''<tr class="valid"'''
			if cache[si][j]['lst'] == get_CLK() - 1:
				if get_Hit_Type() == 1: 
					ret += ''' id="hit" '''
					print '!'
				elif get_Hit_Type() == 0: 
					ret += ''' id="miss" '''
					print '?'
				print '...........................................'
			ret += '''><td>'''+hex(cache[si][j]['tag'])+'''</td>'''
			from_= ((cache[si][j]['tag']<<s)+si)<<b
			to_ = from_+(1<<b)-1
			ret += '''<td>'''+hex(from_)+'''</td><td>'''+hex(to_)+'''</td></tr>'''
		ret += '''</table>'''
	return ret
