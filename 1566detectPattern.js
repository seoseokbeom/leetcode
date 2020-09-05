var containsPattern = function (arr, m, k) {
  let count = 0;
  for (var i = 0; i + m < arr.length; i++) {
    if (arr[i] == arr[i + m]) {
      count++;
      if (count == m * (k - 1)) return true;
    } else count = 0;
  }
  return false;
};
console.log(containsPattern(((arr = [1, 2, 3, 1, 2]), (m = 2), (k = 2))));
