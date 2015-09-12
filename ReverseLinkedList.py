def reverseList(self, head):
    current = head
    prev = None
    _next = None
    while current is not None:
        _next = current.next
        current.next = prev
        prev = current

        current = _next

    return prev

def reverseList(self, head):
    if head is None:
        return None

    return self.reverseRecur(head, None)

def reverseRecur(self, curr, prev):
    result = None
    if curr.next is not None:
        result = reverseRecur(curr.next, curr)
    else:
        result = curr # new head
    curr.next = prev

    return result