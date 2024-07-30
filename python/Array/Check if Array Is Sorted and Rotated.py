def check_rotated_sorted(nums):
    # Count the number of breaks in the non-decreasing order
    count_breaks = 0
    n = len(nums)
    
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count_breaks += 1
        if count_breaks > 1:
            return False
            
    return True

print(check_rotated_sorted([3, 4, 5, 1, 2]))  # Output: True
print(check_rotated_sorted([2, 1, 3, 4]))     # Output: False
print(check_rotated_sorted([1, 2, 3]))        # Output: True
