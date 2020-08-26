/**
 * @param {number[]} nums
 * @return {number[][]}
 */
// var permute = function(nums) {
//     var res  = [];
//     var recursion = (arr, idx, ans)=> {
//         ans.push(arr[idx]);
//         arr.splice(idx,1);
//         console.log(arr, ans, res);
//         if(!arr.length) {
//             res.push(ans);
//             return;   
//         }
//         let arr2 = arr;
//         for(var i=0; i<arr2.length; i++){
//             recursion(arr, i, ans);
//         }
//     }
//     // for(var i=0; i<nums.length; i++) {
//     //     recursion(nums,i,[])
//     // }
//     // let arr = [...nums];
//     recursion(nums,0,[]);
//     console.log(res);
//     // recursion(arr,1,[]);
//     // console.log(res);
    
//     return res;
// };


var permute = function(nums) {
    var res = [];

    var recursion = (arr, arr2) => {
        if(arr.length==0) {
            res.push(arr2);
            return;
        }
        for(var i=0; i<arr.length; i++) {
            arr2.push(arr[i]);
            recursion([...arr.slice(0,i), ...arr.slice(i+1,arr.length)], [...arr2]);
            arr2.pop();
        }
    }
    
    recursion(nums,[]);
    return res;
};

console.log(permute([1,2,3]));