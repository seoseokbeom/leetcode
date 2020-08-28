var subsets = function (nums) {
  let ans = [];
  var rec = (i, arr) => {
    ans.push(arr);
    for (var j = i + 1; j < nums.length; j++) {
      rec(j, [nums[j], ...arr]);
    }
  };
  rec(-1, []);
  return ans;
};

console.log(subsets([1, 2, 3]));
