function solution(brown, yellow) {
  for (var b = 1; b <= brown + yellow; b++) {
    for (var a = 1; a <= brown + yellow; a++) {
      if (a * b == brown + yellow && (a - 2) * (b - 2) == yellow) return [a, b];
    }
  }
}

console.log(solution(24, 24));
