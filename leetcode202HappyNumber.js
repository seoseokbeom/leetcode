/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {
    var ans = n;
    var count = 0;
    while (ans !== 1) {
        var ansString = ans.toString();
        for (var i = 0; i < ansString.length; i++) {
            ans += Math.pow(Number(ansString[i]), 2);
        }
        count++;
        if (count > 300)
            return false;
    }
    if (ans == 1)
        return true;
    else
        return false;
};
