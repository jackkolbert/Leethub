class Node:
    def __init__(self):
        self.end = False
        self.next = {}

class Trie:
            
    
    def __init__(self):
        self.node = Node()
        

    def insert(self, word: str) -> None:
        temp = self.node
        for letter in word:
            if letter in temp.next:
                temp = temp.next[letter]
            else:
                temp.next[letter] = Node()
                temp = temp.next[letter]
        temp.end = True
            

    def search(self, word: str) -> bool:
        temp = self.node
        for letter in word:
            if letter in temp.next:
                temp = temp.next[letter]
            else:
                return False
        return temp.end
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.node
        for letter in prefix:
            if letter in temp.next:
                temp = temp.next[letter]
            else:
                return False
        return True
                


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)