/**
 * @param {number[][]} grid
 * @return {number}
 */
var getMaximumGold = function(grid) {
    let m = grid.length;
    let n = grid[0].length;
    let Sum=0;
    let dir = [[-1,0],[1,0],[0,1],[0,-1]];
    
    for(var i=0; i<m; i++) {
        for(var j=0; j<n; j++){
            if(grid[i][j]!=0) {
                console.log(i,j);
                console.log(grid[i][j],count, Sum);
                // count+= grid[i][j];
                recursion(0,i,j);
            }
        }
    }

    var recursion =(count, a, b) => {
        
        if(grid[a][b]==0) {
            Sum = Math.max(Sum, count);
            return Sum;
        } else {
            count+=grid[a][b];
        }
        for(var k=0; k<dir.length; k++) {
            let tmp=grid[i][j];
            grid[i][j]=0;
            if(i+dir[k][0] >=0 && i+dir[k][0] <m && j+dir[k][1] >=0 && j+dir[k][1] <n ) {
                recursion(count,i+dir[k][0],j+dir[k][1]);
            }
            grid[i][j]= tmp;
        }
    }
    
    return recursion(0,0,0);
};
console.log(getMaximumGold([[0,6,0], [5,8,7], [0,9,0]]));