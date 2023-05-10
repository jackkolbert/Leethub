class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ret = []
        left = 0
        right = 0
        for i in range(len(intervals)):
   
            if newInterval[1] < intervals[i][0]:
                ret.append(newInterval)
                return ret + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                ret.append(intervals[i])
            else:
                left = min(newInterval[0], intervals[i][0])
                right = max(newInterval[1], intervals[i][1])
                newInterval = [left, right]
        ret.append(newInterval)

        return ret
                