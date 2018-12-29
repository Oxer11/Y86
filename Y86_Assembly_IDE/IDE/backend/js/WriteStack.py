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
	fr = ''
	if rsp == rbp:
		return fr
	l = sorted(stack.items(),key = lambda d:int(d[0],16),reverse = True)
	for item in l:
		fr = fr + '''<tr>'''
		fr = fr + '''<td>'''+item[0]+'''</td>'''
		fr = fr + '''<td>'''+item[1]+'''</td>'''
		if rsp == int(item[0], 16):
			fr = fr + '''<td class="pointer">%rsp</td>'''
		elif rbp == int(item[0], 16):
			fr = fr + '''<td class="pointer">%rbp</td>'''
		else:
			fr = fr + '''<td></td>'''
		fr = fr + '''</tr>'''
	return fr
