
var openLock = function(deadends, target) {
    let min = 20;
    let visited = new Set();
    visited.add("0000");
    let queue = [["0000"]];
    let level = 0;
    while(queue.length) {
        let size = queue.length;
        while(size>0) {
            let path = queue.shift();
            // arr.slice(-1)[0] 
            let lock_position = path.slice(-1)[0];
            console.log(lock_position);
            if(deadends.includes(lock_position)) {
                size--;
                continue;
            }
            if(lock_position==target) return path;
            let sb = lock_position;
            for(var i=0; i<4; i++) {
                let current_position=sb.charAt(i);
                let s1 = sb.slice(0,i) + (current_position == '9' ? 0 : current_position-'0'+1) + sb.slice(i+1);
                let s2 = sb.slice(0,i) + (current_position == '0' ? 9 : current_position - '0' -1 ) +sb.slice(i+1);
                if(!visited.has(s1) && !deadends.includes(s1)) {
                    let new_path = [...path];
                    new_path.push(s1);
                    queue.push(new_path);
                    // queue.push(s1);
                    visited.add(s1);
                }

                if(!visited.has(s2) && !deadends.includes(s2)) {
                    let new_path = [...path];
                    new_path.push(s2);
                    queue.push(new_path);
                    // queue.push(s2);
                    visited.add(s2);
                }
            }
            size--;
        }
        level++;
    }
    return -1;
};
// console.log(openLock(["8888"], "0009"));
let ans = openLock(["0201","0101","0102","1212","2002"], "0202");
let str = '';
for(var i=0; i<ans.length; i++) {
    str+=ans[i];
    if(i<ans.length-1) str+=' -> ';
}
console.log(str);
// console.log(openLock(["0000"], "0009"));
