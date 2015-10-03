def moveZeros(nums):
    count = 0
    for index, val in enumerate(nums[:]):
        if val == 0:
            nums.remove(0)
            count += 1
    for _ in xrange(count):
        nums.append(0)
