/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function (p, q) {
    var recursion = function (l, r) {
        if (!l && !r)
            return true;
        if (!l || !r)
            return false;
        if (l.val != r.val)
            return false;
        return recursion(l.left, r.left) && recursion(l.right, r.right);
    };
    return recursion(p, q);
};
