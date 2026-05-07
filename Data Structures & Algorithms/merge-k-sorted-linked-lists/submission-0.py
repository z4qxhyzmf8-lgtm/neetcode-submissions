# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwo(list1, list2):
            node1 = list1
            node2 = list2

            if node1 and not node2:
                return node1
            if node2 and not node1:
                return node2
            if (not node1) and (not node2):
                return None

            if node1.val <= node2.val:
                head = node1
                node1 = node1.next
            else:
                head = node2
                node2 = node2.next
                
            node = head
            while node1 and node2:
                if node1.val <= node2.val:
                    next1 = node1.next
                    node.next = node1
                    node1 = next1 
                else:
                    next2 = node2.next
                    node.next = node2
                    node2 = next2
                node = node.next
            if node1:
                node.next = node1
            if node2:
                node.next = node2

            return head
            
        
        n = len(lists)
        if not n:
            return None
        for i in range(1, n):
            lists[i] = mergetwo(lists[i - 1], lists[i])
            
                

        return lists[n - 1]
        



        