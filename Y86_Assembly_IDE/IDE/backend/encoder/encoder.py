# -*- coding: UTF-8 -*-

import re

INS = 0
error={}
count=1

def register(REG):
	global error,count
	if REG == '%rax':
		return '0'
	elif REG == '%rcx':
		return '1'
	elif REG == '%rdx':
		return '2'
	elif REG == '%rbx':
		return '3'
	elif REG == '%rsp':
		return '4'
	elif REG == '%rbp':
		return '5'
	elif REG == '%rsi':
		return '6'
	elif REG == '%rdi':
		return '7'
	elif REG == '%r8':
		return '8'
	elif REG == '%r9':
		return '9'
	elif REG == '%r10':
		return 'a'
	elif REG == '%r11':
		return 'b'
	elif REG == '%r12':
		return 'c'
	elif REG == '%r13':
		return 'd'
	elif REG == '%r14':
		return 'e'
	else:
		error[count]='Error: Invalid Register '+REG+'!'
		global INS
		INS = 1
		return ''


def little_endian(v, length=0x8):
	global INS
	global error,count
	if len(v) == 0: v = '0'
	if v[0:2] == '0x':
		if not re.match(r'^0x[0-9a-fA-F]+$', v):
			INS = 1
			error[count]='Error: Invalid Number '+v+'!'
			return ''
		x = long(v, 16)
	else:
		if not v.isdigit() and not (v[0] == '-' and v[1:len(v)].isdigit()):
			INS = 1
			error[count]='Error: Invalid Number '+v+'!'
			return ''
		x = long(v, 10)
	ans = ''
	for i in range(0, length):
		ans += hex(x / 16 % 16)[2] + hex(x % 16)[2]
		x /= 256
	return ans

def Label(labels, str):
	global error,count
	if not labels.has_key(str):
		error[count]='Error: Invalid Label '+str+'!'
		global INS
		INS = 1
		return '0'
	else: return labels[str]

