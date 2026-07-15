# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        end = head
        count = 1
        while end.next:
            end = end.next
            count+=1
        half = count//2
        prev = None
        left = head

        for i in range(half-1):
            left = left.next
        curr = left.next
        left.next = None
        while curr:
            follow = curr.next
            curr.next = prev
            prev = curr
            curr = follow

        start = head
        dummy = ListNode()
        check = dummy
        for i in range(count):
            if i %2 ==0:
                
                if start:
                    check.next = start
                    start = start.next
            else:
                
                if prev:
                    check.next = prev
                    prev = prev.next
            check = check.next
        head = dummy.next


        