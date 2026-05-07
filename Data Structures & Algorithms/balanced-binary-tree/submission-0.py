# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [root]
        mp = {None: (0, 0)}

        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                mp[node] = (1 + max(mp[node.left][0], mp[node.left][1]), 1 + max(mp[node.right][0], mp[node.right][1]))
        
        for key in mp:
            if abs(mp[key][0] - mp[key][1]) > 1:
                return False
        return True
        