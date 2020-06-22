/**
 * @param {number} n
 * @return {string}
 */
var nextNum = function(strNum) {
    var ret = "";
    var count=1;
    for(var i=0;i<strNum.length-1;i++){
        if(strNum[i]==strNum[i+1]) count++;
        else {
            ret+=count;
            ret+=strNum[i];
            count=1;
        };
        if(i==strNum.length-2) {
            ret+=count;
            ret+=strNum[strNum.length-1];
        }
    }
    return ret;
}
var countAndSay = function(n) {
    if(n==1) return "1";
    if(n==2) return "11";
    var strNum = n.toString();
    var tmp = "11";
    for(var i=2; i<n; i++) {
        tmp = nextNum(tmp);
    }
    return tmp;
};

console.log(countAndSay(1));
console.log(countAndSay(2));
console.log(countAndSay(3));
console.log(countAndSay(4));
console.log(countAndSay(5));
console.log(countAndSay(6));
console.log(countAndSay(7));
console.log(countAndSay(8));

// console.log(countAndSay(23423));