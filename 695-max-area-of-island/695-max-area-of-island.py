class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        
        def area(row, col):
            if (row < 0 or col < 0 or
                row >= m or col >= n or
                grid[row][col] != 1):
                return 0
            
            grid[row][col] = -1
            left = area(row, col-1)
            right = area(row, col+1)
            up = area(row-1, col)
            down = area(row+1, col)
            
            return left+right+up+down+1
                
        max_area = 0
        for i in range(m):
            for k in range(n):
                if grid[i][k] == 1:
                    temp = area(i, k)
                    max_area = max(max_area, temp)
                    
        return max_area        