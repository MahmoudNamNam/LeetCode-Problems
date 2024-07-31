class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        specialChars = "!@#$%^&*()-+"
        prevChar = ""
        lower = False
        upper = False
        digit = False
        special = False
        subsequent = False

        for character in password:
            if character.islower():
                lower = True
            elif character.isupper():
                upper = True
            elif character.isdigit():
                digit = True
            elif character in specialChars:
                special = True
            
            if prevChar == character:
                subsequent = True

            prevChar = character

        return lower and upper and digit and special and not subsequent

    

"""
Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.
Example 2:

Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. Therefore, we return false.
Example 3:

Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.

"""