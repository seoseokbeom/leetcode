/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let carry = 0;
    let sum = 0; 
    let head = new ListNode(0);
    let node = head;
    while (l1 || l2 ) {
        let l1Val = l1 ? l1.val : 0;
        let l2Val = l2 ? l2.val : 0;
        sum = l1Val + l2Val + carry;
        if(sum > 9) {
            carry = 1;
            sum -= 10;
        } else {
            carry =0;
        }
        l1.val=sum;
        node.next = new ListNode(sum);
        node = node.next;
        if (l1) {
            l1=l1.next;
        }
        if (l2) {
            l2=l2.next;
        }
    }
    if(carry) node.next = new ListNode(carry);

    return head.next;
};

