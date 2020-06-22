/**
 * @param {string} digits
 * @return {string[]}
 */

var numToChar = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

var recursive = function(digits) {
    if(digits.length==0) return "";
    // var str = 
    console.log(digits[0]);
    console.log(parseInt(digits[0]));
    console.log(numToChar[parseInt(digits[0])]);
    var  a = numToChar[parseInt(digits[0])].length;
    for(var i=0; i<a; i++) {
        return numToChar[digits[0]][i]+recursive(digits.slice(1));
    }
}

var letterCombinations = function(digits) {
    var array = [];
    array.push(recursive(digits));
    return array;
};

console.log(recursive("23"));
// var tmp = "123";
// console.log(tmp[0]);