/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    var obj = {};
    for(let str of strs) {
        let sorted = str.split('').sort().join('');
        // console.log(str, sorted, obj);
        obj[sorted] ? obj[sorted].push(str) : obj[sorted]=[str];

    }
    return Object.values(obj);
};