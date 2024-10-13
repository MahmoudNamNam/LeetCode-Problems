from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.Height(root) >= 0

    def Height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        leftheight = self.Height(root.left)
        rightheight = self.Height(root.right)
        
        # Check if the left or right subtree is unbalanced
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1
        
        # Return the height of the tree
        return max(leftheight, rightheight) + 1


# Usage example
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.isBalanced(root))  # Output: (balanced tree)

# Unbalanced tree example
root_unbalanced = TreeNode(1)
root_unbalanced.right = TreeNode(2)
root_unbalanced.right.right = TreeNode(3)

print(solution.isBalanced(root_unbalanced))  # Output:  (unbalanced tree)

