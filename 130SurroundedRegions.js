/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    if(!board || !board.length) return board;
    let rowL = board.length;
    let colL = board[0].length;
    var first = () => {
        for(var i=0; i<colL; i++) {
            // console.log(i,board[0][i],board[rowL-1][i]);
            if(board[0][i] == "O") bfs(i,0);
            if(board[rowL-1][i] == "O") {
                bfs(i,rowL-1);}
        }
        for(var j=1; j<rowL-1; j++) {
            if(board[j][0]=="O") bfs(0,j);
            if(board[j][colL-1]=="O") bfs(colL-1,j);
        }
    }
    
    var bfs = (i,j) => {
        if(i<0 || i>=colL || j<0 || j>=rowL) return;
        if(board[j][i]=="O"){
            board[j][i]="#";
            bfs(i-1,j);
            bfs(i+1,j);
            bfs(i,j-1);
            bfs(i,j+1);
            }
    }
    
    var second = () => {
        for(var j=0; j<rowL; j++) {
            for(var i=0; i<colL; i++) {
                if(board[j][i]=="X") continue;
                if(board[j][i]=="O") board[j][i]="X";
                if(board[j][i]=="#") board[j][i]="O";
            }
        }
    }
    
    
    first();
    second();
    return board;    
};