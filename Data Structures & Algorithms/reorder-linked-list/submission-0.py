# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = 0 
        node = head
        #figure out length of list
        while node:
            node = node.next
            l += 1

        #save first half of list in node1
        node1 = head
        node = node1
        i = 1
        max = l // 2 if l % 2 else l // 2 - 1
        while i <= max:
            node = node.next
            i += 1

        #save second half in node2 and cut them off
        node2 = node.next
        node.next = None

        #reverse second half
        prev = None
        while node2:
            next_node = node2.next
            node2.next = prev
            prev = node2
            node2 = next_node 
        node2 = prev

        #interlink the halves
        flip = 1
        node = node1
        while node:
            if flip:
                if node1:
                    node1 = node1.next
                node.next = node2
                node = node.next
                flip = 0
            else:
                if node2:
                    node2 = node2.next
                node.next = node1
                node = node.next
                flip = 1
        




    
        