/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    var maxSub=nums[0];
    var curSum = 0;
    for(var n in nums) {
        if(curSum < 0 ){
            curSum =0;
        }
        curSum += nums[n];
        maxSub = Math.max(maxSub, curSum);
    }
    return maxSub;
};

console.log(maxSubArray([-2,1]));
console.log(maxSubArray([-2,-2]));
console.log(maxSubArray([1,-2]));
console.log(maxSubArray([1,2]));
console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]));
console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4,-100,1,-2,5,-1,5]));
console.log(maxSubArray([-2,1,-3,4,-1,2,1,-5,4,-100,1,-2,5,-1,5,-1]));
