class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        min_val = 5001
        while(l <= r):
            
            mid = ((r - l)//2) + l
            
            min_val = min(min_val, nums[mid])
            
            if nums[mid] > nums[r]:  # min is in right half
                l = mid + 1
            
            elif nums[mid] < nums[l]:
                r = mid - 1
            else:
                r = mid - 1
                
        return min_val