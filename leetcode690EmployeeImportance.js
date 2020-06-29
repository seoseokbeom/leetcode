/**
 * Definition for Employee.
 * function Employee(id, importance, subordinates) {
 *     this.id = id;
 *     this.importance = importance;
 *     this.subordinates = subordinates;
 * }
 */

/**
 * @param {Employee[]} employees
 * @param {number} id
 * @return {number}
 */
var find = (employees, id) => {
    employees.forEach(employee => {
        if(employee.id == id) return employee
    });
    return 0;
}

var GetImportance = function(employees, id) {
    let employee = find(employees, id);
    let sum = 0;
    let queue = [employee];

    while(queue.length) {
        let p = queue.shift();
        sum += p.importance;
        p.subordinates.map(id => {
            queue.push(find(employees,id));
        })
        // if(p.subordinates == undefined) p.subordinates = [];
        // p.subordinates.forEach(id => {
        //     let subEmployee = find(employees, id)
        //     queue.push(subEmployee);
        // })
    }
    return sum;
};