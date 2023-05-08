class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path = set()
        rows = len(board)
        cols = len(board[0])
        
        def search(r, c, w_ind):
            
            if w_ind == len(word):
                return True
            
            if (r < 0 or
                r >= rows or
                c < 0 or
                c >= cols or
                (r, c) in path
                or word[w_ind] != board[r][c]):
                return False
            
            path.add((r, c))
            res = (
                search(r + 1, c, w_ind + 1) or
                search(r - 1, c, w_ind + 1) or
                search(r, c + 1, w_ind + 1) or
                search(r, c - 1, w_ind + 1)
            )
            path.remove((r,c))
            return res
        
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for i in range(0, rows):
            for k in range(0, cols):
                if search(i, k, 0):
                    return True
                
        return False
        
            
            