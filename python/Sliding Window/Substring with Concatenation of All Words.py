from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # If the string or the list of words is empty, return an empty list
        if not s or not words:
            return []
        
        # Length of each word (all words are assumed to be the same length)
        word_len = len(words[0])
        # Total length of the concatenated string we need to find (all words combined)
        total_len = word_len * len(words)
        # Create a frequency count of all words in the list 'words'
        word_count = Counter(words)
        # List to store the starting indices of valid substrings
        result = []

        # Iterate over possible starting points in 's' that align with word boundaries
        for i in range(word_len):
            left = i 
            right = i  
            # Counter to track the number of words seen in the current window
            current_count = Counter()

            # Expand the sliding window by moving 'right' in steps of 'word_len'
            while right + word_len <= len(s):
                # Extract a word of length 'word_len' from 's'
                word = s[right:right + word_len]
                # Move 'right' pointer forward by 'word_len'
                right += word_len

                # If the extracted word is in 'word_count' (i.e., part of the 'words' list)
                if word in word_count:
                    # Increment the count of this word in the current window
                    current_count[word] += 1

                    # If the current count of the word exceeds the required count
                    # (i.e., there are more occurrences of the word than allowed)
                    while current_count[word] > word_count[word]:
                        # Move the 'left' pointer to the right by 'word_len'
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1  # Decrease the count of the word at 'left'
                        left += word_len  # Move 'left' forward

                    # If the size of the current window matches 'total_len',
                    # it means we found a valid concatenated substring
                    if right - left == total_len:
                        result.append(left)  # Add the starting index of this valid substring to the result list

                else:
                    # If the extracted word is not in 'word_count', reset the current window
                    current_count.clear()
                    left = right  # Move 'left' to 'right', effectively resetting the window

        # Return the list of starting indices of all valid concatenated substrings found
        return result



sol= Solution()
#  1
s1 = "barfoothefoobarman"
words1 = ["foo", "bar"]
print(sol.findSubstring(s1, words1))  # Output: [0, 9]

#  2
s2 = "wordgoodgoodgoodbestword"
words2 = ["word", "good", "best", "word"]
print(sol.findSubstring(s2, words2))  # Output: []

#  3
s3 = "barfoofoobarthefoobarman"
words3 = ["bar", "foo", "the"]
print(sol.findSubstring(s3, words3))  # Output: [6, 9, 12]

#  4 (Edge case: Empty string)
s4 = ""
words4 = ["foo", "bar"]
print(sol.findSubstring(s4, words4))  # Output: []

#  5 (Edge case: Single word, repeated)
s5 = "aaaaaa"
words5 = ["aa", "aa", "aa"]
print(sol.findSubstring(s5, words5))  # Output: [0]

#  6 (Multiple valid substrings)
s6 = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words6 = ["fooo", "barr", "wing", "ding", "wing"]
print(sol.findSubstring(s6, words6))  # Output: [13]

#  7 (Words contain repeated elements)
s7 = "barfoofoobarthefoobarman"
words7 = ["bar", "foo", "foo"]
print(sol.findSubstring(s7, words7))  # Output: [0,3]