class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # start from every point
        
        # memoize max branches starting on certain index
        
        # memo tracks the length of subsequence after index
        memo = {}
        index = 0
        for num in nums:
            self.work(nums, memo, index, num) # starting a new branch at every index
            index += 1
            
        return max(memo.values()) + 1 # inlcude starting pos for +1
        
    def work(self, nums, memo, index, last_num):
        
        if index in memo:
            return memo[index] # adjust to include index on return +1
        
        max_a = 0 # keeps track of however many are added after
        for i in range(index + 1, len(nums)):
            if last_num < nums[i]: # start a new branch
                temp = self.work(nums, memo, i, nums[i]) + 1
                max_a = max(max_a, temp)
        
        memo[index] = max_a
        return memo[index]
        
        
        
        
        