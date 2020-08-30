var levelOrder = function (root) {
  let queue = [root];
  let arr = [];
  let count = 0;
  while (queue.length) {
    let size = queue.length;
    for (var i = 0; i < size; i++) {
      let node = queue.shift();
      if (arr[count]) arr[count].push(node.val);
      else arr[count] = node.val;
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    count++;
  }
  return arr;
};

console.log(levelOrder());
