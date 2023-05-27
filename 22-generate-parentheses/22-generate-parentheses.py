class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
            
        def validate(s):
            stack = []
            for let in s:
                if let == '(':
                    stack.append(')')
                elif let == ')':
                    if len(stack) == 0 or stack.pop() != ')':
                        return False
            if len(stack) != 0:
                return False
            return True
        
        paren = []
        def generate(s):
            if len(s) == 2 * n:
                paren.append(s)
                return
            a = s + '('
            b = s + ')'
            generate(a)
            generate(b)
            
        generate('')
        
        ret = []
        for par in paren:
            if validate(par):
                ret.append(par)
        return ret
            