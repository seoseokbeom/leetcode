/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var getDecimalValue = function(head) {
    let S = [];
    // console.log(head);
    // console.log(head.val);
    while(head) {
        S.push(head.val);
        head=head.next;
    }
    
    console.log(S);
    return parseInt(S.join(''),2);
};