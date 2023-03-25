class Solution {
public:
    int climbStairs(int n) {
        unordered_map<int, int> mem;
        
        return mapper(n, mem);
    }
    int mapper(int n, unordered_map<int, int>&mem) {
        if(n == 0) {
            return 1;
        }
        if(n == -1) {
            return 0;
        }
        if(mem.find(n) != mem.end()) {
            return mem[n];
        }
        else{
            mem[n] = mapper(n - 1, mem) + mapper(n - 2, mem);
            return mem[n];
        }
    }
};