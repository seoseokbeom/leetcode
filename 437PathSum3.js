/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number}
 */
var pathSum = function (root, sum) {
  var dfs = (node, sum, sum2) => {
    count = 0;
    if (!node) return;
    if (sum == sum2 + node.val) {
      count += 1;
      return count;
    }
    count += dfs(node.left, sum, sum2 + node.val);
    count += dfs(node.right, sum, sum2 + node.val);
    return count;
  };
  if (!root) return 0;

  return (
    pathSum(root.left, sum, 0) + dfs(root, sum, 0) + pathSum(root.right, sum, 0)
  );
};
