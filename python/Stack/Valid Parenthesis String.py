class Solution:
    def checkValidString(self, s: str) -> bool:
        # Initialize minimum and maximum possible counts of open parentheses
        leftMin, leftMax = 0, 0

        # Iterate through each character in the string
        for c in s:
            if c == "(":
                # Increment counts for open parentheses
                leftMin += 1
                leftMax += 1
            elif c == ")":
                # Decrement counts for closed parentheses
                leftMin -= 1
                leftMax -= 1
            else:
                # For '*', it could represent open, closed, or empty string
                # So, consider it as both open and closed
                leftMin -= 1
                leftMax += 1

            # Check if there are more closed parentheses than open ones so far
            if leftMax < 0:
                return False
            
            # Ensure leftMin is never negative
            if leftMin < 0:
                leftMin = 0

        # If after iterating through the entire string, leftMin is 0, it indicates
        # all open parentheses can be matched with closed ones, making the string valid
        return leftMin == 0
