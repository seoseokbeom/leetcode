/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */

var trueFalse = (i,j) => {
    if(i>=0 && i< board.length && j>=0 && j< board[0].length) return true
    return false
}


var exist = function(board, word) {
    var recursion = (i,j,count) => {
        if(i<0 || i>=board.length || j<0 || j>=board[0].length || vis[i][j]==1) return false
        var dir = [[-1,0],[1,0],[0,1],[0,-1]];
        console.log(board[i][j]);
        if(board[i][j]==word[count]) {
            if(count==word.length-1) return true;
            vis[i][j]=1;
            return recursion(i+1,j,count+1) || recursion(i-1,j,count+1) || 
                recursion(i,j+1,count+1) || recursion(i,j-1,count+1);

        }
    }
    var vis = new Array(board.length).fill().map(
    ()=> Array(board[0].length).fill(0)
    )

    for(var i=0; i<board.length; i++) {
        for(var j=0; j<board[0].length; j++){
            // console.log(board[i][j]);
            if(board[i][j] != word[0]) continue;
            else if (recursion(i,j,0)) return true;
            // else continue;
        }
    }
    return false;
};


console.log(exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"));
// ["A","B","C","E"]
// ["S","F","C","S"]
// ["A","D","E","E"]