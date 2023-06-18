class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        fin_max = -sys.maxsize
        curr = 0
        for num in nums:
            curr += num
            fin_max = max(fin_max, curr)
            if curr < 0:
                curr = 0
        return fin_max
        