function map(arr, fn) {
  const result = [];

  arr.forEach((element, index) => {
    result.push(fn(element, index));
  });

  return result;
}

// Example 1
const arr1 = [1, 2, 3];
const plusOne = function plusone(n) {
  return n + 1;
};
const result1 = map(arr1, plusOne);
console.log(result1); // Output: [2, 3, 4]

// Example 2
const arr2 = [1, 2, 3];
const plusI = function plusI(n, i) {
  return n + i;
};
const result2 = map(arr2, plusI);
console.log(result2); // Output: [1, 3, 5]

// Example 3
const arr3 = [10, 20, 30];
const constant = function constant() {
  return 42;
};
const result3 = map(arr3, constant);
console.log(result3); // Output: [42, 42, 42]
