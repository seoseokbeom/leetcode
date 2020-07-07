/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let arr = [];
    if(!head) return true;
    
    var recursion = function(node) {
        if(!node) return;
        recursion(node.next);
        arr.push(node.val);
        return;
    }
    recursion(head);
    // console.log(arr);
    let i=0;
    while(head){
        if(head.val != arr[i]) return false;
        head=head.next;
        i++;
    }
    return true;
    
};