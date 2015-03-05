def maxSubArray(A):
    _sum = 0
    _max = -9 * 99
    for a in A:
        _sum += a
        if _sum < 0:
            _sum = 0
        _max = max(_sum, _max)
    return _max

if __name__ == '__main__':
    print maxSubArray([-2,-1,-3,-4,-1,-2,-1,-5,-4])
