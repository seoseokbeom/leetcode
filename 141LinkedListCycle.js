/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let walk = head;
    let jump = head;
    if(!head) return false;
    while(jump && jump.next) {
        walk=walk.next;
        if(!walk) return false;
        jump=jump.next.next;
        if(!jump) return false;
        if(walk== jump) return true;
    }
    return false;
};