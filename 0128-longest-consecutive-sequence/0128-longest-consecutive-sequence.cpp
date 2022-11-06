class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, bool> map;
        if(nums.size() == 0) {return 0;}
        
        int max_fin = 0;
        for(int i = 0; i < nums.size(); i++) {
            map[nums[i]] = true;
        }
        for(int i = 0; i < nums.size(); i++) {
                        int temp_max = 1;

            if(map[nums[i]-1] == true) {
                
            }
            else{
            
            while(map[nums[i]+temp_max] == true) {
                temp_max++;
            }
            }
            max_fin = max(temp_max, max_fin);
        }
        return max_fin;
    }
};