class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        arr = [[0 for k in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
                
        for i in range(len(text1)-1, -1, -1):
            for k in range(len(text2)-1, -1, -1):
                
                if text1[i] == text2[k]:
                    arr[i][k] = arr[i+1][k+1] + 1
                else:
                    arr[i][k] = max(arr[i+1][k], arr[i][k+1])
        
        return arr[0][0]    