/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSumClosest = function(nums, target) {
    sortArr=nums.sort(function(a, b){return a - b});
    var arr=[];
    var ans = sortArr[0]+sortArr[1]+sortArr[nums.length-1];
    var smallestGap = Math.abs(sortArr[0]+sortArr[1]+sortArr[nums.length-1] -target);
    for(var i=0; i<nums.length-2; i++){
        if (i > 0 && nums[i] == nums[i - 1]) {              // skip same result
            continue;
        }
        var j=i+1;
        var k=nums.length-1;
        while(i<j && j<k) {
            var l=arr.length;
            if(Math.abs(sortArr[i]+sortArr[j]+sortArr[k] - target) < smallestGap ) {
                smallestGap = Math.abs(sortArr[i]+sortArr[j]+sortArr[k] - target);
                ans = sortArr[i]+sortArr[j]+sortArr[k];
            }
            if(sortArr[i]+sortArr[j]+sortArr[k]<=target) j++;
            if(sortArr[i]+sortArr[j]+sortArr[k]>target) k--;
        }
    }
    return ans;
};
console.log(threeSumClosest([-1,2,1,-4], 1));
// console.log(threeSumClosest([-1,2,1,-4], 1));
// console.log(threeSumClosest([-1,2,4,2,2,3,1,3,1,-4], 23));
// console.log(threeSumClosest([-1,2,4,2,2,3,1,3,1,-4], -23));
// console.log(threeSum( [-4,-4,8]));
// console.log(threeSum( [-1, 0, 1, 2, -1, -4]));
// console.log(threeSum( [0,0,0,0]));
// console.log(threeSum( [0,0]));
// console.log(threeSum( [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]));
// console.log(threeSum( [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]));