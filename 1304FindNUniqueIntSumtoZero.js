
var sumZero = function(n) {
    var arr = [];
    let half = Math.floor(n/2);
    for(var i=0; i<Math.floor(n/2); i++){
        arr.push(n-2*i);
        arr.push(-n+2*i);
    }
    if(n%2) arr.push(0);
    return arr;
};