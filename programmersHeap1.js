function solution(jobs) {
    jobs.sort((a,b)=>(a[1]-a[0]) - (b[1]-b[0]) )
     console.log(jobs);

}
console.log(solution([[0, 3], [1, 9], [2, 6]]	));