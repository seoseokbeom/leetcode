/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    if(!nums.length) return;
    // if(nums[0]==0) return 0;
    if(nums.length==1) return 0
    let queue = [];
    let str = {
        val: nums[0],
        idx: 0,
        count:0
    };
    queue.push({...str});
    while(queue.length) {
        var first = {...queue[0]};
        // console.log(first);
        for(var i=1; i<=first.val; i++) {
            // console.log('i',i);
            if(first.idx+i >= nums.length-1) return first.count+1;
            str.idx= first.idx+i;
            str.val= nums[first.idx+i];
            str.count= first.count+1;
            // console.log('str',str);
            queue.push({...str});
        }        
        // console.log('queue shift', queue.shift());
        // queue.shift();
    }
};


console.log(jump([9,4,5,4,1,8]));