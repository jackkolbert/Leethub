class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int>alph(26, 0);
        //cout << ('a' - 97);
        
        if(s.size() != t.size()) {return false;}
        for(int i = 0; i  < s.size(); i++) {
            alph[s[i]-97]++;
            alph[t[i]-97]--;
        }
        for(int i = 0 ; i < alph.size(); i++) {
            if(alph[i] != 0) {
                return false;
            }
        }
        
        
        return true;
    }
};