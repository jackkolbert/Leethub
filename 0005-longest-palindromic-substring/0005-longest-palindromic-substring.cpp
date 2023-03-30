class Solution {
public:
    string longestPalindrome(string s) {
        int max_l = 0;
        int max_first = 0;
        int max_second = 0;
        for(int i = 0; i < s.size(); i++) {
            int temp_max = 1;
            int l_1 = i;
            int r_1 = i;
            
            // case 1 - outwards expansion
            while( r_1 < s.size() && l_1 >= 0 && s[l_1] == s[r_1]) {
                temp_max += 2;
                l_1--;
                r_1++;
            }
            // -1 for beginning index
            if(temp_max - 2 > max_l) {
                max_l = temp_max - 2;
                max_first = l_1+1;
                max_second = r_1-1;
            }
            
            // case 2 - center and right of center expand both ways - only if bb
            if(s[i] == s[i+1]) {
                int temp_max_2 = 2;
                int l_2 = i;
                int r_2 = i+1;
                while( r_2 < s.size() && l_2 >= 0 && s[l_2] == s[r_2]) {
                    temp_max_2 += 2;
                    l_2--;
                    r_2++;
                }
                if(temp_max_2 - 2 > max_l) {
                    max_l = temp_max_2 - 2;
                    max_first = l_2+1;
                    max_second = r_2-1;
                }
            }
        }
        return s.substr(max_first,max_second-max_first+1); 
    }
    

};