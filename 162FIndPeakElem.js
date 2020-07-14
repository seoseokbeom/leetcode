/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    if(nums.length===1) return 0;
    if(nums[0] > nums[1]) return 0;
    if(nums[nums.length-2] < nums[nums.length-1]) return nums.length-1;
    for(var i=1; i<=nums.length-2; i++) {
        if(nums[i] >nums[i-1] && nums[i] > nums[i+1]) return i;
    }
};