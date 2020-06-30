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
 * @return {boolean}
 */
function TreeNode(val, left, right) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
    
var isSymmetric = function(root) {
    if(!root) return false;
    var isMirror = (r,l) => {
        if(!r && !l) return true
        if(!r || !l || r.val!=l.val) return false;
        return isMirror(r.left, l.right) && isMirror(r.right, l.left);
    }
    
    return isMirror(root.left, root.right);
};

let n1= new TreeNode(3);
let n2= new TreeNode(2);
let n3= new TreeNode(1,n1,n2);

console.log(isSymmetric(n3));