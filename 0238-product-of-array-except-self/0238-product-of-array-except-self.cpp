class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
       //first 
        vector<int> left(nums.size());
        vector<int> right(nums.size());
        vector<int> ret_arr(nums.size());
        //create left array
        left[0] = 1;
        for(int i = 1; i < nums.size(); i++) {
            left[i] = left[i - 1] * nums[i - 1]; 
        }
        
        right[nums.size() - 1] = 1;
        //create right array
        for(int i = nums.size() - 2; i >= 0; i--) {
            right[i] = right[i + 1] * nums[i + 1];
        }
        
        //iterate through nums
        for(int i = 0; i < nums.size(); i++) {
            ret_arr[i] = left[i] * right[i];
        }
        
        return ret_arr;
    }
};