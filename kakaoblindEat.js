const { slice } = require("lodash");

function solution(food_times, k) {
  let count = 0;
  let arr = [];
  for (let i = 0; i < food_times.length; i++) {
    arr.push([food_times[i], i + 1]);
  }
  let i = 0;
  arr.sort((a, b) => a[0] - b[0]);
  console.log(arr);
  if (arr.reduce((acc, curr) => acc + curr[0], 0) < k) return -1;
  let prev = 0;
  let len = arr.length;
  let idx = 0;
  let sum = 0;
  while (sum < k && idx < arr.length) {
    if (prev == arr[0][idx]) {
      idx++;
      continue;
    }
    let curr = arr[0][idx];
    sum += (curr - prev) * (len - idx);
    console.log((curr - prev) * (len - idx));
    if (sum > k) {
      sum -= (curr - prev) * (len - idx);
      break;
    }
    idx++;
  }
  console.log("sum", sum);
  console.log("idx", idx);
  let newarr = [...arr.slice(idx, arr.length)];
  newarr.sort((a, b) => a[1] - b[1]);
  console.log(newarr);
  console.log("count", sum);
  i = idx;
  while (sum < k) {
    if (i == arr.length) {
      i = idx;
      continue;
    }
    sum++;
    i++;
  }
  console.log("i", i);
  if (i == arr.length) return 1;
  else return i;
}

console.log(solution([3, 1, 2], 5));

//   while (count < k) {
//     if (arr.length == 0) return -1;
//     if (arr[i][0] > 0) {
//       arr[i][0]--;
//       count++;
//     }
//     if (arr[i][0] == 0) {
//       arr = [...arr.slice(0, i), ...arr.slice(i + 1, arr.length)];
//     } else {
//       i++;
//     }

//     if (i == arr.length) i = 0;
//   }
//   if (arr.length) return arr[i][1];
//   else return -1;
