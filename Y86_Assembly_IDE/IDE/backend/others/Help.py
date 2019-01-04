#This help refers to the help of gdb.
def Help(arg):
	cr=''
	if len(arg)==0: cr=cr+'''<tr><td  class="info"><pre>Commands:
    #Step
    #Jump
    #Breakpoints
    #Display
    #I/O
    #Others
</pre></td></tr>'''
	elif (arg == '#Step'): cr=cr+'''<tr><td  class="info"><pre>#Step:
  s, step           Step one infotruction exactly.
  n, next           Step one infotruction, but proceed through subroutine calls.
  c, continue       Continue program being debugged, after signal or breakpoint.
  finish            Execute until selected stack frame returns.
</pre></td></tr>'''
	elif (arg == '#Jump'): cr=cr+'''<tr><td  class="info"><pre>#Jump:
  j, jump           Continue program being debugged at specelified line or address.
  return            Make selected stack frame return to its caller.
  call              Call a function in the program.
</pre></td></tr>'''
	elif (arg == '#Breakpoints'): cr=cr+'''<tr><td  class="info"><pre>#Breakpoints:
  b, break          Set breakpoint at specelified location.
  info breakpoints  Status of all user-settable breakpoints.
  enable            Enable some breakpoints.
  disable           Disable some breakpoints.
  delete            Delete some breakpoints.
</pre></td></tr>'''
	elif (arg == '#Display'): cr=cr+'''<tr><td  class="info"><pre>#Display:
  display           Print value of expression EXP each time the program stops.
  undisplay         Cancel some expressions to be displayed when program stops.
</pre></td></tr>'''
	elif (arg == '#I/O'): cr=cr+'''<tr><td  class="info"><pre>#I/O:
  w, write          Output the infotruction and assembly code into a .yo file.
  list              List infotruction and assembly code.
  load              Input the infotruction or assembly code from a .yo/.ys file.
  read              Dynamically input the assembly code and append it to the end of original codes.
</pre></td></tr>'''
	elif (arg == '#Others'): cr=cr+'''<tr><td  class="info"><pre>#Others:
  set               Set some value for expression EXP.   
  clear             Clear the code and the current status.
  h, help           Print list of commands.
  q, quit           Exit Y86 Assembly IDE.
</pre></td></tr>'''
	elif (arg == 's') or (arg == 'step'): cr=cr+'''<tr><td  class="info"><pre>Step one infotruction exactly.
Usage: step [N]
Argument N means step N times (or till program stops for another reason).
</pre></td></tr>'''
	elif (arg == 'n') or (arg == 'next'): cr=cr+'''<tr><td  class="info"><pre>Step one infotruction, but proceed through subroutine calls.
Usage: next [N]
Argument N means step N times (or till program stops for another reason).
</pre></td></tr>'''
	elif (arg == 'c') or (arg == 'continue'): cr=cr+'''<tr><td  class="info"><pre>Continue program being debugged, after signal or breakpoint.
Usage: continue
</pre></td></tr>'''
	elif (arg == 'finish'): cr=cr+'''<tr><td  class="info"><pre>Execute until selected stack frame returns.
Usage: finish
</pre></td></tr>'''
	elif (arg == 'j') or (arg == 'jump'): cr=cr+'''<tr><td  class="info"><pre>Continue program being debugged at specelified address.
Usage: jump <location>
Give as argument *ADDR, where ADDR is an expression for an address to start at.
</pre></td></tr>'''
	elif (arg == 'return'): cr=cr+'''<tr><td  class="info"><pre>Make selected stack frame return to its caller.
Usage: return
</pre></td></tr>'''
	elif (arg == 'call'): cr=cr+'''<tr><td  class="info"><pre>Call a function in the program.
Usage: call <label>
Argument <label> should be a valid label in assembly code.
</pre></td></tr>'''
	elif (arg == 'b') or (arg == 'break'): cr=cr+'''<tr><td  class="info"><pre>Set breakpoint at specelified location.
Usage: break <location>
Argument <location> should be a infotruction address or a valid label in assembly code.
</pre></td></tr>'''
	elif (arg == 'info breakpoints'): cr=cr+'''<tr><td  class="info"><pre>Status of all user-settable breakpoints.
Usage: info breakpoints
</pre></td></tr>'''
	elif (arg == 'enable'): cr=cr+'''<tr><td  class="info"><pre>Enable some breakpoints.
Give breakpoint numbers (separated by spaces) as arguments.
To enable all breakpoints, give no argument.
This is used to cancel the effect of the disable command.
</pre></td></tr>'''
	elif (arg == 'disable'): cr=cr+'''<tr><td  class="info"><pre>Disable some breakpoints.
Arguments are breakpoint numbers with spaces in between.
To disable all breakpoints, give no argument.
A disabled breakpoint is not forgotten, but has no effect until re-enabled.
</pre></td></tr>'''
	elif (arg == 'delete'): cr=cr+'''<tr><td  class="info"><pre>Delete some breakpoints.
Arguments are breakpoint numbers with spaces in between.
To delete all breakpoints, give no argument.
</pre></td></tr>'''
	elif (arg == 'display'): cr=cr+'''<tr><td  class="info"><pre>Print value of expression EXP each time the program stops.
Usage: display <EXP>
Some choices of <EXP>:
	REG <REGNAME>    e.g. REG %rax
	MEM <ADDR>       e.g. MEM 0x200
	STACK <NUMID>    e.g. STACK 1
</pre></td></tr>'''
	elif (arg == 'undisplay'): cr=cr+'''<tr><td  class="info"><pre>Cancel some expressions to be displayed when program stops.
Usage: undisplay <EXP>
Some choices of <EXP>:
	REG <REGNAME>    e.g. REG %rax
	MEM <ADDR>       e.g. MEM 0x200
	STACK <NUMID>    e.g. STACK 1
</pre></td></tr>'''
	elif (arg == 'w') or (arg == 'write'): cr=cr+'''<tr><td  class="info"><pre>Output the infotruction and assembly code into a .yo file.
Usage: write <FILENAME>
</pre></td></tr>'''
	elif (arg == 'list'): cr=cr+'''<tr><td  class="info"><pre>List infotruction and assembly code.
Usage: list
</pre></td></tr>'''
	elif (arg == 'load'): cr=cr+'''<tr><td  class="info"><pre>Input the infotruction or assembly code from a .yo/.ys file.
Usage: load <FILENAME>
<FILENAME> should be a valid file address ending with .yo or .ys.
</pre></td></tr>'''
	elif (arg == 'read'): cr=cr+'''<tr><td  class="info"><pre>Dynamically input the assembly code and append it to the end of original codes.
Usage: read [Enter]
<Assembly Code>
[Enter]
e.g.
read
addq %rax, %rax

</pre></td></tr>'''
	elif (arg == 'set'): cr=cr+'''<tr><td  class="info"><pre>Set some value for expression EXP.
Usage: set <EXP> <value>
Some choices of <EXP>:
	REG <REGNAME>    e.g. REG %rax
	MEM <ADDR>       e.g. MEM 0x200
	STACK <NUMID>    e.g. STACK 1
<value> is a decimal number.
</pre></td></tr>'''
	elif (arg == 'clear'): cr=cr+'''<tr><td  class="info"><pre>Clear the code and the current status.
Usage: clear
</pre></td></tr>'''
	elif (arg == 'h') or (arg == 'help'): cr=cr+'''<tr><td  class="info"><pre>Print list of commands.
Usage: help <CMD>
<CMD> denotes a command or a group of commands.
To show all groups of commands, give no argument.
</pre></td></tr>'''
	elif (arg == 'q') or (arg == 'quit'): cr=cr+'''<tr><td  class="info"><pre>Exit Y86 Assembly IDE.
Usage: quit
</pre></td></tr>'''
	else:
		cr=cr+'<tr><td  class="error">Invalid Instruction</td></tr>'
	return cr
