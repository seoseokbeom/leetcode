/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let nums3 = [];
    let i=0;
    let j=0;
    while(i<nums1.length && j<nums2.length) {
        if(nums1[i] < nums2[j]){
            nums3.push(nums1[i]);
            i++;
        } else {
            nums3.push(nums2[j]);
            j++;
        }
    }
    while(i<nums1.length) {
        nums3.push(nums1[i]);
        i++;
    }
    while(j<nums2.length) {
        nums3.push(nums2[j]);
        j++;
    }
    let len = nums1.length+nums2.length;
    if((len)%2==0) {
        return (nums3[len/2] + nums3[len/2-1])/2;
    } else {
        return nums3[len/2-0.5];
    }
};

console.log(findMedianSortedArrays([1,3],[2]));
console.log(findMedianSortedArrays([1,2],[3,4]));