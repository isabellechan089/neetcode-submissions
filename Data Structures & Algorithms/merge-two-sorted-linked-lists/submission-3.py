# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        new = ListNode()
        tail = new
        one = list1
        two = list2
        while one and two:
            if one.val <= two.val:
                tail.next = one
                one = one.next
            else:
                tail.next = two
                two = two.next
            tail = tail.next
        if not one:
            tail.next = two
        else:
            tail.next = one
        return new.next

