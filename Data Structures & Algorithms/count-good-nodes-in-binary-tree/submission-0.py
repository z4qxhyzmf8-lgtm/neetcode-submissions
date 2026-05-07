# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [root]
        dict = {root: root.val}
        sol = 1
        while stack:
            node = stack.pop()
            if node.left:
                dict[node.left] = max(node.left.val, dict[node])
                if dict[node.left] == node.left.val:
                    sol += 1
                stack.append(node.left)
            if node.right:
                dict[node.right] = max(node.right.val, dict[node])
                if dict[node.right] == node.right.val:
                    sol += 1
                stack.append(node.right)
        return sol
            
        