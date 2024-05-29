class Solution:
    def numSteps(self, s: str) -> int:
        
        numSteps = 0
        
        while len(s) > 1:
            
            # add 1 to the end if odd
            if s[-1] == "1":
                
                add_ind = len(s) - 1
                while s[add_ind] == "1":
                    s = s[:add_ind] + '0' + s[add_ind+1:]
                    add_ind -= 1
                    if add_ind == -1:
                        s = "1" + s
                        break
            
                if add_ind != -1:
                    s = s[:add_ind] + '1' + s[add_ind+1:]
                        
            # greedily divide by 2 if possible
            else:
                s = s[0:len(s)-1]
                
            numSteps += 1
            print(s)
        
        if s == "1":
            return numSteps
        else:
            return numSteps + 1
                
            
                
            