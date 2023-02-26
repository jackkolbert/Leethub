class Solution {
public:
    int characterReplacement(string s, int k) {
        
        // maintain an vector with a leader and margin of error
        int left = 0;
        int right = 1;
        int fin_max = 0;
        
        // initialize vector
        vector<int> c_window(26, 0);
        c_window[s[0]-65]++;
        c_window[s[1]-65]++;
                
        while(right < s.size()) {
            int count = 0;
            int leader = 0;
            // count up character replacement
            for(int i = 0; i < c_window.size(); i++) {
                count += c_window[i];
                leader = max(leader, c_window[i]);
            }
            if(count - leader > k) {
                c_window[s[left]-65]--;
                left++;
            }
            else {
                fin_max = max(right - left + 1, fin_max);
                right++;
                if(right < s.size()) {
                    c_window[s[right]-65]++;
                }
            }
        }
        
        return fin_max;
    }
};