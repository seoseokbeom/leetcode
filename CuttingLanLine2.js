
var CuttingLine = (n,k,arr) => {
    let hi = arr[0];
    arr.forEach(e=> {
        if(e<hi) hi=e;
    } );
    let count=n;
    while(hi>0) {
        if(arr.reduce((acc, curr) => acc+Math.floor(curr/hi),0) >= k) return hi;
        else hi--;
    }
}

let res = CuttingLine(4,11,[802,743,457,539]);
console.log(res);