from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(node1, node2):
            if node1 and node2:
                root = TreeNode(node1.val+node2.val)
                root.left = merge(node1.left, node2.left)
                root.right = merge(node1.right, node2.right)
                return root
            else:
                return node1 or node2
            
        return merge(root1, root2)
    


# Tree 1:       1
#              / \
#             3   2
#            /
#           5

# Tree 2:       2
#              / \
#             1   3
#              \    \
#               4    7

root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
root2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))

solution = Solution()
merged_root = solution.mergeTrees(root1, root2)

# Merged Tree:
#                3
#              /   \
#             4     5
#            / \      \
#           5   4      7
