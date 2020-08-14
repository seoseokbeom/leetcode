/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    let tmp = 1;
    let visited = new Set();
    visited.add(0);
    while(true) {
        console.log("tmp",tmp)
        console.log(nums, visited);
        console.log('-----------');
        // visited.add(0);
        // console.log(nums[tmp-1]);
        while(nums[tmp-1] && !visited.has(tmp-1)){
            let tmp2 = nums[tmp-1];
            visited.add(tmp-1);
            nums[nums[tmp-1]] = 0;
            tmp=tmp2;
            console.log(nums, visited);
            // console.log(nums);
        }
        console.log('---------')
        tmp=0;
        while(tmp < nums.length && visited.has(tmp)) {
            tmp++;
        }
        if(tmp== nums.length) break;
        visited.add(tmp);
        tmp = nums[tmp];
    }
    console.log(nums, visited);

    let idx =0;
    for(var i=0; i<nums.length; i++) {
        if(nums[i]!==0) {
            nums[idx++]=i+1;
        };
    }
    return nums.slice(0,idx);
};

console.log(findDisappearedNumbers([2,2]));