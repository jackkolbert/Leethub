class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        fin = 0
        time = 0
        for i in range(len(timeSeries)-1):
            time = timeSeries[i]
            if time + duration <= timeSeries[i+1]:
                fin += duration
            else:
                fin += timeSeries[i+1]-time
            
            
        fin += duration
        return fin
    