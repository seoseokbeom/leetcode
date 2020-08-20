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
var diameterOfBinaryTree = function(root) {

    var recursion = (node, level) => {
        if(!node) return -1;
        node.level = level;
        node.rightV = recursion(node.right, level+1)+1;
        node.leftV = recursion(node.left, level)+1;
        node.V= node.rightV+node.leftV;
        return Math.max(node.rightV, node.leftV);
    }
    recursion(root, 0);
    
    // console.log(root.rightV, root.leftV, root.V);
    var recursion2 = (node) => {
        if(!node) return 0;
        let a = node.right ? node.right.V : 0;
        let b = node.left ? node.left.V : 0; 
        return Math.max(a,b, node.V);
        
    }

    var print = (node, space) => {
        if(!node) return;
        space += 10
        print(node.right, space);
        console.log('');
        let str = '';
        for(var i=10; i<space; i++) {
            str+=' ';
        }
        console.log(str+node.V);
        print(node.left, space);
    }

    print2D = (node) => {
        print(node,0);
    }

    print2D(root);
    return recursion2(root);
    
};
