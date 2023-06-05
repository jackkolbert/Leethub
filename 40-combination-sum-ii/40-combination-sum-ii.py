class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        print(candidates)
        ret = []
        
        def backtrack(nums, res, curr):
            if curr == 0:    
                ret.append(res.copy())
                return            
            elif curr < 0:
                return
            elif len(nums) == 0:
                return
            else:
                res.append(nums[0])
                backtrack(nums[1:], res, curr - nums[0])
                prev = res.pop()
                while len(nums) > 1 and prev == nums[1]:
                    nums.pop(1)
                backtrack(nums[1:], res, curr)
            
            
        backtrack(candidates, [], target)
        return ret