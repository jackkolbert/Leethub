class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        alr_rot = set()
        rotted = collections.deque()
        
        r = len(grid)
        c = len(grid[0])
        
        z_count = 0
        for i in range(r):
            for k in range(c):
                if grid[i][k] == 2:
                    rotted.append((i, k))
                if grid[i][k] == 0:
                    z_count += 1
        if z_count == r*c:
            return 0
        time = 0
        
        def dfs(i, k):
            
            if (i < 0 or i > r-1 or k < 0 or k > c-1 or (i, k) in alr_rot):
                return
            
            if grid[i][k] == 1:
                rotted.append((i, k))
                grid[i][k] = 2
            
            elif grid[i][k] == 2:
                alr_rot.add((i, k))

        while len(rotted) != 0:
            time += 1
            for i in range(len(rotted)):
                x, y = rotted.popleft()
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y-1)
                dfs(x, y+1)
        
        
        for i in range(r):
            for k in range(c):
                if grid[i][k] == 1:
                    return -1
        
        
        return time - 1
            
            
            
                    