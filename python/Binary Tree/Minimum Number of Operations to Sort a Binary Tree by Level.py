from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        total_swaps = 0

        # Level-order traversal (BFS)
        while queue:
            level_size = len(queue)
            level_values = []

            # Collect values and enqueue children
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Calculate swaps needed to sort the current level
            total_swaps += self._get_min_swaps(level_values)

        return total_swaps

    def _get_min_swaps(self, original: list) -> int:
        swaps = 0
        target = sorted(original)
        pos = {val: idx for idx, val in enumerate(original)}

        # Swap elements to match the sorted target
        for i in range(len(original)):
            if original[i] != target[i]:
                swaps += 1
                cur_pos = pos[target[i]]

                # Swap and update positions
                pos[original[i]] = cur_pos
                original[cur_pos], original[i] = original[i], target[i]

        return swaps
