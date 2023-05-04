class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0] = 0
        for i in range(1, (amount + 1)):
            self.work(coins, i, memo)
        return memo[amount]
        
    def work(self, coins, amount, memo):
        
        if amount < 0:
            return -1
        
        if amount in memo:
            return memo[amount]
        
        min_coins = 10002
        for coin in coins:
            temp_c = self.work(coins, amount - coin, memo)
            if temp_c != -1:
                min_coins = min(min_coins, temp_c + 1)
        if min_coins != 10002: # found one
            memo[amount] = min_coins
            return memo[amount]
        else: # didn't find one
            memo[amount] = -1
            return -1