from typing import Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def find(self, root: Optional[TreeNode], parent: Optional[TreeNode], value: int, depth: int = 0) -> Tuple[Optional[TreeNode], int]:
        # Base case: if the current node is None
        if not root:
            return None, -1  # Return -1 for depth if node not found
        
        # If the current node is the value we're looking for
        if root.val == value:
            return parent, depth
        
        # Search in the left subtree
        left_parent, left_depth = self.find(root.left, root, value, depth + 1)
        if left_parent:
            return left_parent, left_depth
        
        # Search in the right subtree
        return self.find(root.right, root, value, depth + 1)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        xParent, xDepth = self.find(root, None, x)
        yParent, yDepth = self.find(root, None, y)
        # Check if both nodes are at the same depth and have different parents
        return xDepth == yDepth and xParent != yParent


# Creating the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)

# Creating the solution object
sol = Solution()

# Debugging example
x = 4
y = 5

# Check if x and y are cousins
result = sol.isCousins(root, x, y)

# Output the result
print(f"Are nodes {x} and {y} cousins? {result}")


