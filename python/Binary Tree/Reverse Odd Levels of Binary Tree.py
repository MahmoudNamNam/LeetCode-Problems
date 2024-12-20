from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left_child, right_child, lvl):
            if left_child is None or right_child is None:
                return
    
            if lvl %2== 0:
                left_child.val,right_child.val = right_child.val,left_child.val
            
            dfs(left_child.left , right_child.right , lvl+1)
            dfs(left_child.right , right_child.left , lvl+1)
        dfs(root.left,root.right,0)
        return root
