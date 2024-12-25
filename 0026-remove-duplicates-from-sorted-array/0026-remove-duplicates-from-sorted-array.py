class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        curr_ind = 0
        placement_ind = 0
        curr_value = -101
        k = 0
        
        while curr_ind < len(nums):
            
            if nums[curr_ind] != curr_value:
                # case where new value is found
                curr_value = nums[curr_ind]
                nums[placement_ind] = nums[curr_ind]
                placement_ind += 1
                k += 1
                
            curr_ind += 1
        return k