class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> map;
        
        for(int i = 0; i < s.size(); i++) {
            map[s[i]]++;
        }
        for(int k = 0; k < t.size(); k++) {
            map[t[k]]--;
        }
        for(auto& it : map) {
            if(it.second != 0) {
                return false;
            }
        }
        return true;
        
    }
};