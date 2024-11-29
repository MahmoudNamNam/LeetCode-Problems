from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        nodes_queue = deque([root])
        result = []

        while nodes_queue:
            temp = deque()
            sz = len(nodes_queue)

            for _ in range(sz):
                cur = nodes_queue.popleft()
                temp.append(cur.val)

                if cur.left:
                    nodes_queue.append(cur.left)
                if cur.right:
                    nodes_queue.append(cur.right)


            
            result.append(temp.pop())

        return result