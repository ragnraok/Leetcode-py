def hammingWeight(n):
    str_repr = bin(n)[2:]
    return len(filter(lambda x: x == '1', str_repr))
