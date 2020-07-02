/**
 * @param {number} area
 * @return {number[]}
 */
var constructRectangle = function(area) {
    let sqrt = Math.floor(Math.sqrt(area));
    while(area%sqrt != 0 && sqrt>0) {
        sqrt--;
    }
    let W = area/sqrt;
    return [W, sqrt];
};