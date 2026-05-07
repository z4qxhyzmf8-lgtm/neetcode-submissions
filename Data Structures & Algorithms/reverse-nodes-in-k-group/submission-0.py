# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(list):
            head = list
            node = head
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return [head, prev]

        if k == 1:
            return head

        dummy = ListNode(0, head)
        prev_root = dummy

        node = head
        counter = 0
        root = node

        while node:
            if counter < k:
                #find k group
                prev = node
                node = node.next
                counter += 1
            else:
                counter = 0

                #take k group out
                prev_root.next = None
                prev.next = None

                #reverse k group
                A = reverse(root)
                prev = A[0]

                #glue k group back in
                prev_root.next = A[1]
                A[0].next = node
                prev_root = prev
                root = node
        if counter == k:
            #take k group out
            prev_root.next = None
            prev.next = None

            #reverse k group
            A = reverse(root)
            prev = A[0]

            #glue k group back in
            prev_root.next = A[1]
            A[0].next = node
            prev_root = prev
            root = node

        return dummy.next



        