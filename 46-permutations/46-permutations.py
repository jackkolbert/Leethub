class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        # c_nums is the rest of the nums, res is current perm
        def backtrack(c_nums, res):
            if len(c_nums) == 0:
                ret.append(res.copy())
                return
                
            for i in range(len(c_nums)):
                temp = c_nums.pop(0)
                res.append(temp)
                backtrack(c_nums, res)
                res.pop(len(res)-1)
                c_nums.append(temp)
            
        
        backtrack(nums, [])
        return ret
        