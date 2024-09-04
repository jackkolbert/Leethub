class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        
        def dfs(r, c):
            if (r,c) in visited:
                return 
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        total = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    print('found')
                    total += 1 
                    dfs(row, col)
        return total
                
        