var __spreadArrays =
  (this && this.__spreadArrays) ||
  function () {
    for (var s = 0, i = 0, il = arguments.length; i < il; i++)
      s += arguments[i].length;
    for (var r = Array(s), k = 0, i = 0; i < il; i++)
      for (var a = arguments[i], j = 0, jl = a.length; j < jl; j++, k++)
        r[k] = a[j];
    return r;
  };
/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function (candidates, target) {
  var res = [];
  var arr = [];
  var sortedArr = candidates.sort(function (a, b) {
    return a - b;
  });
  // console.log(candidates);
  console.log(sortedArr);
  var recursion = function (sum, idx) {
    if (sum == target) {
      res.push(__spreadArrays(arr));
      return;
    }
    if (sum > target) return;
    if (idx == sortedArr.length) return;
    arr.push(sortedArr[idx]);
    recursion(sum + sortedArr[idx], idx + 1);
    arr.pop();
    // if(idx>0 && sortedArr[idx]==sortedArr[idx-1]) idx++;
    console.log(arr, arr[arr.length - 1], idx);
    if (arr[arr.length - 1] !== sortedArr[idx]) {
      console.log("------", arr, idx);
      recursion(sum, idx + 1);
    } else console.log("llllllll");
  };
  recursion(0, 0);
  return res;
};
// [10,1,2,7,6,1,5], target = 8,
console.log(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8));
