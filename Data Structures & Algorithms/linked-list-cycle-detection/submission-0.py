# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use a set
        # fast and slow node, O(n)
        traversed = set()
        while head:
            if head in traversed:
                return True
            traversed.add(head)
            head = head.next
        return False