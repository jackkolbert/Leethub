class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        complete = 0
        arr_sum = 0
        for i in range(len(nums)):
            complete += i
            arr_sum += nums[i]
        complete += len(nums)
        
        return complete-arr_sum