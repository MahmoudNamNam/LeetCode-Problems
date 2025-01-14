from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common_array = [0] * n

        elements_in_A, elements_in_B = set(), set()

        for current_index in range(n):
            # Add current elements from A and B to respective sets
            elements_in_A.add(A[current_index])
            elements_in_B.add(B[current_index])

            # Count common elements using set intersection
            common_count = len(elements_in_A & elements_in_B)

            # Store the count of common elements for the current prefix
            prefix_common_array[current_index] = common_count

        return prefix_common_array


sol = Solution()

print(sol.findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4]))
print(sol.findThePrefixCommonArray(A = [2,3,1], B = [3,1,2]))