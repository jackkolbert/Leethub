class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        
        def dfs(pos, cool):
            
            if pos >= len(nums):
                return 0
            
            if cool is True:
                return dfs(pos+1, False)
            
            if pos in memo:
                return memo[pos]
            
            # steal
            op1 = dfs(pos+1, True) + nums[pos]
            # don't steal
            op2 = dfs(pos+1, False)
            
            memo[pos] = max(op1, op2)
            return memo[pos]
        
        return dfs(0, False)