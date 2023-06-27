class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        ret = []
        fin = 0
        diff = sys.maxsize
        
        nums.sort()
        
        for i in range(len(nums) - 2):
            
            l = i + 1
            r = len(nums) - 1
            while l < r:
                temp = nums[l] + nums[r] + nums[i]
                
                if abs(target - temp) < diff:
                    diff = abs(target - temp)
                    fin = temp
                    
                if temp == target:
                    return target
                elif temp > target:
                    r -= 1
                else:
                    l += 1
                
        return fin
        