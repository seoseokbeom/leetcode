/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    if (nums.length < 3) return [];
    sortArr=nums.sort(function(a, b){return a - b});
    var arr=[];
    console.log(sortArr);
    for(var i=0; i<nums.length-2; i++){
        if (sortArr[i] > 0) break;
        if (i > 0 && nums[i] == nums[i - 1]) {              // skip same result
            continue;
        }
        var j=i+1;
        // if (sortArr[i] === sortArr[i + 1]) continue;
        var k=nums.length-1;
        while(i<j && j<k) {
            var l=arr.length;
            if(l!=0 && arr[l-1][0]==sortArr[i] && arr[l-1][1]==sortArr[j]) {
                j++;
                continue;
            }
            if(sortArr[i]+sortArr[j]+sortArr[k]==0) {
                // console.log(i,j,k);
                arr.push([sortArr[i],sortArr[j],sortArr[k]])
                j++;
            };
            if(sortArr[i]+sortArr[j]+sortArr[k]<0) j++;
            if(sortArr[i]+sortArr[j]+sortArr[k]>0) k--;
        }
    }
    return arr;
};

console.log(threeSum(  [-1, 0, 1, 2, -1, -4]));
// console.log(threeSum( [-1, 0, 1, 2, -1, -4]));
// console.log(threeSum( [0,0,0,0]));
// console.log(threeSum( [0,0]));
// console.log(threeSum( [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]));
// console.log(threeSum( [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]));