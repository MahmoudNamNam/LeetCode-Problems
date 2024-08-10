from typing import List
import collections

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # If the string or the list of words is empty, return an empty list
        if not s or not words:
            return []

        # Length of each word (all words are assumed to be the same length)
        word_length = len(words[0])
        # Total length of the concatenated string we need to find (all words combined)
        total_length = len(words) * word_length
        # List to store the starting indices of valid substrings
        result = []
        # Dictionary to store the frequency count of each word in 'words'
        word_count = {}

        # Populate the word_count dictionary with the frequency of each word
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        # Iterate over possible starting points in 's' that align with word boundaries
        for i in range(word_length):
            left = i  # Initialize the left boundary of the sliding window
            sub_count = {}  # Dictionary to count words in the current window
            count = 0  # Counter to track the number of words matched in the current window

            # Expand the sliding window by moving 'right' in steps of 'word_length'
            for j in range(i, len(s) - word_length + 1, word_length):
                # Extract a word of length 'word_length' from 's'
                sub_word = s[j:j + word_length]

                # If the extracted word is in 'word_count' (i.e., part of the 'words' list)
                if sub_word in word_count:
                    # Increment the count of this word in the current window
                    if sub_word in sub_count:
                        sub_count[sub_word] += 1
                    else:
                        sub_count[sub_word] = 1
                    count += 1

                    # If the current count of the word exceeds the required count
                    # (i.e., there are more occurrences of the word than allowed)
                    while sub_count[sub_word] > word_count[sub_word]:
                        # Move the 'left' pointer to the right by 'word_length'
                        sub_count[s[left:left + word_length]] -= 1  # Decrease the count of the word at 'left'
                        count -= 1  # Decrease the matched word count
                        left += word_length  # Move 'left' forward

                    # If the size of the current window matches 'total_length',
                    # it means we found a valid concatenated substring
                    if count == len(words):
                        result.append(left)  # Add the starting index of this valid substring to the result list

                else:
                    # If the extracted word is not in 'word_count', reset the current window
                    sub_count.clear()
                    count = 0 
                    left = j + word_length  # Move 'left' to 'right', effectively resetting the window

        # Return the list of starting indices of all valid concatenated substrings found
        return result

# Example usage and test cases:

# Test Case 1
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
# Expected output: [0, 9]
print(Solution().findSubstring(s1, words1))  # Output: [0, 9]

# Test Case 2
s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
# Expected output: []
print(Solution().findSubstring(s2, words2))  # Output: []

# Test Case 3
s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
# Expected output: [6, 9, 12]
print(Solution().findSubstring(s3, words3))  # Output: [6, 9, 12]

# Test Case 4 (Edge case: Empty string)
s4 = ""
words4 = ["foo", "bar"]
# Expected output: []
print(Solution().findSubstring(s4, words4))  # Output: []

# Test Case 5 (Edge case: Single word, repeated)
s5 = "aaaaaa"
words5 = ["aa", "aa", "aa"]
# Expected output: [0]
print(Solution().findSubstring(s5, words5))  # Output: [0]
