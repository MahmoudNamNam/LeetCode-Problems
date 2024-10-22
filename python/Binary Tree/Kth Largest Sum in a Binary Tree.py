from typing import Optional, List
from collections import deque
import heapq
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        nodes_queue =deque([root])
        result=[]

        while nodes_queue:
            level_sum=0
            sz=len(nodes_queue)
            for _ in range(sz):
                cur=nodes_queue.popleft()
                level_sum+=cur.val

                if cur.left:
                    nodes_queue.append(cur.left)
                if cur.right:
                    nodes_queue.append(cur.right)
            
            result.append(level_sum)
        result.sort()
        # print(result)
        if k >len(result):
            return -1
        else: return result[-k]


# root = TreeNode(5)
# root.left = TreeNode(8)
# root.right = TreeNode(9)
# root.right.left = TreeNode(3)
# root.right.right = TreeNode(7)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(1)
# root.left.left.left = TreeNode(4)
# root.left.left.right = TreeNode(6)

root = TreeNode(605481)
root.right = TreeNode(87336)
root.right.right = TreeNode(226750)
sol = Solution()
print(sol.kthLargestLevelSum(root,1))


from typing import Optional
from collections import deque
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        nodes_queue = deque([root])
        min_heap = []

        while nodes_queue:
            level_sum = 0
            sz = len(nodes_queue)
            for _ in range(sz):
                cur = nodes_queue.popleft()
                level_sum += cur.val

                if cur.left:
                    nodes_queue.append(cur.left)
                if cur.right:
                    nodes_queue.append(cur.right)

            # Maintain a min-heap of size k
            if len(min_heap) < k:
                heapq.heappush(min_heap, level_sum)
            else:
                heapq.heappushpop(min_heap, level_sum)
        
        # If we have fewer than k level sums, return -1
        return min_heap[0] if len(min_heap) == k else -1

root = TreeNode(605481)
root.right = TreeNode(87336)
root.right.right = TreeNode(226750)

sol = Solution()
print(sol.kthLargestLevelSum(root,1))

