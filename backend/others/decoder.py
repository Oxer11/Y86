# -*- coding: UTF-8 -*-

def decoder(fname):
    codes = {}
    with open(fname) as fo:
        for line in fo:
            beg = line.find(":")
            end = line.find("|")
            if beg == -1: continue
            if end == -1: end = len(line)
            addr = line[0:beg]
            ins = line[beg + 1:end]
            ins = ins.strip()
            if len(ins) == 0:
                continue
            codes[int(addr,16)] = ins
    return codes

