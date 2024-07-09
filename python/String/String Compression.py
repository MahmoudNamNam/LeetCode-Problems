from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
            
        write = 0  # position to write in the array
        read = 0  # position to read in the array
        n = len(chars)
        while read <n:
            char = chars[read]
            count = 0
            
            # Count the number of occurrences of the current character
            while read <n and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character to the array
            chars[write] = char
            write += 1
            
            # If count is greater than 1, write the count to the array
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write

solution = Solution()
print(solution.compress(["a","a","b","b","c","c","c"]))
print(solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))