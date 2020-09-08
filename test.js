function arrangeIntoTree(paths) {
  // Adapted from http://brandonclapp.com/arranging-an-array-of-flat-paths-into-a-json-tree-like-structure/
  var tree = [];

  for (var i = 0; i < paths.length; i++) {
    var path = paths[i];
    var currentLevel = tree;
    for (var j = 0; j < path.length; j++) {
      var part = path[j];

      var existingPath = findWhere(currentLevel, "name", part);

      if (existingPath) {
        currentLevel = existingPath.children;
      } else {
        var newPart = {
          name: part,
          children: [],
        };

        currentLevel.push(newPart);
        currentLevel = newPart.children;
      }
    }
  }
  return tree;

  function findWhere(array, key, value) {
    // Adapted from https://stackoverflow.com/questions/32932994/findwhere-from-underscorejs-to-jquery
    t = 0; // t is used as a counter
    while (t < array.length && array[t][key] !== value) {
      t++;
    } // find the index where the id is the as the aValue

    if (t < array.length) {
      return array[t];
    } else {
      return false;
    }
  }
}

console.log(arrangeIntoTree([3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]));
