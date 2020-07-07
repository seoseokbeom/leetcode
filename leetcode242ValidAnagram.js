/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    var s1 = s.split('').sort(function (a, b) {
        return a.localeCompare(b);
    });
    var t1 = t.split('').sort(function (a, b) {
        return a.localeCompare(b);
    });
    console.log(s1);
    console.log(t1);
    // console.log(s1==t1);
    // console.log(s1===t1);
    console.log(s1.length, t1.length);
    return arrEqual(s1, t1);
};
function arrEqual(a, b) {
    if (a === b)
        return true;
    if (!a || !b) {
        console.log('---');
        return false;
    }
    if (a.length != b.length) {
        console.log(a.length);
        console.log(b.length);
        return false;
    }
    for (var i = 0; i < a.length; i++) {
        if (a[i] !== b[i]) {
            console.log("element diff");
            return false;
        }
    }
    return true;
}
