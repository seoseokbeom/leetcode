function solution(clothes) {
    let map = new Map();
    for(var i=0; i<clothes.length; i++){
        if(!map.has(clothes[i][1])) map.set(clothes[i][1], [clothes[i][0]]);
        else map.set(clothes[i][1], [...map.get(clothes[i][1]), clothes[i][0]]);
    }
    // console.log(map);
    let mult = 1;
    map.forEach((a,key)=>{
        console.log(a, key);
        mult *= a.length+1;
    })
    console.log(mult);
    return mult-1;
}

console.log(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]));