/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    let count=0;
    var isPrime = (num) => {
        for(var i=2; i<num; i++) {
            if(num%i == 0) return false;
        }
        return true;
    }
    
    for(var i=2; i<n; i++) {
        if(isPrime(i)) count++;
    }
    return count;
};

console.log(countPrimes(499979));