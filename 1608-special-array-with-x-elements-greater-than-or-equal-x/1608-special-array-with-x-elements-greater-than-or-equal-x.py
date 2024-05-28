class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()
        
        gte = [0] * (len(nums) + 1)
        
        
        for x in range(len(gte)):
            for i in range(len(nums)):
                if nums[i] >= x:
                    gte[x] += 1
            if x == gte[x]:
                return x
                    
        return -1
            
        
        