/**
 * @param {number[]} nums
 * @return {number[]}
 */
var decompressRLElist = function (nums) {
    let arr = [];
    let freq = 0;
    for (var i = 0; i < nums.length; i++) {
        if (i % 2 == 0) {
            freq = nums[i];
        } else {
            arr.push(...Array(freq).fill(nums[i]));
        }
    }
    return arr;
};

console.log(decompressRLElist([1, 1, 2, 3]));
