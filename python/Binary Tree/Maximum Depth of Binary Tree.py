# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        left_depth = self.maxDepth(node.left)
        right_depth = self.maxDepth(node.right)
        
        return 1 + max(left_depth, right_depth)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.left.right= TreeNode(15)
root.right.right = TreeNode(9)

sol = Solution()
print(sol.maxDepth(root))