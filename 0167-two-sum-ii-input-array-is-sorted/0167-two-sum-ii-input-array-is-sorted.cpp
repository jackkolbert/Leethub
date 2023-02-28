class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;
        vector<int>ret_vec(2);
        
        while(left < right) {
            if(numbers[left] + numbers[right] == target) {
                ret_vec[0] = left + 1;
                ret_vec[1] = right + 1;
                return ret_vec;
            }
            else if(numbers[left] + numbers[right] < target) {
                left++;
            }
            else{
                right--;
            }
        }
        return ret_vec;
    }
};