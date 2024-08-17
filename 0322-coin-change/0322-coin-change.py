class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        memo = {}
        
        def dfs(curr):
            
            if curr in memo:
                return memo[curr]
            elif curr == 0:
                return 0
            elif curr < 0:
                return -1
            else:
                min_coins = sys.maxsize
                for coin in coins:
                    temp = dfs(curr - coin)
                    if temp == -1:
                        continue
                    else:
                        min_coins = min(temp+1, min_coins)
                if min_coins == sys.maxsize:
                    memo[curr] = -1
                    return -1
                else:
                    memo[curr] = min_coins
                    return min_coins
        return dfs(amount)
            
            