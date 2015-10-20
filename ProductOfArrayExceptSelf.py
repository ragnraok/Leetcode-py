def productExceptSelf(nums):
    if nums is None or len(nums) == 0:
        return nums
    result = []
    current = 1
    for i in xrange(len(nums)):
        result.append(current)
        current = current * nums[i]

    current = 1
    for i in xrange(len(nums)-1, -1, -1):
        result[i] = current * result[i]
        current = current * nums[i]

    return result

if __name__ == '__main__':
    print productExceptSelf([2, 3, 4, 5])
