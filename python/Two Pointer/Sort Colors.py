class Solution:
    def sort012(self, arr, n):
        """
        To solve this problem efficiently with a one-pass algorithm and constant space, 
        we can use the Dutch National Flag algorithm. 
        This algorithm uses three pointers to sort the array in a single pass. 

        Explanation:
            Three Pointers:
                low: This pointer is used to place the next 0.
                mid: This pointer is used to explore the array.
                high: This pointer is used to place the next 2.

            Process:
                Traverse the array with the mid pointer.
                If nums[mid] is 0, swap it with nums[low] and increment both low and mid.
                If nums[mid] is 1, just move the mid pointer.
                If nums[mid] is 2, swap it with nums[high] and decrement high.

            Termination:
                The loop terminates when mid surpasses high.
        """




        low = 0
        high = n - 1
        mid = 0

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr



solution = Solution()
arr = [2, 1, 0, 1, 2, 0, 1]
sorted_arr = solution.sort012(arr, len(arr))