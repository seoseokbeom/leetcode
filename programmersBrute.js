function solution(answers) {
  let a = 0;
  let b = 0;
  let c = 0;
  for (var i = 0; i < answers.length; i++) {
    if (answers[i] % 6 == (i + 1) % 6) a++;
    if (i % 2 == 0 && answers[i] == 2) b++;
    if (i % 2) {
      if (i % 8 == 1 && answers[i] == 1) b++;
      if (i % 8 == 3 && answers[i] == 3) b++;
      if (i % 8 == 5 && answers[i] == 4) b++;
      if (i % 8 == 7 && answers[i] == 5) b++;
    }
    console.log(i % 10, answers[i] == 3);
    if (i % 10 <= 1 && answers[i] == 3) c++;
    else if (i % 10 > 1 && i % 10 <= 3 && answers[i] == 1) c++;
    else if (i % 10 > 3 && i % 10 <= 5 && answers[i] == 2) c++;
    else if (i % 10 > 5 && i % 10 <= 7 && answers[i] == 4) c++;
    else if (i % 10 > 7 && i % 10 <= 9 && answers[i] == 5) c++;
  }
  let arr = [a, b, c];
  let max = Math.max(...arr);
  let arr2 = [];
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] == max) arr2.push(i + 1);
  }
  return arr2;
}

console.log(solution([1, 3, 2, 4, 2]));
