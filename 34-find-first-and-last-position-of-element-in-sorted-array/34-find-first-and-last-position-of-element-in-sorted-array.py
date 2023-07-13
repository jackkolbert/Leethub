class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(nums)-1
        
        # find instance target
        targ_ind = -1
        while l <= r:
            m = (r-l) // 2 + l
            if nums[m] == target:
                targ_ind = m
                break
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        if targ_ind == -1:
            return [-1, -1]
        # find start
        l = 0
        r = targ_ind
        start = -1
        while l <= r:
            m = (r-l) // 2 + l
            if nums[m] == target:
                start = m
                r = m -1 
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        # find end
        l = targ_ind
        r = len(nums) - 1
        end = -1
        found = False
        while l <= r:
            m = (r-l) // 2 + l
            if nums[m] == target:
                end = m
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
                
        return [start, end]
        
                