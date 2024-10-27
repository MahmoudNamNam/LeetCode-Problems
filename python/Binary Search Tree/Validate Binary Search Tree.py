from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
        if not root:
            return True
        
        if not (low < root.val < high):
            return False
        
        return (self.isValidBST(root.left, low, root.val) and
                self.isValidBST(root.right, root.val, high))


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode], result: Optional[List[int]] = None) -> List[int]:
        if result is None:
            result = []
        # In-order: Left, Root, Right
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.val)
            self.inorderTraversal(root.right, result)
        return result
    def isValidBST(self, root: Optional[TreeNode], low=float('-inf'), high=float('inf')) -> bool:
        lst = self.inorderTraversal(root)
        for idx in range(1,len(lst)):
            if lst[idx-1]>=lst[idx]:
                return False
        return True