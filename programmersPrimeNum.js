function solution(numbers) {
    let visited = [];
    let count=0;
    var recursion = (prev, curr) => {
        if(prime(parseInt(curr)) && !visited[parseInt(curr)]) {
            visited[parseInt(curr)]=1;
            count++;
        }
        if(prev.length==0) {
            return;
        }
        for(var j=0; j<prev.length; j++) {
            recursion(prev.slice(0,j).concat(prev.slice(j+1, prev.length)), curr.concat(prev.charAt(j)))
        }
    }
    recursion(numbers, '');
    return count;
}

function prime(num) {
    if(isNaN(num)) return false;
    let tmp = Math.floor(Math.sqrt(num));
    if(num==0 || num==1) return false;
    for(var i=2; i<=tmp; i++) {
        if(num%i==0) return false;
    }
    return true;
}

// console.log(solution("011"));