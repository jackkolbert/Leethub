class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> my_set;
        
        int left = 0;
        int right = 0;
        
        int max = 0;
        
        if(s.size() == 0 || s.size() == 1) {
            return s.size();
        }
        
        while(right < s.size()) {
            int temp_size = my_set.size();
            my_set.insert(s[right]);
            if(temp_size == my_set.size()) {
                //problem
                my_set.erase(s[left]);
                left++; 
            }
            else{
                int temp_max = right - left + 1;
                if(temp_max > max) {
                    max = temp_max;
                }
                right++;
            }
        }
        return max;
    }
};