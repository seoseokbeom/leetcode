/**
 * @param {string} s
 * @return {number}
 */
var titleToNumber = function (s) {
    return s.split('').map(function (e) { return e.charCodeAt(0)-64; }).reduce(function (a, b) { return 26*a + b; });
};
console.log(titleToNumber('A'));
console.log(titleToNumber('AB'));
console.log(titleToNumber('ZY'));
