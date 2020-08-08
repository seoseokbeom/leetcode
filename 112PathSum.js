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
 * @return {boolean}
 */
var hasPathSum = function(root, sum) {
    if(!root) return false;
    let res = false;
    var recursion = (sum2, node) => {
        if(!node) return;
        if(!node.left && !node.right) {
            if(sum===sum2+node.val) res = true;
            return;
        }
        recursion(sum2+node.val, node.left);
        recursion(sum2+node.val, node.right);
    }
    recursion(0,root)
    return res;
};