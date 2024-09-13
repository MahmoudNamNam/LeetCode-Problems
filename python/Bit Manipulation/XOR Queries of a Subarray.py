from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n=len(arr)
        prefix_xor=[0]*n
        prefix_xor[0]=arr[0]
        for i in range(1,n):
            prefix_xor[i] = arr[i] ^prefix_xor[i-1]
        result=[]
        for left,right in queries:
            if left ==0:
                result.append(prefix_xor[right])
            else:
                result.append(prefix_xor[right] ^ prefix_xor[left - 1])
        return result

sol = Solution()
print(sol.xorQueries(arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))