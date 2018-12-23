# -*- coding: utf-8 -*-
'''
dis:元组的列表
'''
def WriteDisplay(dis):
    fr = ''
    for item in dis:
        s='''<tr class="column" draggable="true">
                <td>'''+item[0]+'''</td>
                <td>'''+item[1]+'''</td>
            </tr>'''
        fr = fr + s
    return fr
