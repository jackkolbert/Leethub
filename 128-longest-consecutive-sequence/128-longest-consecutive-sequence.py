class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        my_set = set()
        max_seq = 0
        
        for num in nums:
            my_set.add(num)
            
        for num in nums:
            
            
            if num-1 in my_set:
                continue
            else:
                temp = num
                count = 1
                while temp+1 in my_set:
                    count += 1
                    temp += 1
                max_seq = max(count, max_seq)
                
        return max_seq
            
                
            
            
            
            
        
            
        
            
        
            