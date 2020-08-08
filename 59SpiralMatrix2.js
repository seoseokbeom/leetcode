/**
 * @param {number} n
 * @return {number[][]}
 */
var generateMatrix = function(n) {
    let matrix = Array(n).fill().map(()=>Array(n).fill(Number.MAX_VALUE));
    // console.log(matrix);
    let i=0;
    let j=0;
    let count=1;
    matrix[0][0]=count;
    while(count<n*n){
        console.log('5');
        while(j<n-1 && count < matrix[i][j+1] ) {
            console.log('1');
            ++j;
            matrix[i][j]=++count;
        }
        while(i<n-1 && count < matrix[i+1][j]) {
            console.log('2');
            ++i;
            matrix[i][j]=++count;
        }
        while(j>0 && count < matrix[i][j-1]) {
            console.log('3');
            --j;
            matrix[i][j]=++count;
        }
        while(i>0 && count < matrix[i-1][j]) {
            console.log('4');
            --i;
            matrix[i][j]=++count;
        }
        console.log('count',count);
    }
    return matrix;
};

console.log(generateMatrix(3));

// o o o o o 
// o o o o o 
// o o o o o
// o o o o o
// o o o o o

// 1 4 4 4 3 3 2 2 1 1