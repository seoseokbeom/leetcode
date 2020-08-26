function solution(distance, rocks, n) {
    rocks.sort((a,b)=> a-b);
    rocks.unshift(0);
    rocks.push(distance);
    let dist = [];
    for(var i=0; i<rocks.length-1; i++) {
        dist.push(rocks[i+1]-rocks[i]);
    }
    console.log(dist);


}

console.log(solution(25,	[2, 14, 11, 21, 17],	2))