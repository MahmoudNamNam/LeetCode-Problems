var reduce = function (nums, fn, init) {
  return nums.reduce((accum, curr) => fn(accum, curr), init);
};

// Example 1
const nums1 = [1, 2, 3, 4];
const fn1 = function sum(accum, curr) {
  return accum + curr;
};
const init1 = 0;
console.log(reduce(nums1, fn1, init1)); // Output: 10

// Example 2
const nums2 = [1, 2, 3, 4];
const fn2 = function sum(accum, curr) {
  return accum + curr * curr;
};
const init2 = 100;
console.log(reduce(nums2, fn2, init2)); // Output: 130

// Example 3
const nums3 = [];
const fn3 = function sum(accum, curr) {
  return 0;
};
const init3 = 25;
console.log(reduce(nums3, fn3, init3)); // Output: 25


var reduce = function(nums, fn, init) {
    const length = nums.length;
    let result = init;

    for (let i = 0; i < length; i++) {
        result = fn(result, nums[i]);
    }

    return result;
}