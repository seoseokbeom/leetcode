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
    var arr = [];
    
    var recursion = (node, count) => {
        if(!node) return;
        if(arr.length < count) {
            arr.push([node.val]);
        } else {
            arr[count-1].push(node.val);
        }
        console.log(node.val, count);
        recursion(node.left, count+1);
        recursion(node.right, count+1);
    }
    
    recursion(root, 1);
    console.log(arr);
    return arr;
    
};