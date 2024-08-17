class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        memo = {}
        def dfs(curr):
            if curr == 0:
                return 0
            elif curr < 0:
                return -1
            elif curr in memo:
                return memo[curr]
            else:
                local_min = sys.maxsize
                found = False
                for coin in coins:
                    temp_steps = dfs(curr - coin)
                    if temp_steps == -1:
                        continue
                    else:
                        found = True
                        local_min = min(local_min, temp_steps)
                if found:
                    memo[curr] = local_min + 1
                    return local_min + 1 
                else:
                    memo[curr] = -1
                    return -1
        
        return dfs(amount)
            
            