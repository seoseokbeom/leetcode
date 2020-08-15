/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.elem = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    this.elem.push({val: x,
    min: this.elem.length === 0 ? x : Math.min(x, this.getMin())})
    
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.elem.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.elem[this.elem.length-1].val;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.elem[this.elem.length-1].min;
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */