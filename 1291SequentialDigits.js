/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function (low, high) {
    var lowDigitN = Math.floor(Math.log(low) / Math.log(10) + 1.00001);
    var upperDigitN = Math.floor(Math.log(high) / Math.log(10) + 1.00001);
    console.log(lowDigitN, upperDigitN);
};
sequentialDigits(1000, 13000);
