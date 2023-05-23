class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:

        
        if len(self.minHeap) == 0:
            self.minHeap.append(num)
            return
        
        if num < self.minHeap[0]:
            heapq.heappush(self.maxHeap, num * -1)
        else:
            heapq.heappush(self.minHeap, num)

        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, temp * -1)

        elif len(self.maxHeap) > len(self.minHeap) + 1:
            temp = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, temp * -1)

    def findMedian(self) -> float:
        if len(self.minHeap) == 0:
            return self.maxHeap[0] * - 1
        if len(self.maxHeap) == 0:
            return self.minHeap[0]
        
        
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
           
            return (self.minHeap[0] + (-1 * self.maxHeap[0])) / 2

        else:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return -1 * self.maxHeap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()