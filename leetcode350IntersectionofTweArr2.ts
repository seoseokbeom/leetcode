/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1: number[], nums2: number[]): number[] {
    let map = new Map();
    for(var i=0; i<nums1.length; i++) {
        if(map.has(nums1[i])) {
            map.set(nums1[i], map.get(nums1[i])+1);
        } 
        else {
            map.set(nums1[i], 1);
        }
    }

    let arr = [];
    for(let n of nums2) {
       if(map.has(n) && map.get(n)>0) {
            arr.push(n);
            map.set(n,map.get(n)-1); 
        }
    }
    return arr;

};