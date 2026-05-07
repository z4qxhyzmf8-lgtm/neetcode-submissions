# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inv(root):
            if root.left or root.right:
                root.left, root.right = root.right, root.left
                if root.left:
                    inv(root.left)
                if root.right:
                    inv(root.right)
        if root:
            inv(root)
        return root
        