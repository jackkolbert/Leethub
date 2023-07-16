class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        
        length = 0
        for k in range(len(strs[0])):
            a = strs[0][k]
            for i in range(len(strs)):    
                if length >= len(strs[i]):
                    return strs[0][0:length]
                elif a != strs[i][length]:
                    return strs[0][0:length]
                
            length += 1
        return strs[0][0:length]

            
            
            