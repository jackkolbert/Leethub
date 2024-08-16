class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}
        
        def dfs(i):
            if i in memo:
                return memo[i] + 1
            if i >= len(nums) - 1:
                return 0
            elif nums[i] == 0:
                return 99999
            else:
                min_jumps = 99999
                for j in range(1, nums[i]+1):
                    temp_min = 9999
                    min_jumps = min(dfs(i + j), min_jumps)
                memo[i] = min_jumps
                return min_jumps + 1
        
        return dfs(0)