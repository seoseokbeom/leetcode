/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    var res = 1;
    var key = nums.sort((a,b)=> a-b);
    for(var i=0; i<nums.length; i++) {
        if(nums[i] <=0) continue;
        if(nums[i]==res) {
            res++;
            continue;
        }
        else if(nums[i]==nums[i-1]) continue;
        else break;
    } 
    return res;
    
};