class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> ret_vec;        
        if(p.size() > s.size()) {
            return ret_vec;
        }
        
        unordered_map<char, int> map;
        for(int i = 0; i < p.size(); i++) {
            map[p[i]]--;
        }
        
        for(int i = 0; i < s.size(); i++) {
            bool anagram = true;
            if(i >= p.size()) {
                map[s[i - p.size()]]--;
            }
            map[s[i]]++;
            for(auto& it : map) {
                if(it.second > 0 || it.second < 0) {
                    anagram = false;
                }
            }
            if(anagram == true) {
                ret_vec.push_back(i - p.size() + 1);    
            } 
        }
        return ret_vec;
    }
};