# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None, None, None)
        node = head
        i, j = 0, 0
        n = len(preorder)
        while i < n and j < n:
            node.right = TreeNode(preorder[i], right = node.right)
            node = node.right
            i += 1
            while i < n and node.val != inorder[j]:
                node.left = TreeNode(preorder[i], right = node)
                node = node.left
                i += 1
            j += 1
            while node.right and j < n and node.right.val == inorder[j]:
                prev = node.right
                node.right = None
                node = prev
                j += 1
        return head.right
        





        return root
        