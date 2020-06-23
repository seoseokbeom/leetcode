/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSumClosest = function(nums, target) {
    sortArr=nums.sort(function(a, b){return a - b});
    var arr=[];
    console.log(sortArr);
    for(var i=0; i<nums.length-2; i++){
        // if (sortArr[i] > target) break;
        if (i > 0 && nums[i] == nums[i - 1]) {              // skip same result
            continue;
        }
        var j=i+1;
        // if (sortArr[i] === sortArr[i + 1]) continue;
        var k=nums.length-1;
        var ans = sortArr[0]+sortArr[1]+sortArr[2];
        var smallestGap = Math.abs(sortArr[i]+sortArr[j]+sortArr[k] -target);
        while(i<j && j<k) {
            console.log(smallestGap);
            var l=arr.length;
            // if(l!=0 && arr[l-1][0]==sortArr[i] && arr[l-1][1]==sortArr[j]) {
            //     j++;
            //     continue;
            // }
            if(Math.abs(sortArr[i]+sortArr[j]+sortArr[k] - target) < smallestGap ) {
                smallestGap = Math.abs(sortArr[i]+sortArr[j]+sortArr[k] - target);
                ans = sortArr[i]+sortArr[j]+sortArr[k];
                j++;
            }
            else if(sortArr[i]+sortArr[j]+sortArr[k]<target) j++;
            else if(sortArr[i]+sortArr[j]+sortArr[k]>target) k--;
            else j++;
        }
    }
    return ans;
};
console.log(threeSumClosest([0,2,1,-3],1));
// console.log(threeSumClosest([-1,2,1,-4], 1));
// console.log(threeSumClosest([-1,2,4,2,2,3,1,3,1,-4], 23));
// console.log(threeSumClosest([-1,2,4,2,2,3,1,3,1,-4], -23));
// console.log(threeSum( [-4,-4,8]));
// console.log(threeSum( [-1, 0, 1, 2, -1, -4]));
// console.log(threeSum( [0,0,0,0]));
// console.log(threeSum( [0,0]));
// console.log(threeSum( [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]));
// console.log(threeSum( [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]));