# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def Solve_Diameter(node):
            nonlocal diameter
            if not node:
                return 0
            left_max_depth=Solve_Diameter(node.left)
            right_max_depth=Solve_Diameter(node.right)
            diameter = max(diameter,left_max_depth+ right_max_depth)
            return max(left_max_depth,right_max_depth)+1
        Solve_Diameter(root)
        return diameter
    

# Example Usage:
# Constructing the binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

solution = Solution()
print(solution.diameterOfBinaryTree(root))  # Output: 3