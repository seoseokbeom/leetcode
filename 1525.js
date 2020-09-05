var numSplits = function (s) {
  let count = 0;
  for (var i = 1; i < s.length; i++) {
    let setA = new Set();
    let setB = new Set();
    for (var j = 0; j < i; j++) {
      setA.add(s.charAt(j));
    }
    for (var k = i; k < s.length; k++) {
      setB.add(s.charAt(k));
    }
    if (setA.size == setB.size) count++;
  }
  return count;
};

console.log(numSplits("abcd"));
