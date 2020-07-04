/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {  
    var major = nums[0];
    var count = 1;
    for(var i=1; i<nums.length;i++){
        if(count==0){
            count++;
            major=nums[i];
        }
        else if(major==nums[i]){
            count++;
        }
        else count--;

    }
    return major;
};