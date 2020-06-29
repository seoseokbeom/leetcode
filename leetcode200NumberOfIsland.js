/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    if(grid.length==0) return 0;
    let h = grid.length;
    let w = grid[0].length;
    let vis2 = new Array(h).fill(false).map(()=>new Array(w).fill(false));
    let answer=0;
    function inside(row, col) {
        return 0<=row && row <h && 0<=col && col<w;
    }
    let directions = [[-1,0],[1,0],[0,1],[0,-1]];
    let q = [];
    for(let row=0; row<h; row++) {
        for(let col=0; col<w; col++) {
            if(!vis2[row][col] && grid[row][col]==='1') {
                answer++;
                q.push([row,col]);
                vis2[row][col]= true;
                while(q.length) {
                    let p = q.shift();
                    directions.forEach(dir => {
                        var new_row = p[0]+ dir[1];
                        var new_col = p[1]+ dir[0];
                        if(inside(new_row, new_col) && !vis2[new_row][new_col]
                        && grid[new_row][new_col]=='1') {
                            q.push([new_row,new_col]);
                            vis2[new_row][new_col]=true;
                        }
                        
                    });
                }
            }
        }
    }
    return answer;
};
let grid = [['1','1','0','0','0']
    ,['1','1','0','0','0']
    ,['0','0','1','0','0']
    ,['0','0','0','1','1']];