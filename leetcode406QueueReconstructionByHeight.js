/**
 * @param {number} num
 * @return {number[]}
 */

var sortP = (a,b) => {
    if(a[0]!==b[0]) return b[0]-a[0];
    else return a[1]-b[1];
}

var reconstructQueue = function(people) {
    let peopleSort = people.sort(sortP)
    let res = [];
    peopleSort.forEach(person => {
        res.splice(person[1],0,person);
    });
    return res;
};

let input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]];
let person = countBits(input);
person.forEach(element => {
    console.log(element);
});