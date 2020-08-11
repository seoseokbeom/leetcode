const readline = require('readline');
const rl = readline.createInterface(
    {input : process.stdin, output: process.stdout});
let num1 = Math.floor(Math.random() * 10+1);
let num2 = Math.floor(Math.random() * 10+1);

let ans = num1+num2;
let arr = [];
rl.question(`What is ${num1} + ${num2}? \n`,
(_n,_k) => {
    let n=_n;
    let k=_k;
});

for(var i=0; i<k; i++) {
    rl.question(`${i} \n`,
    (tmp) => {
        arr.push(tmp)
    });
}

rl.on('line', (input) => {
    if(input.trim() == ans) {
        rl.close();
    } else {
        rl.setPrompt(`Your ans ${input} is incorrect. try again.\n`);
        rl.prompt();
    }
})

rl.on('close', ()=>{
    console.log("Correcct!!!");
});

