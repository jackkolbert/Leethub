# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.target = target
        self.ret = []
        self.k = k
        self.visited = set()
        self.find_target(root)
        return self.ret
    
    def find_target(self, root):
        if root is None:
            return (False, -1)
        elif root.val == self.target.val:
            # recurse downwards
            self.downwards(root, 0)
            self.visited.add(root.val)
            return (True, 1)
        else:
            l = self.find_target(root.left)
            r = self.find_target(root.right)
            if l[0] is True:
                self.downwards(root.right, l[1]+1)
            if r[0] is True:
                self.downwards(root.left, r[1]+1)
            
            if l[1] == self.k:
                self.ret.append(root.val)
            elif r[1] == self.k:
                self.ret.append(root.val)

            if l[0] or r[0]:
                self.visited.add(root.val)
                return (True, max(l[1], r[1])+1)
            else:
                return (False, -1)
            
            
    def downwards(self, root, distance):
        if root is None or root in self.visited:
            return (False, -1)
        elif distance == self.k:
            self.ret.append(root.val)
        else:
            self.downwards(root.left, distance+1)
            self.downwards(root.right, distance+1)
        