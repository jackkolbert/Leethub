# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(split_nums):
            if len(split_nums) == 0:
                return None
            
            mid = len(split_nums) // 2
            root = TreeNode(val=split_nums[mid], left=None,right=None)
            root.left = helper(split_nums[0:mid])
            root.right = helper(split_nums[mid+1:len(split_nums)])
            
            return root
        
        return helper(nums)
        