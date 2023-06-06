class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def rec(i):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            else:
                a = min(rec(i+1), rec(i+2)) + cost[i]
                memo[i] = a
                return memo[i]
        
        return min(rec(0), rec(1))