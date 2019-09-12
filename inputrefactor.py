def numToStr(instr, sep):
    arr = instr.replace(".", " .").replace(",", " ,").replace(sep, " + ").split()
    retstr = ""

    for char in arr:
        if char == '+':
            retstr += ' '
        elif char == '.':
            retstr += '.'
        else:
            x = int(char)
            nch = chr(x + 65)
            retstr += nch
    return retstr