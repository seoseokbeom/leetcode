
arr=[[0,0,0]];
let unique = [[0,0,0]];
for (let i = arr.length - 1; i >= 0; i--){
    console.log(unique.indexOf(arr[i]));
    if (unique.indexOf(arr[i]) == -1) {
        unique.push(arr[i])
    }
}
