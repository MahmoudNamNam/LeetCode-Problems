// Function to find the median of two sorted arrays
function findMedianSortedArrays(nums1, nums2) {
  // Ensure nums1 is the shorter array
  if (nums1.length > nums2.length) {
    [nums1, nums2] = [nums2, nums1]; // Swap nums1 and nums2 using destructuring assignment
  }

  const x = nums1.length; // Length of nums1
  const y = nums2.length; // Length of nums2
  let low = 0; // Initialize low for binary search
  let high = x; // Initialize high for binary search

  while (low <= high) {
    // Binary search to find the correct partition in nums1
    const partitionX = Math.floor((low + high) / 2);
    const partitionY = Math.floor((x + y + 1) / 2) - partitionX;

    // Calculate the elements on the left and right sides of the partitions
    const maxX =
      partitionX === 0 ? Number.NEGATIVE_INFINITY : nums1[partitionX - 1];
    const minX =
      partitionX === x ? Number.POSITIVE_INFINITY : nums1[partitionX];
    const maxY =
      partitionY === 0 ? Number.NEGATIVE_INFINITY : nums2[partitionY - 1];
    const minY =
      partitionY === y ? Number.POSITIVE_INFINITY : nums2[partitionY];

    // Check conditions for finding the median
    if (maxX <= minY && maxY <= minX) {
      if ((x + y) % 2 === 0) {
        // If total elements are even, return the average of the middle elements
        return (Math.max(maxX, maxY) + Math.min(minX, minY)) / 2;
      } else {
        // If total elements are odd, return the maximum of the middle elements
        return Math.max(maxX, maxY);
      }
    } else if (maxX > minY) {
      // Adjust the partition in nums1 to the left
      high = partitionX - 1;
    } else {
      // Adjust the partition in nums1 to the right
      low = partitionX + 1;
    }
  }
}

// Example 1
const nums1 = [1, 3];
const nums2 = [2];
const result1 = findMedianSortedArrays(nums1, nums2);
console.log(result1); // Output: 2.0

// Example 2
const nums3 = [1, 2];
const nums4 = [3, 4];
const result2 = findMedianSortedArrays(nums3, nums4);
console.log(result2); // Output: 2.5
