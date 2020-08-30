function solution(record) {
  for (var i = 0; i < record.length; i++) {
    record[i] = record[i].split(" ");
  }
  let map = new Map();
  for (var i = 0; i < record.length; i++) {
    if (record[i][0] == "Change" || record[i][0] == "Enter")
      map.set(record[i][1], record[i][2]);
  }
  let arr = [];
  for (var i = 0; i < record.length; i++) {
    if (record[i][0] == "Enter")
      arr.push(`${map.get(record[i][1])}님이 들어왔습니다.`);
    else if (record[i][0] == "Leave")
      arr.push(`${map.get(record[i][1])}님이 나갔습니다.`);
  }

  return arr;
}

console.log(
  solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
  ])
);
