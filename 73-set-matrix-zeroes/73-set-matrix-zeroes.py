class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
       
        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
        
                if matrix[i][k] == 0:
                    for row in range(len(matrix)):
                        if matrix[row][k] != 0:
                            matrix[row][k] = 2147483648
                    for col in range(len(matrix[0])):
                        if matrix[i][col] != 0:
                            matrix[i][col] = 2147483648
        
        for i in range(len(matrix)):
            for k in range(len(matrix[0])):
                if matrix[i][k] == 2147483648:
                    matrix[i][k] = 0
        