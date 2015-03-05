# a reverse pre order
def postorderTraversal(root):
    ret = []
    stack = [root]
    while stack:
        top = stack.pop()
        ret.insert(0, top)
        if top.left:
            stack.append(top.left)
        if top.right:
            stack.append(top.right)
