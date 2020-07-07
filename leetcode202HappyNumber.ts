/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n: number): boolean {
    let ans:number = n;
    let count:number = 0;
    while(ans!== 1) {
        let ansString:string = ans.toString();
        for(var i=0; i< ansString.length; i++) {
            ans += Math.pow(Number(ansString[i]),2);
        }
        count++;
        if(count> 300) return false;
    }
    if(ans==1) return true;
    else return false;
    

};