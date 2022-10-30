class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>>ret_vec;
        map<vector<int>, vector<string>>maps;
        
        for(int i = 0; i < strs.size(); i++) {
            vector<int>temp_vec(26, 0);
            
            for(int k = 0; k < strs[i].size(); k++) {
                //counting letters
                string temp_s = strs[i];
                int temp_i = temp_s[k];
                temp_i = temp_i - '0' - 49;
                //cout << temp_i << " ";
                temp_vec[temp_i] += 1;
            }
            maps[temp_vec].push_back(strs[i]);
        }
        
        for(auto &it : maps) {
            ret_vec.push_back(it.second);
        }
        
        return ret_vec;
    }
};