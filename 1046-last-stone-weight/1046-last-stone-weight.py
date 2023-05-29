class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)        
        while(len(stones) > 1):
            a = heapq.heappop(stones) * -1
            b = heapq.heappop(stones) * -1
            
            if a > b:
                heapq.heappush(stones, b-a)
            elif a < b:
                heapq.heappush(stones, a-b)
                               
        if len(stones) == 1:
            return -1 * stones[0]
        return 0