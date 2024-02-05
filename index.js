var a = [1, 2, 3];
var b = [1, 2, 3];
var c = "1,2,3";

a == c; // true
b == c; // true
a == b; // false

console.log(a === b);
console.log(a == b);
console.log(a === c);
console.log(a == c);
