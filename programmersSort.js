function solution(array, commands) {
    function find(command) {
        return ( array.slice(command[0]-1,command[1]).sort((a,b)=>a-b)
        [command[2]-1]);
        
    }
    let arr =[];
    for(var i=0; i<commands.length; i++) {
        arr.push(find(commands[i]));
    }
    // console.log(array);
    return arr;
}

console.log(solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]));