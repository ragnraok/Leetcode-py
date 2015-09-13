def invertTree(self, root):
        if root:
            node = root.left
            root.left = root.right
            root.right = node

            self.invertTree(root.left)
            self.invertTree(root.right)

        return root

def invertTreeNonRecur(self, root):
    stack = [root]
    while stack:
       node = stack.pop()
        _node = node.left
        node.left = node.right
        node.right = _node
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root