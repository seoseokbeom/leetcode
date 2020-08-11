const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

var a;
var b;
var count=0;
let input = [];
let arr = [];

rl.on('line', function (line) {
    [a,b] = line.split(' ').map(e=> Number(e));
    console.log(a-b);
    rl.close();
           
     
})  
  .on('close', function () {
  process.exit();
});