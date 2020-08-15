
var countBits = function(num) {
    // let dp = new Array(num.length+1).fill(0);
    // dp[1]=1;
    let tmp= [0,1];
    let arr = [1];
    while(tmp.length<=num){
        arr=[...arr, ...arr.map(e=>e+1)];
        tmp.push(...arr);
        console.log(tmp);
    }
    return tmp.slice(0,num+1);
};
console.log(countBits(5));