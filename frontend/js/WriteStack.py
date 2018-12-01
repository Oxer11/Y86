# -*- coding: utf-8 -*-
'''
<tr>
    <td>0x030</td>
    <td>0xa000a000a000a000</td>
    <td class="pointer">%rbp</td>
</tr>
'''

'''
stack:以栈的地址为键,栈的值为值的map，键值均为字符串
rsp：%rsp的值，整数
rbp：%rbp的值，整数
'''
def WriteStack(stack,rsp,rbp):
	fr = open('../frontend/js/ajax/Stack.txt','w')
	if rsp == rbp:
		fr.close()
		return 
	l = sorted(stack.items(),key = lambda d:int(d[0],16),reverse = True)
	for item in l:
		fr.write('''<tr>''')
		fr.write('''<td>'''+item[0]+'''</td>''')
		fr.write('''<td>'''+item[1]+'''</td>''')
		if hex(rsp) == item[0]:
			fr.write('''<td class="pointer">%rsp</td>''')
		elif hex(rbp) == item[0]:
			fr.write('''<td class="pointer">%rbp</td>''')
		else:
			fr.write('''<td></td>''')
		fr.write('''</tr>''')
	fr.close()		 
