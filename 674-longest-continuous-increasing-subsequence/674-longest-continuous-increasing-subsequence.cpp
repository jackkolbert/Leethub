class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int left = 0;
        int right = 0;
        
        int max_fin = 0;
        int temp_max = 1;
        while(right != nums.size() -1 ) {
            
            if(right+1 != nums.size() && nums[right] < nums[right+1]) {
                temp_max++;
            }
            else {
                temp_max = 1;
                left = right;
            }
            
            max_fin = max(temp_max, max_fin);
            right++;
        }
        return max(temp_max, max_fin);
    }
};