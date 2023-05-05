"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited = {}
        return self.clone(node, visited) if node else None
        
    def clone(self, node, visited):
        
        if node.val in visited:
            return visited[node.val]
        
        else:
            copy = Node(val=node.val)
            visited[node.val] = copy
            for nei in node.neighbors:
                copy.neighbors.append(self.clone(nei, visited))
            return copy
            