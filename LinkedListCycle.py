def hasCycle(self, head):
    if head is None or head.next is None:
        return False
    tmp = head
    tmp_next = head.next
    while tmp_next is not None and tmp_next.next is not None:
        tmp = tmp.next
        tmp_next = tmp_next.next.next
        if tmp is tmp_next:
            return True
    return False


