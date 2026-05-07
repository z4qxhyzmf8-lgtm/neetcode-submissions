# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse list
        node = head
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        node = prev
        
        #if n = 1 remove head, else remove n-th node
        if n == 1:
            next_node = node.next
            node.next = None
            root = next_node
        else:
            i = 1
            root = node
            while i < n - 1:
                i += 1
                node = node.next
            next_node = node.next
            node.next = next_node.next
            next_node.next = None

        #reverse list again
        node = root
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        node = prev

        
        return node

        
        