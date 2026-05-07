"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque()
        q.append(node)
        copy_root = Node()
        mp = {1: copy_root}#val to copied node
        while q:
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                if curr.val not in mp:
                    mp[curr.val] = Node()
                mp[curr.val].val = curr.val
                for nb in curr.neighbors:
                    if nb.val not in mp:
                        q.append(nb)
                    if nb.val not in mp:
                        mp[nb.val] = Node()
                    mp[curr.val].neighbors.append(mp[nb.val])
                    
        return copy_root
        
        
        
        