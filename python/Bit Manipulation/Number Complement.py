class Solution:
    def findComplement(self, num: int) -> int:
        binary_num = bin(num)[2:] 
        complement_str = ''.join('1' if bit == '0' else '0' for bit in binary_num)
        return int(complement_str, 2)


class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()
        mask = (1 << bit_length) - 1
        return num ^ mask
        