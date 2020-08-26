function solution(N, number) {
    let queue = [`${N}`];
    let visited = new Array(100000).fill(0);
    let count=0;
    while(queue.length) {
        let size = queue.length;
        count++;
        for(var i=0; i<size; i++) {
            let n = queue.shift();
            console.log(n, 'count', count);
            function evil(fn) {
                return new Function('return ' + fn)();
            }
            let n_calc = Math.floor(evil( n));
            // console.log(`n calc:`, evil( n));
            if(visited[n_calc]) continue;
            if(count>8) return -1;
            if(n_calc==number) return count;
            visited[n]=1;
            queue.push(n.concat(`${N}`));
            queue.push(n.concat(`*${N}`));
            queue.push(n.concat(`/${N}`));
            queue.push(n.concat(`+${N}`));
            queue.push(n.concat(`-${N}`));
        }
    }
}

console.log(solution(5,12))