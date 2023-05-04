class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        solution = []
        
        # for each element - run sliding window on excess
        nums.sort()
        
        prev_val = -10001
        for i in range(0, len(nums)):
            if prev_val == nums[i]:
                continue
            else:
                prev_val = nums[i]
                
                l = i+1
                r = len(nums)-1
                while(l < r):
                    if nums[i] + nums[l] + nums[r] == 0:
                        solution.append([nums[i], nums[l], nums[r]])
                        prev_l = nums[l]
                        prev_r = nums[r]
                        while l < r and prev_l == nums[l]:
                            l += 1
                        while l < r and prev_r == nums[r]:
                            r -= 1
                    elif nums[i] + nums[l] + nums[r] > 0:
                        r -= 1
                    else:
                        l += 1
        return solution
    
        