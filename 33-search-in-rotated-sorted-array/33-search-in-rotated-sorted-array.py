class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while(l <= r):
            
            mid = ((r - l)//2) + l
            
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target < nums[mid] and target >= nums[l]:  # in left
                    r = mid-1
                else:
                    l = mid + 1
                    
            else:
                if target >= nums[mid] and target <= nums[r]:  # in right
                    l = mid + 1
                else:
                    r = mid - 1
        return -1