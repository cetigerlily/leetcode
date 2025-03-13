# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        appeared = set()
        temp = head
        prev = None
        while temp:
            if temp.val not in appeared:
                appeared.add(temp.val)
                prev = temp
            else:
                prev.next = temp.next

            temp = temp.next
        return head
