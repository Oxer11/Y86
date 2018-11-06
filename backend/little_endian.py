# -*- coding: UTF-8 -*-

def rearrange(s):
	ans = ""
	for i in range(0,0xF,2):
		ans = s[i] + s[i+1] + ans
	return ans
