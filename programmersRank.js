// const { Map, Set } = require("immutable");
// const { result } = require("lodash");
class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

function solution(n, results) {
  let arr = [];
  let map = new Map();
  for (var i = 0; i < results.length; i++) {
    if (!map.has(results[i][0])) {
      map.set(results[i][0], [results[i][1]]);
    } else {
      map.set(results[i][0], [...map.get(results[i][0]), results[i][1]]);
    }
  }
  console.log(map);
}

console.log(
  solution(5, [
    [4, 3],
    [4, 2],
    [3, 2],
    [1, 2],
    [2, 5],
  ])
);
