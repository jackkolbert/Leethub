class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i : i[0])
        ret = []
        
        left_val = intervals[0][0]
        right_val = intervals[0][1]
        for i in range(1, len(intervals)):
            
            # left_val = min(left_val, intervals[i][0])
            print([left_val, right_val])
            if right_val < intervals[i][0]:  # case of no overlap
                ret.append([left_val, right_val])
                left_val = intervals[i][0]
                right_val = intervals[i][1]
            
            elif intervals[i][0] <= right_val:  # case of overlap - hold on putting in array
                right_val = max(right_val, intervals[i][1])
                
        ret.append([left_val, right_val])
        
        return ret