/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function(nums) {
    var recursive = (s) => {
        if(s.length==1) return s
        for(let i=0; i<s.length; i++) {
            let s2 = s.splice(i,1);
            recursive(s2);
        }
    }  
};