class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        if(s.size() == 1) {
            return 1;
        }
        
        // maintain an sliding unordered map
        unordered_map<char, int> c_map;
        
        int left = 0;
        int right = 1;
        
        c_map[s[0]]++;
        c_map[s[1]]++;
        
        int max_length = 0;
        
        while(right < s.size()) {
            while(c_map[s[right]] > 1) {
                c_map[s[left]]--;
                left++;
            }
            max_length = max(max_length, right - left + 1);
            right++;
            c_map[s[right]]++;
        }
        return max_length;
    }
};