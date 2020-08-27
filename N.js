const cached = Array(10)
  .fill(null)
  .map(() => Array());

function N_n(N, n) {
  let answer = 0;
  for (let i = 0; i < n; i++) {
    answer += Math.pow(10, i) * N;
  }
  return answer;
}

function allCase(N, n) {
  const Nn = [];
  if (n === 1) {
    return [N];
  }
  if (cached[N][n]) {
    return cached[N][n];
  }
  Nn.push(N_n(N, n));
  for (let i = 1; i <= parseInt(n / 2); i++) {
    allCase(N, n - i).map((v1) => {
      allCase(N, i).map((v2) => {
        if (v1 !== 0) Nn.push(parseInt(v2 / v1, 10));
        if (v2 !== 0) Nn.push(parseInt(v1 / v2, 10));
        Nn.push(v1 * v2);
        Nn.push(v1 - v2);
        Nn.push(v1 + v2);
        Nn.push(v2 - v1);
      });
    });
  }
  cached[N][n] = Nn;
  return Nn;
}
function solution(N, number) {
  for (let i = 1; i < 9; i++) {
    if (allCase(N, i).includes(number)) {
      return i;
    }
  }
  return -1;
}
