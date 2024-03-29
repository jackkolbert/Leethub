# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def dfs(root):
            if root is None:
                return 9999
            
            if root.left is None and root.right is None:
                return 1
            a = dfs(root.left) + 1
            b = dfs(root.right) + 1
            
            return min(a, b)
        
        return dfs(root)