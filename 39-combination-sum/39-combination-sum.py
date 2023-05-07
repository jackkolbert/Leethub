import copy

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.results = []
        i = 0
        for num in candidates:
            self.backtrack(candidates[i:], target - num, [num])
            i += 1
        return self.results
    
    
    def backtrack(self, candidates, target, curr):
        
        if target == 0:
            a = copy.copy(curr)
            self.results.append(a)
            curr.pop()
            return
        
        elif target < 0:
            curr.pop() # take the back off
            return
        
        elif target > 0:
            i = 0
            for num in candidates:
                curr.append(num)
                self.backtrack(candidates[i:], target - num, curr)
                i += 1
            curr.pop()
            