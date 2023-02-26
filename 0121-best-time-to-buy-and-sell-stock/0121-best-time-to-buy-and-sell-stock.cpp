class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int left = 0;
        int right = 1;
        
        int diff_max = 0;
        int temp_diff = 0;
        
        int lowest_price = prices[0];
        int highest_price = prices[0];
        
        while(right < prices.size()) {
            // insight - move left whenever you see a lower left
            
            if(prices[right] < lowest_price) {
                left = right;
                lowest_price = prices[right];
                highest_price = 0;
            }
            else if(prices[right] > highest_price) {
                highest_price = prices[right];
                diff_max = max(diff_max, highest_price - lowest_price);
                std::cout << highest_price << " " << lowest_price << '\n';
            }
            right++;
        }
        return diff_max;
    }
};