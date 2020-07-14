/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    for(var i=1; i< nums.length; i++) {
        if(i==0) continue;
       if(nums[i-1]>nums[i]) {
           var tmp = nums[i];
           nums[i] = nums[i-1];
           nums[i-1] = tmp;
           i-=2;
       }
    }
};