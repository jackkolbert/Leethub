# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_sum = -1001
        self.fallback = -1001
        self.found = False
        
        self.rec(root)
        if self.found is False:
            return self.fallback
        return self.max_sum

    
    def rec(self, root):
            
            if not root:
                return 0
                
            if root.val >= 0:
                self.found = True
            self.fallback = max(self.fallback, root.val)
    
            branch_sum = root.val
            left_sum = max(0, self.rec(root.left))
            right_sum = max(0, self.rec(root.right))
            self.max_sum = max(branch_sum + left_sum + right_sum, self.max_sum)
            
            return branch_sum + max(left_sum, right_sum)
                
        
        
        