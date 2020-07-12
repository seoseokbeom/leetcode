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
var sortList = function(head) {
    var curr = head;
    var notSorted=1;
    while(notSorted) {
        notSorted=0;
        while(curr && curr.next) {
            var tmp  = curr;
            curr=tmp.next;
            if(tmp.val > curr.val) {
                var tmp2 = curr.val;
                curr.val = tmp.val;
                tmp.val = tmp2;
                notSorted=1;
            }
            // curr=curr.next;
        }
        curr = head;
    }
    return head;
};