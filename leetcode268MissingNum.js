/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
    var arr = Array(nums.length + 1).fill(null);
    // console.log(arr);
    for (var i = 0; i < nums.length; i++) {
        arr[nums[i]] = 1;
    }
    for (var i = 0; i < nums.length + 1; i++) {
        if (arr[i] != 1)
            return i;
    }
    console.log(arr);
    return -1;
};
console.log(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]));
