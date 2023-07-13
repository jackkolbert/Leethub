class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        
        def dfs(c_nums, curr_perm):
            
            if len(c_nums) == 0:
                # add tuple
                ret.add(tuple(curr_perm))
                    
            else:
                for i in range(len(c_nums)):
                    curr_perm.append(c_nums[i])
                    dfs(c_nums[0:i] + c_nums[i + 1:len(c_nums)], curr_perm)
                    curr_perm.pop(-1)
                    
        dfs(nums, [])
        return list(ret)