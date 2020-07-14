/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function (matrix) {
    if (!matrix || !matrix.length)
        return;
    var row = new Set();
    var col = new Set();
    for (var i = 0; i < matrix.length; i++) {
        for (var j = 0; j < matrix[0].length; j++) {
            if (!matrix[i][j]) {
                row.add(i);
                col.add(j);
            }
        }
    }
    for(var rVal of row) {
        for(var i=0; i<matrix[0].length; i++) {
            matrix[rVal][i]=0;
        }
    }
    for(var cVal of col) {
        for(var i=0; i<matrix.length; i++) {
            matrix[i][cVal]=0;
        }
    }
    
};
