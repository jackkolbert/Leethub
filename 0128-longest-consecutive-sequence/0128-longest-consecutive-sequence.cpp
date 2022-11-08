class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        int fin_max = 0;
        unordered_map<int, bool>map;
        
        for(int i = 0; i < nums.size(); i++) {
            map[nums[i]] = true;
        }
        
        for(int i = 0; i < nums.size(); i++) {
            int temp_max = 1;
            if(map[nums[i] -1] != true) {
            while(map[nums[i]+temp_max] == true) {
                temp_max++;
            }
            }
            fin_max = max(temp_max, fin_max);
        }
        return fin_max;
    }
};