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
 * @return {number[][]}
 */    

var levelOrder = function(root) {
    let arr = [];
    if(!root) return [];
    var recursion = (node, c) => {
        if(!node) return;
        if(arr.length-1 < c) {
            arr.push([node.val]);
        } else{
            arr[c].push(node.val);
        }
        recursion(node.left, c+1);
        recursion(node.right, c+1);
    }
    recursion(root, 0);
    return arr;
};