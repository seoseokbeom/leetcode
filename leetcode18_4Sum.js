/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */

var threeSum = function(nums, target) {
    if (nums.length < 3) return [];
    sortArr=nums.sort(function(a, b){return a - b});
    var arr=[];
    console.log(sortArr);
    for(var i=0; i<nums.length-2; i++){
        // if (sortArr[i] > 0) break;
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
            if(sortArr[i]+sortArr[j]+sortArr[k]==target) {
                // console.log(i,j,k);
                arr.push([sortArr[i],sortArr[j],sortArr[k]])
                j++;
            };
            if(sortArr[i]+sortArr[j]+sortArr[k]<target) j++;
            if(sortArr[i]+sortArr[j]+sortArr[k]>target) k--;
        }
    }
    return arr;
};

// function sum(total, curr) {
//     return total + curr; 
// }

const reducer = (accumulator, currentValue) => accumulator + currentValue;

var fourSum = function(nums, target) {
    let sorted = nums.sort((a,b)=>a-b);
    // let i=0;
    let arr=[];
    if (nums.length<4) return [];
    console.log(sorted);
    let sum =0;
    for(let i=0; i<nums.length-3; i++) {
        // console.log("---");
        if(i>0 && sorted[i]==sorted[i-1]) continue;
        console.log(sorted.slice(i+1,nums.length));
        console.log("i:",i,", sorted[i]:",sorted[i]);
        let Sum3 = threeSum(sorted.slice(i+1,nums.length), target-sorted[i]);
        if(Sum3.length>0){
            console.log(Sum3);
            Sum3.forEach(element => {
                element.unshift(sorted[i]);
                arr.push(element);
            });
            console.log("arr:",arr);
            // arr.push(Sum3);
        }
        // console.log(sorted);
    }
    console.log("arr:",arr);
    return arr;
};

console.log(fourSum([1, 0, -1, 0, -2, 2], 0));

