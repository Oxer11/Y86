def decode(fname):
    codes = {}
    with open(fname) as fo:
        for line in fo:
            beg = line.find(":")
            end = line.find("|")
            if beg == -1:
                continue
            addr = line[0:beg]
            ins = line[beg + 1:end]
            ins = ins.strip()
            if len(ins) == 0:
                continue
            codes[addr] = ins
    return codes
