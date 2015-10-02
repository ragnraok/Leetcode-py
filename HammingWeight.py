def hammingWeight(n):
    #str_repr = bin(n)[2:]
    #return len(filter(lambda x: x == '1', str_repr))
    ret = 0
    for i in xrange(32):
        ret += (n >> i) & 1

    return ret
