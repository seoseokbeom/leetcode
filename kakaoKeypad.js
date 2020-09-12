const { result } = require("lodash");

function solution(numbers, hand) {
  let left_key = [1, 4, 7];
  let right_key = [3, 6, 9];
  let hand_position = ["*", "#"];

  let position = {
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
    "*": [3, 0],
    0: [3, 1],
    "#": [3, 2],
  };
  let result = "";

  for (var i = 0; i < numbers.length; i++) {
    // console.log(i, result);
    console.log(hand_position, numbers[i]);
    if (left_key.includes(numbers[i])) {
      result += "L";
      hand_position[0] = numbers[i];
      continue;
    } else if (right_key.includes(numbers[i])) {
      result += "R";
      hand_position[1] = numbers[i];
      continue;
    } else {
      let near_hand = get_near_hand(
        position,
        hand_position[0],
        hand_position[1],
        numbers[i],
        hand
      );
      if (near_hand == "L") {
        result += "L";
        hand_position[0] = numbers[i];
      } else {
        result += "R";
        hand_position[1] = numbers[i];
      }
    }
  }

  function get_near_hand(p, l, r, n, hand) {
    let ld = Math.abs(p[l][0] - p[n][0]) + Math.abs(p[l][1] - p[n][1]);
    let rd = Math.abs(p[r][0] - p[n][0]) + Math.abs(p[r][1] - p[n][1]);
    let near_hand;
    // console.log(p, l, r, n, hand);
    // console.log("dis", ld, rd);
    // console.log(hand);
    if (ld == rd) {
      near_hand = hand == "left" ? "L" : "R";
    } else if (ld < rd) {
      near_hand = "L";
    } else {
      near_hand = "R";
    }
    return near_hand;
  }
  return result;
}

console.log(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"));

var a = () => {
  return 2;
};

console.log(a());
