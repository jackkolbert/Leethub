class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        count = 0
        i = 0
        while i < len(intervals) - 1:
            
            if intervals[i][1] > intervals[i+1][1]:
                intervals.pop(i)
                count += 1
            elif intervals[i][1] > intervals[i+1][0]:
                intervals.pop(i+1)
                count += 1

            else:
                i += 1
        return count