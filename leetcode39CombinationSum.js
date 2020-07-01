/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */

 /**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    var buffer= [];
    var result= [];
    var recursive= (index, target) => {
        if(target ==0 ) return result.push(buffer.slice());
        if(target < 0) 
        {
            return;
        }
        if(index == candidates.length) return;
        buffer.push(candidates[index]);
        recursive(index, target-candidates[index]);
        buffer.pop();
        recursive(index+1, target);
    }           
    
    recursive(0,target);
    return result;
};

console.log(combinationSum([2,3,6,7],7));

// var combinationSum = function(candidates, target) {
//     candidates.sort((a,b)=> a-b);
//     for(let i=0; i<candidates.length; i++) { 
//         if(candidates[i] > target) candidates.splice(i,1);
//     }
//     let sum=0;
//     arr2d=[];
//     let recersive = (arr, i, sum, target) => {
//         if(sum+candidates[i]>target) {
//             console.log('canceled');
//             return;}
//         if(sum+candidates[i]==target) {
//             console.log("--matched sum--",sum+candidates[i]);
//             arr.push(candidates[i]);
//             arr2d.push(arr);
//             console.log("arr2d",arr2d);
//             return;
//         }
//         if(sum+candidates[i]<target) {
//             arr.push(candidates[i]);
//             sum=sum+candidates[i];
//             console.log("sum",sum, "added num:",candidates[i]);
//             for(let j=0; j<candidates.length; j++) {
//                 recersive(arr, j, sum, target);
//             }
//         }
//         return;
//     }
//     for(let i=0; i<candidates.length; i++){
//         recersive([], i, 0, target);
//     }
//     return arr2d;
// //     recersive(arr2d, arr, i, sum, target) {
// //     }
// };