def plusOne(digits):
    i = len(digits) - 1
    while i >= 0:
        if digits[i] + 1 == 10:
            digits[i] = 0
            i -= 1
        else:
            digits[i] += 1
            break

    if digits[0] == 0:
        digits.insert(0, 1)

    return digits

if __name__ == '__main__':
    print plusOne([1,2,3])
    print plusOne([9,9,9])
    print plusOne([9,8,9])
