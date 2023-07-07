class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq_list = []
        groups = []
        
        for string in strs:
            freq = {}
            for let in string:
                if let in freq:
                    freq[let] += 1
                else:
                    freq[let] = 1
                
            found = False
            for i in range(len(freq_list)):
                if freq == freq_list[i]:
                    groups[i].append(string)
                    found = True
                    break
            if found is False:  
                groups.append([string])
                freq_list.append(freq)
                    
        return groups
                    