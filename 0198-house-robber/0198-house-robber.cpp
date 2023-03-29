class Solution {
public:
    int rob(vector<int>& nums) {
        // skip over a house if the next two combined are worth less
        
        vector<int>memo(nums.size(), -1);
        return max(nums[0] + rob(nums, 2, memo), rob(nums, 1, memo));
    }
    
    int rob(vector<int>& nums, int start, vector<int>& memo) {
        if(start >= nums.size()) {
            return 0;
        }
        else{
            if(memo[start] == -1) {
                memo[start] = max(nums[start] + rob(nums, start + 2, memo),
                                  rob(nums, start + 1, memo));
            }
            return memo[start];
        }
    }
};