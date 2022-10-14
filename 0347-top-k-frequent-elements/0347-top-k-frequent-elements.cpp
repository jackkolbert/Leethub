class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        priority_queue<pair<int, int>> pq;
        
        for(int i = 0; i < nums.size(); i++) {
            map[nums[i]]++;
        }
        
        for(auto &it: map) {
            pq.push(make_pair(it.second, it.first));
        }
        vector<int> ret_vec;
        for(int i = 0; i < k; i++) {
            ret_vec.push_back(pq.top().second);
            pq.pop();
        }
                         
        return ret_vec;
    }
};