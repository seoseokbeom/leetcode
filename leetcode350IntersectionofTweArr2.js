/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function (nums1, nums2) {
    var map = new Map();
    for (var i = 0; i < nums1.length; i++) {
        if (map.has(nums1[i])) {
            map.set(nums1[i], map.get(nums1[i]) + 1);
        }
        else {
            map.set(nums1[i], 1);
        }
    }
    var arr = [];
    for (var _i = 0, nums2_1 = nums2; _i < nums2_1.length; _i++) {
        var n = nums2_1[_i];
        if (map.has(n) && map.get(n) > 0) {
            arr.push(n);
            map.set(n, map.get(n) - 1);
        }
    }
    return arr;
};
