# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []
        list1 = l1
        list2 = l2
        while list1:
            arr1.append(str(list1.val))
            list1 = list1.next
        while list2:
            arr2.append(str(list2.val))
            list2 = list2.next
        num1 = int((''.join(arr1)[::-1]))
        num2 = int((''.join(arr2)[::-1]))
        res = str(num1+num2)[::-1]
        start = ListNode()
        current = start
        for char in res:
            start.next = ListNode(int(char))
            start = start.next
        return current.next
