class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        let = {}
        
        for i in s:
            if i in let:
                let[i] += 1
            else:
                let[i] = 1
        
        for i in t:
            if i not in let:
                return False
            else:
                let[i] -= 1
        
        for i in let:
            if let[i] != 0:
                return False
            
        return True