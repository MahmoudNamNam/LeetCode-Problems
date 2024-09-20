from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            idx = nums2.index(i) 
            found = False
            # Look for the next greater element
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > i:
                    res.append(nums2[j])
                    found = True
                    break
            if not found:
                res.append(-1)  # If no greater element is found
        return res






class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        while stack:
            next_greater[stack.pop()] = -1

        res = [next_greater[num] for num in nums1]
        return res


sol = Solution()
print(sol.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))