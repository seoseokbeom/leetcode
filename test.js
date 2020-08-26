function solution(p) {
    if(!p || !p.length) return '';
    if(check(p)) return p;
    // while(!check(p)) {

        let tmp = '';
        for(var i=0; i<p.length; i++) {
            // console.log(i);
            if(check(p.slice(0,i+1))) {
                tmp=p.slice(0,i+1);
                p=p.slice(i+1, p.length);
                break;
            }
        }
        // console.log('tmp',tmp);
        // console.log('p',p);
    
        let tmp2;
        for(var i=p.length-1; i>=0; i--) {
            // console.log(i);
            if(check(p.slice(i, p.length))) {
                tmp2=p.slice(i, p.length);
                p=p.slice(0, i);
                break;
            }
        }

        if(p) tmp=tmp.concat(' ( ');
        if(tmp2) tmp=tmp.concat(tmp2);
        if(p) tmp=tmp.concat(' ) ');
        if(p.length) p=p.slice(1,p.length-1);
        p=p.split("").reverse().join("");
        // console.log('p',p);
        if(p.length) tmp=tmp.concat(p);
        return tmp;

        // console.log('p',p);
        let ans = tmp.concat(p);
        if(tmp2) ans= ans.concat(tmp2);
        // console.log(ans);
        p= ans;
    // }
    return p;


}

function check(p) {
    let queue = [];
    for(var i=0; i<p.length; i++) {
        if(p[i]=="(") queue.unshift('(');
        else {
            if(queue.pop() !=='(') return false;
        }
        // console.log('queue',queue);
    }
    if(!queue.length) return true;
    else return false;
}

console.log(solution("()))((()"	));
// console.log(check("("));