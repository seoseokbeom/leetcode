function solution(n, edge) {
  let visited = [1];
  let queue = [1];
  let count = 0;
  while (visited.length < n) {
    let size = queue.length;
    count++;
    for (var i = 0; i < size; i++) {
      let node = queue.shift();
      for (let j = 0; j < edge.length; j++) {
        if (edge[j].includes(node)) {
          edge[j].forEach((e) => {
            if (!visited.includes(e)) {
              queue.push(e);
              visited.push(e);
            }
          });
          edge = [...edge.slice(0, j), ...edge.slice(j + 1, edge.length)];
          j--;
        }
      }
    }
  }
  return queue.length;
}

console.log(
  solution(6, [
    [3, 6],
    [4, 3],
    [3, 2],
    [1, 3],
    [1, 2],
    [2, 4],
    [5, 2],
  ])
);
