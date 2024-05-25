
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = 0
        for i in num1:
            a = a*10 + int(i)
        b = 0
        for i in num2:
            b = b*10 + int(i)

        return str(a * b)
    
