/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if(s.length<=1) return s;
    var maxLeft=0;
    var maxRight=0;
    var k;
    var max =1;
    for(var i=1;i<=s.length-2; i++){
        k=1;
        // one char pivot
        while(i-k>=0 && i+k <=s.length-1 && s[i-k]==s[i+k]){
            if(max < 2*k+1){
                max=2*k+1;
                maxLeft = i-k; 
                maxRight = i+k;
            }
            k++;
        }
    }
    //center pivot
    for(var i=1;i<=s.length-1; i++){
        k=1;
        while(i-k>=0 && i+k-1<=s.length-1 && s[i-k]===s[i+k-1]){
            if(max < 2*k){
                max=2*k+1;
                maxLeft = i-k; 
                maxRight = i+k-1;
            }
            k++;
        }
    }
    console.log(maxLeft,maxRight);

    return s.slice(maxLeft,maxRight+1);
};


// console.log(longestPalindrome("1111"));
// console.log(longestPalindrome("1221"));
// console.log(longestPalindrome("12321"));
console.log(longestPalindrome("ccc"));