/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    if(!matrix.length || !matrix[0].length) return [];
    var arr = [];
    var i=0; 
    var j=0;
    var count=1;
    while(count) {
        count=0;
        while(j+1<matrix[0].length && matrix[i][j+1]!='x') {
            // console.log("----");
            count=1;
            arr.push(matrix[i][j]);
            matrix[i][j] = 'x';
            j++;}
        while(i+1<matrix.length && matrix[i+1][j]!='x') {
            count=1;
            arr.push(matrix[i][j]);
            matrix[i][j] = 'x';
            i++;}
        while(j-1>=0 && matrix[i][j-1]!='x') {
            count=1;
            arr.push(matrix[i][j]);
            matrix[i][j] = 'x';
            j--;
        }
        while(i-1>=0 && matrix[i-1][j]!='x') {
            count=1;
            arr.push(matrix[i][j]);
            matrix[i][j] = 'x';
            i--;
        }
    }
    arr.push(matrix[i][j]);
    // console.log(arr);
    return arr;
};
