class MedianFinder:

    def __init__(self):
        self.queue = []

    def addNum(self, num: int) -> None:
        self.queue.append(num)

    def findMedian(self) -> float:      
        self.queue = sorted(self.queue)
        #print(self.queue)
        s = len(self.queue)
        if s % 2 == 0:
            return (self.queue[s // 2] + self.queue[(s // 2) - 1]) / 2
        else:
            return self.queue[s // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()