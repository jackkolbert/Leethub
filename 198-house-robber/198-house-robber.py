class Solution:
    def rob(self, nums: List[int]) -> int:
        
        self.memo = {}
        
        return self.dfs(nums, 0, 0)
        
    def dfs(self, nums, curr_ind, curr_money):
        
        if curr_ind >= len(nums):
            return 0
        
        elif curr_ind in self.memo:
            return self.memo[curr_ind]
        
        a = self.dfs(nums, curr_ind+1, curr_money)
        b = self.dfs(nums, curr_ind+2, curr_money+nums[curr_ind]) + nums[curr_ind]
        
        self.memo[curr_ind] = max(a, b)
        return self.memo[curr_ind]
        