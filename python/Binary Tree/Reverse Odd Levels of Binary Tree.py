from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left_child: Optional[TreeNode], right_child: Optional[TreeNode], level: int) -> None:
            # Base case
            if not left_child or not right_child:
                return

            # Swap values at odd levels
            if level % 2 == 1:
                left_child.val, right_child.val = right_child.val, left_child.val

            # Recursively process the next level
            dfs(left_child.left, right_child.right, level + 1)
            dfs(left_child.right, right_child.left, level + 1)

        if root:
            dfs(root.left, root.right, 1)

        return root
