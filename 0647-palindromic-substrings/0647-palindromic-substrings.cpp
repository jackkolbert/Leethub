class Solution {
public:
    int countSubstrings(string s) {
        
        vector<string> palis;
        for(int i = 0; i < s.size(); i++) {
            int l_1 = i;
            int r_1 = i;
            
            // case 1 - starts from one 
            while(l_1 >= 0 && r_1 < s.size() && s[l_1] == s[r_1]) {
                palis.push_back(s.substr(l_1, r_1 - l_1 + 1));
                l_1--;
                r_1++;
            }
            
            // case 2 - expand out
            l_1 = i;
            r_1 = i+1;
            while(l_1 >= 0 && r_1 < s.size() && s[l_1] == s[r_1]) {
                palis.push_back(s.substr(l_1, r_1 - l_1 + 1));
                l_1--;
                r_1++; 
            }
        }
        return palis.size();
    }
};