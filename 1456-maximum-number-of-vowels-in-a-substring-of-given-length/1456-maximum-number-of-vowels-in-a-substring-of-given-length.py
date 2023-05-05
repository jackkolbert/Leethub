class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
    
        l = 0
        r = 0
        count = 0
        max_count = 0
        
        if s[0] in vowels:
            count += 1
        while True:
            if r - l + 1 < k:
                r += 1
                if s[r] in vowels:
                    count += 1
                    max_count = max(max_count, count)
            elif r-l + 1 == k:
                if s[l] in vowels:
                    count -= 1
                l += 1
                r += 1
                
                if r >= len(s):
                    break
                if s[r] in vowels:
                    count += 1
                    max_count = max(max_count, count)
                                
        return max_count
                        