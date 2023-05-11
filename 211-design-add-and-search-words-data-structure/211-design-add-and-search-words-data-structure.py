class Node:
    def __init__(self):
        self.children = [None] * 26
        self.l_letter = False
        


class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        
        temp = self.root
        for letter in word:
            ind = ord(letter) - ord('a')
            if temp.children[ind] is None:
                temp.children[ind] = Node()
            temp = temp.children[ind]
        temp.l_letter = True

    def search(self, word: str) -> bool:
        
        return self.helper(self.root, word)
        
     
    def helper(self, node, word):
        
        temp = node
        for i in range(len(word)):
            if word[i] == '.':
                for child in temp.children:
                    if child is not None:
                        print('hi')
                        if self.helper(child, word[i+1:]) is True:
                            return True
                return False
            else:
                ind = ord(word[i]) - ord('a')
                if temp.children[ind] is None:
                    return False 
                temp = temp.children[ind]
        return temp.l_letter
            
    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)