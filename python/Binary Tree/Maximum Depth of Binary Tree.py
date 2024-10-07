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