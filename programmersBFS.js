function solution(tickets) {
  tickets.sort((a, b) => a[1].localeCompare(b[1]));
  // console.log(tickets);
  let stack = [];
  let vis = [];
  for (var i = 0; i < tickets.length; i++) {
    if (tickets[i][0] == "ICN") {
      stack.push(...tickets[i]);
      vis[i] = 1;
      break;
    }
  }
  // console.log(stack);
  for (var j = 0; j < tickets.length - 1; j++) {
    for (var i = 0; i < tickets.length; i++) {
      if (!vis[i] && tickets[i][0] == stack[stack.length - 1]) {
        vis[i] = 1;
        stack.push(tickets[i][1]);
        break;
      }
    }
  }
  // console.log(stack);
  return stack;
}

console.log(
  solution([
    ["ICN", "JFK"],
    ["HND", "IAD"],
    ["JFK", "HND"],
  ])
);
