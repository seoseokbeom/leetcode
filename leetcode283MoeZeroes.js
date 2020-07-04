
var moveZeroes = function(nums) {
    let count=0;
  for(var i=0; i<nums.length-count; i++) {
      if(nums[i]==0) {
          count++;
          nums.splice(i,1);
          i--;
      }
  }  
    for(var i=0; i<count; i++) {
        nums.push(0);
    }
    // console.log(nums);
};