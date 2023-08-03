class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        res = []
        def backtrack(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            for digit in digitToChar[digits[i]]:
                backtrack(i+1, curr + digit)
            
        backtrack(0, "")
        return res