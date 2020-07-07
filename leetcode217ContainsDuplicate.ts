/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums:number[]): boolean {
    let set1 = new Set();    // set1.add(nums);
    nums.forEach(element => {
        set1.add(element);
    });
    console.log(set1);
    if(nums.length > set1.size) return false;
    return true;
};
// var containsDuplicate = function (nums) {
//     var sorted = nums.sort(function (a, b) { return a - b; });
//     for (var i = 0; i < nums.length - 2; i++) {
//         if ((sorted[i] ^ sorted[i + 1]) == 0)
//             return true;
//     }
//     return false;
//     // return true;
// };
