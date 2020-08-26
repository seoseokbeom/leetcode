function solution(phone_number) {
    let len = phone_number.length;
    let post = '';
    for(var i=0; i<len-4; i++) {
        post=post.concat('*');
    }
    let last = phone_number.slice(len-4, len);
    return post.concat(last);
}

console.log(solution("027778888"));


function prime(num) {
    let dp = [];
    let count =0;
    for(var i=2; i<=n; i++) {
        if(dp[i]==undefined) {
            console.log('i',i);
            dp[i] =1;
            count++;
            let j=2;
            while(i*j<=n) {
                dp[i*j]=0;
                j++;
            }
        }
    }
    return count;
}