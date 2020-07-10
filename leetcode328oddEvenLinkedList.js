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
var oddEvenList = function(head) {
    let arr = [];
    let curr = head;
    if(!curr) return null;
    while(curr.next && curr.next.next) {
        arr.push(curr.next);
        curr.next=curr.next.next;
        curr=curr.next;
    }
    if(curr.next) arr.push(curr.next);
    for(var i=0; i<arr.length; i++) {
        curr.next=arr[i];
        curr=curr.next;
    }
    curr.next=null;
    return head;
};