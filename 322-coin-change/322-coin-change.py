class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        memo[0] = 0
        def dfs(amount):
            
            if amount in memo:
                return memo[amount]
        
            if amount < 0:
                return -1
        
            g_min = sys.maxsize
            found = False
            
            for coin in coins:
                temp = dfs(amount - coin)
                if temp != -1:
                    g_min = min(g_min, temp)
                    found = True
            if found == False:
                memo[amount] = -1
                return -1
            memo[amount] = g_min + 1
            return memo[amount]
            
        
        for i in range(1, amount + 1):
            dfs(i)

        return memo[amount]
            
                