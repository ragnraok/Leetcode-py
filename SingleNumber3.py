def singleNumber(nums):
    result_dict = {}
    for n in nums:
        if n not in result_dict:
            result_dict[n] = 1
        else:
            result_dict[n] += 1

    result = []
    for key in result_dict.keys():
        if result_dict[key] == 1:
            result.append(key)

    return result

def singleNumber2(nums):
    record = 0
    for n in nums:
        record ^= n

    #print bin(record), bin(-record), record
    record &= -record

    #print bin(record), record

    result = [0, 0]
    for n in nums:
        if n & record == 0:
            result[0] ^= n
        else:
            result[1] ^= n

        #print result

    return result

if __name__ == '__main__':
    print singleNumber2([1, 2, 1, 3, 2, 6])
