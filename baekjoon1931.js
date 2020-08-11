
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

var n;
var count =0;
var arr= [];
rl.on('line', (line) => {
    if(!count) {
        n=parseInt(line);
        count++;
        if(n==1) return 1;
    }
    else {
        arr.push(line.split(' ').map(e=> parseInt(e)));
        count++;
        if(count==n+1) {
            arr= arr.sort((a,b)=> {
                if (a[1] !== b[1]) {
                return a[1] - b[1];
                } else {
                return a[0] - b[0];
                }
            });
            let end = 0;
            const maxN = arr.reduce((acc, cur) => {
                if(cur[0]>=end) {
                    end=cur[1];
                    return acc+1;
                }
                return acc;
            },0)
            console.log(maxN);
            rl.close()
        }
    }
})
.on('close', () => { process.exit() })