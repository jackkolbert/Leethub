class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict_list = []
        
        ret = []
        
        for s in strs:
            my_dict = {}
            for let in s:
                if let not in my_dict:
                    my_dict[let] = 1
                else:
                    my_dict[let] += 1
            
            found = False
            for i in range(len(dict_list)):
                if my_dict == dict_list[i]:
                    ret[i].append(s)
                    found = True
            if found == False:
                dict_list.append(my_dict)
                ret.append([s])
            
        return ret
                    
                    
            