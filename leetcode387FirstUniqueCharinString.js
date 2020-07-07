/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
    var set1 = new Map();
    for (var i = 0; i < s.length; i++) {
        if (set1.has(s[i])) {
            set1.set(s[i], 2);
        }
        else
            set1.set(s[i], 1);
    }
    for (var i = 0; i < s.length; i++) {
        if (set1[s[i]] == 1)
            return i;
    }
    return -1;
};
