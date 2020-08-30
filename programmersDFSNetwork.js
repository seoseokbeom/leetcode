function solution(n, computers) {
  var recursion = (i, j) => {
    if (i < 0 || i >= computers.length || j < 0 || j >= computers.length)
      return;

    if (computers[i][j] == 1) computers[i][j] = "v";
    // console.log(computers, i,j);
    recursion(i, j + 1);
    if (computers[i][j] == "v") {
      if (computers[j][0] !== "v" && j > i) recursion(j, 0);
    }
  };
  let count = 0;
  for (var i = 0; i < computers.length; i++) {
    for (var j = 0; j < computers.length; j++) {
      if (computers[i][j] == 1) {
        recursion(i, j);
        count++;
      }
    }
  }
  // console.log(computers);
  return count;
}

console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1],
  ])
);

// [1,1,0,1]
// [1,1,1,0]
// [0,1,1,0]
// [1,0,0,1]
