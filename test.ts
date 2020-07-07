/**
 * @param {string} s
 * @return {number}
 */
var titleToNumber = function(s) {
    return s.split('').map(e=> e.charCodeAt(0)).reduce((a,b)=>a+b);
};

console.log(titleToNumber('A'));
console.log(titleToNumber('AB'));