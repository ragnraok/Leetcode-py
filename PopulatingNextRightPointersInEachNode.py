def connect(root):
    if root is None:
        return
    prev = root
    while prev.left:
        curr = prev
        while curr:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        prev = prev.left
