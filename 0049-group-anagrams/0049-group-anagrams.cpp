class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
            vector<unordered_map<char, int>> maps;
            vector<bool>already_counted(strs.size(), false);
                
            vector<vector<string>> ret_vec;
            for(int i = 0; i < strs.size(); i++) {
                unordered_map<char, int> temp_map;
                string temp_str = strs[i];

                for(int k = 0; k < strs[i].size(); k++) {
                    temp_map[temp_str[k]]++;
                }
                maps.push_back(temp_map);
            }
            for(int i = 0; i < strs.size(); i++) {
                vector<string> temp_vec;
                if(already_counted[i] == false) {
                    already_counted[i] = true;
                    temp_vec.push_back(strs[i]);
                }
                
                for(int k = i; k < strs.size(); k++) {
                    if(i != k && already_counted[k] == false) {
                        if(maps[i] == maps[k]) {
                            temp_vec.push_back(strs[k]);
                            already_counted[k] = true;
                        }
                    }
                }
                if(temp_vec.size() > 0) {
                    ret_vec.push_back(temp_vec);
                }
            }
        
            return ret_vec;
        }
};