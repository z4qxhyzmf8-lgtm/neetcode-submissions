# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def Z_func(s):
            n = len(s)
            z = [0 for _ in range(n)]
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l = i
                    r = i + z[i] - 1
            return z
                

        
        s_root = ''
        s_sub = ''
        if not root:
            return False
        if not subRoot:
            return True
        
        #serialise the two trees
        stack = [root]
        while stack:
            node = stack.pop()
            s_root += '@' + str(node.val)
            
            if node.right:
                stack.append(node.right)
            else:
                s_root += '#'
            
            if node.left:
                stack.append(node.left)
            else:
                s_root += '#'
        
        stack = [subRoot]
        while stack:
            node = stack.pop()
            s_sub += '@' + str(node.val)
            
            if node.right:
                stack.append(node.right)
            else:
                s_sub += '#'
            
            if node.left:
                stack.append(node.left)
            else:
                s_sub += '#'

        #patter matching on the two obtained strings
        m = len(s_sub)
        print(s_sub, s_root)
        combined = s_sub + '|' + s_root
        n = len(combined)
        z = Z_func(combined)
        for num in z:
            if num == m:
                return True
        return False

        
        