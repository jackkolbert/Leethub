class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """        
        n = len(matrix) - 1  # 0 indexed

        left = 0
        right = n
        
        # 4 pointers
        t_l = [0, 0]
        t_r = [0, n]
        b_l = [n, 0]
        b_r = [n, n]
        
        temp_store = 0
        # while l is less than r
        while left < right:  # num of sub squares
            x = range(left, right)
            print(x)
            for k in range(right - left): 
                temp = matrix[t_l[0]][t_l[1]+ k]
                matrix[t_l[0]][t_l[1]+k] = matrix[b_l[0]-k][b_l[1]]

                matrix[b_l[0]-k][b_l[1]] =  matrix[b_r[0]][b_r[1]-k]

                matrix[b_r[0]][b_r[1]-k] =  matrix[t_r[0]+k][t_r[1]]

                matrix[t_r[0]+k][t_r[1]] = temp
            
            t_l[0] += 1
            t_l[1] += 1
            t_r[0] += 1
            t_r[1] -= 1
            b_r[0] -= 1
            b_r[1] -= 1
            b_l[0] -= 1
            b_l[1] += 1
            left += 1
            right -= 1
                
                
                
        
        
        
        
        