/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    var recursive = (nums) => {
        if(nums.length==1) return nums
        for(let i=0; i<nums.length; i++) {
            let nums2 = nums.splice(i,1);
            recursive(nums2);
        }
    }  
};