# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 and list2:
            if list1.val <= list2.val:
                temp = list1
                l1_remaining = list1.next
                l2_remaining = list2
            else:
                temp = list2
                l1_remaining = list1
                l2_remaining = list2.next
        elif list1:
            return list1
        else:
            return list2

        start = temp
        while l1_remaining and l2_remaining:
            if l1_remaining.val <= l2_remaining.val:
                temp.next = l1_remaining
                l1_remaining = l1_remaining.next
            else:
                temp.next = l2_remaining
                l2_remaining = l2_remaining.next
            temp = temp.next

        if l1_remaining:
            temp.next = l1_remaining
        else:
            temp.next = l2_remaining

        return start
