class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        r = 0
        longest = 0
        window = 26 * [0]
        window[ord(s[0])-65] += 1


        while r < len(s):            
            # find the current leader
            leader_count = 0
            for i in range(len(window)):
                if window[i] > leader_count:
                    leader_count = window[i]
                    
            window_length = r-l+1
            if window_length > k + leader_count:
                window[ord(s[l])-65] -= 1
                l += 1
            else:
                longest = max(longest, window_length)
                r += 1
                if r < len(s):
                    window[ord(s[r])-65] += 1
        return longest

            
            
            
        
        