class Solution {
public:
    int rob(vector<int>& nums) {
        // bottom up approach - checking every single possibility path, but using memoization 
        vector<int>memo_first(nums.size(), -1);
        vector<int>memo_second(nums.size(), -1);
        
        return max(nums[0] + rob(nums, 2, memo_first, true), rob(nums, 1, memo_second, false));
    }
    
    int rob(vector<int>& nums, int start, vector<int>& memo, bool first) {
        
        if(start >= nums.size()) {
            return 0;
        }
        if(start == nums.size() - 1 && first) {
            return 0;
        }
        else if(start == nums.size() - 1 && first != true) {
            return nums[nums.size() - 1];
        }
        if(memo[start] == -1) {
            memo[start] = max(nums[start] + rob(nums, start + 2, memo, first),
                              rob(nums, start + 1, memo, first));
        }
        return memo[start];
    }
};