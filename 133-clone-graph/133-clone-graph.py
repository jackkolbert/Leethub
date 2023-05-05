"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        self.visited = {}
        return self.clone(node) if node else None
        
    def clone(self, node):
        
        if node.val in self.visited:
            return self.visited[node.val]
        
        else:
            copy = Node(val=node.val)
            self.visited[node.val] = copy
            for nei in node.neighbors:
                copy.neighbors.append(self.clone(nei))
            return copy
            