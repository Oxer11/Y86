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

def WriteCode(lines,PC):
    fr = open('../frontend/js/ajax/Codes.txt','w')
    count = -1
    fr.write('''<pre>''')
    for line in lines:
        count += 1
        i = line.find(':')
        if i != -1 and int(line[0:i],16) == PC and line[i+2] != ' ':
            fr.write('''<mark>'''+line+'''</mark>''')
        else:
            fr.write(line)
    fr.write('''</pre>''')
    fr.close()
    
