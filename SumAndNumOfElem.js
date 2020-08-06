// Given a sum of elements (n) and a number of elements (k), find the number of distinct arrays under these conditions:

// In each array, the there are k elements whose sum is equal to n.

// In each array, each element should be greater than or equal to the element on its left.

// The elements formed in each array are distinct

// Edit: elements have to be positive integers

let func(n,k) {
    let arr = [];
    for(var a = 0; a< Math.floor(n/4); a++) {
        for(var b = a; b<Math.floor(n/3); b++ ) {
            for(var c = b; c<Math.floor(n/2); c++) {
                for(var d = c; d<=n-3; d++) {
                    
                }
            }
        }
    }
}