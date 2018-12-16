'''
pipereg:piperegister
ins:list of instructions
'''

def WriteStage(pipereg,ins):
    dic_reg = {0:'%rax', 1:'%rcx', 2:'%rdx', 3:'%rbx', 4:'%rsp', 5:'%rbp', 6:'%rsi', 7:'%rdi', 8:'%r8', 9:'%r9', 10:'%r10',\
        11:'%r11', 12:'%r12', 13:'%r13', 14:'%r14', 15:'----'}
    
    fr = open('../frontend/js/ajax/Stage.txt','w')
    s = '''<tr><td style="font-family:myFont;color:rgb(147,112,219);text-align:center;">Write</td>
			<td><button class="button" style="width:80px;">

                <span class="name">ins</span><br />
                <span class="value">'''+ins[3]+'''</span>
            </button></td>
			<td><button class="button" style="width:80px;">
                <span class="name">stat</span><br />
                <span class="value">'''+pipereg.regW['stat']+'''</span>
            </button></td>
			<td><button class="button" style="width:80px;">
                <span class="name">dstE</span><br />
                <span class="value">'''+dic_reg[pipereg.regW['dstE']]+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">dstM</span><br />
                <span class="value">'''+dic_reg[pipereg.regW['dstM']]+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">valE</span><br />
                <span class="value">'''+hex(pipereg.regW['valE'])+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">valM</span><br />
                <span class="value">'''+hex(pipereg.regW['valM'])+'''</span>
            </button></td>
			</tr>'''
    fr.write(s)

    s = '''<tr><td style="font-family:myFont;color:rgb(147,112,219);text-align:center;">Memory</td>
			<td><button class="button" style="width:80px;">

                <span class="name">ins</span><br />
                <span class="value">'''+ins[2]+'''</span>
            </button></td>
			<td><button class="button" style="width:80px;">
                <span class="name">stat</span><br />
                <span class="value">'''+pipereg.regM['stat']+'''</span>
            </button></td>
			<td><button class="button" style="width:80px;">
                <span class="name">Cnd</span><br />
                <span class="value">'''+str(pipereg.regM['Cnd'])+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">valE</span><br />
                <span class="value">'''+hex(pipereg.regM['valE'])+'''</span>
            </button></td><td><button class="button">
                <span class="name">valA</span><br />
                <span class="value">'''+hex(pipereg.regM['valA'])+'''</span></span>
            </button></td>
			<td><button class="button">
                <span class="name">dstE</span><br />
                <span class="value">'''+dic_reg[pipereg.regM['dstE']]+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">dstM</span><br />
                <span class="value">'''+dic_reg[pipereg.regM['dstM']]+'''</span>
            </button></td>
			</tr>'''
    fr.write(s)

    s = '''<tr><td style="font-family:myFont;color:rgb(147,112,219);text-align:center;">Execute</td>
			<td><button class="button" style="width:80px;">
                <span class="name">ins</span><br />
                <span class="value">'''+ins[1]+'''</span>
            </button></td>
			<td><button class="button" style="width:80px;">
                <span class="name">stat</span><br />
                <span class="value">'''+pipereg.regE['stat']+'''</span>
            </button></td>
			<td><button class="button" style="width:80px;">
                <span class="name">dstE</span><br />
                <span class="value">'''+dic_reg[pipereg.regE['dstE']]+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">dstM</span><br />
                <span class="value">'''+dic_reg[pipereg.regE['dstM']]+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">valA</span><br />
                <span class="value">'''+hex(pipereg.regE['valA'])+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">valB</span><br />
                <span class="value">'''+hex(pipereg.regE['valB'])+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">valC</span><br />
                <span class="value">'''+hex(pipereg.regE['valC'])+'''</span>
            </button></td>
		</tr>'''
    fr.write(s)
    
    s = '''<tr><td> </td>
			<td><button class="button" style="width:80px;">
                <span class="name">srcA</span><br />
                <span class="value">'''+dic_reg[pipereg.regE['srcA']]+'''</span>
            </button></td>
			<td><button class="button" style="width:80px;">
                <span class="name">srcB</span><br />
                <span class="value">'''+dic_reg[pipereg.regE['srcB']]+'''</span>
            </button></td>
		</tr>'''
    fr.write(s)

    s = '''<tr><td style="font-family:myFont;color:rgb(147,112,219);text-align:center;">Decode</td>
			<td><button class="button" style="width:80px;">
                <span class="name">ins</span><br />
                <span class="value">'''+ins[0]+'''</span>
            </button></td>
			<td><button class="button" style="width:80px;">
                <span class="name">stat</span><br />
                <span class="value">'''+pipereg.regD['stat']+'''</span>
            </button></td>
			<td><button class="button" style="width:80px;">
                <span class="name">rA</span><br />
                <span class="value">'''+dic_reg[pipereg.regD['rA']]+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">rB</span><br />
                <span class="value">'''+dic_reg[pipereg.regD['rB']]+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">valC</span><br />
                <span class="value">'''+hex(pipereg.regD['valC'])+'''</span>
            </button></td>
			<td><button class="button">
                <span class="name">valP</span><br />
                <span class="value">'''+hex(pipereg.regD['valP'])+'''</span>
            </button></td>
		</tr>'''
    fr.write(s)

    s = '''<tr><td style="font-family:myFont;color:rgb(147,112,219);text-align:center;">Fetch</td>
				<td><button class="button" style="width:80px;">
                    <span class="name">predPC</span><br />
                    <span class="value">'''+hex(pipereg.regF['predPC'])+'''</span>
                </button></td>
           </tr>'''
    fr.write(s)
    
    fr.close()
