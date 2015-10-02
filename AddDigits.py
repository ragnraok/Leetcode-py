def addDigits(num):
    if num == 0:
        return 0
    result = num - 9 * ((num - 1) / 9)
    return result
