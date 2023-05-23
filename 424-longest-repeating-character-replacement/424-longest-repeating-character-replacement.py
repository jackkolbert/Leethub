class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        
        window = {}
        ret = 0
        window[s[0]] = 1
        
        while r < len(s):
            
            max_key = max(zip(window.values(), window.keys()))[1]
            max_key = window[max_key]
            
            window_len = r - l + 1
            
            if max_key + k >= window_len:  # valid, expand
                
                ret = max(ret, window_len) 
                r += 1
                if r == len(s):
                    break
                if s[r] in window:
                    window[s[r]] += 1
                else:
                    window[s[r]] = 1
            else:
                
                window[s[l]] -= 1
                l += 1
                
        return ret
                
            
            