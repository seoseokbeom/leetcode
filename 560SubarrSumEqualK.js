/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

//Brute Forece
var subarraySum = function(nums, k) {
    var count=0;
    for(var i=0; i<nums.length; i++) {
        var j=i;
        var sum=0;
        while(j<nums.length) {
            sum+=nums[j++];
            if(sum==k)  count++;
        }
    }
    return count;
};