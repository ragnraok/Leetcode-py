
def inorderTraversal(self, root):
    ret = []
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left

        if len(stack) == 0:
            break

        top = stack.pop()
        ret.append(top.val)
        root = top.right
    return ret
