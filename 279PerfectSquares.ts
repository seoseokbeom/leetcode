/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n: number): number {
    var map = new Map();
    var squareList: number[] = [];
    for(var i=1; Math.pow(i,2) <= n; i++) {
        squareList.push(Math.pow(i,2));
    } 
    var recursion=(arr2, count, target)=> {
        if(target===0) {
            map.set(arr2, count);
            return;
        }
        if(target<0) return;
        for(var elem in squareList) {
            if(elem <= target) {
                arr2.push(elem);
                recursion(arr2, count+1, target-elem);
                arr2.pop();
            }
        }
    }
    
    recusion([],0,n);
};