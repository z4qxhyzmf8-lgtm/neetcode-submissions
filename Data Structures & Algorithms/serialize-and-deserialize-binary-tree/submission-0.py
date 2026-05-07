# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        s = ''
        q = deque ()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node:
                    s += '@' + str(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    s += '#'
            
        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        n = len(data)
        s = data
        i = 0
        if s[i] == '#':
            return None
        i += 1
        temp = ''
        while i < n and s[i] != '#' and s[i] != '@':
            temp += s[i]
            i += 1
        root = TreeNode(int(temp), None, None)
        node = root

        q = deque()
        q.append(node)
        while i < n:
            node = q.popleft()
            count = 0
            while count < 2:
                if s[i] == '#':
                    count += 1
                    i += 1
                else:
                    count += 1
                    i += 1
                    temp = ''
                    while i < n and s[i] != '#' and s[i] != '@':
                        temp += s[i]
                        i += 1
                    if count % 2:
                        node.left = TreeNode(int(temp), None, None)
                        q.append(node.left)
                    else:
                        node.right = TreeNode(int(temp), None, None)
                        q.append(node.right)
        return root





