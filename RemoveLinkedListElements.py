def removeElements(head, val):
    if head is None:
        return head
    ret = head
    cur = head.next
    while cur.next is not None:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    if ret.val == val:
        ret = ret.next

    return ret
