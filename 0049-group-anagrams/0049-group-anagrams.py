class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        
        for i in range(len(strs)):
            temp = strs[i]
            res = ''.join(sorted(strs[i]))
            print(res)
            if res in groups:
                groups[res].append(temp)
            else:
                groups[res] = [temp]
                
        print(groups)
        return list(groups.values())
            