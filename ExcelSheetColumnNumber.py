def titleToNumber(s):
    result = 0
    #for i in s:
    #    result = result * 26 + (ord(i) - ord('A') + 1)

    pow_num = 0
    for i in reversed(s):
        result += (ord(i) - ord('A') + 1) * (26 ** pow_num)
        pow_num += 1

    return result

if __name__ == '__main__':
    print titleToNumber("A")
    print titleToNumber("Z")
    print titleToNumber("AA")
    print titleToNumber("ZZ")
    print titleToNumber("AAA")
    print titleToNumber("ZZZ")
