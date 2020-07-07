function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}
// @param {number[]} nums
// @return {TreeNode}
var sortedArrayToBST = function (nums) {
    var left = 0;
    var right = nums.length - 1;
    var recursion = (left, right) => {
        if (left == right)
            return new TreeNode(nums[left], null, null);
        if (left > right)
            return null;
        var mid = left + Math.ceil((right - left) / 2);
        var node = new TreeNode(nums[mid], null, null);
        node.left = recursion(left, mid - 1);
        node.right = recursion(mid + 1, right);
        return node;
    };
    var ans = recursion(left, right);
    return ans;
};
