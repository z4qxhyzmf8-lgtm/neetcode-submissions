# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        n1 = 0
        while node:
            n1 += 1
            node = node.next
        node = l2
        n2 = 0
        while node:
            n2 += 1
            node = node.next
        
        node1 = l1
        node2 = l2
        if n1 < n2:
            node1, node2 = l2, l1


        r = 0
        while node2:
            x = node1.val
            y = node2.val
            s = x + y + r
            node1.val = s % 10 
            if s >= 10:
                r = 1
            else:
                r = 0
            prev = node1
            node1 = node1.next
            node2 = node2.next

        while r == 1 and node1:
            x = node1.val
            s = x + r
            node1.val = s % 10
            if s >= 10:
                r = 1
            else:
                r = 0
            if node1.next is None and r:
                node1.next = ListNode(0, None)
            node1 = node1.next
        if r == 1:
            prev.next = ListNode(1, None)

        if n1 < n2:
            return l2
        else:
            return l1
        
        