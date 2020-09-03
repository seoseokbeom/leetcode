/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */

var selfd = (n) => {
  let s = n.toString();
  for (var i = 0; i < s.length; i++) {
    if (n % parseInt(s.charAt(i)) !== 0) return false;
  }
  return true;
};

var selfDividingNumbers = function (left, right) {
  let arr = [];
  for (var i = left; i <= right; i++) {
    if (selfd(i)) arr.push(i);
  }
  return arr;
};

console.log(selfDividingNumbers(1, 22));
