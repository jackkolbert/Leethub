class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> ret_vec(n+1);
        
        for(int i = 1; i < n + 1; i++) {
        if(i % 3 == 0 && i % 5 == 0) {
            ret_vec[i] = "FizzBuzz";
        }
        else if (i % 3 == 0) {
            ret_vec[i] = "Fizz"; 
        }
        else if (i % 5 == 0) {
            ret_vec[i] = "Buzz";
        }
        else {
            ret_vec[i] = to_string(i);
        }
        }
        ret_vec.erase(ret_vec.begin());
        return ret_vec;
    }
};