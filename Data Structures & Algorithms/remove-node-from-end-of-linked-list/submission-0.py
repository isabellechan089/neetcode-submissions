# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        if n == 1:
            head = head.next
        else:
            for _ in range(n-2):
                prev = prev.next
            prev.next = prev.next.next

        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev