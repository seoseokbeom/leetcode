/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    let count = 0; 
    for (let i = 0; i < nums.length; i++) {
        for (let j = nums.length - 1; j > i; j--) {
            if (nums[i] === nums[j]) count++;
        }
    }
    
    return count;
};