class Solution {
public:
    bool isPalindrome(int x) {
        string eric = to_string(x);
        //cout << eric;
        int p = eric.size()-1;
        
        for(int i = 0; i < eric.size() / 2; i++) {
            if(eric[i] == eric[p]) {
                p--;
            }
            else {
                return false;
            }
        }
        return true;
    }
};