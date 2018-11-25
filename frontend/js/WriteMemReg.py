# -*- coding: utf-8 -*-
'''
mem:map，键为内存地址，值为内存内容，均为字符串
Reg：map，键为寄存器名字，值为寄存器内容，均为字符串
'''

def WriteMemReg(mem,Reg):
    fr_m = open('../frontend/js/ajax/tab_content2.txt','w')
    fr_m.write('<table>')
    for addr in mem.keys():
        s = '''<tr>
                    <td>'''+addr+'''</td>
                    <td>'''+mem[addr]+'''</td>
                </tr>'''
        fr_m.write(s)
    fr_m.write('''</table>''')
    fr_m.close()
    
    fr_r = open('../frontend/js/ajax/tab_content3.txt','w')
    fr_r.write('<table>')
    for reg in Reg.keys():
        s = '''<tr>
                    <td>'''+reg+'''</td>
                    <td><span id=RBX>'''+Reg[reg]+'''</span></td>
                </tr>'''
        fr_r.write(s)
    fr_r.write('''</table>''')
    fr_r.close()
