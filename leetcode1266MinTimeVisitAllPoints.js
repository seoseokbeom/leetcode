/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function (points) {
  var shortRoute = (p1, p2) => {
    // if(p1[0]==p2[0] && p1[1]==p2[1]) return 0;
    return Math.max(Math.abs(p1[0] - p2[0]), Math.abs(p1[1] - p2[1]));
  };
  let output = 0;
  var recursion = (i) => {
    if (i == points.length - 1) return;

    output += Math.max(
      Math.abs(points[i][0] - points[i + 1][0]),
      Math.abs(points[i][1] - points[i + 1][1])
    );
    recursion(i + 1);   
  };
  recursion(0);
  return output;
};

// var minTimeToVisitAllPoints = function(points) {

//     var shortRoute=(p1, p2)=> {
//         // if(p1[0]==p2[0] && p1[1]==p2[1]) return 0;
//         return Math.max(Math.abs(p1[0]-p2[0]), Math.abs(p1[1]-p2[1]));
//     }
//     let output=0;
//     var recursion =(i)=>{
//         if(i==points.length-1) return;
//         output+= shortRoute(points[i],points[i+1]);
//         recursion(i+1);
//     }
//     recursion(0);
//     return output;
// };
