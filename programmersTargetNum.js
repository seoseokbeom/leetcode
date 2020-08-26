function solution(numbers, target) {
    let count =0;
    var recursion = (sum, i) => {
        if(i==numbers.length) {
            if(sum==target) count++;
            return;
        }
        recursion(sum+numbers[i],i+1);
        recursion(sum-numbers[i],i+1);
    }
    recursion(0,0);
    return count;
}

console.log(solution([1, 1, 1, 1, 1], 3));