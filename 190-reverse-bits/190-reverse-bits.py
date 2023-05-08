class Solution:
    def reverseBits(self, n: int) -> int:
        count = 0
        for i in range(0, 32):
            
            temp = n & 1
            count = count << 1
            if temp:
                count += 1
            n = n >> 1
                
        return count
            