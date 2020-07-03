/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function (nums, n) {
    var arr2 = nums.splice(n);
    var arr3 = [];
    for (var i = 0; i < n; i++) {
        arr3.push(nums[i]);
        arr3.push(arr2[i]);
    }
    // console.log(arr3);
    return arr3;
};
