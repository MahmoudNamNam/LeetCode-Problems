from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode], res=None) -> List[int]:
        if res is None:
            res = []
        
        if not root:
            return res  
        
        res.append(root.val) 
        self.preorderTraversal(root.left, res) 
        self.preorderTraversal(root.right, res) 
        
        return res  
