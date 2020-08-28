function solution(words, queries) {
  let i = 0;
  let j = 0;
  let idx = 0;
  let count = 0;
  let ans = [];
  let map = new Map();
  while (i < queries.length) {
    if (map.has(queries[i])) {
      ans.push(map.get(queries[i]));
      i++;
      continue;
    }
    // if (!isRight(queries[i])) {
    //   i++;
    //   continue;
    // }
    while (j < words.length) {
      // 길이가 다를때
      if (words[j].length != queries[i].length) j++;
      else {
        // 길이가 같을때

        //idx 끝에 도달
        if (idx == words[j].length) {
          count++;
          j++;
          idx = 0;
          //도중에 char가 같을때
        } else if (
          words[j].charAt(idx) == queries[i].charAt(idx) ||
          queries[i].charAt(idx) == "?"
        ) {
          idx++;

          //도중 char가 다를떄
        } else {
          idx = 0;
          j++;
        }
      }
    }
    ans.push(count);
    map.set(queries[i], count);
    count = 0;
    j = 0;
    i++;
  }
  return ans;
}

// function isRight(word) {
//   let mark = 0;
//   let i = 0;
//   while (i < word.length - 1) {
//     if (word.charAt(i) == "?" && word.charAt(i + 1) != "?") mark++;
//     if (word.charAt(i + 1) == "?" && word.charAt(i) != "?") mark++;
//     i++;
//   }
//   //   console.log(mark);
//   if (mark >= 2) return false;
//   else return true;
// }

console.log(
  solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?"]
  )
);

// isRight("fr?do");
