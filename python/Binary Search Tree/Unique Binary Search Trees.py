"""
n = 0 → 1 (= nothing is one of patterns)
n = 1 → 1
n = 2 → 2
n = 3 → 5


number of left nodes = current root - 1
number of right nodes = all nodes - current root
"""


class Solution:
    def numTrees(self, n: int) -> int:
        uniq_tree = [1] * (n + 1)
        
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root -1
                right =nodes - root
                total += uniq_tree[left] * uniq_tree[right]
            uniq_tree[nodes] = total
        
        return uniq_tree[n]