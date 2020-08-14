/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */


var coinChange = function(coins, amount) {
    if(!amount) return 0;
    let queue =[];
    coins.reverse();
    queue.push(...coins);
    let count=1;
    let dp = new Set();
    // coins.forEach(e=>dp.add(e));
    while(queue.length){
        let size = queue.length;
        for(var i=0; i<size; i++) {
            let acc = queue.shift();
            if(dp.has(acc)) continue;
            dp.add(acc);
            console.log(acc, count);
            if(acc>amount) continue;
            if(acc==amount) return count;
            for(var j=0; j<coins.length; j++){
                queue.push(acc+coins[j]);
            }
        }
        console.log('---');
        count++;
    }
    return -1;
}
console.log(coinChange([186,419,83,408],6249));