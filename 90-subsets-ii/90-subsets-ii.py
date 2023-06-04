class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # keep track of subset as a dict
        ret = []
        def backtrack(i, curr):
            if i == len(nums):
                if curr not in ret:
                    ret.append(curr.copy())
                return
            else:
                if nums[i] in curr:
                    curr[nums[i]] += 1
                else:
                    curr[nums[i]] = 1
                backtrack(i+1, curr)
                curr[nums[i]] -= 1
                if curr[nums[i]] == 0:
                    curr.pop(nums[i])
                backtrack(i+1, curr)
            
        backtrack(0, {})
        ret_2 = []
        for dic in ret:
            temp = []
            for key in dic:
                for i in range(dic[key]):
                    temp.append(key)
            ret_2.append(temp)
            
        return ret_2