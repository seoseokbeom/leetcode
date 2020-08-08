/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    let arr = Array(grid.length).fill().map(()=> Array(grid[0].length).fill(0));
    for(var i=0; i<grid.length; i++) {
        for(var j=0; j<grid[0].length; j++) {
            if(i==0 && j==0) continue;
            else if(j==0 && i-1>=0) arr[i][j]= arr[i-1][j]+grid[i-1][j];
            else if(i==0 && j-1>=0) arr[i][j]= arr[i][j-1]+grid[i][j-1];
            else arr[i][j]= Math.min(arr[i-1][j]+grid[i-1][j], arr[i][j]= arr[i][j-1]+grid[i][j-1]);
        }
    }
    i=grid.length-1;
    j=grid[0].length-1;
    return arr[i][j]+grid[i][j];
};