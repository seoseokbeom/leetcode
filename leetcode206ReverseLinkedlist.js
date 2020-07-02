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
var reverseList = function(head) {
    var prev=null;
    var nextNode;
    while(head) {
        nextNode = head.next;
        head.next= prev;
        prev=head;
        head=nextNode;
    } 
    return prev;
};