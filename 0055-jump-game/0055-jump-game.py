class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        power = nums[0]
        curr = 0
                
        while power != 0:
            
            if power + curr >= len(nums) - 1:
                return True
            local_max_power = 0
            local_max_ind = 0
            for i in range(1, power+1): # testing candidate powers
                if i+curr < len(nums): # bounds check
                    if nums[i+curr] + i >= local_max_power:
                        local_max_power = nums[i+curr] + i
                        local_max_ind = i
                else:
                    return True
            curr += local_max_ind
            power = nums[curr]
            print("im at: " + str(curr))
            
        return False