from collections import Counter
from itertools import combinations_with_replacement
from math import gcd, comb

class Solution:
    def countPairs(self, A: list[int], k: int) -> int:
        cnt = Counter(gcd(a, k) for a in A)
        output = 0

        for a, b in combinations_with_replacement(cnt, 2):
            if a * b % k == 0:
                if a == b:
                    output += comb(cnt[a], 2)  # Pairs within the same group
                else:
                    output += cnt[a] * cnt[b]  # Pairs from different groups

        return output

# Example usage:
sol = Solution()
nums1 = [1, 2, 3, 4, 5]
k1 = 2
print(sol.countPairs(nums1, k1))  # Output: 7

nums2 = [1, 2, 3, 4]
k2 = 5
print(sol.countPairs(nums2, k2))  # Output: 0


''''
Example Usage:
First Example:

nums1 = [1, 2, 3, 4, 5]
k1 = 2
GCDs with k1 are [1, 2, 1, 2, 1] leading to Counter({1: 3, 2: 2}).
Valid pairs:
(1, 2): 3 * 2 = 6 (valid pairs between different groups).
(2, 2): comb(2, 2) = 1 (valid pairs within the same group).
Total pairs: 6 + 1 = 7.


Second Example:

nums2 = [1, 2, 3, 4]
k2 = 5
GCDs with k2 are [1, 1, 1, 1] leading to Counter({1: 4}).
No valid pairs since 1 * 1 % 5 != 0.

'''