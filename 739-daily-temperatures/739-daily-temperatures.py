class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []  # holds temp, index
        stack.append((temperatures[0], 0))
        
        ret = [0] * (len(temperatures))
        
        for i in range(1, len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                ret[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))

        return ret