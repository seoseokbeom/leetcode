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
 * @return {number}
 */
var minDepth = function(root) {
    if(!root) return 0;
    let queue= [{node:root, height:1}];
    while(queue) {
        let p = queue.shift();
        if(!p.node.left && !p.node.right) return p.height; 
        if(p.node.left) queue.push({node:p.node.left, height:p.height+1});
        if(p.node.right) queue.push({node:p.node.right, height:p.height+1});        
    }
};