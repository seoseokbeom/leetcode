var copyRandomList = function(head) {
    if(!head) {
      return null;
    }
    const node2 = new Map();
    let n = head;
    while(n) {
      node2.set(n, new Node(n.val));
      n = n.next
    }
    n = head;
    while(n) {
      node2.get(n).next = node2.get(n.next) || null;
      node2.get(n).random = node2.get(n.random) || null;
      n = n.next
    }
    return node2.get(head);
};