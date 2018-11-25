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
lines_ins:一个list，每个元素是指令码的一行
lines_as:一个list，每个元素是汇编代码的一行
PC:整数，需要高亮行的地址
'''

def WriteCode(lines_ins,lines_as,PC):
    fr_i = open('../frontend/js/ajax/InsCode.txt','w')
    count = -1
    mark = 0
    fr_i.write('<pre>')
    for line in lines_ins:
        count += 1
        i = line.find(':')
        if i != -1 and int(line[0:i],16) == PC:
            fr_i.write("<mark>"+line+"<//mark>")
            mark = count
        else:
            fr_i.write(line)
    fr_i.write('<//pre>')
    fr_i.close()
    fr_a = open('../frontend/js/ajax/Assembly.txt','w')
    fr_a.write('<pre>')
    for i in range(0,len(lines_as)):
        if i != mark:
            fr_a.write(lines_as[i])
        else:
            fr_a.write('<mark>'+lines_as[i]+'<//mark>')
    fr_a.write('<//pre>')
    fr_a.close()
