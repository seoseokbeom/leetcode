/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function (nums, n) {
    let arr2 = nums.splice(n);
    let arr3 = [];
    for (var i = 0; i < n; i++) {
        arr3.push(nums[i]);
        arr3.push(arr2[i]);
    }
    console.log(nums, arr2);
};
