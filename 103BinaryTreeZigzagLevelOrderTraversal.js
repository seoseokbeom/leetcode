var zigzagLevelOrder = function(root) {
    var arr = [];
    if(!root) return [];
    
    var recursion = (node, count) => {
        if(arr.length < count) {
            arr.push([node.val]);
        } else {
            arr[count-1].push(node.val);
        }
        if(node.left) recursion(node.left, count+1);
        if(node.right) recursion(node.right, count+1);
    }
    recursion(root, 1);
	
	// [ [3], [20,9], [15,7] ]  => [ [3], [9,20], [15,7] ] 
    for(var i=1; i<arr.length; i=i+2) {
        arr[i] = arr[i].reverse();
    }
    return arr;
};