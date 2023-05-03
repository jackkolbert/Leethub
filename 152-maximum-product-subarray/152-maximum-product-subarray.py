class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        prod = 1
        max_prod = 0
        
        # left traversal
        for num in nums:
            if num != 0:
                prod *= num
                max_prod = max(prod, max_prod)
            else:
                prod = 1
        
        prod = 1
        for num in reversed(nums):
            if num != 0:
                prod *= num
                max_prod = max(prod, max_prod)
            else:
                prod = 1
        
        return max_prod 