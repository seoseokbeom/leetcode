const { isPlainObject } = require("lodash");

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let joinStr = s.replace(/[`~!@#$%^&*()_|+\-=?;: '",.<>\{\}\[\]\\\/]/gi, '').toLowerCase();
    console.log(joinStr);
    if(joinStr.length==0) return true;
    let i =0;
    let j = joinStr.length-1;
    while(i<j) {
        if(joinStr[i]==joinStr[j]) {
            i++;
            j--;
            continue
        }
        else return false;
    }
    return true;
};

console.log(isPalindrome("ab  _a"));