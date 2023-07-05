# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # maintain a range allowed
        
        def dfs(root, my_min, my_max):
            
            if root is None:
                return True
            
            if root.val >= my_max or root.val <= my_min:
                return False
            
            l = dfs(root.left, my_min, root.val)
            r = dfs(root.right, root.val, my_max)
            
            return l and r
        
        return dfs(root, -sys.maxsize, sys.maxsize)
            
            
        