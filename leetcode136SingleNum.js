/**
 * @param {number[]} nums
 * @return {number}
 */
function singleNumber(nums) {
	return nums.reduce((prev, curr) => prev ^ curr, 0);
}