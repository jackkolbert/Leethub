class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # manage a top, bottom, left, and right
        # if you hit a border, shift direction
        # end hitting either two borders in a row or with num el
        
        m = len(matrix)  # dimensions
        n = len(matrix[0])
        
        top = 0  # borders
        bot = m - 1
        left = 0
        right = n -1
        
        ret_list = []
        
        r = 0  # coords
        c = 0
        
        direction = 'right' 
        
        num_elt = m*n
        while(len(ret_list) < num_elt):
            ret_list.append(matrix[r][c])
            
            if direction == 'right':
                if c == right:
                    top += 1
                    direction = 'down'
                    r += 1
                else:
                    c += 1
                    
            elif direction == 'down':
                if r == bot:
                    right -= 1
                    direction = 'left'
                    c -= 1
                else:
                    r += 1
            elif direction == 'left':
                if c == left:
                    bot -= 1
                    direction = 'up'
                    r -= 1
                else:
                    c -= 1
            elif direction == 'up':
                if r == top:
                    left += 1
                    direction = 'right'
                    c += 1
                else:
                    r -= 1
                    
        return ret_list        
            
        
        