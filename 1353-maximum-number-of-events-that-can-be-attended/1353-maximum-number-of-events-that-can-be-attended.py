class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        pq = []
    
        events.sort()
        endDay = 0
        endDay = max(end for start, end in events)

            
        startDay = events[0][0]
        
        count = 0
        ending_ind = 0
        for i in range(startDay, endDay+1):
            
            while ending_ind < len(events) and i == events[ending_ind][0]:
                heapq.heappush(pq, events[ending_ind][1])
                ending_ind += 1

            while len(pq) != 0 and pq[0] < i:
                heapq.heappop(pq)
            
            if len(pq) != 0:           
                a = heapq.heappop(pq)
                count += 1
        return count
        
            