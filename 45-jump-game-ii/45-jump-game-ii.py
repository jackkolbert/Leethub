class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}
        def dfs(ind):
            
            if ind in memo:
                return memo[ind]
            
            if ind > len(nums) - 1:
                return -1
            
            if ind == len(nums) - 1:
                return 0
            
            if nums[ind] == 0:
                memo[ind] = -1
                return -1
            
           
            
            local_min = sys.maxsize
            found = False
            for i in range(ind+1,nums[ind]+ind+1):
                res = dfs(i) 
                if dfs(i) > -1:
                    found = True
                    local_min = min(local_min, res)
            
            if found == False:
                memo[ind] = -1
                return -1
            
            memo[ind] = local_min + 1
            return memo[ind]
            
            
            
        return dfs(0)
        