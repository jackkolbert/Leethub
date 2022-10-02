class Solution {
public:
    bool isPalindrome(string s) {
        for(int i = 0; i < s.size(); i++) {
            s[i] = tolower(s[i]);
        }
        
        for(int i = 0; i < s.size(); i++) {
            if(!iswalnum(s[i])) {
                s.erase(i, 1);
                i--;
            }
        }
        cout << s;
        int left = 0;
        int right = s.size() - 1;
        while(left < right) {
            if(s[left] == s[right]) {
                left++;
                right--;
            }
            else {
                return false;
            }
        }
        return true;
    }
};