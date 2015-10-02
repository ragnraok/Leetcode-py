def deleteNode(node):
    if node is None:
        return
    if node.next is None:
        return
    node.val = node.next.val
    node.next = node.next.next
