class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int num = 0;
        for(int i = 0; i < grid.size(); i++) {
            for(int k = 0; k < grid[0].size(); k++) {
                if(grid[i][k] == '1') {
                    recursive(grid, i, k);
                    num++;
                }
               
            }
        }
        return num;
    }
    void recursive(vector<vector<char>>& grid, int row, int col) {
        grid[row][col] = '0';
        
        if(row + 1 < grid.size() && grid[row + 1][col] == '1') {
            recursive(grid, row + 1, col);
        }
        if(row - 1 >= 0 && grid[row-1][col] == '1') {
            recursive(grid, row-1,col);
        }
        if(col + 1 < grid[0].size() && grid[row][col+1] == '1') {
            recursive(grid, row, col + 1);
        }
        if(col - 1 >= 0 && grid[row][col-1] == '1') {
            recursive(grid, row, col - 1);
        }
        
    }
};