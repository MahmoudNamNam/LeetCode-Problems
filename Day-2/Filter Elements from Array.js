// Define a function named 'filter' that takes an array 'arr' and a filtering function 'fn'
function filter(arr, fn) {
  // Use Array.reduce to build the filtered array
  return arr.reduce((filteredArr, element, index) => {
    // Use the filtering function to determine if the current element should be included
    fn(element, index) && filteredArr.push(element);
    // Return the updated filtered array for the next iteration
    return filteredArr;
  }, []); // Initialize the accumulator with an empty array
}

// Example 1
const arr1 = [0, 10, 20, 30];
const greaterThan10 = (n) => n > 10;
const result1 = filter(arr1, greaterThan10);
console.log(result1); // Output: [20, 30]

// Example 2
const arr2 = [1, 2, 3];
const firstIndex = (_, i) => i === 0;
const result2 = filter(arr2, firstIndex);
console.log(result2); // Output: [1]

// Example 3
const arr3 = [-2, -1, 0, 1, 2];
const plusOne = (n) => n + 1;
const result3 = filter(arr3, plusOne);
console.log(result3); // Output: [-2, 0, 1, 2]
