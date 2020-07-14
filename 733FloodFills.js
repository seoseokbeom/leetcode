/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, newColor) {
    var firstColor = image[sr][sc];
    var vis = new Array(image.length).fill().map(e=> new Array(image[0].length).fill(0));
    var recursion = (i,j) => {
        if(i<0|| i>=image.length || j<0 || j>=image[0].length || vis[i][j]) return;
        if(image[i][j]!=firstColor) return;
        if(image[i][j]==firstColor) 
        {
            vis[i][j] = 1;
            image[i][j] = newColor;
            recursion(i-1,j);
            recursion(i+1,j);
            recursion(i,j+1);
            recursion(i,j-1);
        }
    }
    recursion(sr,sc);
    return image;
};