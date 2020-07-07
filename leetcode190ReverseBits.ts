/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n:number):number {
    var ans = 0;
    for (var i = 0; i < 32; i++) {
        ans += (n % 2)*Math.pow(2, 31 - i);
        n=Math.floor(n/2);
    }
    return ans;
};
