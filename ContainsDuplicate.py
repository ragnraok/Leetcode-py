def containsDuplicate(nums):
    if len(nums) == 0 or len(nums) == 1:
        return False
    nums = sorted(nums)
    for i in xrange(0, len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False
