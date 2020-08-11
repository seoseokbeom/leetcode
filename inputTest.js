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
        [k,n] = line.split(' ').map(e=> Number(e));
        count++;
    }
    else if(count==1) {
        n=Number(line);
        count++;
    }else {
        arr.push(line);
        count++;

        if(count>=k+1){
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
        }   
    }  
})  
  .on('close', function () {
    
  process.exit();
});