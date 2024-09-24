from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def common_prefix_length(str1, str2):
            # Compare characters of str1 and str2 from the start
            length = 0
            for ch1, ch2 in zip(str1, str2):
                if ch1 == ch2:
                    length += 1
                else:
                    break
            return length
        
        max_length = 0
        
        # Iterate through all pairs (x, y) from arr1 and arr2
        for num1 in arr1:
            for num2 in arr2:
                str1 = str(num1)
                str2 = str(num2)
                max_length = max(max_length, common_prefix_length(str1, str2))
        
        return max_length

sol = Solution()
arr1 = [1, 10, 100]
arr2 = [1000]

print(sol.longestCommonPrefix(arr1, arr2))

arr1 = [1, 2, 3]
arr2 = [4, 4, 4]
print(sol.longestCommonPrefix(arr1, arr2))





class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def generate_prefixes(num):
            """ Generate all possible prefixes of a number (as a string) """
            s = str(num)
            return [s[:i] for i in range(1, len(s) + 1)]

        # Step 1: Store all possible prefixes of elements in arr1 in a set
        prefixes_set = set()
        for num in arr1:
            for prefix in generate_prefixes(num):
                prefixes_set.add(prefix)

        # Step 2: Check for common prefixes from arr2 and find the longest
        max_length = 0
        for num in arr2:
            for prefix in generate_prefixes(num):
                if prefix in prefixes_set:
                    max_length = max(max_length, len(prefix))
        
        return max_length
sol = Solution()
arr1 = [1, 10, 100]
arr2 = [1000]

print(sol.longestCommonPrefix(arr1, arr2))

arr1 = [1, 2, 3]
arr2 = [4, 4, 4]
print(sol.longestCommonPrefix(arr1, arr2))


"""
Example 1:

    arr1 = [1, 10, 100]
        Prefixes of 1: ["1"]
        Prefixes of 10: ["1", "10"]
        Prefixes of 100: ["1", "10", "100"]
        prefixes_set = {"1", "10", "100"}

    arr2 = [1000]
        Prefixes of 1000: ["1", "10", "100", "1000"]

    Longest common prefix is "100", so the result is 3.


Example 2:

arr1 = [1, 2, 3]

    Prefixes: ["1"], ["2"], ["3"]
    prefixes_set = {"1", "2", "3"}
arr2 = [4, 4, 4]

Prefixes: ["4"] for each
No common prefix, so the result is 0.

"""