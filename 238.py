def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    try:
        nums.index(0)
    except ValueError:
        return nums

    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i == count:
                count += 1
            else:
                nums[count] = nums[i]
                nums[i] = 0
                count += 1
    return nums
