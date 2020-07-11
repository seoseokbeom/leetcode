/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low: number, high: number) {
    var lowDigitN = Math.floor(Math.log(low) / Math.log(10) + 1.00001);
    var upperDigitN = Math.floor(Math.log(high) / Math.log(10) + 1.00001);
    // console.log(lowDigitN, upperDigitN);
    let lowStart=0;
    for(var i=1; i<=lowDigitN; i++) {
        lowStart*=10;
        lowStart+=i;
    }
    if(lowDigitN!== upperDigitN) {
        let upperStart=0;
        for(var i=1; i<=upperDigitN; i++) {
            upperStart*=10;
            upperStart+=i;
        }
    }

    
};

sequentialDigits(1000, 13000);
