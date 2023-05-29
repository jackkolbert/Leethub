# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def dfs(level, pos, root):
            
            if root is None:
                return
            
            if level not in sight:
                sight[level] = (pos, root.val)
            else:
                if pos > sight[level][0]:
                    sight[level] = (pos, root.val)
                
            dfs(level + 1, 2*pos, root.left)
            dfs(level + 1, 2*pos + 1, root.right)
        
        sight = {}
        dfs(0, 0, root)
        ret = []
        for level in sight:
            ret.append(sight[level][1])
        return ret
        