/**
 * @param {string} val
 * @return {Object}
 */
var expect = function (val) {
  return {
    toBe: (otherVal) => {
      if (val === otherVal) {
        return true;
      } else {
        throw "Not Equal";
      }
    },
    notToBe: (otherVal) => {
      if (val !== otherVal) {
        return true;
      } else {
        throw "Equal";
      }
    },
  };
};

var expect = function (val) {
  return {
    toBe: (otherVal) =>
      val === otherVal
        ? true
        : (() => {
            throw "Not Equal";
          })(),
    notToBe: (otherVal) =>
      val !== otherVal
        ? true
        : (() => {
            throw "Equal";
          })(),
  };
};
