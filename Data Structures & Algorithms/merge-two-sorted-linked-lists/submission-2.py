# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        if node1 and node2:
            if node1.val < node2.val:
                head, node1 = node1, node1.next
            else:
                head, node2 = node2, node2.next
        elif node1:
            head, node1 = node1, node1.next
        elif node2:
            head, node2 = node2, node2.next
        else:
            return list1
        node = head 
        while node1 and node2:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
        if node1:
            node.next = node1 
        if node2:
            node.next = node2
        return head


        