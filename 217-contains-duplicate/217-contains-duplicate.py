class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        my_dict = {}
        for i in nums:
            if i in my_dict:
                return True
            my_dict[i] = True
            
        return False