var numSubmat = function (mat) {
  let count = 0;
  for (var i = 0; i < mat.length; i++) {
    for (var j = 0; j < mat[0].length; j++) {
      if (mat[i][j] == 0) continue;
      let w = 1;
      while (j + w < mat[0].length && mat[i][j + w] == 1) {
        w++;
      }
      let v = 1;
      while (i + v < mat.length && mat[i + v][j] == 1) {
        v++;
      }
      console.log(i, j, w, v);
      count += w * v;
    }
  }
  return count;
};

console.log(
  numSubmat([
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 1, 0],
  ])
);
