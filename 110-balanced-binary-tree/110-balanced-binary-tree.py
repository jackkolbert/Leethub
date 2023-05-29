# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.status = True
        self.height(root)
        return self.status
        
    def height(self, root):
        
        if root is None:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        if left - right > 1 or left - right < -1:
            self.status = False
        
        return max(left,right) + 1
            