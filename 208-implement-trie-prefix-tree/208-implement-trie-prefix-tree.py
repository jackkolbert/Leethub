class Node:
    def __init__(self):
        self.children = [None] * 26  
        self.l_letter = False  # last letter before word

class Trie:

    def __init__(self):
        
        self.node = Node() 

    def insert(self, word: str) -> None:
        
        temp = self.node
        for letter in word:
            ind = ord(letter) - ord('a')
            if temp.children[ind] is None:
                temp.children[ind] = Node()
            temp = temp.children[ind]
        
        temp.l_letter = True


    def search(self, word: str) -> bool:
        
        temp = self.node
        for letter in word:
            ind = ord(letter) - ord('a')
            if temp.children[ind] is None:
                return False
            temp = temp.children[ind]
        if temp.l_letter == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        temp = self.node
        for letter in prefix:
            ind = ord(letter) - ord('a')
            if temp.children[ind] is None:
                return False
            temp = temp.children[ind]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)