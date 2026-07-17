"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        start = Node(0)
        new = start
        og = head
        meta = {None:None}
        while og:
            start.next = Node(og.val)
            meta[og] = start.next
            og = og.next
            start = start.next
        start = new.next
        while start:
            start.random = meta[head.random]
            head = head.next
            start = start.next
        return new.next

        
