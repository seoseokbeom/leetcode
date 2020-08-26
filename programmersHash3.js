function solution(genres, plays) {
    let map = new Map();
    for(var i=0; i<genres.length; i++){
        if(!map.has(genres[i])) map.set(genres[i], [[i, plays[i]]]);
        else map.set(genres[i],  [...map.get(genres[i]), [i,plays[i]]]);
    }
    // console.log(map) => 
    // Map {
    //     'classic' => [ [ 0, 500 ], [ 2, 150 ], [ 3, 800 ] ],
    //     'pop' => [ [ 1, 600 ], [ 4, 2500 ] ]
    //   }

    let arr = [];
    map.forEach((v,k)=>{
        v.sort((a,b)=> b[1]-a[1]);
        arr.push([k, v.reduce((acc,curr)=>{
            return acc+curr[1]
        },0)]);
    })
    // console.log(map) =>
    // Map {
    //     'classic' => [ [ 3, 800 ], [ 0, 500 ], [ 2, 150 ] ],
    //     'pop' => [ [ 4, 2500 ], [ 1, 600 ] ]
    //   }

    // console.log(arr) =>
    //   [ [ 'classic', 1450 ], [ 'pop', 3100 ] ]
    arr.sort((a,b)=>b[1]-a[1]);
    // console.log(arr) =>
    // [ [ 'pop', 3100 ], [ 'classic', 1450 ] ]
    let ans=[];
    for(var i=0; i<arr.length; i++) {
        let arr2 = map.get(arr[i][0]);
        for(var j=0; j<arr2.length; j++) {
            if(j>=2) break;
            ans.push(arr2[j][0]);
        }
        // console.log(arr2) =>
        // [ [ 4, 2500 ], [ 1, 600 ] ]
        // [ [ 3, 800 ], [ 0, 500 ], [ 2, 150 ] ]
    }

    // console.log(ans) => [ 4, 1, 3, 0 ]
    return ans;
}

console.log(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))