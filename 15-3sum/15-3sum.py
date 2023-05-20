class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        nums.sort()
        po = -10001
        
        for i in range(len(nums) - 2):
            if nums[i] == po:
                continue
            else:
                po = nums[i]
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                temp_res = nums[i] + nums[left] + nums[right]

                if temp_res > 0:
                    right -= 1
                elif temp_res < 0:
                    left += 1
                elif temp_res == 0:
                    
                    ret.append([nums[i], nums[left], nums[right]])
                    while left+1 < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    
            
            
        return ret
            
             