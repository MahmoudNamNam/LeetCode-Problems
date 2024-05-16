# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return

        if not root.left and not root.right:
            if root.val == 0:
                return False
            else:
                return True

        lTree = self.evaluateTree(root.left)
        rTree = self.evaluateTree(root.right)

        if root.val == 2:
            return lTree or rTree
        else:
            return lTree and rTree
