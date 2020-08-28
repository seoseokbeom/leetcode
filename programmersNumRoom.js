const { result } = require("lodash");

function solution(arrows) {
  let arr = new Array(100000).fill(new Array(100000).fill(0));
  if (arrows.length <= 2) return 0;
  let start = [50000, 50000];

  function direction(array, dir) {
    if (dir == 0) return [array[0], array[1] + 1];
    if (dir == 1) return [array[0] + 1, array[1] + 1];
    if (dir == 2) return [array[0] + 1, array[1]];
    if (dir == 3) return [array[0] + 1, array[1] - 1];
    if (dir == 4) return [array[0], array[1] - 1];
    if (dir == 5) return [array[0] - 1, array[1] - 1];
    if (dir == 6) return [array[0] - 1, array[1]];
    if (dir == 7) return [array[0] - 1, array[1] + 1];
  }
  let third = direction(start, arrows[0]);
  console.log(third);
  let second = direction(third, arrows[1]);
  console.log(second);
  let curr = direction(second, arrows[2]);
  console.log(curr);
  for (var i = 3; i < arrows.length; i++) {
    third = second;
    second = curr;
    curr = direction(second, arrows[i]);
    console.log(curr);
  }

  return curr;

  return answer;
}

console.log(solution([6, 6, 6, 4, 4, 4]));
