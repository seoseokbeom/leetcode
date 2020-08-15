
var rob = function(nums) {
    if(!nums || !nums.length) return 0;
    var dp = new Array(nums.length).fill(0);
    if(nums.length<=2) return Math.max(...nums);
    dp[0]=nums[0];
    dp[1]=nums[1];
    dp[2]=nums[0]+nums[2];
    for(var i=3; i<nums.length; i++) {
        dp[i]=nums[i]+Math.max(dp[i-2], dp[i-3]);
    }
    return Math.max(dp[nums.length-1], dp[nums.length-2]);
};



console.log(rob([1]))
console.log(rob([0]))
console.log(rob([0,1]))
console.log(rob([2,8,3]))