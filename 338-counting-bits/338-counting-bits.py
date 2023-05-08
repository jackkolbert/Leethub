class Solution:
    def countBits(self, n: int) -> List[int]:
        
        memo = [0] * (n + 1)
        memo[0] = 0
        if n > 0:
            memo[1] = 1
        if n > 1:
            memo[2] = 1
        if n > 2:
            memo[3] = 2
        a = 4
        for i in range(4, n + 1):
            if a * 2 == i:
                a = i
            memo[i] = 1 + memo[i-a]
            
        return memo