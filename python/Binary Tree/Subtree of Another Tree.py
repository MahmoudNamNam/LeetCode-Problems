from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subRoot):
            # Check if two trees are the same
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            if root.val != subRoot.val:
                return False
            if not isSame(root.left, subRoot.left):
                return False
            if not isSame(root.right, subRoot.right):
                return False
            
            return  True 
        
        def isSubtreeRec(root, subRoot):
            if not root:
                return False
            # Check if the current root matches subRoot
            if isSame(root, subRoot):
                return True
            #  check left and right subtrees
            return isSubtreeRec(root.left, subRoot) or isSubtreeRec(root.right, subRoot)
        
        return isSubtreeRec(root, subRoot)
