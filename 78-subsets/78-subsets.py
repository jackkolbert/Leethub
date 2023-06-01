class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        temp = []
        ret = [] 
        def backtrack(i):
            
            if i >= len(nums):
                ret.append(temp.copy())
                return
            
            temp.append(nums[i])
            backtrack(i+1)
            temp.pop()
            backtrack(i+1)

        backtrack(0)
        return ret