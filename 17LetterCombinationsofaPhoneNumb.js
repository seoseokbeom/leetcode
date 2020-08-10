/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if(!digits) return [];
    let arr = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'];
    let res = [];
    var recursion = (idxOfDigits, str) => {
        if(idxOfDigits==digits.length) {
            res.push(str);
            return;
        }
        let btnNum = Number(digits[idxOfDigits]);  //ex) digits[idxOfDigits] = 3
        let btnStr = arr[btnNum]; 
        for(var j=0; j< btnStr.length; j++) {
            str+=btnStr[j];
            recursion(idxOfDigits+1,str);
            str=str.slice(0, -1);
        }
    }
    recursion(0, '', digits);
    return res;
};
