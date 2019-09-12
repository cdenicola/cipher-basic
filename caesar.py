def caesar(instr, shift):
    #print("Input String:", instr)
    instr = instr.upper()
    newstr = ""
    for char in instr:
        if char == " " or char == ".":
            newstr += char
            continue
        ltr = ord(char) - 65
        newstr += chr(((ltr + shift) % 26) + 65)
    print("Ciphered String:", newstr)


def numToStr(instr, sep):
    arr = instr.replace(".", " .").replace(","," ,").replace(sep, " + ").split()
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


# caesar("efgfoe uif fbtu xbmm pg uif dbtumf", -1)
# caesar(numToStr("""4	18	15	 	13	19	11	 	19	3
# 22	25	13	11	4 15 14	 	19	24	 	22	11	24	17	22	15	9
# 6	11.	""", "	 	"), 15)

