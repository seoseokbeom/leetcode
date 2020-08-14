let wrongMap = new Map()
wrongMap.set('bla', 'blaa')
wrongMap.set('bla2', 'blaa2')

console.log(wrongMap) 
console.log(wrongMap.has('bla'))  
console.log(wrongMap.get('bla2'))  
console.log(wrongMap) 
console.log(wrongMap.delete('bla')) 
console.log(wrongMap.delete('blaa')) 
console.log(wrongMap) 

let arr = [1,3,2];
arr.sort((a,b)=> a-b);
console.log(arr);