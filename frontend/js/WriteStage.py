'''
pipereg:piperegister
'''

def WriteStage(pipereg):
    dic_reg = {0:'%rax', 1:'%rcx', 2:'%rdx', 3:'%rbx', 4:'%rsp', 5:'%rbp', 6:'%rsi', 7:'%rdi', 8:'%r8', 9:'%r9', 10:'%r10',\
        11:'%r11', 12:'%r12', 13:'%r13', 14:'%r14', 15:'----'}
    
    fr = open('../frontend/js/ajax/Stage.txt','w')
    s = '''<tr>
                <td style="font-family:myFont;color:rgb(147,112,219)">Fetch</td>
                <td>predPC:'''+hex(pipereg.regF['predPC'])+'''</span></td>
            </tr>'''
    fr.write(s)
    
    s = '''<tr>
                <td style="font-family:myFont;color:rgb(147,112,219)">Decode</td>
                <td> icode:'''+str(pipereg.regD['icode'])+'''</td>
                <td> ifun:'''+str(pipereg.regD['ifun'])+'''</td>
                <td> rA:'''+dic_reg[pipereg.regD['rA']]+'''</td>
                <td>rB:'''+dic_reg[pipereg.regD['rB']]+'''</td>
                <td>valC:'''+hex(pipereg.regD['valC'])+'''</td>
                <td>valP:'''+hex(pipereg.regD['valP'])+'''</td>
            </tr>'''
    fr.write(s)
    
    s = '''<tr>
                <td style="font-family:myFont;color:rgb(147,112,219)">Execute</td>
                <td>icode:'''+str(pipereg.regE['icode'])+'''</td>
                <td>ifun:'''+str(pipereg.regE['ifun'])+'''</td>
                <td>valC:'''+hex(pipereg.regE['valC'])+'''</td>
                <td>valA:'''+hex(pipereg.regE['valA'])+'''</td>
                <td>valB:'''+hex(pipereg.regE['valB'])+'''</td>
                <td>dstE:'''+dic_reg[pipereg.regE['dstE']]+'''</td>
            </tr>'''
    fr.write(s)
    
    s = '''<tr>
                <td> </td>
                <td>dstM:'''+dic_reg[pipereg.regE['dstM']]+'''</td>
                <td>srcA:'''+dic_reg[pipereg.regE['srcA']]+'''</td>
                <td>srcB:'''+dic_reg[pipereg.regE['srcB']]+'''</td>
            </tr>'''
    fr.write(s)
    
    s = '''<tr>
                <td style="font-family:myFont;color:rgb(147,112,219)">Memory</td>
                <td>icode:'''+str(pipereg.regM['icode'])+'''</td>
                <td>Cnd:'''+str(pipereg.regM['Cnd'])+'''</td>
                <td>valE:'''+hex(pipereg.regM['valE'])+'''</td>
                <td>valA:'''+hex(pipereg.regM['valA'])+'''</td>
                <td>dstE:'''+dic_reg[pipereg.regM['dstE']]+'''</td>
                <td>dstM:'''+dic_reg[pipereg.regM['dstM']]+'''</td>
            </tr>'''
    fr.write(s)
    
    s = '''<tr>
                <td style="font-family:myFont;color:rgb(147,112,219)">Write</td>
                <td>icode:'''+str(pipereg.regW['icode'])+'''</td>
                <td>valE:'''+hex(pipereg.regW['valE'])+'''</td>
                <td>valM:'''+hex(pipereg.regW['valM'])+'''</td>
                <td>dstE:'''+dic_reg[pipereg.regW['dstE']]+'''</td>
                <td>dstM:'''+dic_reg[pipereg.regW['dstM']]+'''</td>
            </tr>'''
    fr.write(s)
    
    fr.close()
