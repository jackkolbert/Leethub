class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        unique_pointer = 0
        curr_val = -101
        curr_count = 0
        
        i = 0
        k = 0
        while i < len(nums):
            if nums[i] == curr_val and curr_count < 2:
                # if second instance of value
                k += 1
                curr_count += 1
                nums[unique_pointer] = nums[i]
                unique_pointer += 1
            
            elif nums[i] == curr_val and curr_count >= 2:
                # if past second instance of value
                curr_count += 1
                
            else:
                # first instance of new value
                nums[unique_pointer] = nums[i]
                curr_count = 1
                k += 1
                unique_pointer += 1
                curr_val = nums[i]
            
            i += 1
        return k