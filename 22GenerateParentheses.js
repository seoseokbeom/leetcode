var generateParenthesis = function (n) {
  let ans = [];
  let left = 0;
  let right = 0;
  var recursion = (left, right, arr) => {
    if (left + right == 2 * n) {
      ans.push(arr.join(""));
      return;
    }
    if (left <= right) {
      recursion(left + 1, right, [...arr, "("]);
    } else if (left == n) {
      recursion(left, right + 1, [...arr, ")"]);
    } else {
      recursion(left + 1, right, [...arr, "("]);
      recursion(left, right + 1, [...arr, ")"]);
    }
  };

  recursion(0, 0, []);
  return ans;
};

console.log(generateParenthesis(3));
