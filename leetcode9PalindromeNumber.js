/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var numString = x.toString();
    for(var i=0;i<numString.length/2; i++){
        if(numString[i] != numString[numString.length-1-i]) return false;
    }
    return true;
};

console.log(isPalindrome(121));
console.log(isPalindrome(-121));
console.log(isPalindrome(10));
console.log(isPalindrome(11));
console.log(isPalindrome(-1111));
console.log(isPalindrome(1331));