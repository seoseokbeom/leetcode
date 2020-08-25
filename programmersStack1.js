function solution(progresses, speeds) {
    var arr = [];
    if(!progresses || !progresses.length || !speeds || !speeds.length) return [];
    for(var i=0; i<progresses.length; i++) {
        arr.push(
            Math.ceil((100-progresses[i])/speeds[i])
            )
    }
    var arr2 =[];
    let max = arr[0]
    let count=1;

    if(arr.length==1) return[1];
    for(var i=0; i<arr.length-1; i++) {
        if(max>=arr[i+1]) {
            count++;
        }   
        else {
            max=arr[i+1];
            arr2.push(count);
            count=1;
        }
        if(i==arr.length-2) arr2.push(count);
    }
    return arr2;
}

console.log(solution([99, 1], [1, 99]));