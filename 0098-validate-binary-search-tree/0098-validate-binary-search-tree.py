# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr, minVal, maxVal):
            if curr is None:
                return True
            
            valid_l = False
            valid_r = False
            
            # left branch
            if curr.left is None:
                valid_l = True
            elif curr.left.val > minVal and curr.left.val < maxVal and curr.left.val < curr.val:
                valid_l = dfs(curr.left, minVal, curr.val)                
            else:
                valid_l = False
            
            # right branch
            if curr.right is None:
                valid_r = True
            elif curr.right.val < maxVal and curr.right.val > minVal and curr.right.val > curr.val:
                valid_r = dfs(curr.right, curr.val, maxVal)
            else:
                valid_r = False

            return valid_l and valid_r
            
        return dfs(root, -sys.maxsize, sys.maxsize)
        