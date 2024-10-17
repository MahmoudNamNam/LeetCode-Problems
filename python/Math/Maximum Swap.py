class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number into a list of digits
        digit_list = [int(digit) for digit in str(num)]
        
        # Create a dictionary to store the last occurrence of each digit
        last = {digit: i for i, digit in enumerate(digit_list)}
        
        # Traverse the list of digits
        for i, digit in enumerate(digit_list):
            # Try to find a larger digit to swap with, starting from 9 down to current digit + 1
            for d in range(9, digit, -1):
                if last.get(d, -1) > i:  # A larger digit exists to the right
                    # Swap the current digit with the found larger digit
                    digit_list[i], digit_list[last[d]] = digit_list[last[d]], digit_list[i]
                    # Return the number after the first swap
                    return int(''.join(map(str, digit_list)))
        
        # If no swap was made, return the original number
        return num

sol = Solution()
print(sol.maximumSwap(2736))  # Output: 7236
print(sol.maximumSwap(9973))  # Output: 9973
print(sol.maximumSwap(98368))  # Output: 98863
