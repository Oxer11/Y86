# -*- coding: utf-8 -*-
'''
dis:map，键为要展示内容的名称，字符串；值为内容，字符串
'''
def WriteDisplay(dis):
    fr = open('../frontend/js/ajax/columns.txt','w')
    for name in dis.keys():
        s='''<tr class="column" draggable="true">
                <td>'''+name+'''</td>
                <td>'''+dis[name]+'''</td>
            </tr>'''
        fr.write(s)
    fr.close()
