def lowestCommonAncestor(root, p, q):
    result = root
    while result:
        if result.val > p.val and result.val > q.val and result.left:
            result = result.left
            continue
        elif result.val < p.val and result.val < q.val and result.right:
            result = result.right
            continue
        break
    return result


def lowestCommonAncestor2(root, p, q):
    if root is None:
        return root
    elif root.val < p.val and root.val < q.val and root.right:
        return lowestCommonAncestor2(root.right, p, q)
    elif root.val > p.val and root.val > q.val and root.left:
        return lowestCommonAncestor2(root.left, p, q)
    return root
