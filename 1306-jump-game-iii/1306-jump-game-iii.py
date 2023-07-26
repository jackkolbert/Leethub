class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        memo = {}
        
        def dfs(ind, visited):
            
            if ind in visited:
                return False
            
            if ind < 0 or ind >= len(arr):
                return False
            
            if arr[ind] == 0:
                return True
            
            if ind in memo:
                return memo[ind]
            
            visited.add(ind)
            # right and left
            r = dfs(ind+arr[ind], visited)
            if r is True:
                memo[ind] = True
                return True
            
            l = dfs(ind-arr[ind], visited)
            
            if l:
                memo[ind] = True
            else:
                memo[ind] = False
            
            return l
        
        return dfs(start, set())