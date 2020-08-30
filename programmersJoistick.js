function solution(name) {
  for (var i = 0; i < name.length; i++) {
    let a = name.charCodeAt(i);
    if (a >= 78) a = 91 - a;
    else a = a - 65;
    console.log(a);
  }
  let arr = route();

  var route = (arr, i, count) => {
    if (arr[i] > 1) return;
    arr[i]++;
    if (i + 1 < arr.length) route(arr, i + 1, count + 1);
    else route(arr, 0, count + 1);
    if (i - 1 >= 0) route(arr, i - 1, count + 1);
    else route(arr, arr.length - 1, count + 1);
  };
}

console.log(solution("JAN"));
