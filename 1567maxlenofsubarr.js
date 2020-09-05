var getMaxLen = function (nums) {
  let cnt = 0;
  let str = nums.toString();

  let arr = str.split(0);
  console.log(arr);
  let leftmost = -1;
  let rightmost = -1;
  let res = 0;
  for (var i = 0; i < arr.length; i++) {
    let i = 0;
    let j = arr[i].length - 1;
    while (i <= j) {
      if (nums[i] < 0) {
        if (leftmost == -1) letmost = i;
        cnt++;
      }
      if (i != j && nums[j] < 0) {
        if (rightmost == -1) rightmost = j;
        cnt++;
      }
      i++;
      j--;
    }
    if (cnt % 2 == 0) res = Math.max(res, cnt);
    else res = Math.max(res, rightmost, arr[i].length - leftmost - 1);
  }
  return res;
};

console.log(getMaxLen([-1, -2, -3, 0, 1]));
