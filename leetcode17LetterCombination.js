/**
 * @param {string} digits
 * @return {string[]}
 */

var map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

// var print = (a,b) {

// }


var recursive = function(digits) {
    if(digits.length==0) return "";
    // var str = 
    // console.log(digits[0]);
    // console.log(parseInt(digits[0]));
    let digitsNum = parseInt(digits);

    // console.log(digits);
    // console.log(numToString[parseInt(digits[0])]);
    var arr = [];
    for(let i=0;i<digits.length;i++) {
        arr.push()
    }
    // var a = numToString[parseInt(digits[0])].length;
    // var b = numToString[parseInt(digits[0])].length;
    // for(var i=0; i<a; i++) {
    //     return numToString[digits[0]][i]+recursive(digits.slice(1));
    // }
}

var letterCombinations = function(digits) {
    let res = [];
    function go(i,s) {
        if(i === digits.length) {
            res.push(s);
            return;
        }

        for(let c of map[digits[i]]) {
            go(i+1, s+c);
        }
    }

    go(0, '');
    return res;
};

console.log(letterCombinations("23"));
// var tmp = "123";
// console.log(tmp[0]);