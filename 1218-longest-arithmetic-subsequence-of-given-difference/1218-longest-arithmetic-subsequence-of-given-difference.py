class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        # stores next val with, count 
        memo = {}
        k = difference
        for i in range(len(arr)):
            memo[arr[i]] = 0
        
        fin_max = 0
        for i in range(len(arr)):
            count = 0
            memo[arr[i] + k] = memo[arr[i]] + 1
            fin_max = max(fin_max, memo[arr[i] + k])
            
        return fin_max
            
                    
                    