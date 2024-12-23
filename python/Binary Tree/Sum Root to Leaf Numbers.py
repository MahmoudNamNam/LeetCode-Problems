# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def process(cur , num):
            if not cur:
                return 0
            num = num *10 + cur.val
            if not cur.left and not cur.right:
                return num
            return process(cur.left,num)+ process(cur.right,num)
        return process(root,0)