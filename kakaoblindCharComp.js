function solution(s) {
  let min = sub(s, 1);
  for (var i = 2; i < s.length; i++) {
    min = Math.min(sub(s, i), min);
  }
  return min;
}
function sub(s, len) {
  s = s.split("");
  let i = 0;
  let j = 0;
  while (i < s.length) {
    if (s.slice(i, i + len).join("") == s.slice(j, j + len).join("")) {
      j += len;
    } else {
      if (j == i + len) {
        i = j;
        j += len;
      } else {
        let nums = ((j - i) / len).toString().split("");
        s.splice(i, j - i - len, ...nums);
        j = i = i + len + nums.length;
      }
    }
  }
  return s.join("").length;
}

console.log(solution("xababcdcdababcdcd"));
