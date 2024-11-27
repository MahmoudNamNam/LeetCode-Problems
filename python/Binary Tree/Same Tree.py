# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def sameTreeRec(p,q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            
            if p.val != q.val:
                return False
            isSameLeftSubTree =  sameTreeRec(p.left,q.left)
            isSameRightSubTree=sameTreeRec(p.right,q.right)
            return isSameLeftSubTree and isSameRightSubTree
        return sameTreeRec(p,q)