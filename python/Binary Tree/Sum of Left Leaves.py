class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        # Check if the root is None (empty tree)
        if not root:
            return 0
        
        # Initialize the variable to store the sum of left leaves
        ans = 0
        
        # If the root has a left child
        if root.left:
            # If the left child is a leaf node (no left or right children)
            if not root.left.left and not root.left.right:
                # Add the value of the left leaf to the sum
                ans += root.left.val
            else:
                # If the left child is not a leaf node, recursively call the function
                # to find the sum of left leaves in the left subtree
                ans += self.sumOfLeftLeaves(root.left)
        
        # Recursively call the function to find the sum of left leaves in the right subtree
        ans += self.sumOfLeftLeaves(root.right)
        
        # Return the sum of left leaves
        return ans
