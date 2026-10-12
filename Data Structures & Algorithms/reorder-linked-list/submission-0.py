# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        right = slow.next
        slow.next = None
        # reverse second half
        prev = None
        curr = right
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        right = prev

        # merge
        left = head
        while right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next
        return
            

