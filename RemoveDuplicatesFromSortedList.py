def deleteDuplicates(self, head):
    if head is None or head.next is None:
        return head
    prev = head
    curr = head.next

    while curr is not None:
        if curr.val == prev.val:
            prev.next = curr.next
        else:
            prev = curr

        curr = curr.next
    return head
