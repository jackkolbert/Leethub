class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = []
        return self.work(s, wordDict, memo)
    
    def work(self, s, wordDict, memo):
        
        if len(s) == 0:
            return True
        
        for s_ind in range(1, len(s) + 1):
            # branch off - branching off too much
            if s[0:s_ind] in wordDict and s[s_ind:len(s) + 1] not in memo: 
                
                status = self.work(s[s_ind:len(s) + 1], wordDict, memo)
                if status is True:
                    return True
                else:
                    memo.append(s[s_ind:len(s) + 1])
        return False
