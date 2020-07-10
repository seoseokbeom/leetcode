/**
 * @param {number} num
 * @return {string[]}
 */

var readBinaryWatch = function(num) {
    if(num==0) return ["0:00"];
    let arr = [-1,-2,-4,-8,1,2,4,8,16,32];
    let res = [];
    let answer=[];
    var recursion = (prev, curr) => {
        if(curr.length==num) res.push(curr);
        for(var i=0; i<prev.length; i++){
            recursion([...prev.slice(i+1)], [...curr, prev[i]]);
        }
    }
    recursion(arr, []);
    for(var i=0; i<res.length; i++) {
        let hour=0;
        let min=0;
        for(var j=0; j<num; j++) 
            if(res[i][j]<0) hour-=res[i][j];
            else min+=res[i][j];
        
        if(hour>=12 || min>=60) continue;
        answer.push(`${hour}:${min >= 10 ? min : '0'+min}`);
    }
    return answer;
};
