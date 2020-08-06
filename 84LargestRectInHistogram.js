/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    if(!heights.length) return 0;
    var max= 0;
    for(var i=0; i<heights.length; i++) {
        var w = 1;
        var j=i;
        while(heights[j-1]>= heights[i]) {
            j--;
        }
        while(heights[j+1]>= heights[i]) {
            j++;
            w++;
        }

        max=Math.max(max, w*heights[i]);
    }
    return max;
};