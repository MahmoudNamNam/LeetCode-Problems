class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Pointer for the position to place the next element in the final array
        insert_pos = 0
        
        # Iterate through the list
        for num in nums:
            # If insert_pos is less than 2 or the current number is different from 
            # the number at insert_pos - 2, we can add the number to the array.
            if insert_pos < 2 or num != nums[insert_pos - 2]:
                nums[insert_pos] = num
                insert_pos += 1
        
        return insert_pos
