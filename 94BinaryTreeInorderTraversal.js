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
 * @return {number[]}
 */
var inorderTraversal = function (root) {
    var arr = [];
    var recursion = function (node) {
        if(!node) return;
        if(node.left) recursion(node.left);
        if(node) arr.push(node.val);   
        if(node.right) recursion(node.right);
    }
    recursion(root);
    // console.log(arr);
    return arr;
};
