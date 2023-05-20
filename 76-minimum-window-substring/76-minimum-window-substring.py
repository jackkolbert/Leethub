class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # checking for possible
        map_s = {}
        for letter in s:
            if letter not in map_s:
                map_s[letter] = 1
            else:
                map_s[letter] += 1
        map_t = {}
        for letter in t:
            if letter not in map_t:
                map_t[letter] = 1
            else:
                map_t[letter] += 1
                
        for letter in t:
            if letter not in map_s:
                return ""
            if map_s[letter] < map_t[letter]:
                return ""
            
        # rest
        
        my_list = []
        
        l_min = 0
        r_min = 0
        
        l = 0
        r = 0
        
        
        
        for let in t:
            my_list.append(let)
        
        if s[0] in my_list:
            my_list.pop(my_list.index(s[0]))
        else:
            left = 1
            right = 0
            
        
        min_fin = 20000
        overkill = []
        
        
        
        while r < len(s):
            
            if len(my_list) == 0: 
                if r-l < min_fin:
                    r_min = r
                    l_min = l
                    min_fin = r-l

            if s[l] not in t:
                l += 1
                
            elif s[l] in overkill:
                overkill.pop(overkill.index(s[l]))
                l += 1
            else:
                r += 1
                if r < len(s) and s[r] in my_list:
                    my_list.pop(my_list.index(s[r]))
                elif r < len(s) and s[r] in t:
                    overkill.append(s[r])
        print(my_list)     
        if len(my_list) == 0: 
            print('fire')
            if r-l < min_fin:
                r_min = r
                l_min = l
                min_fin = r-l
        
        return s[l_min:r_min+1]
        
                
                    
                
            