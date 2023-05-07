class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        for(int i = 0; i < matrix.size(); i++) {
            for(int k = 0; k < matrix[0].size(); k++) {
                if(matrix[i][k] == 0) {
                    for(int row = 0; row < matrix.size(); row++) {
                        if(matrix[row][k] != 0) {
                            matrix[row][k] = 13001023;
                        }
                    }
                    for(int col = 0; col < matrix[0].size(); col++) {
                        if(matrix[i][col] != 0) {
                            matrix[i][col] = 13001023;
                        }
                    }
                }
            }
        }
        for(int i = 0; i < matrix.size(); i++) {
            for(int k = 0; k < matrix[0].size(); k++) {
                if(matrix[i][k] == 13001023) {
                    matrix[i][k] = 0;
                }
            }
        }
    }
};