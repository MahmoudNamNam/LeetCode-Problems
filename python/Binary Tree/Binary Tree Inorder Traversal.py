from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # Recursively get the values from the left subtree
        res = self.inorderTraversal(root.left)
        
        # Add the current node's value
        res.append(root.val)
        
        # Recursively get the values from the right subtree and concatenate
        res += self.inorderTraversal(root.right)
        
        return res
