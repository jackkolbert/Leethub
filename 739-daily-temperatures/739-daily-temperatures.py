class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []  # holds temp, index
        stack.append((temperatures[0], 0))
        
        ret = [None] * (len(temperatures))
        
        for i in range(1, len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                ind = stack[-1][1]
                ret[ind] = i - ind
                stack.pop()
            stack.append((temperatures[i], i))
        
        for i in range(len(stack)):
            ind = stack[i][1]
            ret[ind] = 0
        return ret