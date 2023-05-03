class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        my_sum = 0
        my_final = -1 * sys.maxsize
        for num in nums:
            my_sum += num
            my_final = max(my_sum, my_final)
            if my_sum < 0:
                my_sum = 0
        return my_final
        