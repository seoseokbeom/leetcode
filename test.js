let arr = [1,2,3,4,2,3];

let svg = arr.splice();
let svg2 = arr.slice();
console.log(arr);
// console.log(svg);
console.log(svg2);
arr[0]=5;
console.log(arr);
console.log(svg2);
console.log(svg2==arr);