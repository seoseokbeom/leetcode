
function solution(n, costs) {

    let ret = ( mid) => {
        return costs.reduce((acc,curr) => {
            return acc+Math.floor(mid/curr); 
        },0)
    }

    let binary = ( hi, lo) => {
        var mid = Math.floor((hi+lo)/2);
        let res = ret(mid);
        if(res> n) {
            if(ret(mid-1)<n && n<res) return mid; 
            hi=mid-1;
        }
        else if(res== n ) {
            if(ret(mid-1)<n) return mid;
            hi=mid-1;
        }
        else {
            lo=mid+1;
        }
        return binary( hi,lo);
    }
    let min = Math.min(...costs);
    return binary(2*n*min,0);
}

console.log(solution(30,	[7, 1,2,4]	));