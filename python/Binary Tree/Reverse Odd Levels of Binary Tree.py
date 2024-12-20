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

#*-> BFS

from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        level = 0

        while queue:
            # Number of nodes in the current level
            level_size = len(queue)
            current_level_nodes = []

            # Traverse the current level
            for _ in range(level_size):
                node = queue.popleft()

                # Collect nodes in current level if it's odd
                if level % 2:
                    current_level_nodes.append(node)

                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse node values at the odd level
            if current_level_nodes:
                values = [node.val for node in current_level_nodes]
                values.reverse()
                for i, node in enumerate(current_level_nodes):
                    node.val = values[i]

            # Move to the next level
            level += 1

        return root