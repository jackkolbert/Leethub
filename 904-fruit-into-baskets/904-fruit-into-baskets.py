class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        l = 0
        r = -1
        
        counts = {}
        unique = 0
        
        my_max = 0
        while r < len(fruits):
            
            if unique <= 2:
                my_max = max(r-l+1, my_max)
            
            if r == len(fruits) - 1:
                break
            
            # grow condition
            if unique <= 2:
                r += 1
                if fruits[r] in counts:
                    if counts[fruits[r]] == 0:
                        unique += 1
                    counts[fruits[r]] += 1
                    
                else:
                    counts[fruits[r]] = 1
                    unique += 1
                
            # shrink condition
            elif unique > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    unique -= 1
                l += 1
        return my_max
                
                