# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.dfs(root)
        
    def dfs(self, root):

        if root is None:
            return 0
        
        else:
            l = self.dfs(root.left)
            r = self.dfs(root.right)
            if l is False or r is False:
                return False
            if abs(l - r) > 1:
                return False
            return max(l, r) + 1
            
            
        
        