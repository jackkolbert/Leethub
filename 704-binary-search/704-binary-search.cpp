class Solution {
public:
    int search(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int mid = (high - low) / 2 + low;
        while(low <= high) {
            if(target == nums[mid]) {
                return mid;
            }
            else if (target > nums[mid]) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
            mid = (high - low) / 2 + low;
        }
        return -1;
       
        
    }
};