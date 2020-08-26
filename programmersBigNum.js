function solution(number, k) {
    let arr = [];
    let max = 0;
    let find = (num, count, startIdx) => {
        if(count==0) {
            if(max==0) max = Number(num);
            else max= Math.max(max, Number(num));
        }
        for(var i=startIdx; i<num.length; i++){
            let sliced = num.slice(0,i)+num.slice(i+1,num.length);
            find(sliced, count-1, i);
        }
    }
    find(number, k,0);
    return max.toString();
}
console.log(solution("456123789400", 7))