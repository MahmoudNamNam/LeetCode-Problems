from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Count occurrences of each number
        counter = Counter(nums)
        
        # Step 2: Sort Counter items by counts in descending order
        sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        
        # Step 3: Take the first k items from the sorted list and extract their keys
        result = [item[0] for item in sorted_items[:k]]
        
        # Step 4: Return the result
        return result


nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
solution = Solution()
print(solution.topKFrequent(nums1, k1))  # Output: [1, 2]

nums2 = [1]
k2 = 1
print(solution.topKFrequent(nums2, k2))  # Output: [1]




from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        
        # Extract only the elements, ignoring the frequencies
        return [element for element, frequency in counter.most_common(k)]
