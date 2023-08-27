class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        ret = []
        
        temp = -99999
        for i in range(len(nums) - 2):
            if nums[i] == temp:
                continue
            else:
                temp = nums[i]
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                temp_sum = nums[i] + nums[l] + nums[r]

                if temp_sum == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    temp_2 = nums[l]
                    while l < r and temp_2 == nums[l]:
                        l += 1
                elif temp_sum > 0:
                    r -= 1
                elif temp_sum < 0:
                    l += 1
        return ret
            