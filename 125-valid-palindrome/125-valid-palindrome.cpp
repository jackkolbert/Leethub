class Solution {
public:
    bool isPalindrome(string s) {

        int left = 0;
        int right = s.size() - 1;
        while(left < right) {
            if(!iswalnum(s[left])) {
                left++;
                continue;
            }
            if(!iswalnum(s[right])) {
                right--;
                continue;
            }
            
            if(tolower(s[left]) == tolower(s[right])) {
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