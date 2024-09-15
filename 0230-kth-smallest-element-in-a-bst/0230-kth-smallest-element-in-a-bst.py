# Definition for a binary tree node.
# class TreeNode:
# def init(self, val=0, left=None, right=None):
# self.val = val
# self.left = left
# self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.currK = 0
        self.finalValue = 0

        def recursiveTreeTraversal(currNode):

            if currNode:
                recursiveTreeTraversal(currNode.left)
            else:
                return
            self.currK += 1
            print(self.currK)
            
            if self.currK == k:
                print("Kth smallest value:", currNode.val)
                
                self.finalValue = currNode.val
                self.currK += 1
                return

            if currNode.right:
                recursiveTreeTraversal(currNode.right)

        recursiveTreeTraversal(root)

        return self.finalValue
