// Define a function called 'once' that takes another function 'fn' as a parameter
function once(fn) {
  // Initialize a variable 'called' to keep track of whether 'fn' has been called
  let called = false;
  // Initialize a variable 'result' to store the result of the first call to 'fn'
  let result;

  // Return a new function that can be called multiple times
  return function (...args) {
    // Check if 'fn' has not been called before
    if (!called) {
      // Mark 'fn' as called
      called = true;
      // Call 'fn' with the provided arguments and store the result
      result = fn(...args); // Store the result of the first call

      // Return the result value
      return result;
    } else {
      // If 'fn' has been called before, return undefined
      return undefined;
    }
  };
}

// Example 1
const fn1 = (a, b, c) => a + b + c;
const onceFn1 = once(fn1);
console.log(onceFn1(1, 2, 3)); // Output: 6
console.log(onceFn1(2, 3, 6)); // Output: undefined

// Example 2
const fn2 = (a, b, c) => a * b * c;
const onceFn2 = once(fn2);
console.log(onceFn2(5, 7, 4)); // Output: 140
console.log(onceFn2(2, 3, 6)); // Output: undefined
console.log(onceFn2(4, 6, 8)); // Output: undefined
