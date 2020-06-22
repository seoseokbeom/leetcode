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

 
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}
    
var addTwoNumbers = function(l1, l2) {
    var List = new ListNode(0,null);
    var head = List;
    var sum = 0;
    var carry =0;
    while(l1!==null || l2!==null || sum>0) {
        if(l1!==null) {
            sum+=l1.val;
            l1=l1.next
        } 
        if(l2!==null) {
            sum+=l2.val;
            l2=l2.next;
        }
        if(sum>=10) {
            carry=1;
            sum-=10;
        }
        head.next=new ListNode(sum);
        head=head.next;
        sum=carry;
        carry =0;
    }
    return List.next;
};

var l10 = new ListNode(3,null);
var l11 = new ListNode(4,l10);
var l12 = new ListNode(2,l11);

var l20 = new ListNode(4,null);
var l21 = new ListNode(6,l20);
var l22 = new ListNode(5,l21);

console.log(addTwoNumbers(l22,l12));
var a = addTwoNumbers(l22,l12);
while(a!==null) {
    console.log(a.val);
    a=a.next;
}