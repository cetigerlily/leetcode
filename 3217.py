# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # (1, ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}})

    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums_set = set(nums)

        # delete head
        temp = head
        while temp is not None and temp.next is not None:
            if temp.val in nums_set:
                temp = temp.next
            else:
                break
        print("temp:", temp)
        print("head:", head)

        # delete middle
        head = temp
        while temp is not None and temp.next is not None:
            if temp.next.val in nums_set:
                temp.next = temp.next.next
                continue
            temp = temp.next

        print("temp:", temp)
        print("head:", head)
        return head
