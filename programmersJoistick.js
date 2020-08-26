function solution(name) {

    for(var i=0; i<name.length; i++) {
        let a = name.charCodeAt(i);
        if(a>=78) a=91-a;
        else a= a-65;
        console.log(a);
    }
}

console.log(solution("JAN"))