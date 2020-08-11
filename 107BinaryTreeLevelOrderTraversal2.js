var levelOrderBottom = function(root) {
    let arr = [];
    let recursion = (node, count) => {
        if(!node) return;
        if(arr.length <=count) {
            arr.push([node.val])
        } else {
            arr[count].push(node.val);
        }
        recursion(node.left,count+1);
        recursion(node.right,count+1);
    }
    recursion(root, 0);
    return arr.reverse();
};