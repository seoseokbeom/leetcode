function solution(n) {
    let n_str = n.toString();
    let mincut = Number.MAX_VALUE;
    let addresult = 0;
    if (n < 10) {
        return [0, n];
    }
    var split = (s_num, i, cnt) => {
        if (s_num.length == 1) {
            if (mincut > cnt) {
                mincut = cnt;
                addresult = parseInt(s_num);
            }
            return;
        }
        if (i > s_num.length - 1) {
            return;
        }
        split(s_num, i + 1, cnt);
        let a = s_num.slice(0, i);
        let b = s_num.slice(i);
        if (b.length >= 2 && b.charAt(0) == "0" && b.charAt(1) == "0") return;
        else {
            let tmpaddstr = (parseInt(a) + parseInt(b)).toString();
            split(tmpaddstr, 1, cnt + 1);
        }
    };

    split(n_str, 1, 0);
    return [mincut, addresult];
}

console.log(solution(10204067));
// console.log(solution(10007));
// console.log(solution(9));
// console.log(mincut, addresult);

// console.log("----");
// console.log(mincut, addresult);
