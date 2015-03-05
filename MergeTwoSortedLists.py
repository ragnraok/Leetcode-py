def mergeTwoLists(l1, l2):
    if not l1 and not l2:
        return None

    result = ListNode(0)
    tracer = result
    while l1 and l2:
        if l1.val < l2.val:
            tracer.next = l1
            l1 = l1.next
        else:
            tracer.next = l2
            l2 = l2.next
        tracer = tracer.next
    if l1 is None:
        tracer.next = l2
    else:
        tracer.next = l1

    return result.next
