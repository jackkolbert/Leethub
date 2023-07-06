class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        l = 0
        r = 0
        my_max = 0
        after_zero_ind = 0
        contains_zero = False
        while r < len(nums):
            
            if nums[r] == 1:
                my_max = max(my_max, r-l)
                r += 1
                
            elif nums[r] == 0:
                if contains_zero:
                    my_max = max(my_max, r-l)
                    l = after_zero_ind
                    
                contains_zero = True
                after_zero_ind = r + 1
                r += 1
                    
        my_max = max(my_max, r-l)
        
        return my_max - 1
                    
            