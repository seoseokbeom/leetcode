/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    if(!head) return head;
    var curr = head;
    var count =0;
    while(curr) {
        count++;
        curr= curr.next;
    }
    curr = head;
    var numOfMove = Math.floor(count/2);
    for(var i=0; i<numOfMove; i++) {
        curr = curr.next;
    }
    return curr;
};