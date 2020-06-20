/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var index = nums.indexOf(val);
    while(index>-1){
        nums.splice(index,1);
        index = nums.indexOf(val);
    }
    return nums.length;
};

console.log(removeElement([2,2,3],3));
console.log(removeElement([0,1,2,2,3,0,4,2], 2));