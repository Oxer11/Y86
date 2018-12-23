# -*- coding: utf-8 -*-
'''
<pre id="InsCode"> 
                            
0x000:                      
0x000: 30f40002000000000000 
<mark>0x00a: 803800000000000000</mark>   
0x013: 00                   
</pre>
'''

'''
lines:一个list，每个元素是指令码的一行
PC:整数，需要高亮行的地址
'''
import re

def WriteCode(lines,PC):
    fr = '''<pre>\n'''
    count = -1
    for line in lines:
        count += 1
        cmd = re.sub(r'(#.*$)|(/\*(.|\n)*\*/)',"",line)
        i = cmd.find(':')
        if i != -1 and int(cmd[0:i],16) == PC and cmd[i+2] != ' ':
            fr = fr + '''<mark>''' + line + '''</mark>\n'''
        else:
            fr = fr + line + '\n'
    fr = fr + '''</pre>\n'''
    return fr
    
