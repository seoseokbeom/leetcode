/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length!=t.length) return false;
    if(!s.length && !t.length) return true;
    if([...s].sort().join('') == [...t].sort().join('')) return true;
    else return false;
};