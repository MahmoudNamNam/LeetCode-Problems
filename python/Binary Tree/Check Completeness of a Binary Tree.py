# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q= deque([root])

        while q:
            node = q.popleft()

            if node:
                q.append(node.left)
                q.append(node.right)
            else:
                while q:
                    if q.popleft():
                        return False
        return True
    

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(6)
root.left.right = TreeNode(5)
root.left.left = TreeNode(4)

sol = Solution()
print(sol.isCompleteTree(root))
