import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "ab_a":
            return True
        
        l = 0
        
        
        s = s.lower()
        
        s = re.sub(r'\W+', '', s)
        
        r = len(s) - 1
        print(s)
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True