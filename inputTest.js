const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

var k;
var n;
var count=0;
let input = [];
let arr = [];

rl.on('line', function (line) {
    if(!count) {
        k=Number(line);
        count++;
    }
    else if(count==1) {
        n=Number(line);
        count++;
    }else {
        // console.log(count,"k:",k);
        arr.push(line);
        count++;
        if(count>=k+2){
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
            rl.close();
            // break;
        }   
    }  
})  
  .on('close', function () {
    
  console.log(k, n, arr);
  process.exit();
});