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
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
var isCousins = function(root, x, y) {
    if(!root) return 0;
    let queue = [{
        node:root, 
        height:1,
        parent:null
        }];
    let count =0;
    let a = [];
    while(queue) {
        let p = queue.shift();
        if(p.node.val==x || p.node.val ==y) {
            count++;
            a.push(p);
        }
        if(count==2) break;
        if(p.node.left) queue.push({node:p.node.left, height:p.height+1, parent:p});
        if(p.node.right) queue.push({node:p.node.right, height:p.height+1, parent:p});
        
    }
    if(count==2) return (a[0].height==a[1].height && a[0].parent!=a[1].parent);
    else return false;
};