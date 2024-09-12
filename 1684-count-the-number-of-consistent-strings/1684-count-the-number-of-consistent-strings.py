class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        allowCount = len(words)
        for word in words:
            for char in word:
                if char not in allowed:
                    allowCount -= 1
                    break
                    
        return allowCount