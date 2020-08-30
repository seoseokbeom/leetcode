function solution(n, weak, dist) {
  let weakDist = [];
  weakDist.push(weak[0] + n - weak[weak.length - 1]);
  for (var i = 1; i < weak.length; i++) {
    weakDist.push(weak[i] - weak[i - 1]);
  }
}

console.log(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]));

let arr = [];
arr[-1] = 2;
