class Solution:
    def checkSubarraySum(self, nums, k):
        prefix_mod = 0
        mod_seen = {0: -1}

        for i, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % k
            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                mod_seen[prefix_mod] = i

        return False

    
sol =Solution()

nums = [23,2,4,6,7]
k = 6
print(sol.checkSubarraySum(nums,k))


nums = [23,2,6,4,7]
k = 13
print(sol.checkSubarraySum(nums,k))