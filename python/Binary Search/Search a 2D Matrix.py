import numpy as np
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        matrix = np.array(matrix).flatten()
        left, right = 0, len(matrix)-1
        mid = (left + right) //2
        while left <= right:
            if target == matrix[mid]:
                return True
            elif target < matrix[mid]:
                right = mid - 1
            else:
                left = mid + 1
            mid = (left + right) // 2
        return False