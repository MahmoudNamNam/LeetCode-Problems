from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root) :
        current,next_node = root , root.left if root else None
        while current and next_node:
            current.left.next = current.right
            if current.next:
                current.right.next = current.next.left
            current = current.next
            if not current:
                current = next_node
                next_node = current.left
        return root

"""
         1
      /    \
     2 ----  3
    / \    /   \
   4 -- 5-- 6 -- 7


"""


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

sol = Solution()
sol.connect(root)