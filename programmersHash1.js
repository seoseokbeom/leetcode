function solution(participant, completion) {
    let map = new Map();
    for(var i=0;i<completion.length; i++) {
        if(!map.has(completion[i])) map.set(completion[i],1);
        else map.set(completion[i], map.get(completion[i])+1);
    }
    console.log(map);

    for(var i=0; i<participant.length; i++) {
        if(!map.has(participant[i])) return participant[i];
        map.set(participant[i], map.get(participant[i])-1);
        if(map.get(participant[i])<0) return participant[i];
        
    console.log(map);
    }
}

console.log(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))