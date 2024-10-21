from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None

        root = TreeNode(preorder.pop(0))
        pos = inorder.index(root.val)

        root.left = self.buildTree(preorder, inorder[:pos])
        root.right = self.buildTree(preorder, inorder[pos + 1:])

        return root


class Solution:
    def buildTree(self, preorder, inorder):
        preorder = deque(preorder)  
        
        def helper(inorder):
            if not inorder:
                return None

            root = TreeNode(preorder.popleft())  
            pos = inorder.index(root.val)

            root.left = helper(inorder[:pos])
            root.right = helper(inorder[pos + 1:])

            return root
        
        return helper(inorder)
