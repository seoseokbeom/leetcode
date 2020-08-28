function rightorwrong(s) {
  let result = true;
  let count = 0;
  //   if (s.length == 0) return false;
  for (var i = 0; i < s.length; i++) {
    if (s.charAt(i) == "(") count++;
    else {
      count--;
    }
    if (count < 0) {
      result = false;
      break;
    }
  }
  return result;
}
// console.log(rightorwrong(""));
console.log("rightworong", rightorwrong("))(("));
// console.log(rightorwrong("("));

function solution(p) {
  let left = 0;
  let right = 0;
  let idx = 0;
  if (p.length == 0 || !p) return "";
  for (var i = 0; i < p.length; i++) {
    if (p.charAt(i) == "(") left++;
    if (p.charAt(i) == ")") right++;
    if (left == right) {
      idx = i;
      //   console.log("i", i);
      break;
    }
  }
  console.log("p", p);
  let u = p.slice(0, idx + 1);
  let v = p.slice(idx + 1, p.length);
  console.log("u", u, "v", v);
  let stack = [];
  if (rightorwrong(u)) {
    // if (!v.length) return solution(v);
    let tmp = u.concat(solution(v));
    return tmp;
  } else {
    console.log("v rec");
    console.log(solution(v));
    let tmp2 = "";
    for (var i = 0; i < u.length; i++) {
      if (u.charAt(i) == "(") tmp2 = tmp2.concat(")");
      else tmp2 = tmp2.concat("(");
    }
    tmp2 = tmp2.slice(1, tmp2.length - 1);
    // let tmp2 = u
    //   .slice(1, u.length - 1)
    //   .split("")
    //   .reverse()
    //   .join("");
    console.log("tmp2", tmp2);
    let tmp = "(".concat(solution(v)).concat(")").concat(tmp2);
    console.log("tmp", tmp);
    return tmp;
  }
}

// let u = "()))()((()";
// let tmp2 = "";
// for (var i = 0; i < u.length; i++) {
//   //   console.log(u.charAt(i));
//   if (u.charAt(i) == "(") tmp2 = tmp2.concat(")");
//   else tmp2 = tmp2.concat("(");
//   console.log(tmp2);
// }
console.log(solution("()))((()"));
