# -*- coding: utf-8 -*-
'''
Reg：元组的列表
'''

def WriteReg(Reg):    
    fr_r = open('../frontend/js/ajax/tab_content3.txt','w')
    fr_r.write('<table>')
    for reg in Reg:
        s = '''<tr>
                    <td>'''+reg[0]+'''</td>
                    <td><span id=RBX>'''+reg[1]+'''</span></td>
                </tr>'''
        fr_r.write(s)
    fr_r.write('''</table>''')
    fr_r.close()
