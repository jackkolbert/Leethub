"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        ret_dict = {}                
        if node is None:
            return None
        return self.clone(node, ret_dict)
        
    def clone(self, node, ret_dict):
        
        # check if node taken care of already
        if node in ret_dict:
            return ret_dict[node]
        
        else:
            copy = Node(node.val)
            ret_dict[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(self.clone(nei, ret_dict))
        
            return copy 

        