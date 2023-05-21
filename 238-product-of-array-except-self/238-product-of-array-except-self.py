class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        sum_arr = [1] * len(nums)
        
        running = 1
        
        for i in range(len(nums)):
            sum_arr[i] *= running
            running *= nums[i]
            
        running = 1
        for k in reversed(range(len(nums))):
            sum_arr[k] *= running
            running *= nums[k]
            
        return sum_arr