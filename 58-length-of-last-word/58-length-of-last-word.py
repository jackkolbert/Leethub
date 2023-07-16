class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        parse = s.split()
         
        return len(parse[-1])