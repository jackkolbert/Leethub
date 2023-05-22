class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_map = {}
        for i in s1:
            if i not in s1_map:
                s1_map[i] = 1
            else:
                s1_map[i] += 1
        left = 0
        right = len(s1)
        
        window = {}
        
        for i in range(0, right):
            if s2[i] in window:
                window[s2[i]] += 1
            else:
                window[s2[i]] = 1
        right -= 1
        while(True):
            
            if s1_map == window:
                return True
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                window.pop(s2[left])
            left += 1

            right +=  1
            
            if right == len(s2):
                break
                
            if s2[right] in window:
                window[s2[right]] += 1
            else:
                window[s2[right]] = 1
            
        return False
                
        
        
                
            