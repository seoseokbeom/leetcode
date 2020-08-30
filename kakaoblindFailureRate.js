function solution(N, stages) {
  let len = stages.length;
  let dp = Array(N + 2).fill(0);
  let arr = [];
  for (var i = 0; i < stages.length; i++) {
    dp[stages[i]] += 1;
  }
  for (var i = 1; i <= N; i++) {
    if (len == 0) len = 1;
    arr.push([i, dp[i] / len]);
    len -= dp[i];
  }
  arr.sort((a, b) => (b[1] == a[1] ? a[0] - b[0] : b[1] - a[1]));
  let ans = [];
  for (var i = 0; i < arr.length; i++) {
    ans.push(arr[i][0]);
  }
  return ans;
} // console.log(i, dp[i], len);

// console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]));
console.log(solution(8, [1, 2, 3, 4, 5, 6, 6, 6]));
