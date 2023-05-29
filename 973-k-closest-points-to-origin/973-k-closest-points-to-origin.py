class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []  # minHeap
        heapq.heapify(heap)
        # map distance to index
        for point in points:
            x = point[0]
            y = point[1]
            
            dist = x * x + y * y
            heapq.heappush(heap, (dist, point))
        
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])
            
        return ret
            
            
            