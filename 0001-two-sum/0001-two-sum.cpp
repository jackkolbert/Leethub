class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        vector<int> ret_vec(2);
        for(int i = 0; i < nums.size(); i++) {
            //store the indices in the value - key is the thing we 
            int temp = target - nums[i];
            map[temp] = i;
        }
        
        for(int k = 0; k < nums.size(); k++) {
            if(map.find(nums[k]) != map.end() && map[nums[k]] != k) {
                ret_vec[0] = map[nums[k]];
                ret_vec[1] = k;
                return ret_vec;
            }
        }
        return ret_vec;
    }
};