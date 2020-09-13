function solution(orders, course) {
    var ans = [];
    for (var i = 0; i < course.length; i++) {
        ans = [...ans, ...solution2(orders, course, course[i])];
    }
    ans.sort();

    return ans;
}

function solution2(orders, course, cnt) {
    // res = [];
    // console.log(orders);
    for (var i = 0; i < orders.length; i++) {
        orders[i] = orders[i]
            .split("")
            .sort((a, b) => a.localeCompare(b))
            .join("");
    }
    // console.log(orders);
    // tmp = [];

    var res = [];
    function rec(str, chars, i, count) {
        if (count == 0) {
            res.push(chars);
            return;
        } else if (i >= str.length) {
            return;
        }
        rec(str, chars, i + 1, count);
        chars += str.charAt(i);
        rec(str, chars, i + 1, count - 1);
        chars = chars.slice(0, chars.length - 1);
    }
    var contacts = new Map();
    for (var i = 0; i < orders.length; i++) {
        rec(orders[i], "", 0, cnt);
        // console.log("res", res, res.length);
        for (var j = 0; j < res.length; j++) {
            if (!contacts.has(res[j])) {
                contacts.set(res[j], 1);
            } else {
                // console.log("object", res[j], contacts.get(res[j]));
                contacts.set(res[j], contacts.get(res[j]) + 1);
            }
        }
        res = [];
    }
    // console.log("--");
    var ans = [];
    var max = 0;
    for (var [key, value] of contacts) {
        // console.log(key, value);
        max = Math.max(max, value);
    }
    for (var [key, value] of contacts) {
        if (max >= 2 && value == max) {
            ans.push(key);
        }
    }
    return ans;
}

console.log(
    solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
);
