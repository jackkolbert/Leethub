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
        def generate(s, l, r):
            if len(s) == 2 * n:
                paren.append(s)
                return
            if l > n:
                return
            if r > n:
                return
            a = s + '('
            b = s + ')'
            generate(a, l + 1, r)
            generate(b, l, r + 1)
            
        generate('', 0, 0)
        
        i = 0
        while True:
            if i >= len(paren):
                break
            if validate(paren[i]) is False:
                paren.pop(i)
            else:
                i += 1
        return paren
            