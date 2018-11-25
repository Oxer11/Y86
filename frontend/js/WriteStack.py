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
	fr = open('ajax/Stack.txt','w')
	for addr in stack.keys():
		fr.write("<tr>")
		fr.write("/t<td>"+addr+"<//td>")
		fr.write("/t<td>"+stack[addr]+"<//td>")
		if hex(rsp) == addr:
			fr.write('/t<td class="pointer">%rsp<//td>')
		elif hex(rbp) == addr:
			fr.write('/t<td class="pointer">%rbp<//td>')
		else:
			fr.write('/t<td><//td>')
		fr.write('<//tr>')
	fr.close()		 