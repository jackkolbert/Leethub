class Solution:
    def numDecodings(self, s: str) -> int:
        # if theres a 0 it must be followed by and consume a number
        memo = {} 
        
        if(int(s) == 0):
            memo[0] = 0
        def dfs(ind):
            
            if (ind == len(s) - 1 and int(s[ind]) == 0):
                memo[ind] = 0
                return 0
            if ind == len(s) - 1 or ind == len(s):
                memo[ind] = 1
                return 1
            
            if ind in memo:
                return memo[ind]
            
            stuff = (int(s[ind]) * 10) + int(s[ind + 1])
            if stuff > 26: # greater than 26
                print('here1')
                if stuff % 10 == 0:
                    memo[0] = 0
                    memo[ind] = 0
                    return 0
                
                if int(s[ind + 1]) == 0:
                    memo[ind] = dfs(ind+2)
                else:
                    memo[ind] = dfs(ind+1)
                return memo[ind]
            
            elif stuff <= 26:  # less than 26 - 2 possiblies
                print('here2')
                if int(int(s[ind]) == 0):
                    print('here3')
                    memo[ind] = 0
                
                elif int(s[ind + 1]) == 0:
                    memo[ind] = dfs(ind+2)
                else:
                    memo[ind] = dfs(ind+1) + dfs(ind+2)
                return memo[ind]
            else:
                print('oops')
                return 0
            
        print(dfs(0))
        return memo[0]

            