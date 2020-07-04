/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    
    var bruteforce(coins: number[], amount: number, sum: number, count: number) {
        if(sum == amount) {
            return count;
        }
        let Obj = [];
        Obj.push(coins.forEach(element => {
            return {
                sum: element,
                count: 1
            }
        }));
        console.log(Obj);
        let queue = [...Obj];
        while(!queue && queue.length) {
            let p = queue.shift();
            queue.push(coins.forEach(element => {
                return {
                    sum: {p.sum}+element,
                    count: {p.count}+1
                }
            }))
            
        }
        
        for(var i=0; i<coins.length; i++ ) {
            bruteforce(coins, amount, sum+coins[i], count+1 );
        }

    }
};