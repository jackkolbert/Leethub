import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        self.path = []
        for i in range(len(board)):
            for k in range(len(board[0])):
                if self.search(board, word, 0, i, k, path):
                    return True
        return False             
                    
    def search(self, board, word, w_ind, r, c, path):

        if w_ind == len(word):
            print('fire')
            return True
        
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or word[w_ind] != board[r][c] or (r, c) in self.path:
            return False
        
        self.path.append((r, c))
        up = self.search(board, word, w_ind + 1, r + 1, c, path)  # up
        down = self.search(board, word, w_ind + 1, r - 1, c, path)  # down
        left = self.search(board, word, w_ind + 1, r, c + 1, path)  # left
        right = self.search(board, word, w_ind + 1, r, c - 1, path)  # right
        
        self.path.pop()
        return up or left or down or right
