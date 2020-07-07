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


function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

var inorderTraversal = function(root) :number[] {
    let arr = [];
    var recursion = (node) => {
        if(!node) return;
        if(node.left)  recursion(node.left);
        arr.push(node.value);
        if(!node.right) recursion(node.right);        
    }

    recursion(root);
    return arr;
};
