
var productExceptSelf = function(nums) {
    let count =0;
    nums.map((e) => e==0 ? count++ : e);
    console.log(count);
    
    if(count>1) return new Array(nums.length).fill(0);
    let multiply = nums.reduce((acc, curr)=> curr==0 ? acc : acc*curr, 1);
    let res = [];
    if(count==1) {
        for(var i=0; i<nums.length; i++) {
            if(nums[i]!==0) res.push(0);
            else res.push(multiply);
        }
    }
    else{
        for(var i=0; i<nums.length; i++) {
            res.push(multiply/nums[i]);
        }   
    }
    return res;
};