class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        if len(nums) == 1:
            return 1
        seqs = {}
        longest = 0
        
        for i in nums:
            seqs[i] = 1

        num_set = set(nums)
        for i in num_set:
            k = 1
            while i + k in seqs:
                temp = seqs[i+k]  
                seqs.pop(i+k)
                k += temp
            seqs[i] = k
            longest = max(k, longest)
            
        print(seqs)
        return longest
                
        
                