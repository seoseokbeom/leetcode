/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    var res =[];
    var recursion =(sum, arr, idx) => {
        if(sum>target) return;
        if(sum==target){
            // console.log(arr);
            res.push([...arr]);
            // console.log(res);
            return;
        }
        if(idx==candidates.length) return;
        // console.log(idx);
        arr.push(candidates[idx]);
        recursion(sum+candidates[idx], arr, idx);
        arr.pop();
        recursion(sum, arr, idx+1);
        // for(var elem of candidates) {
        //     arr.push(elem);
        //     // console.log(sum+elem, arr);
        //     recursion(sum+elem, arr);
        //     arr.pop();
        // }
    }
    recursion(0,[],0);
    return res;
};