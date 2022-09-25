class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char> s_stack;
        stack<char> t_stack;
        
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == '#'&& s_stack.empty() == false) {
                s_stack.pop();
            }
            else{
                if(s[i] != '#') {
                    s_stack.push(s[i]);
                }
            }
        }
        
        for(int i = 0; i < t.size(); i++) {
            if(t[i] == '#' && t_stack.empty() == false) {
                t_stack.pop();
            }
            else{
                if(t[i] != '#') {
                    t_stack.push(t[i]);
                }
            }
        }
       
        stack<char> s_stack_copy = s_stack;
        stack<char> t_stack_copy = t_stack;
        
        while(s_stack_copy.empty() == false) {cout << s_stack_copy.top();
                                        s_stack_copy.pop();}
        std::cout << endl;
        while(t_stack_copy.empty() == false) {cout << t_stack_copy.top();
                                        t_stack_copy.pop();}
        if(s_stack.size() != t_stack.size()) {return false;}
        while(t_stack.empty() == false) {
            cout << "s: " << s_stack.top() << " " << endl;
            cout << "t: " << t_stack.top() << " " << endl;
            
            if(s_stack.top() != t_stack.top()) {
                return false;
            }
            else {
                s_stack.pop();
                t_stack.pop();
            }
        }
        return true;
    }
};