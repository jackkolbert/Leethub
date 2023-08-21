class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ret = []
        def backtrack(pos, c_sum, curr_nums):
            if c_sum > target:
                return
            elif c_sum == target:
                ret.append(curr_nums.copy())
            else:
                for i in range(pos, len(candidates)):
                    curr_nums.append(candidates[i])
                    backtrack(i, c_sum+candidates[i], curr_nums)
                    curr_nums.pop()
            
        backtrack(0, 0, [])
        return ret