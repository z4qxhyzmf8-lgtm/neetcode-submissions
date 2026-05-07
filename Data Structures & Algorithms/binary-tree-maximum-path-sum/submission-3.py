# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(root):
            nonlocal ans
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)
            ans = max(ans, root.val + l + r, root.val, root.val + l, root.val + r)
            return max(root.val + max(l, r), root.val)
        dfs(root)
        return ans

        