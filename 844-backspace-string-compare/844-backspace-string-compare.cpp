class Solution {
public:
    bool backspaceCompare(string s, string t) {
        
        int i = 0;
        while(i < s.size()) {  
            if(s[i] == '#') {
                if(i - 1 >= 0) {
                    s.erase(i - 1, 2);
                    i = i - 2;
                }
                else{
                    s.erase(i, 1);
                    i = i -1;
                }
            }
            i++;
        }
        i = 0;
        while(i < t.size()) {
            if(t[i] == '#') {
                if(i - 1 >= 0) {
                    t.erase(i - 1, 2);
                    i = i - 2;
                }
                else{
                    t.erase(i, 1);
                    i = i - 1;
                }
            }
            i++;
        }
        cout << s << " ";
        cout << t;
        if(s == t) {
            return true;
        }
        return false;
    }
};