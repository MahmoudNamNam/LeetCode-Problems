
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def in_order(root):
            if not root:
                return []
            return in_order(root.left)+[root.val]+in_order(root.right)
        values = in_order(root) # Sorted (BST & inorder) 
        min_diff=float('inf')
        for i in range(1,len(values)):
            min_diff=min(min_diff,values[i]-values[i-1])
        return min_diff