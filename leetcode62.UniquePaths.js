/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    let sum=0;
    let recursive = (m,n,m2,n2) => {
        if(m2==m || n2==n) return 1;
        return recursive(m,n,m2+1,n2)+recursive(m,n,m2,n2+1);
    }
    return recursive(m,n,1,1);
}
    

console.log(uniquePaths(23,12));