def encoder(AssemblyCode, labels, nowPC):
	global error,count
	codes = []
	now = nowPC
	lst_labels = labels
	global INS
	INS = 0
	count=0
	error={}
	for line in AssemblyCode:
		count += 1
		cmd = re.sub(r'(#.*$)|(/\*(.|\n)*\*/)', "", line)
		cmd = cmd.strip()
		end = cmd.find(':')
		if end != -1:
			labels[cmd[0:end]] = hex(now)
			ins = cmd[end + 1:len(cmd)]
		else:
			ins = cmd
		ins = ins.strip()
		if len(ins) == 0: continue
		end = ins.find(' ')
		if end != -1:
			cmd = ins[0:end]
		else:
			cmd = ins

		if cmd in ['halt', 'nop', 'ret', '.byte']:
			now += 1
		elif cmd in ['rrmovq', 'xorq', 'andq', 'addq', 'subq', 'cmovle', 'cmovl', 'cmove', 'cmovne', 'cmovge', 'cmovg',
					 'pushq', 'popq']:
			now += 2
		elif cmd in ['call', 'jmp', 'jle', 'jl', 'je', 'jne', 'jge', 'jg']:
			now += 9
		elif cmd in ['irmovq', 'rmmovq', 'mrmovq', 'iaddq']:
			now += 10
		elif cmd == '.quad':
			now += 8
		elif cmd == '.pos':
			now = int(ins[end + 1:len(ins)], 16)
		elif cmd == '.align':
			x = int(ins[end + 1:len(ins)], 16)
			if now % x != 0:
				now += x - now % x
		else:
			error[count]='Error: Invalid Instruction '+line+'!'
			labels = lst_labels

	now = nowPC
	count=0
	for line in AssemblyCode:		
		count += 1
		cmd = re.sub(r'(#.*$)|(/\*(.|\n)*\*/)', "", line)
		ans = ''
		cmd = cmd.strip()
		if len(cmd) == 0:
			codes.append(ans.ljust(28) + '| ' + line)
			continue

		end = cmd.find(':')
		if end != -1:
			ins = cmd[end + 1:len(cmd)]
		else:
			ins = cmd

		ans = hex(now) + ': '
		ins = ins.strip()
		if len(ins) == 0:
			codes.append(ans.ljust(28) + '| ' + line)
			continue

		end = ins.find(' ')
		if end != -1:
			cmd = ins[0:end]
		else:
			cmd = ins

		if cmd in ['.pos', '.align']:
			pass
		elif cmd in ['.byte', '.quad']:
			if cmd == '.byte': length = 1
			else: length = 8
			if labels.has_key(ins[end + 1:len(ins)].strip()):
				ans += little_endian(labels[ins[end + 1:len(ins)].strip()], length)
			else:
				ans += little_endian(ins[end + 1:len(ins)].strip(), length)
		elif cmd == 'halt':
			ans += '00'
		elif cmd == 'nop':
			ans += '10'
		elif cmd in ['rrmovq', 'cmovle', 'cmovl', 'cmove', 'cmovne', 'cmovge', 'cmovg']:
			if cmd == 'rrmovq':
				ans += '20'
			elif cmd == 'cmovle':
				ans += '21'
			elif cmd == 'cmovl':
				ans += '22'
			elif cmd == 'cmove':
				ans += '23'
			elif cmd == 'cmovne':
				ans += '24'
			elif cmd == 'cmovge':
				ans += '25'
			elif cmd == 'cmovg':
				ans += '26'
			end1 = ins.find(',')
			ans += register(ins[end + 1:end1].strip()) + register(ins[end1 + 1:len(ins)].strip())
		elif cmd == 'irmovq':
			end1 = ins.find(',')
			ans += '30f' + register(ins[end1 + 1:len(ins)].strip())
			if ins[end + 1:end1].strip()[0] == '$':
				end2 = ins.find('$')
				ans += little_endian(ins[end2 + 1:end1].strip())
			else:
				ans += little_endian(Label(labels, ins[end + 1:end1].strip()))
		elif cmd == 'rmmovq':
			end1 = ins.find(',')
			end2 = ins.find('(')
			end3 = ins.find(')')
			ans += '40' + register(ins[end + 1:end1].strip()) + register(ins[end2 + 1:end3].strip()) + little_endian(
				ins[end1 + 1:end2].strip())
		elif cmd == 'mrmovq':
			end1 = ins.find('(')
			end2 = ins.find(')')
			end3 = ins.find(',')
			ans += '50' + register(ins[end3 + 1:len(ins)].strip()) + register(
				ins[end1 + 1:end2].strip()) + little_endian(ins[end + 1:end1].strip())
		elif cmd in ['addq', 'subq', 'andq', 'xorq']:
			if cmd == 'addq':
				ans += '60'
			elif cmd == 'subq':
				ans += '61'
			elif cmd == 'andq':
				ans += '62'
			elif cmd == 'xorq':
				ans += '63'
			end1 = ins.find(',')
			ans += register(ins[end + 1:end1].strip()) + register(ins[end1 + 1:len(ins)].strip())
		elif cmd in ['jmp', 'jle', 'jl', 'je', 'jne', 'jge', 'jg']:
			if cmd == 'jmp':
				ans += '70'
			elif cmd == 'jle':
				ans += '71'
			elif cmd == 'jl':
				ans += '72'
			elif cmd == 'je':
				ans += '73'
			elif cmd == 'jne':
				ans += '74'
			elif cmd == 'jge':
				ans += '75'
			elif cmd == 'jg':
				ans += '76'
			ans += little_endian(Label(labels, ins[end + 1:len(ins)].strip()))
		elif cmd == 'call':
			ans += '80' + little_endian(Label(labels, ins[end + 1:len(ins)].strip()))
		elif cmd == 'ret':
			ans += '90'
		elif cmd == 'pushq':
			ans += 'a0' + register(ins[end + 1:len(ins)].strip()) + 'f'
		elif cmd == 'popq':
			ans += 'b0' + register(ins[end + 1:len(ins)].strip()) + 'f'
		elif cmd == 'iaddq':
			end1 = ins.find(',')
			ans += 'c0f' + register(ins[end1 + 1:len(ins)].strip())
			if ins[end + 1:end1].strip()[0] == '$':
				end2 = ins.find('$')
				ans += little_endian(ins[end2 + 1:end1].strip())
			else:
				ans += little_endian(Label(labels, ins[end + 1:end1].strip()))

		if cmd in ['halt', 'nop', 'ret', '.byte']:
			now += 1
		elif cmd in ['rrmovq', 'xorq', 'andq', 'addq', 'subq', 'cmovle', 'cmovl', 'cmove', 'cmovne', 'cmovge', 'cmovg',
					 'pushq', 'popq']:
			now += 2
		elif cmd in ['call', 'jmp', 'jle', 'jl', 'je', 'jne', 'jge', 'jg']:
			now += 9
		elif cmd in ['irmovq', 'rmmovq', 'mrmovq', 'iaddq']:
			now += 10
		elif cmd == '.quad':
			now += 8
		elif cmd == '.pos':
			now = int(ins[end + 1:len(ins)].strip(), 16)
			ans = hex(now) + ': '
		elif cmd == '.align':
			x = int(ins[end + 1:len(ins)].strip(), 16)
			if now % x != 0:
				now += x - now % x
			ans = hex(now) + ': '
		codes.append(ans.ljust(28) + '| ' + line)
		if INS:
			labels = lst_labels
	return codes, now, error


if __name__ == '__main__':
	encoder("../test/new/load_forward.ys")
