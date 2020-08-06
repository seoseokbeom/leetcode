/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let L = nums.length;
    for(var i=0; i<L; i++) {
        if(nums[i]==0) {
            nums.push(nums.splice(i--,1));
            L--;
        }
    }
};