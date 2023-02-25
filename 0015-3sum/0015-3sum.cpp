class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        vector<vector<int>> ret_vec;
        sort(nums.begin(), nums.end());
        
        for(int i = 0; i < nums.size() - 2; i++) {
            // do two pointer
            if (nums[i] > 0) {
                break;
            }
            if (i > 0 && nums[i - 1] == nums[i]) {
                continue;
            }
            
            int left = i+1;
            int right = nums.size() - 1;
            
            while(left < right) {
                int temp = nums[i] + nums[left] + nums[right];
                if(temp == 0) {
                    vector<int>temp_vec(3);
                    temp_vec[0] = nums[i];
                    temp_vec[1] = nums[left];
                    temp_vec[2] = nums[right];
                    ret_vec.push_back(temp_vec);
                    
                    while(left < right && nums[left] == nums[left+1]) {
                        left++;
                    }
                    left++;
                    while(left < right && nums[right] == nums[right - 1] ) {
                        right--;
                    }
                    right--;
                }
                else if(temp > 0) {
                    right--;
                }
                else if(temp < 0) {
                    left++;
                }
            }
            
        }
        return ret_vec;
    }
};