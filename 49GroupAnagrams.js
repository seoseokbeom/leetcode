/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const map  = {};
    for (let str of strs) {
        const key = [...str].sort();
        console.log(key);
        if(!map[key]) {
            map[key] = [];
        }
        map[key].push(str);
    }

    return Object.values(map);
};

console.log(groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]));