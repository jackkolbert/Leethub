class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()
        
        gte = [0] * (len(nums) + 1)
        
        
        for x in range(len(gte)):
            for i in range(len(nums)):
                if nums[i] >= x:
                    gte[x] += 1

        for i in range(len(gte)):
            if i == gte[i]:
                return i
        return -1
            
        
        