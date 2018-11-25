#This help refers to the help of gdb.
def Help(arg):
	if len(arg)==0: print '''
Commands:
    #Step
    #Jump
    #Breakpoints
    #Display
    #I/O
    #Others
'''
	if (arg == '#Step'): print '''
#Step:
  s, step           Step one instruction exactly.
  n, next           Step one instruction, but proceed through subroutine calls.
  c, continue       Continue program being debugged, after signal or breakpoint.
  finish            Execute until selected stack frame returns.
'''
	if (arg == '#Jump'): print '''
#Jump:
  j, jump           Continue program being debugged at specified line or address.
  return            Make selected stack frame return to its caller.
  call              Call a function in the program.
'''
	if (arg == '#Breakpoints'): print '''
#Breakpoints:
  b, break          Set breakpoint at specified location.
  info breakpoints  Status of all user-settable breakpoints.
  enable            Enable some breakpoints.
  disable           Disable some breakpoints.
  delete            Delete some breakpoints.
'''
	if (arg == '#Display'): print '''
#Display:
  display           Print value of expression EXP each time the program stops.
  undisplay         Cancel some expressions to be displayed when program stops.
'''
	if (arg == '#I/O'): print '''
#I/O:
  w, write          Output the instruction and assembly code into a .yo file.
  list              List instruction and assembly code.
  load              Input the instruction or assembly code from a .yo/.ys file.
  read              Dynamically input the assembly code and append it to the end of original codes.
'''
	if (arg == '#Others'): print '''
#Others:
  set               Set some value for expression EXP.   
  clear             Clear the code and the current status.
  h, help           Print list of commands.
  q, quit           Exit Y86 Assembly IDE.
'''
	if (arg == 's') or (arg == 'step'): print '''
Step one instruction exactly.
Usage: stepi [N]
Argument N means step N times (or till program stops for another reason).
'''
	if (arg == 'n') or (arg == 'next'): print '''
Step one instruction, but proceed through subroutine calls.
Usage: nexti [N]
Argument N means step N times (or till program stops for another reason).
'''
	if (arg == 'c') or (arg == 'continue'): print '''
Continue program being debugged, after signal or breakpoint.
Usage: continue
'''
	if (arg == 'finish'): print '''
Execute until selected stack frame returns.
Usage: finish
'''
	if (arg == 'j') or (arg == 'jump'): print '''
Continue program being debugged at specified address.
Usage: jump <location>
Give as argument *ADDR, where ADDR is an expression for an address to start at.
'''
	if (arg == 'return'): print '''
Make selected stack frame return to its caller.
Usage: return
'''
	if (arg == 'call'): print '''
Call a function in the program.
Usage: call <label>
Argument <label> should be a valid label in assembly code.
'''
	if (arg == 'b') or (arg == 'break'): print '''
Set breakpoint at specified location.
Usage: break <location>
Argument <location> should be a instruction address or a valid label in assembly code.
'''
	if (arg == 'info breakpoints'): print '''
Status of all user-settable breakpoints.
Usage: info breakpoints
'''
	if (arg == 'enable'): print '''
Enable some breakpoints.
Give breakpoint numbers (separated by spaces) as arguments.
To enable all breakpoints, give no argument.
This is used to cancel the effect of the disable command.
'''
	if (arg == 'disable'): print '''
Disable some breakpoints.
Arguments are breakpoint numbers with spaces in between.
To disable all breakpoints, give no argument.
A disabled breakpoint is not forgotten, but has no effect until re-enabled.
'''
	if (arg == 'delete'): print '''
Delete some breakpoints.
Arguments are breakpoint numbers with spaces in between.
To delete all breakpoints, give no argument.
'''
	if (arg == 'display'): print '''
Print value of expression EXP each time the program stops.
Usage: display <EXP>
Some choices of <EXP>:
	REG <REGNAME>    e.g. REG %rax
	MEM <ADDR>       e.g. MEM 0x200
	STACK <NUMID>    e.g. STACK 1
'''
	if (arg == 'undisplay'): print '''
Cancel some expressions to be displayed when program stops.
Usage: undisplay <EXP>
Some choices of <EXP>:
	REG <REGNAME>    e.g. REG %rax
	MEM <ADDR>       e.g. MEM 0x200
	STACK <NUMID>    e.g. STACK 1
'''
	if (arg == 'w') or (arg == 'write'): print '''
Output the instruction and assembly code into a .yo file.
Usage: write <FILENAME>
'''
	if (arg == 'list'): print '''
List instruction and assembly code.
Usage: list
'''
	if (arg == 'load'): print '''
Input the instruction or assembly code from a .yo/.ys file.
Usage: load <FILENAME>
<FILENAME> should be a valid file address ending with .yo or .ys.
'''
	if (arg == 'read'): print '''
Dynamically input the assembly code and append it to the end of original codes.
Usage: read [Enter]
<Assembly Code>
[Enter]
e.g.
read
addq %rax, %rax

'''
	if (arg == 'set'): print '''
Set some value for expression EXP.
Usage: set <EXP> <value>
Some choices of <EXP>:
	REG <REGNAME>    e.g. REG %rax
	MEM <ADDR>       e.g. MEM 0x200
	STACK <NUMID>    e.g. STACK 1
<value> is a decimal number.
'''
	if (arg == 'clear'): print '''
Clear the code and the current status.
Usage: clear
'''
	if (arg == 'h') or (arg == 'help'): print '''
Print list of commands.
Usage: help <CMD>
<CMD> denotes a command or a group of commands.
To show all groups of commands, give no argument.
'''
	if (arg == 'q') or (arg == 'quit'): print '''
Exit Y86 Assembly IDE.
Usage: quit
'''
