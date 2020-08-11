const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
var k,n;
var count=0;
let arr = [];
rl.on('line', function (line) {
    if(!count) {
        [k,n] = line.split(' ').map(e=> Number(e));
        count++;
    }
    else {
        arr.push(line);
        count++;
        if(count==k+1){
            let binarySearch = function (start, end) {
                if(end-start == 1) return start;
                let mid = Math.floor((start+end)/2);
                let bool = arr.reduce((acc, curr) => acc+Math.floor(curr/mid),0) >= n;;
                bool ? start = mid :  end = mid;
                return binarySearch(start,end);
            } 
            let res = binarySearch(1,arr[0]);
            console.log(res);
            rl.close();
        }   
    }  
})  
  .on('close', function () {
  process.exit();
});


            // var cutting = (k,n,arr) => {
            //     let hi = arr[0];
            //     return binarySearch(1,hi);
            // }