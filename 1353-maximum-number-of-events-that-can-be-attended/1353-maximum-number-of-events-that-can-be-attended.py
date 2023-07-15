class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        pq = []
    
        events.sort()
        endDay = 0
        for event in events:
            endDay = max(endDay, event[1])
            
        startDay = events[0][0]
        
        count = 0
        ending_ind = 0
        for i in range(startDay, endDay+1):
            
            for k in range(ending_ind, len(events)):
                if i == events[k][0]:
                    heapq.heappush(pq, events[k][1])
                    ending_ind += 1
                else:
                    break
            
            while len(pq) != 0 and pq[0] < i:
                heapq.heappop(pq)
            
            if len(pq) != 0:           
                a = heapq.heappop(pq)
                print(a)
                count += 1
        return count
        
            