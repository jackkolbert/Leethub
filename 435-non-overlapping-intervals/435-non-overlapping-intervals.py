class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        count = 0
        # consecutive overlap
        right_val = intervals[0][1]
        
        for i in range(1, len(intervals)):
            
            if right_val > intervals[i][0]:
                count += 1
                right_val = min(intervals[i][1], right_val)
            else:
                right_val = intervals[i][1]
            
    
        return count
        
        