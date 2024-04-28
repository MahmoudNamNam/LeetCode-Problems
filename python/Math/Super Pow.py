from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 0:
            return 0
        if a == 1:
            return 1
        
        # Compute (a^b) % 1337 using modular exponentiation
        def modular_exponentiation(base, exp, modulus):
            result = 1
            base %= modulus  # Reduce base modulo modulus
            
            while exp > 0:
                # If exp is odd, multiply base with result
                if exp % 2 == 1:
                    result = (result * base) % modulus
                
                # Divide exp by 2
                exp = exp >> 1
                base = (base * base) % modulus
            
            return result
        
        exponent = int(''.join(map(str, b)))  # Convert list b to integer
        return modular_exponentiation(a, exponent, 1337)

# Example usage:
s = Solution()
a = 2
b = [1, 0]
result = s.superPow(a, b)
print(result)  # Output: 1024


class Solution:
    def superPow(self, base: int, exponent_list: List[int]) -> int:
        if base % 1337 == 0:
            return 0
        
        # Compute the exponent 'power' based on the list of digits 'exponent_list'
        power = 0
        for digit in exponent_list:
            power = (power * 10 + digit) % 1140
        
        # Compute (base^power) % 1337 using modular exponentiation
        return pow(base, power + 1140, 1337)