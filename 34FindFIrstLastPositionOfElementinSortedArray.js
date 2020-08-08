/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    
    var recursion = (start, end) => {
        let mid = Math.floor((start+end)/2);
        console.log('mid',mid,'nums[mid]', nums[mid], 'target',target, start,end,'true false:', nums[mid]==target);
        if(start>end) return [-1,-1]
        if(nums[mid]==target) return mid;
        if(nums[mid]>target) end = mid-1;
        else start=mid+1;
        return recursion(start,end)
        // return [-1,-1];
    }
    
    let idx = recursion(0,nums.length-1);
    console.log(idx);
    if(idx==[-1,-1]) return [-1,-1]
    let i=idx;
    let j=idx;
    while(i>0 && nums[i-1]==target) {
        i--;
    }
    while(j<nums.length && nums[j+1]==target){
        j++;
    }
    
    return [i,j];
};

console.log(searchRange([5,7,7,8,8,10],8))