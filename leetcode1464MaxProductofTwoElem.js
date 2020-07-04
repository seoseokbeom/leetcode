/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let max = nums[0];
    let secondMax = null;
    for(let i=1; i<nums.length; i++) {
        if(nums[i] >= max) {
            secondMax = max;
            max = nums[i];
            continue;
        }
        if(nums[i] > secondMax) {
            secondMax = nums[i];
        }
    }
    if(!secondMax) {
        secondMax = nums[1];
        for(let i=2; i<nums.length; i++) {
            if(nums[i] > secondMax) secondMax = nums[i];
        }
    }
    console.log(max, secondMax);
    return (max-1)*(secondMax-1);
    
};