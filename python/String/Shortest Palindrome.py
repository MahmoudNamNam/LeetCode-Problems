
#* Sol-1 Brute-Force
#* Time complexity: O(n^2).
class Solution:
  def shortestPalindrome(self, s: str) -> str:
    n = len(s)
    rev = s[::-1]  
    for i in range(n):
      print(s[:n - i])
      print(rev[i:])

      if s[:n - i] == rev[i:]:
        return rev[:i] + s  
    return s[::-1]  



s=  Solution()
s.shortestPalindrome("abcd")

