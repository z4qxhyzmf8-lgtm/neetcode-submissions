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
        if not head:
            return None

        new_head = Node(head.val, None, None)
        node_list = [new_head]
        node_dict = {head: new_head}
        node = head.next
        new_node = new_head

        while node:
            node2 = Node(node.val, None, None)
            node_list.append(node2)
            node_dict[node] = node2
            new_node.next = node2 
            new_node = new_node.next
            node = node.next
        
        node = head
        new_node = new_head
        while node:
            rand = node.random
            if rand:
                new_node.random = node_dict[rand]
            node = node.next
            new_node = new_node.next



        

        return new_head

                



        