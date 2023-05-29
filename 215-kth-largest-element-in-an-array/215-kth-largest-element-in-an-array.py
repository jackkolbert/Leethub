class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, nums[i])
                
            else:
                a = heap[0] 
                
                if a < nums[i]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, nums[i])
                    
        return heap[0]
                