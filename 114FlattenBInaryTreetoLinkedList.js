
var flatten = function(root) {
    let arr = [];
    if(!root) return;
    var recursion = (node) => {
        arr.push(node);
        if(node.left) recursion(node.left);
        if(node.right) recursion(node.right);
    }
    recursion(root);
    for(var i=0; i<arr.length; i++) {
        arr[i].left=null;
        arr[i].right = (i!=arr.length-1) ? arr[i+1] : null;
    }
};