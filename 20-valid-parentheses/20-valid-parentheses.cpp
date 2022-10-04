class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        if(s.size() % 2 != 0) {return false;}
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[') {
                stack.push(s[i]);
            }
            else {
                if(stack.size() == 0) {
                    return false;
                }
                if(s[i] == ')' && stack.top() == '(') {
                    stack.pop();    
                }
                else if (s[i] == '}' && stack.top() == '{') {
                    stack.pop();
                }
                else if (s[i] == ']' && stack.top() == '[') {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
        }
        if(stack.size() != 0) {
            return false;
        } 
        return true;
    }
};