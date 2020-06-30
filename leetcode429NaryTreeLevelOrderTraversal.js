/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if(!root) return []
    let queue = [{node:root,
                 height:1
                 }]
    let arr = [];
    let ans = [];
    let p;
    while(queue.length){
        p = queue.shift();
        // console.log(p);
        // console.log(p.node.children);
        arr.push(p.node.val);
        // console.log("arr",arr);
        for(elem of p.node.children) {
            queue.push({node: elem, height:p.height+1});
        }
        // console.log(queue);
        if(queue.length>0 && p.height!=queue[0].height || !queue.length) { 
            ans.push(arr);
            arr = [];
        }
        // if(p.node.right) queue.push({node: p.node.right, height:p.height+1});
        // if(p.node.left) queue.push({node:p.node.left, height:p.height+1});
    }
    
    return ans;
};