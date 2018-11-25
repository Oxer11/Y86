# -*- coding: utf-8 -*-
'''
cycle：整数，周期数
stat：字符串，状态
cpi：整数，cpi
zf、sf、of：整数
'''

def WriteStat(cycle,stat,cpi,zf,sf,of):
    fr = open('../frontend/js/ajax/tab_content1.txt','w')
    s = '''<div><p id="cycle" style="font-size:80px;font-weight:700;text-align:center;color:white;background-color:rgb(147,112,219);padding-top:10px;padding-bottom:10px;">'''+str(cycle)+'''</p></div>
                    <div style="text-align:center;margin-top:0px;margin-bottom:0px;">
                        <button class="button">
                            <span style="font-size:15px;">State</span><br />
                            <span style="font-weight:bold;"><span id="Stat">'''+stat+'''</span></span>
                        </button>
                        <button class="button">
                            <span style="font-size:15px;">CPI</span><br />
                            <span style="font-weight:bold;"><span id="CPI">'''+str(cpi)+'''</span></span>
                        </button>
                    </div>
                    <div style="text-align:center;margin-left:10px;margin-top:0px;">
                        <button class="button">
                            <span style="font-size:15px;">ZF</span><br />
                            <span style="font-weight:bold;"><span id="ZF">'''+str(zf)+'''</span></span>
                        </button>
                        <button class="button">
                            <span style="font-size:15px;">SF</span><br />
                            <span style="font-weight:bold;"><span id="SF">'''+str(sf)+'''</span></span>
                        </button>
                        <button class="button">
                            <span style="font-size:15px;">OF</span><br />
                            <span style="font-weight:bold;"><span id="OF">'''+str(of)+'''</span></span>
                        </button>
                    </div>
                    '''
    fr.write(s)
    fr.close()
