class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        my_set = set(nums)
        max_seq = 0
            
        for num in nums:
            if num-1 not in my_set:
                count = 1
                while num+1 in my_set:
                    count += 1
                    num += 1
                max_seq = max(count, max_seq)
                
        return max_seq
            
                
            
            
            
            
        
            
        
            
        
            