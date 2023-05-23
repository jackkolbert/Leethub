class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        l = 0
        r = len(nums) - 1
        
        nums.sort()
        
        ret = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                
                temp = nums[l] + nums[i] + nums[r]
            
                if temp == 0:
                    ret.append([nums[l], nums[i], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                elif temp < 0:
                    l += 1
                elif temp > 0:
                    r -= 1
                
        return ret
                