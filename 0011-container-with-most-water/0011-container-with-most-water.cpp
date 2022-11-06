class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max = 0;
        
        while(left < right) {
            int temp = 0;
            temp = min(height[left], height[right]) * (right - left);
            
            if(height[left] < height[right]) {
                left++;
            }
            else {
                right--;
            }
            
            if(temp > max) {
                max = temp;
            }
            
        }
        return max;
        
        
        
    }
};