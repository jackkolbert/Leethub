class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.rows = len(heights)
        self.cols = len(heights[0])
    
        
        pac = set()
        atl = set()
        
        results = []
        for i in range(self.rows):
            self.dfs(i, 0, -1, heights, pac)
            self.dfs(i, self.cols - 1, -1, heights, atl)
        
        for k in range(self.cols):
            self.dfs(0, k, -1, heights, pac)
            self.dfs(self.rows - 1, k,-1, heights, atl)
            
        
        for i in range(self.rows):
            for k in range(self.cols):
                if (i, k) in atl and (i, k) in pac:
                    results.append((i,k))
                    
        return results
                    
    
    def dfs(self, row, col, prev_height, heights, sea):
        if(row < 0 or 
           row == self.rows or 
           col < 0 or
           col == self.cols or
           prev_height > heights[row][col] or
           (row, col) in sea):
            return
        
        else:
            sea.add((row, col))
            self.dfs(row+1,col,heights[row][col],heights,sea)
            self.dfs(row-1,col,heights[row][col],heights,sea)
            self.dfs(row,col+1,heights[row][col],heights,sea)
            self.dfs(row,col-1,heights[row][col],heights,sea)
            
        
        