/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    var arr = s.split(" ");
    console.log(arr);
    var i=arr.length-1;
    while(i>=0 && arr[i]==''){
        i--;
    }
    if(i==-1) return 0;
    return arr[i].length;
};

console.log(lengthOfLastWord(""));
console.log(lengthOfLastWord("   "));
console.log(lengthOfLastWord("a    "));
console.log(lengthOfLastWord("a   bd   d "));
console.log(lengthOfLastWord("a   bd   "));
// console.log(lengthOfLastWord("Hello World"));
console.log(lengthOfLastWord("Hello World"));