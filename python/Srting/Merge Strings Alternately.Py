class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately.

        Args:
            word1 (str): The first string to be merged.
            word2 (str): The second string to be merged.

        Returns:
            str: The merged string where characters from word1 and word2 are
                 alternately combined.

        Example:
            >>> solution = Solution()
            >>> solution.mergeAlternately("abc", "123")
            'a1b2c3'
            >>> solution.mergeAlternately("hello", "world")
            'hweolrllod'

        Complexity Analysis:
            - Time complexity: O(n), where n is the length of the shorter string.
            - Space complexity: O(n), where n is the length of the merged string.
        """
        merged = ''
        # Determine the length of the shorter string
        min_length = min(len(word1), len(word2))
        
        # Merge the strings alternately up to the length of the shorter string
        for i in range(min_length):
            merged += word1[i] + word2[i]
        
        # Append the remaining characters from the longer string, if any
        if len(word1) > min_length:
            merged += word1[min_length:]
        elif len(word2) > min_length:
            merged += word2[min_length:]
    
        return merged
