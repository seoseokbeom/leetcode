/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    var map = new Map();
    for(var elem of nums){
        if(!map.has(elem)) map.set(elem, 1);
        else return elem;
    }
    
};