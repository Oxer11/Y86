#This help refers to the help of gdb.
def Help(arg):
	cr=''
	if len(arg)==0: cr=cr+'''<p><pre>
Commands:
    #Step
    #Jump
    #Breakpoints
    #Display
    #I/O
    #Others
</pre></p>'''
	if (arg == '#Step'): cr=cr+'''<p><pre>
#Step:
  s, step           Step one instruction exactly.
  n, next           Step one instruction, but proceed through subroutine calls.
  c, continue       Continue program being debugged, after signal or breakpoint.
  finish            Execute until selected stack frame returns.
</pre></p>'''
	if (arg == '#Jump'): cr=cr+'''<p><pre>
#Jump:
  j, jump           Continue program being debugged at specified line or address.
  return            Make selected stack frame return to its caller.
  call              Call a function in the program.
</pre></p>'''
	if (arg == '#Breakpoints'): cr=cr+'''<p><pre>
#Breakpoints:
  b, break          Set breakpoint at specified location.
  info breakpoints  Status of all user-settable breakpoints.
  enable            Enable some breakpoints.
  disable           Disable some breakpoints.
  delete            Delete some breakpoints.
</pre></p>'''
	if (arg == '#Display'): cr=cr+'''<p><pre>
#Display:
  display           Print value of expression EXP each time the program stops.
  undisplay         Cancel some expressions to be displayed when program stops.
</pre></p>'''
	if (arg == '#I/O'): cr=cr+'''<p><pre>
#I/O:
  w, write          Output the instruction and assembly code into a .yo file.
  list              List instruction and assembly code.
  load              Input the instruction or assembly code from a .yo/.ys file.
  read              Dynamically input the assembly code and append it to the end of original codes.
</pre></p>'''
	if (arg == '#Others'): cr=cr+'''<p><pre>
#Others:
  set               Set some value for expression EXP.   
  clear             Clear the code and the current status.
  h, help           Print list of commands.
  q, quit           Exit Y86 Assembly IDE.
</pre></p>'''
	if (arg == 's') or (arg == 'step'): cr=cr+'''<p><pre>
Step one instruction exactly.
Usage: step [N]
Argument N means step N times (or till program stops for another reason).
</pre></p>'''
	if (arg == 'n') or (arg == 'next'): cr=cr+'''<p><pre>
Step one instruction, but proceed through subroutine calls.
Usage: next [N]
Argument N means step N times (or till program stops for another reason).
</pre></p>'''
	if (arg == 'c') or (arg == 'continue'): cr=cr+'''<p><pre>
Continue program being debugged, after signal or breakpoint.
Usage: continue
</pre></p>'''
	if (arg == 'finish'): cr=cr+'''<p><pre>
Execute until selected stack frame returns.
Usage: finish
</pre></p>'''
	if (arg == 'j') or (arg == 'jump'): cr=cr+'''<p><pre>
Continue program being debugged at specified address.
Usage: jump <location>
Give as argument *ADDR, where ADDR is an expression for an address to start at.
</pre></p>'''
	if (arg == 'return'): cr=cr+'''<p><pre>
Make selected stack frame return to its caller.
Usage: return
</pre></p>'''
	if (arg == 'call'): cr=cr+'''<p><pre>
Call a function in the program.
Usage: call <label>
Argument <label> should be a valid label in assembly code.
</pre></p>'''
	if (arg == 'b') or (arg == 'break'): cr=cr+'''<p><pre>
Set breakpoint at specified location.
Usage: break <location>
Argument <location> should be a instruction address or a valid label in assembly code.
</pre></p>'''
	if (arg == 'info breakpoints'): cr=cr+'''<p><pre>
Status of all user-settable breakpoints.
Usage: info breakpoints
</pre></p>'''
	if (arg == 'enable'): cr=cr+'''<p><pre>
Enable some breakpoints.
Give breakpoint numbers (separated by spaces) as arguments.
To enable all breakpoints, give no argument.
This is used to cancel the effect of the disable command.
</pre></p>'''
	if (arg == 'disable'): cr=cr+'''<p><pre>
Disable some breakpoints.
Arguments are breakpoint numbers with spaces in between.
To disable all breakpoints, give no argument.
A disabled breakpoint is not forgotten, but has no effect until re-enabled.
</pre></p>'''
	if (arg == 'delete'): cr=cr+'''<p><pre>
Delete some breakpoints.
Arguments are breakpoint numbers with spaces in between.
To delete all breakpoints, give no argument.
</pre></p>'''
	if (arg == 'display'): cr=cr+'''<p><pre>
Print value of expression EXP each time the program stops.
Usage: display <EXP>
Some choices of <EXP>:
	REG <REGNAME>    e.g. REG %rax
	MEM <ADDR>       e.g. MEM 0x200
	STACK <NUMID>    e.g. STACK 1
</pre></p>'''
	if (arg == 'undisplay'): cr=cr+'''<p><pre>
Cancel some expressions to be displayed when program stops.
Usage: undisplay <EXP>
Some choices of <EXP>:
	REG <REGNAME>    e.g. REG %rax
	MEM <ADDR>       e.g. MEM 0x200
	STACK <NUMID>    e.g. STACK 1
</pre></p>'''
	if (arg == 'w') or (arg == 'write'): cr=cr+'''<p><pre>
Output the instruction and assembly code into a .yo file.
Usage: write <FILENAME>
</pre></p>'''
	if (arg == 'list'): cr=cr+'''<p><pre>
List instruction and assembly code.
Usage: list
</pre></p>'''
	if (arg == 'load'): cr=cr+'''<p><pre>
Input the instruction or assembly code from a .yo/.ys file.
Usage: load <FILENAME>
<FILENAME> should be a valid file address ending with .yo or .ys.
</pre></p>'''
	if (arg == 'read'): cr=cr+'''<p><pre>
Dynamically input the assembly code and append it to the end of original codes.
Usage: read [Enter]
<Assembly Code>
[Enter]
e.g.
read
addq %rax, %rax

</pre></p>'''
	if (arg == 'set'): cr=cr+'''<p><pre>
Set some value for expression EXP.
Usage: set <EXP> <value>
Some choices of <EXP>:
	REG <REGNAME>    e.g. REG %rax
	MEM <ADDR>       e.g. MEM 0x200
	STACK <NUMID>    e.g. STACK 1
<value> is a decimal number.
</pre></p>'''
	if (arg == 'clear'): cr=cr+'''<p><pre>
Clear the code and the current status.
Usage: clear
</pre></p>'''
	if (arg == 'h') or (arg == 'help'): cr=cr+'''<p><pre>
Print list of commands.
Usage: help <CMD>
<CMD> denotes a command or a group of commands.
To show all groups of commands, give no argument.
</pre></p>'''
	if (arg == 'q') or (arg == 'quit'): cr=cr+'''<p><pre>
Exit Y86 Assembly IDE.
Usage: quit
</pre></p>'''
	return cr
