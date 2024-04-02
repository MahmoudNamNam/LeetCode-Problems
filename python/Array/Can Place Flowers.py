class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        cnt = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i == 0 or flowerbed[i - 1] == 0:
                    if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                        cnt += 1
                        flowerbed[i] = 1
            i += 1
        return cnt >= n

# Test cases
s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1], 2))  # Output: False
