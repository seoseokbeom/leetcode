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
var maxPathSum = function(root) {
    
    var recursion = (node, sum) => {
        if(!node.left && !node.right) return sum+node.val;
        if(!node) return sum;
        return Math.max(recursion(node.right, sum+node.val),recursion(node.left, sum+node.val));
    }
    
    var recursion2 = (node) => {
        return node.val+ recursion(node.left,0)+ recursion(node.right,0);
    }
    
    var recursion3 = (node) => {
        if(!node.left && !node.right) return recursion2(node);
        if(node.left && node.right) return Math.max(recursion2(node), recursion3(node.left), recursion3(node.right));
        if(node.left) return Math.max(recursion2(node), recursion3(node.left));
        if(node.right) return Math.max(recursion2(node), recursion3(node.right));
    }
    return recursion2(root);
};

console.log(maxPathSum)