'''
pipereg:piperegister
ins:list of instructions
'''

def WriteStage(pipereg,ins):
    dic_reg = {0:'%rax', 1:'%rcx', 2:'%rdx', 3:'%rbx', 4:'%rsp', 5:'%rbp', 6:'%rsi', 7:'%rdi', 8:'%r8', 9:'%r9', 10:'%r10',\
        11:'%r11', 12:'%r12', 13:'%r13', 14:'%r14', 15:'----'}
    
    fr = ''
    s = '''<tr>
				<td style="font-family:myFont;color:rgb(147,112,219);">Write</td>
				<td>
					<span class="mytooltip">'''+ins[3]+'''
					<span class="mytooltip_text">ins</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+pipereg.regW['stat']+'''
					<span class="mytooltip_text">stat</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+dic_reg[pipereg.regW['dstE']]+'''
					<span class="mytooltip_text">dstE</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+dic_reg[pipereg.regW['dstM']]+'''
					<span class="mytooltip_text">dstM</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+hex(pipereg.regW['valE'])+'''
					<span class="mytooltip_text">valE</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+hex(pipereg.regW['valM'])+'''
					<span class="mytooltip_text">valM</span></span>
				</td>
				</tr>
			'''
    fr = fr + s

    s = '''<tr>
				<td style="font-family:myFont;color:rgb(147,112,219);">Memory</td>
				<td>
					<span class="mytooltip">'''+ins[2]+'''
					<span class="mytooltip_text">ins</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+pipereg.regM['stat']+'''
					<span class="mytooltip_text">stat</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+str(pipereg.regM['Cnd'])+'''
					<span class="mytooltip_text">Cnd</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+hex(pipereg.regM['valE'])+'''
					<span class="mytooltip_text">valE</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+hex(pipereg.regM['valA'])+'''
					<span class="mytooltip_text">valA</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+dic_reg[pipereg.regM['dstE']]+'''
					<span class="mytooltip_text">dstE</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+dic_reg[pipereg.regM['dstM']]+'''
					<span class="mytooltip_text">dstM</span></span>
				</td>
				</tr>'''
    fr = fr + s

    s = '''<tr>
				<td style="font-family:myFont;color:rgb(147,112,219);">Execute</td>
				<td>
					<span class="mytooltip">'''+ins[1]+'''
					<span class="mytooltip_text">ins</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+pipereg.regE['stat']+'''
					<span class="mytooltip_text">stat</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+dic_reg[pipereg.regE['dstE']]+'''
					<span class="mytooltip_text">dstE</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+dic_reg[pipereg.regE['dstM']]+'''
					<span class="mytooltip_text">dstM</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+hex(pipereg.regE['valA'])+'''
					<span class="mytooltip_text">valA</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+hex(pipereg.regE['valB'])+'''
					<span class="mytooltip_text">valB</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+hex(pipereg.regE['valC'])+'''
					<span class="mytooltip_text">valC</span></span>
				</td>
				</tr>'''
    fr = fr + s
    
    s = '''<tr><td> </td>
				<td>
					<span class="mytooltip">'''+dic_reg[pipereg.regE['srcA']]+'''
					<span class="mytooltip_text">srcA</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+dic_reg[pipereg.regE['srcB']]+'''
					<span class="mytooltip_text">srcB</span></span>
				</td>
				</tr>'''
    fr = fr + s

    s = '''<tr>
				<td style="font-family:myFont;color:rgb(147,112,219);">Decode</td>
				<td>
					<span class="mytooltip">'''+ins[0]+'''
					<span class="mytooltip_text">ins</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+pipereg.regD['stat']+'''
					<span class="mytooltip_text">stat</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+dic_reg[pipereg.regD['rA']]+'''
					<span class="mytooltip_text">rA</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+dic_reg[pipereg.regD['rB']]+'''
					<span class="mytooltip_text">rB</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+hex(pipereg.regD['valC'])+'''
					<span class="mytooltip_text">valC</span></span>
				</td>
				<td>
					<span class="mytooltip">'''+hex(pipereg.regD['valP'])+'''
					<span class="mytooltip_text">valP</span></span>
				</td>
				</tr>'''
    fr = fr + s

    s = '''<tr>
				<td style="font-family:myFont;color:rgb(147,112,219);">Fetch</td>
				<td>
                    <span class="mytooltip">'''+hex(pipereg.regF['predPC'])+'''
                    <span class="mytooltip_text">predPC</span></span>
                </td>
				</tr>'''
    fr = fr + s
    return fr
