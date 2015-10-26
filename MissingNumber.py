def missingNumber(nums):
    n = len(nums)
    sum_len = sum(nums)
    sum_n = sum([x for x in xrange(n + 1)])
    return sum_n - sum_len

if __name__ == '__main__':
    missingNumber([0, 1, 3])

