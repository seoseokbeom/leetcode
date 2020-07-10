/**
 * @param {number} numRows
 * @return {number[][]}
 */
var createRow = (n) => {
    if(n==0) return null;
    if(n==1) return [1];
    if(n==2) return [1,1];
    let arr = [1];
    let arr2 = createRow(n-1);
    for(var i=0; i< n-2; i++) {
        arr.push(arr2[i]+arr2[i+1]);
    }
    arr.push(1);
    return arr;
}
var generate = function(numRows) {
    if(numRows==0) return [];
    if(numRows==1) return [[1]]; 
    if(numRows==2) return [[1],[1,1]];
    let arr = [];
    for(var i=1; i<=numRows; i++){
        arr.push(createRow(i));
    }
    return arr;
};

console.log(generate(1));
console.log(generate(2));
console.log(generate(3));
console.log(generate(4));
console.log(generate(5));
console.log(generate(6));