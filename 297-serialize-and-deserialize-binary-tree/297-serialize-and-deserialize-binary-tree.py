# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        
        self.s = ""
        
        # node seperated by |
        # node: val, level, pos
        
        def dfs(root, level, pos):
            
            temp_str = str(root.val) + ',' + str(level) + ',' + str(pos) + '|'
            self.s += temp_str
            
            if root.left:
                dfs(root.left, level + 1, pos * 2)
            if root.right:
                dfs(root.right, level + 1, pos * 2 + 1)
        dfs(root, 0, 0)
        print(self.s[0:-1])
        return self.s[0:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # node seperated by |
        # node: val, level, pos
        if len(data) == 0:
            return None
        my_map = {}
        
        nodes = data.split('|')
        
        for node in nodes:
            value, level, pos  = node.split(',')
            level = int(level)
            pos = int(pos)
            my_map[(level, pos)]  = TreeNode(val = value)
            
            if (level-1, pos//2) in my_map:
                if pos % 2 == 0:
                    my_map[(level-1, pos//2)].left = my_map[(level, pos)]
                else:
                    my_map[(level-1, pos//2)].right = my_map[(level, pos)]
            
                    
        return my_map[(0, 0)]
                    
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))