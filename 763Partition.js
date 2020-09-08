const { set } = require("lodash");

var partitionLabels = function (S) {
  let set = {};
  for (var i = 0; i < S.length; i++) {
    set[S.charAt(i)] = i;
  }
  let left = 0;
  let right = 0;
  let res = [];
  for (var i = 0; i < S.length; i++) {
    right = Math.max(right, set[S[i]]);
    if (i == right) {
      res.push(right - left + 1);
      left = right + 1;
    }
  }
  return res;
};

console.log(partitionLabels("ababcbacadefegdehijhklij"));
