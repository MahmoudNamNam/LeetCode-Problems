class Solution:
    def convertDateToBinary(self, date: str) -> str:
        lst = date.split(sep='-')
        for i in range(len(lst)):
            lst[i] = bin(int(lst[i]))[2:]
        return '-'.join(lst)
sol=Solution()
print(sol.convertDateToBinary(date = "1900-01-01"))