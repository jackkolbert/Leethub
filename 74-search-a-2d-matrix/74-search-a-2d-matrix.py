class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        m = len(matrix)  # num rows - 3
        n = len(matrix[0])  # num cols - 4
        
        r = m * n - 1

        
        while l <= r:
            
            mid = (r - l) // 2 + l
            
            row = mid // n
            col = mid % n
            
            temp = matrix[row][col]
            
            if temp == target:
                return True
            elif temp > target:
                r = (row * n) + col - 1
                
            else:
                l = (row * n) + col + 1
            
        return False
            
            
            