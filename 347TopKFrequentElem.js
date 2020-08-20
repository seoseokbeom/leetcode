/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let arr = [];
    let map = new Map();
    for(var i=0; i<nums.length; i++) {
        if(map.has(nums[i])) map.set(nums[i],map.get(nums[i])+1);
        else map.set(nums[i],1);
    }
    for(let [key, value] of map) {
        arr.push([key,value]);
    }
    arr.sort((a,b)=>b[1]-a[1]);
    let res = [];
    for(var i=0; i<k; i++) {
        res.push(arr[i][0]);
    }
    return res;
};