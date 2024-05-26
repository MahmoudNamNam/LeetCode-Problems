import numpy as np
class Solution:
    def checkRecord(self, n: int) -> int:

        T = np.array([[1, 1, 0, 1, 0, 0],
                      [1, 0, 1, 1, 0, 0],
                      [1, 0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 1, 0],
                      [0, 0, 0, 1, 0, 1],
                      [0, 0, 0, 1, 0, 0]])

        def matPow(A, p):
            if p == 1:
                return A
            if p % 2 == 0:
                B = matPow(A, p // 2)
                return (np.dot(B,B)) % (10**9 + 7)
            else:
                return (np.dot(A , matPow(A, p-1))) % (10**9 + 7)

        A = matPow(T, n)

        return int(sum(A[0]) % (10**9 + 7))

