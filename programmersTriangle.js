function solution(triangle) {
  let dp = new Array(triangle.length).fill(Array(triangle.length).fill(0));
  for (var i = 0; i < triangle.length; i++) {
    dp[triangle.length - 1][i] = triangle[triangle.length - 1][i];
  }
  var postOrder = (i, j) => {
    return Math.max(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j];
  };

  for (var i = triangle.length - 2; i >= 0; i--) {
    for (var j = 0; j <= i; j++) {
      dp[i][j] = postOrder(i, j);
    }
  }
  return dp[0][0];
}

console.log(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]));
