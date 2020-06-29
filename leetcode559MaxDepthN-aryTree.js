/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

// Definition for a Node.
/**
 * @param {Node} root
 * @return {number}
 */
function Node(val,children) {
    this.val = val;
    this.children = children;
 };
var maxDepth = function(root) {
    if(!root) return 0;
    if(!root.children) return 1;
    console.log(root);
    let depth =0;
    let queue = [];
    console.log(queue.length);
    queue.push(root);
    console.log(queue.length);
    while(queue.length) {
        console.log('---');
        depth++;
        let size = queue.length;
        for(let i=0; i<size; i++) {
            let p = queue.shift();
            if (p.children == null) p.children = [];
            p.children.forEach(child => {
                queue.push(child);
            });
            console.log('pushed', queue);
        }
    }
    return depth;
    
};
 
let n1 = new Node(5,null);
let n2 = new Node(6,null);
let n3 = new Node(3,[n1, n2]);
let n4 = new Node(2,null);
let n5 = new Node(4,null);
let n6 = new Node(1,[n3,n4,n5]);
console.log(maxDepth(n6));