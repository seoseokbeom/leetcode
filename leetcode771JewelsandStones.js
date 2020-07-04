    /**
     * @param {number[]} candies
     * @param {number} extraCandies
     * @return {boolean[]}
     */
    var kidsWithCandies = function(candies, extraCandies) {
        // let max = candies[0];
        // for(var i=1; i<candies.length; i++) {
        //     if(candies[i] > max) max = candies[i];
        // }
        // return candies.map(elem => (max-elem <= extraCandies));
        // console.log(candies);
        // return candies;
        return candies.map(x => Math.max(...candies) <= x + extraCandies);
        // return kidsWithCandies(candies, );
    };

console.log(kidsWithCandies([2,3,5,1,3],3));