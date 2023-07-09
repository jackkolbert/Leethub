class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        dupe = {}
        ret = []
        l = 0
        r = 10
        
        while r <= len(s):
            wind = s[l:r]
            if wind in dupe:
                if dupe[wind] == 1:
                    ret.append(wind)
                dupe[wind] += 1
            
            else:
                dupe[wind] = 1
                
            l += 1
            r += 1
        return ret
            