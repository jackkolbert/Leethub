class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good = [0] * 3
        
        # do in order of triplet
        for trip in triplets:
            if target[0] < trip[0] or target[1] < trip[1] or target[2] < trip[2]:
                continue
            for i in range(3):
                if trip[i] == target[i]:
                    good[i] = 1
                
        count = 0 
        for i in good:
            if i == 1:
                count += 1
        return count == 3
                