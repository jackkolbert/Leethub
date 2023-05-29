# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.count = 0
        self.dfs(root, -99999)
        return self.count  
        
    def dfs(self, root, t_max):

        if root is None:
            return
        
        print('Node: ' + str(root.val) + ',' + str(t_max))

        if root.val >= t_max:
            t_max = root.val
            self.count += 1
            print("counted")

        self.dfs(root.left, t_max)
        self.dfs(root.right, t_max)
            
        
            
        