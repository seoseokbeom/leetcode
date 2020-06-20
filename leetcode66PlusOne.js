/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    for(var i=digits.length-1; i>=0; i--){
        if(digits[i] <9 ) {
            digits[i]+=1;
            return digits;
        } else {
            digits[i]=0;
            if(i==0){
                digits.unshift(1);
            }
        }
    }
    return digits;
};

console.log(plusOne([1,2,3]));
console.log(plusOne([4,3,2,1]));
console.log(plusOne([9,0,9]));