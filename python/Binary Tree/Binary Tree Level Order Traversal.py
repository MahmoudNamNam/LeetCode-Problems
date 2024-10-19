from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes_queue = deque([root])
        result = []
        level = 0

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


            
            result.append(list(temp))
            level += 1  

        return result

# Example usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print(sol.levelOrder(root))
