# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pval = p.val
        qval = q.val
        if pval > qval:
            pval, qval = qval, pval
        
        node = root
        while True:
            val = node.val
            if pval <= val  and val <= qval:
                return node
            elif val < pval:
                node = node.right
            else:
                node = node.left
             

            
        