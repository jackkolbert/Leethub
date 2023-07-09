class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        if len(s) < 4:
            return []
        
        ret = []
        
        def dfs(curr_ip, curr_ind, dots, running):
            
            if curr_ind == len(s):
                if dots == 0 and len(running) > 0 and int(running) <= 255:
                    curr_ip += ('.' + running)
                    ret.append(curr_ip)
                return
            
            running += s[curr_ind]
            if len(running) > 3 or int(running) > 255:
                return
            
            
            
            if len(curr_ip) == 0:
                temp_ip = running
            else:
                temp_ip = curr_ip + '.' + running
            
            if running[0] == '0' and curr_ind != len(s) - 1:
                dfs(temp_ip, curr_ind+1, dots-1, '')
            else:
                dfs(temp_ip, curr_ind+1, dots-1, '')
                dfs(curr_ip, curr_ind+1, dots, running)
            

        dfs('', 0, 3, '')
        return ret