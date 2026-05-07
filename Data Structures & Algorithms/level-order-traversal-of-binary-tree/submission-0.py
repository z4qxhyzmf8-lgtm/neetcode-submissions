# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        sol = []
        while q:
            temp = []
            while q:
                node = q.popleft()
                temp.append(node)
            
            for i in range(len(temp)):
                if temp[i].left:
                    q.append(temp[i].left)
                if temp[i].right:
                    q.append(temp[i].right)
                temp[i] = temp[i].val
                

            sol.append(temp)
        return sol
        
            

        