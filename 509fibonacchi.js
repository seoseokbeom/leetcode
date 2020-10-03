/**
 * @param {number} N
 * @return {number}
 */
var fib = function (N) {
    var a = 0;
    var b = 1;
    if (N == 0) return 0;
    if (N == 1) return 1;
    var tmp;
    for (var i = 2; i <= N; i++) {
        tmp = a + b;
        a = b;
        b = tmp;
    }
    return tmp;
};

for (var i = 0; i < 10; i++) console.log(fib(i));
