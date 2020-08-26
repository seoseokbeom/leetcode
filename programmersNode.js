function solution(n, edge) {
    let visited = [1];
    let queue= [1];
    let count=0;
    while(visited.length<n) {
        let size = queue.length;
        count++;
        // console.log(count, queue);
        for(var i=0; i<size; i++) {
            let node = queue.shift();
            // console.log('edge length:',edge.length);
            for(let j=0; j<edge.length; j++) {
                if(edge[j].includes(node)) {
                    // console.log('j',j)
                    edge[j].forEach(e=> {
                        if(!visited.includes(e)) {
                            console.log('node, e',node, e)
                            queue.push(e);
                            visited.push(e);
                            console.log(queue);
                        }
                    })
                    edge = [...edge.slice(0,j), ...edge.slice(j+1,edge.length)];
                    j--;
                    // let filtered = edge[j].filter(e=> !visited.includes(e));
                    // // console.log('filtered:',filtered);
                    // queue.push(...filtered);
                    // visited.push(...filtered);
                }
            }
        }
    }
    return queue.length;
}


console.log(solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))