/**
 * @param {number[][]} points
 * @return {number}
 */
var minAreaRect = function(points) {
    let i=0;
    let j=0;
    let min = Math.abs(points[1][0]-points[0][0]) * (points[1][1]-points[0][1]);
    var recursion = (i,j) => {
        if(j==points.length) return;
        if(i==points.length-1) return;
        if(Math.abs(points[j][0]-points[i][0]) * (points[j][1]-points[i][1]) < min) min = Math.abs((points[j][0]-points[i][0]) * (points[j][1]-points[i][1]));
        recursion(i,j+1);
        recursion(i+1,i+2);
    }
    return min;
};