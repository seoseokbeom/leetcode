var canCompleteCircuit = function(gas, cost) {
    for(var i=0; i<cost.length; i++) {
        cost[i]  = gas[i] - cost[i];
    }
	// if the cost sum is over the sum of gas, it can't travel all around 
    if(cost.reduce((acc, curr) => acc+curr) <0) return -1;
	// if the cost sum is less than the sum of gas, there must be at least one solution.
    var tank = 0;
    var start =0;
    for(var i=0; i<cost.length; i++) {
        tank+=cost[i];
        if(tank<0) {
            start=i+1;
            tank=0;
        }
    }
    return start;
};