def findDifference(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    """
    nums1_set = set(nums1)
    nums2_set = set(nums2)

    list1 = []
    list2 = []
    for num in nums1_set:
        if num not in nums2_set:
            list1.append(num)

    for num in nums2_set:
        if num not in nums1_set:
            list2.append(num)
    return [list1, list2]
