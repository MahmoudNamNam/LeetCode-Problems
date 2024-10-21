from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # The value of the node
        self.left = left  # Reference to the left child
        self.right = right  # Reference to the right child

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If the root is None, the tree is symmetric by definition
        if not root:
            return True
        
        # Helper function to check if two subtrees are mirror images of each other
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # Both nodes are None, so they are symmetric
            if not left and not right:
                return True
            
            # If one of the nodes is None and the other is not, they are not symmetric
            if not left or not right:
                return False
            
            # Check if the current nodes have the same value and recursively check their children
            return (left.val == right.val) and \
                   isMirror(left.left, right.right) and \
                   isMirror(left.right, right.left)
        
        # Start the comparison from the left and right children of the root
        return isMirror(root.left, root.right)

# Example usage:
# Constructing a symmetric tree:
#       1
#      / \
#     2   2
#    / \ / \
#   3  4 4  3
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))

# Create a Solution object and test the isSymmetric function
solution = Solution()
print(solution.isSymmetric(root))  # Output: True
