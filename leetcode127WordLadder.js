/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    let queue= [{node:beginWord, height:1}];
    let count=0;
    while(queue.length) {
        let p = queue.shift();
        if(p.node == endWord) return p.height;
        for(var i=0; i<wordList.length; i++){
            for(var j=0; j<wordList[i].length; j++){
                if(p.node[j]==wordList[i][j]) count++;
            }
            // console.log(count);
            if(count==beginWord.length-1) {
                queue.push({node:wordList[i], height:p.height+1});
                wordList.splice(i,1);
            }
            count=0;
            
        }
        // wordList.forEach(elem => {
        //     // console.log(p.node[0], elem[0]);
        //     for(var i=0; i<elem.length; i++){
        //         if(p.node[i]==elem[i]) count++;
        //     }
        //     // console.log(count);
        //     if(count==beginWord.length-1) {
        //         queue.push({node:elem, height:p.height+1});
                
        //     }
        //     count=0;
        // })
    }
    return 0;
};