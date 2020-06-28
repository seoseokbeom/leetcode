/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} t1
 * @param {TreeNode} t2
 * @return {TreeNode}
 */

function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

var mergeTrees = function(t1, t2) {
    if(!t1) return t2;
    if(!t2) return t1;
    t1.val +=t2.val;
    t1.left = mergeTrees(t1.left,t2.left);
    t1.right = mergeTrees(t1.right,t2.right);
    return t1;
};


let t1 = new TreeNode(5);
let t2 = new TreeNode(3,t1);
let t3 = new TreeNode(2);
let t4 = new TreeNode(1,t2,t3);
// while(t4!==null){
//     console.log(t4.val);
//     t4=t4.left;
// }

let s1 = new TreeNode(4);
let s2 = new TreeNode(7);
let s3 = new TreeNode(1,null,s1);
let s4 = new TreeNode(3,null,s2);
let s5 = new TreeNode(2,s3,s4);

function print(t1) {
    if(!t1) return;
    console.log(t1.val);
    print(t1.left)
    print(t1.right);
    return;
}
let res = mergeTrees(t4,s5);
print(res);
// console.log(res.left);