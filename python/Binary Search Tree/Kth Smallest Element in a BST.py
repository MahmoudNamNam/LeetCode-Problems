from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorderTraversal(root)[k-1]
    






class Solution_2:
    def __init__(self):
        self.count = 0
        self.kth_value = None

    def inorderTraversal(self, root: Optional[TreeNode], k: int) -> None:
        if not root or self.kth_value is not None:
            return
        
        self.inorderTraversal(root.left, k)
        self.count += 1
        
        if self.count == k:
            self.kth_value = root.val
            return
        
        self.inorderTraversal(root.right, k)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorderTraversal(root, k)
        return self.kth_value
