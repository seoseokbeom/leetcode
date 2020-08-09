
var maxSubArray = function(nums) {
    let dp= Array(nums.length).fill(0);
     dp[0]=nums[0];
    for(var i=1; i<nums.length; i++) {
        dp[i] = dp[i-1]+nums[i] > nums[i] ? dp[i-1]+nums[i] : nums[i];
    }
    return Math.max(...dp);
};