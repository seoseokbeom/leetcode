/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    var i=0;
    var j=0;
    while(i<m || j< n) {
        if(nums1[i] >= nums2[j] || i>=m+j) {
            nums1.splice(i,0,nums2[j]);
            i++;
            j++;
            nums1.pop();
        }
        else i++;
        
    }
        return nums1;
};