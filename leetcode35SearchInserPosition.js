
var searchInsert = function(nums, target) {
    let ret=0;
    for(var i=0;i<nums.length;i++){
        if(nums[i]<target) ret++;
    }
    return ret;
};

console.log(searchInsert( [1,3,5,6], 5));
console.log(searchInsert( [1,3,5,6], 2));
console.log(searchInsert([1,3,5,6], 7));
console.log(searchInsert([1,3,5,6], 0));
// console.log("hiheihishefie");