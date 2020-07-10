/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function(n) {
    let nS = n.toString();
    // let nI = parseInt(nS);
    // console.log(nS, nI);
    let products=1;
    let sum=0;
    for(var i=0; i<nS.length; i++) {
        products *= parseInt(nS[i]);
        sum += Number(nS[i]);
    }
    return products-sum;
};  