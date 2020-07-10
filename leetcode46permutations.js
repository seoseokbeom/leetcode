/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    var res  = [];
    var recursion = (arr, idx, ans)=> {
        ans.push(arr[idx]);
        arr.splice(idx,1);
        console.log(arr, ans, res);
        if(!arr.length) {
            res.push(ans);
            return;   
        }
        let arr2 = arr;
        for(var i=0; i<arr2.length; i++){
            recursion(arr, i, ans);
        }
    }
    // for(var i=0; i<nums.length; i++) {
    //     recursion(nums,i,[])
    // }
    // let arr = [...nums];
    recursion(nums,0,[]);
    console.log(res);
    // recursion(arr,1,[]);
    // console.log(res);
    
    return res;
};

console.log(permute([1,2,3,4]));