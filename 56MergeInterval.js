/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    if(!intervals.length) return intervals;
    intervals.sort((a,b) => a[0]-b[0]);
    // console.log(intervals);
    var prev = intervals[0];
    var res = [];
    for(var curr of intervals) {
        if(curr[0] <= prev[1]) {
            prev[1] = Math.max(curr[1], prev[1]);
        } else {
            res.push(prev);
            prev = curr;
        }
    }
    res.push(prev);
    // console.log(res);
    return res;
};

merge( [[1,4],[4,5]]);