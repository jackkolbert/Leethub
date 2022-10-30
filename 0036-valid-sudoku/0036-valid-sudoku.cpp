class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        //row check
        for(int i = 0; i < 9; i++) {
            unordered_map<char, int> temp_map;
            for(int k = 0; k < 9; k++) {
                //cout << board[i][k] << " ";
                temp_map[board[i][k]]++;
                //cout << temp_map[board[i][k]];
                if(board[i][k] != '.' && temp_map[board[i][k]] > 1) {
                    return false;
                }
            }
            //cout << endl;
        }
        
        //col check
        for(int i = 0; i < 9; i++) {
            unordered_map<char, int> temp_map;
            for(int k = 0; k < 9; k++) {
                temp_map[board[k][i]]++;
                if(board[k][i] != '.' && temp_map[board[k][i]] > 1) {
                    return false;
                }
            }
        }
        
        
        //check boxes with diagonal
        
        for(int row = 0; row < 3; row++) {
            for(int col = 0; col < 3; col++) {
                
                unordered_map<char, int> square;
                for(int i = 0; i < 3; i++) {
                    for(int k = 0; k < 3; k++) {
                        square[board[i+row * 3][k+ col * 3]]++;   
                        if(square[board[i+row * 3][k+ col * 3]] > 1 && board[i+row * 3][k+ col * 3] != '.') {
                            return false;
                        }
                    }
                }
            }
        }
        
        
        return true;
        
    }
};