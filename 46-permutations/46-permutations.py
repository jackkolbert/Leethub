class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        # c_nums is the rest of the nums, res is current perm
        def backtrack(c_nums, res):
            if len(c_nums) == 0:
                ret.append(res.copy())
                return
                
            for i in range(len(c_nums)):
                new_list = c_nums[0:i] + c_nums[i+1:len(c_nums)]
                res.append(c_nums[i])
                backtrack(new_list, res)
                res.pop()
            
        
        backtrack(nums, [])
        return ret
        