# -*- coding: utf-8 -*-
'''
Reg：元组的列表
'''

def WriteReg(Reg):    
    fr_r = '<table>'
    for reg in Reg:
        s = '''<tr>
                    <td>'''+reg[0]+'''</td>
                    <td><span id=RBX>'''+reg[1]+'''</span></td>
                </tr>'''
        fr_r = fr_r + s
    fr_r = fr_r + '''</table>'''
    return fr_r
