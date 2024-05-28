from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])  # Sort along with original indices

        while i < j:
            current_sum = sorted_nums[i][1] + sorted_nums[j][1]

            if target == current_sum:
                # 🎉 We found a pair whose sum equals the target!
                return [sorted_nums[i][0], sorted_nums[j][0]]  # Return the original indices

            elif target < current_sum:
                # 💡 If the current sum is greater than the target, we need to decrease the sum.
                j -= 1
            else:
                # 💡 If the current sum is less than the target, we need to increase the sum.
                i += 1

        # 🤷‍♂️ If no solution is found.
        return []  

# Example usage:
nums = [2, 7, 11, 15]
target = 9

sol = Solution()
result = sol.twoSum(nums, target)
print(result)  # Output: [0, 1] (indices of 2 and 7 whose sum is 9)



class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict={}
        for i,n in enumerate(nums):
            if n in numDict:
                return numDict[n],i
            else:
                numDict[target-n]=i


nums = [2, 7, 11, 15]
target = 9

sol = Solution()
result = sol.twoSum(nums, target)
print(result)  # Output: [0, 1] (indices of 2 and 7 whose sum is 9)
