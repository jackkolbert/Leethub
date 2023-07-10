class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        back = -1
        k = 0
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == val:
                nums[i] = nums[back]
                back -= 1
            else:
                k += 1
                
            i -= 1
        return k